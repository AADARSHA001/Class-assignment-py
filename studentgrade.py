# 1. Student Grade Calculator
# Objective: Build a program to calculate grades for students based on marks entered.
# Steps:
# 1. Ask the user to input marks for 5 subjects.
# 2. Validate that the input is a number and within a valid range (0-100).
# 3. Calculate the total marks and percentage.
# 4. Assign grades based on percentage:
# o 90% and above: A+
# o 80%-89%: A
# o 70%-79%: B
# o 60%-69%: C
# o Below 60%: Fail.
# 5. Display the total marks, percentage, and grade.

choice = 'yes'

while choice == 'yes':
    total_marks = 0

    # Input marks for 5 subjects
    for i in range(1, 6):
        marks = float(input(f"Enter marks for Subject {i} (0-100): "))
        if marks >= 0 and marks <= 100:
            total_marks += marks
        else:
            print("Invalid input. Marks should be between 0 and 100.")
            break

    # Calculate percentage if all marks were valid
    if total_marks > 0:
        percentage = (total_marks / 500) * 100

        # Determine grade using if-else
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        else:
            grade = "Fail"

        # Display results
        print("\n--- Results ---")
        print(f"Total Marks: {total_marks}")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Grade: {grade}")

    # Ask to continue
    choice = input("\nWant to calculate grades for another student? (yes/no): ").lower()
    if choice != 'yes':
        print("Thank you for using the Student Grade Calculator!")
