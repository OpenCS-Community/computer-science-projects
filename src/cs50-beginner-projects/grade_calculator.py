def calculate_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def main():
    subjects = []
    total_subjects = 3

    print("=== Student Grade Calculator ===")

    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    for i in range(total_subjects):
        subject = input(
            f"Enter subject {i + 1} name: "
        ).strip()

        if not subject:
            print("Subject name cannot be empty.")
            return

        while True:
            try:
                mark = float(
                    input(f"Enter mark for {subject}: ")
                )

                if 0 <= mark <= 100:
                    subjects.append((subject, mark))
                    break

                print("Enter a mark between 0 and 100.")

            except ValueError:
                print("Invalid input. Enter a number.")

    average = sum(
        mark for _, mark in subjects
    ) / len(subjects)

    grade = calculate_grade(average)
    status = "PASS" if average >= 50 else "FAIL"

    print("\n=== Student Results ===")
    print(f"Student: {name}")

    for subject, mark in subjects:
        print(f"{subject}: {mark:.1f}%")

    print(f"Average: {average:.2f}%")
    print(f"Grade: {grade}")
    print(f"Status: {status}")


if name == "main":
    main()