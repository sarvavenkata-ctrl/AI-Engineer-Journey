import csv
from pathlib import Path


def grade_from_mark(mark: float) -> str:
    """Convert a mark into a letter grade."""
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


def main():
    print("Welcome to Marks Analyzer!")
    print("Current working directory:", Path.cwd())

    input_csv = Path("notebooks") / "sample_marks.csv"
    output_txt = Path("outputs") / "summary.txt"

    print("Looking for CSV at:", input_csv.resolve())

    students = []

    with input_csv.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["student"]
            mark = float(row["mark"])
            students.append({"student": name, "mark": mark, "grade": grade_from_mark(mark)})

    if not students:
        print("No student data found.")
        return

    marks = [s["mark"] for s in students]
    average_mark = sum(marks) / len(marks)
    highest = max(students, key=lambda s: s["mark"])
    lowest = min(students, key=lambda s: s["mark"])

    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for s in students:
        grade_counts[s["grade"]] += 1

    lines = [
        "Marks Analyzer Summary",
        "======================",
        f"Number of students: {len(students)}",
        f"Class average: {average_mark:.2f}",
        f"Highest mark: {highest['student']} ({highest['mark']:.1f})",
        f"Lowest mark: {lowest['student']} ({lowest['mark']:.1f})",
        "",
        "Grade counts:",
        f"A: {grade_counts['A']}",
        f"B: {grade_counts['B']}",
        f"C: {grade_counts['C']}",
        f"D: {grade_counts['D']}",
        f"F: {grade_counts['F']}",
    ]

    summary = "\n".join(lines)

    print(summary)

    output_txt.parent.mkdir(parents=True, exist_ok=True)
    output_txt.write_text(summary, encoding="utf-8")

    print(f"\nSummary saved to: {output_txt}")


if __name__ == "__main__":
    main()