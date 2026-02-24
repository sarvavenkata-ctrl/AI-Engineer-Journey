def read_mark(i: int) -> float:
    """Read one mark (0-100) from user with validation."""
    while True:
        raw = input(f"Enter mark {i}/5 (0-100): ").strip()
        try:
            mark = float(raw)
        except ValueError:
            print("❌ Please enter a number (e.g., 75 or 82.5).")
            continue

        if not (0 <= mark <= 100):
            print("❌ Mark must be between 0 and 100.")
            continue

        return mark


def grade_from_average(avg: float) -> str:
    """Convert average mark into a letter grade."""
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def main():
    marks = [read_mark(i) for i in range(1, 6)]
    avg = sum(marks) / len(marks)
    grade = grade_from_average(avg)

    print("\n✅ Results")
    print(f"Marks: {marks}")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()