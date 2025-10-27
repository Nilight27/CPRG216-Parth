

students = {}

print("Enter each student's name and score. When done, type END for student's name.")
student_num = 1

while True:

    name = input(f"{student_num}. Student name: ")
    
    if name.upper() == "END":
        break
    
    score = float(input("   Score: "))
    
    students[name] = score
    student_num += 1

if students:
    average = sum(students.values()) / len(students)
    
    highest_name = max(students, key=students.get)
    highest_score = students[highest_name]
    
    print(f"\nClass average score is {average:.1f}")
    print(f"Highest score of {highest_score:.1f} achieved by {highest_name}!")
    
    print(f"\n{'Student Name':<15} {'Grade':<10}")
    print("-" * 25)
    for name, score in students.items():
        print(f"{name:<15} {score:.1f}")
else:
    print("\nNo students entered.") 