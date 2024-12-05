def main():
    first_name, last_name = student_name()
    avg, scores = calc_average()
    print(f"The full name of this student is {first_name} {last_name} \n")
    determine_grade(scores)
    print(f"\n The test score average and letter grade is: {avg} and {grade_check(avg)} \n")
    
    
def student_name():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    return first_name, last_name
def calc_average():
    score1 = int(input("Enter the first score: "))
    score2 = int(input("Enter the second score: "))
    score3 = int(input("Enter the third number: "))
    score4 = int(input("Enter your fourth score: "))
    score5 = int(input("Enter your fifth score: "))
    avg = (score1 + score2 + score3 + score4 + score5) / 5
    return avg, [score1, score2, score3, score4, score5]

def grade_check(grade):
    if grade < 60:
        return "F"
    elif grade < 70:
        return "D"
    elif grade < 80:
        return "C"
    elif grade < 90:
        return "B"
    elif grade <= 100:
        return "A"
def determine_grade(scores_list):
    for score in range(len(scores_list)):
        grade = grade_check(scores_list[score])
        print(f"Your score and grade for entered for score Test{score+1} is: {scores_list[score]}: {grade}")

main()