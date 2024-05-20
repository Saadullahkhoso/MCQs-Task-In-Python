print("'PYTHON MCQS TEST'")
print("'INSTRUCTIONS':")
print("1.Read the question and all the answer options carefully before answering.\n2.And most importantly, stay calm and focused during the exam!\n3.To pass a multiple-choice test, aim to answer at least 8 questions and get at least 6 correct.\n")
score=0
print("Q1:What does the print() function do in Python?")
print("A) Reads input from the user")
print("B) Outputs text to the console")
print("C) Performs mathematical calculations")
print("D) Defines a new function\n")
answer1=input("Enter your answer: ")
if answer1=="a" or answer1=="b" or answer1=="c" or answer1=="d":
    if answer1=="b":
        score=score+1
        print("Correct!")
        print("Score is:",score)
    else:
        print("Incorrect!")
        print("Score is:",score)
else:
    print("Invalid input")
print("\n")

print("Q2:Which of the following data types in Python is mutable?")
print("A) int")
print("B) str")
print("C) tuple")
print("D) list\n")
answer2=input("Enter your answer: ")
if answer2=="a" or answer2=="b" or answer2=="c" or answer2=="d":
    if answer2=="d":
        score=score+1
        print("Correct!")
        print("Score is:",score)
    else:
        print("Incorrect!")
        print("Score is:",score)
else:
    print("Invalid input")
print("\n")

print("Q3:What is the correct way to start a single-line comment in Python?")
print("A) //")
print("B) ||")
print("C) #")
print("D) <!--")
answer3=input("Enter your answer: ")
if answer3=="a" or answer3=="b" or answer3=="c" or answer3=="d":
    if answer3=="c":
        score=score+1
        print("Correct!")
        print("Score is:",score)
    else:
        print("Incorrect!")
        print("Score is:",score)
else:
    print("Invalid input")
print("\n")

print("Q4:Which keyword is used to define a function in Python?")
print("A) func")
print("B) define")
print("C) def")
print("D)funcation")
answer4=input("Enter your answer: ")
if answer4=="a" or answer4=="b" or answer4=="c" or answer4=="d":
    if answer4=="c":
        score=score+1
        print("Correct!")
        print("Score is:",score)
    else:
        print("Incorrect!")
        print("Score is:",score)
else:
    print("Invalid input")
print("\n")

print("Q5:Which data type is used to store a single character in Python?")
print("A) char")
print("B) str")
print("C) character")
print("D) letter")
answer5=input("Enter your answer: ")
if answer5=="a" or answer5=="b" or answer5=="c" or answer5=="d":
    if answer5=="b":
        score=score+1
        print("Correct!")
        print("Score is:",score)
    else:
        print("Incorrect!")
        print("Score is:",score)
else:
    print("Invalid input")
print("\n")

print("Q6:How do you declare a variable in Python?")
print("A) var1=")
print("B) let x")
print("C) var x")
print("D) =var1")
answer6=input("Enter your answer: ")
if answer6=="a" or answer6=="b" or answer6=="c" or answer6=="d":
    if answer6=="a":
        score=score+1
        print("Correct!")
        print("Score is:",score)
    else:
        print("Incorrect!")
        print("Score is:",score)
else:
    print("Invalid input")
print("\n")


print("Q7:What does the len() function return in Python?")
print("A) The length of a string")
print("B) The length of a list")
print("C) The length of a tuple")
print("D) All of the above")
answer7=input("Enter your answer: ")
if answer7=="a" or answer7=="b" or answer7=="c" or answer7=="d":
    if answer7=="d":
        score=score+1
        print("Correct!")
        print("Score is:",score)
    else:
        print("Incorrect!")
        print("Score is:",score)
else:
    print("Invalid input")
print("\n")

print("Q8:Which one of the following is arithmetic operator?")
print("A) +")
print("B) ==")
print("C) =")
print("D) None of these")
answer8=input("Enter your answer: ")
if answer8=="a" or answer8=="b" or answer8=="c" or answer8=="d":
    if answer8=="a":
        score=score+1
        print("Correct!")
        print("Score is:",score)
    else:
        print("Incorrect!")
        print("Score is:",score)
else:
    print("Invalid input")
print("\n")

print("Q9:Which one of the following is logical operator?")
print("A) +")
print("B) =")
print("C) *")
print("D) not")
answer9=input("Enter your answer: ")
if answer9=="a" or answer9=="b" or answer9=="c" or answer9=="d":
    if answer9=="d":
        score=score+1
        print("Correct!")
        print("Score is:",score)
    else:
        print("Incorrect!")
        print("Score is:",score)
else:
    print("Invalid input")
print("\n")

print("Q10:Which keyword is used to exit a loop prematurely in Python??")
print("A) stop")
print("B) break")
print("C) end")
print("D) exit")
answer10=input("Enter your answer: ")
if answer10=="a" or answer10=="b" or answer10=="c" or answer10=="d":
    if answer10=="b":
        score=score+1
        print("Correct!")
        print("Score is:",score)
    else:
        print("Incorrect!")
        print("Score is:",score)
else:
    print("Invalid input")
print("\n")

totalscore=score
print("Total Marks is:",score)
if totalscore<=6:
    print("Sorry You Are fail!\nPlease be prepare for next attempt 'Thank You'")
else:
    print("Oh Great! Congartulations You are Pass in exam")
