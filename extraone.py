print("Welcome astronaut!")
print("There is an asteroid on the distant!")
print("We have to take care of it now!")
command = 0
points = 0 # THE AMOUNT OF ASTEROIDS DESTROYED
from random import random
ran1 = random()
ran1 = ran1*100
ran1 = round(ran1,0)
if ran1 == 0:
 ran1 = 1
print("The target is at latitude" , ran1)
command = 0
while command != ran1:
 command = int(input("Type a value between 1 to 100."))
 if command == ran1:
  print("Target hit!")
  points = points + 1
 elif command != ran1:
  print("Hit the correct target!")
  if command < 0:
   print("Too low!")
  elif command > 100:
   print("Too high!")
print("Asteroids destroyed:" , points)
print("Woah! That was a good first try! Especially with that range!")
print("But don't get so proud that early on. That was nothing...")
print("OH LOOK THERE IS AN ASTEROID AGAIN! IN FACT... TWO OF THEM!")
ran1 = random()
ran1 = ran1*100
ran1 = round(ran1 , 0)
ran2 = random()
ran2 = ran2*100
ran2 = round(ran2 , 0)
print("First asteroid's range:" , ran1)
while command != ran1:
 command = int(input("Input a value from 1 to 100 to destroy the first asteroid!"))
 if command == ran1:
  print("Target hit!")
  points = points + 1
 elif command != ran1:
  print("Missed!")
  if command < 0:
   print("Too low!")
  elif command > 100:
   print("Too high!")
print("Asteroids destroyed:" , points)
print("Second asteroid's range:" , ran2)
while command != ran2:
 command = int(input("Input a value from 1 to 100 to destroy the second asteroid!"))
 if command == ran2:
  print("Target hit!")
  points = points + 1
 elif command != ran2:
  print("Missed!")
  if command < 0:
   print("Too low!")
  elif command > 100:
   print("Too high!")
print("Asteroids destroyed:" , points)
