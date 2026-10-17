import csv
from pathlib import Path
from html import escape
from http.server import HTTPServer, BaseHTTPRequestHandler

DATA_FILE = Path(__file__).with_name("emergency_reports.csv")

def get_reports():
    with open(DATA_FILE, newline="") as f:
        reports = list(csv.DictReader(f))
    for r in reports:
        score = int(r["severity"]) * 10 + min(int(r["people"]), 50) * 0.5
        r["score"] = 0 if r["status"].lower() == "resolved" else score
    return sorted(reports, key=lambda r: r["score"], reverse=True)

class App(BaseHTTPRequestHandler):
    def do_GET(self):
        reports = get_reports()
        pending = [r for r in reports if r["status"].lower() != "resolved"]
        top = pending[0] if pending else None

        rows = "".join(
            "<tr>"
            f"<td>{escape(r['incident'])}</td>"
            f"<td>{escape(r['location'])}</td>"
            f"<td>{escape(r['severity'])}</td>"
            f"<td>{escape(r['people'])}</td>"
            f"<td>{escape(r['status'])}</td>"
            f"<td>{r['score']:.1f}</td></tr>"
            for r in reports
        )

        alert = (
            f"{escape(top['incident'])} - {escape(top['location'])} "
            f"(score {top['score']:.1f})"
            if top else "No unresolved incidents"
        )

        page = f"""<!DOCTYPE html>
<html><head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>RapidRelief AI</title>
<style>
body {{font-family:Arial;margin:30px;background:#f1f5f9;color:#17243a}}
header {{background:#163653;color:white;padding:24px;border-radius:12px}}
.cards {{display:flex;gap:16px;flex-wrap:wrap;margin:20px 0}}
.card {{background:white;padding:18px;border-radius:10px;min-width:130px}}
.alert {{background:#ffeadf;padding:18px;border-radius:8px}}
table {{border-collapse:collapse;width:100%;background:white}}
th,td {{padding:12px;border-bottom:1px solid #ddd;text-align:left}}
th {{background:#dce7f5}}
</style></head><body>
<header><h1>RapidRelief AI</h1>
<p>Real-Time Emergency Resource Prioritization</p></header>
<div class="cards">
<div class="card"><h3>Total Reports</h3><h2>{len(reports)}</h2></div>
<div class="card"><h3>Unresolved</h3><h2>{len(pending)}</h2></div>
<div class="card"><h3>Resolved</h3><h2>{len(reports)-len(pending)}</h2></div>
</div>
<h2>Highest-Priority Alert</h2><div class="alert"><strong>{alert}</strong></div>
<h2>Ranked Emergency Reports</h2>
<table><tr><th>Incident</th><th>Location</th><th>Severity</th>
<th>People</th><th>Status</th><th>Score</th></tr>{rows}</table>
<p><small>Fictional data and illustrative, unvalidated scores.
Not a medical assessment or emergency dispatch system.</small></p>
</body></html>"""

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(page.encode("utf-8"))

print("RapidRelief AI running on port 8000")
HTTPServer(("0.0.0.0", 8000), App).serve_forever()
