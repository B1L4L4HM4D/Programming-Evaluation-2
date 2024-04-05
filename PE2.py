#Q Create a program that asks the user to input their grade for Course 1, Course 2, Course 3 and Course 4. The program should take the 4 course grades and calculate the average. Once the average is calculated, determine the overall letter grade for the student.

#This is a table to determine the letter grade 

#Letter	Percent
#A+	95–100%
#A	87–94%
#A−	80–86%
#B+	77–79%
#B	72–76%
#B−	70–71%
#C	63-66%
#C-	60-62%
#D+	57–61%
#D	54–56%
#D−	50–53%
#F	0–49%

print("This program will calculate your average grade for 4 courses. Please enter your grade for each course!")
course1 = float(input("Enter your grade for Course 1: "))
course2 = float(input("Enter your grade for Course 2: "))
course3 = float(input("Enter your grade for Course 3: "))
course4 = float(input("Enter your grade for Course 4: "))
average = round((course1 + course2 + course3 + course4)/4, 0)

print("Your average grade is: " + str(average) + "%")

if average >= 95:
  print("Your grade is an A+")
elif average >= 87 and average < 94:
  print("Your grade is an A")
elif average >= 80 and average < 86:
  print("Your grade is an A-")
elif average >= 77 and average < 79:
  print("Your grade is a B+")
elif average >= 72 and average < 76:
  print("Your grade is a B")
elif average >= 70 and average < 71:
  print("Your grade is a B-")
elif average >= 67 and average < 69:
  print("Your grade is a C+")
elif average >= 63 and average < 66:
  print("Your grade is a C")
elif average >= 60 and average < 62:
  print("Your grade is a C-")
elif average >= 57 and average < 61:
  print("Your grade is a D+")
elif average >= 54 and average < 56:
  print("Your grade is a D")
elif average >= 50 and average < 53:
  print("Your grade is a D-")
elif average >= 0 and average < 49:
  print("Your grade is an F")
