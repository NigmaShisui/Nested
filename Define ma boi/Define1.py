# Function to check the grade
def check_grade(grade):
    if 90 <= grade <= 100:
        print("Excellent! You did a great job!")
    elif 80 <= grade <= 89:
        print("Good job! Keep it up!")
    elif 70 <= grade <= 79:
        print("You passed, but there's room for improvement.")
    else:
        print("You failed. Better luck next time.")

# Prompt user to input their grade
try:
    grade = int(input("Enter your grade (0-100): "))
    
    # Ensure the grade is within a valid range
    if 0 <= grade <= 100:
        check_grade(grade)  # Call the define function with the input grade
    else:
        print("Please enter a grade between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter a numerical grade.")
