
import csv


def calculate_priority(report):
    severity = int(report["severity"])
    people = int(report["people"])

    score = severity * 10 + min(people, 50) * 0.5

    if report["status"].strip().lower() == "resolved":
        score = 0

    return round(score, 1)


def main():
    reports = []

    try:
        with open("emergency_reports.csv", "r") as file:
            reader = csv.DictReader(file)

            for report in reader:
                report["priority_score"] = calculate_priority(report)
                reports.append(report)

    except FileNotFoundError:
        print("Error: emergency_reports.csv file not found.")
        return

    if not reports:
        print("No emergency reports available.")
        return

    reports.sort(
        key=lambda report: report["priority_score"],
        reverse=True
    )

    print("\n========== RAPIDRELIEF AI ==========")
    print("Emergency Resource Prioritization System")
    print("=" * 60)

    print("\n=== ALL EMERGENCY REPORTS ===")

    for report in reports:
        print(
            "ID: " + report["id"]
            + " | Incident: " + report["incident"]
            + " | Location: " + report["location"]
            + " | Score: " + str(report["priority_score"])
            + " | Status: " + report["status"]
        )

    highest = None

    for report in reports:
        if report["status"].strip().lower() != "resolved":
            highest = report
            break

    print("\n=== PRIORITY ALERT ===")

    if highest is not None:
        print("Incident:", highest["incident"])
        print("Location:", highest["location"])
        print("Priority score:", highest["priority_score"])
        print("Suggested action: Review this incident first.")
    else:
        print("No unresolved incidents.")

    print("\n=== TOP 3 UNRESOLVED INCIDENTS ===")

    count = 0

    for report in reports:
        if report["status"].strip().lower() != "resolved":
            count += 1
            print(
                str(count) + ". "
                + report["incident"] + " in "
                + report["location"]
                + " (Score: "
                + str(report["priority_score"]) + ")"
            )

            if count == 3:
                break

    unresolved = 0
    resolved = 0

    for report in reports:
        if report["status"].strip().lower() == "resolved":
            resolved += 1
        else:
            unresolved += 1

    print("\n=== INCIDENT SUMMARY ===")
    print("Total incidents:", len(reports))
    print("Unresolved incidents:", unresolved)
    print("Resolved incidents:", resolved)

    print("\nNote: This prototype uses fictional data.")
    print("Priority scores are illustrative and not validated.")
    print("It does not dispatch emergency services.")


if __name__ == "__main__":
    main()
