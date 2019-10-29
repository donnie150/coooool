import time

print("Welcome to the Quiz")

time.sleep(.7)

print("Question 1\n What is your name")
name = input()
print("Cool")
print("Question 2\n What is the Capital of Maine\n 1. New York\n 2. Philadelphia\n 3. Augusta\n 4. St. Louis")
cap = input()
cap = int(cap)
score = 0
if cap == 3:
    score = score + 1
else:
    score = 0














finalscore = score/1*100
print("Your Score is " + str(finalscore) + "%")
