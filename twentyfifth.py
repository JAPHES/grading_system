# A program to grade marks for subjects

results = []
number = 1

while True:
    subject = input("Enter Subject " + str(number) + ": ")

    if subject == "done":
        break

    marks = int(input("Enter Marks " + subject + ": "))

    if marks >= 70 and marks <= 100:
        grade = "A Excellent"
    elif marks >= 60 and marks <= 69:
        grade = "B Very Good"
    elif marks >= 50 and marks <= 59:
        grade = "C Good"
    elif marks >= 40 and marks <= 49:
        grade = "D Fair"
    elif marks >= 0 and marks <= 39:
        grade = "Fail"
    else:
        grade = "Invalid marks"

    results.append([subject, marks, grade])
    number = number + 1

print("These are the final results")

for result in results:
    print(result[0],  result[1], result[2])
