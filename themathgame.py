from random import random
int1=0
int2=0
answer=999999
while (int1+int2) != answer:
 print("Easy")
 int1 = round(random()*10,0)
 int2 = round(random()*10,0)
 print("What is ",int1," + ",int2)
 answer = int(input("Answer:"))
 if answer == (int1 + int2):
    print("Correct!")
 else:
    print("Wrong! Try again!")
int1=0
int2=0
answer=999999
while (int1*int2) != answer:
 print("Normal")
 int1 = round(random()*25,0)
 int2 = round(random()*25,0)
 print("What is ",int1," * ",int2)
 answer = int(input("Answer:"))
 if answer == (int1 * int2):
    print("Great job! You are correct!")
 else:
    print("Oopsie! Try again!")
int1=1
int2=4
answer=999999 
tries = 0
correct= (int1 / int2)
correct = round(correct,2)
while correct != answer:
 print("Hard")
 int1 = round(random()*47,0)
 int2 = round(random()*47,0)    
 print("What is ",int1," / ",int2)
 answer = float(input("Answer(2 decimal places):"))
 if answer == correct:
   print("WHAT?! HOW DID YOU GET THAT RIGHT!")
 else:
   print("Well seems like I'm starting to hang the hang of you...")
   tries = tries +1
   if tries > 3:
     print("Stuck? Skip this level!")
     command = str(input("Input yes if you want to skip."))
     if command == 'yes':
       answer = correct
       print("The correct answer was",correct)
int1=33
int2=34
answer=999999
