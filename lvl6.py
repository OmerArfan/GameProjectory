print("Level 6.")
wizde = 21
wizhe = 110
igwizhe = wizhe
yourrev = 49
yourdmg = 25
yourheal = 197
igheal = 197
yourrev = 25/100*yourheal
yourrev = round(yourrev, 0)
heale = 2
dmgle = 2
wins = 5
coins = 50
rook = '1'
rookde = 29 ## ROOKDE IS ROOKIE'S DAMAGE.
rookhe = 219 ## ROOKHE IS ROOKIE'S HEALTH.
mrook = '2'
mrookde = 13 ##MINI ROOKIE'S DAMAGE
mrookhe = 113 ##MINI ROOKIE'S HEALTH
urook = '3'
urookde = 44 # ULTRA ROOKIE'S DAMAGE
urookhe = 307 # ULTRA ROOKIE'S HEALTH
exit = False
levelexit = False
Upexit = False
mrookhe1 = mrookhe
mrookhe2 = mrookhe
from random import random
print("UPCOMING ROBOTS")
print("Mini Rookie's health:" , mrookhe)
print("Mini Rookie's damage" , mrookde)
command = str(input("Input p to play!"))
if command == 'p' or command == 'P':
 print("Wave 1")
 command = str(input("WIZARD: Do you seem to have a problem with taking down multiple opponents?"))
 command = str(input("WIZARD: Well, worry no more! You found some backup!"))
 while wins == 5:
  if mrookhe1 > 0 and mrookhe2 > 0:
   command = str(input("Type A to hit one of the mini rookies, H to heal yourself, or I to check their info!"))
  elif mrookhe1 <= 0 or mrookhe2 <= 0:
   command = str(input("Type A to hit the remaining mini rookie, H to heal yourself, or I to check his info!"))
  if command == 'A' or command == 'a':
   if mrookhe1 > 0 and mrookhe2 > 0:
    if igwizhe > 0:
     if mrookhe1 > 0 and mrookhe2 > 0:
      command = int(input("WIZARD: Type 1 to attack mini rookie 1 or type 2 to attack mini rookie 2."))
      if command == '1':
       mrookhe1 = mrookhe1 - 25
      elif command == '2':
       mrookhe2 = mrookhe2 - 25
      elif command != '1' or command != '2':
       print("Inavlid function!")
     elif mrookhe1 <= 0:
      mrookhe2 = mrookhe2 - 25
     elif mrookhe2 <= 0:
      mrookhe1 = mrookhe1 - 25  
    if igheal > 0:
     if mrookhe1 > 0 and mrookhe2 > 0:
      command = int(input("YOU: Type 1 to attack mini rookie 1 or type 2 to attack mini rookie 2."))
      if command == '1':
       mrookhe1 = mrookhe1 - 25
      elif command == '2':
       mrookhe2 = mrookhe2 - 25
     elif mrookhe1 <= 0:
      mrookhe2 = mrookhe2 - 25
     elif mrookhe2 <= 0:
      mrookhe1 = mrookhe1 - 25
   if mrookhe1 > 0 and mrookhe2 > 0:
    gene = random()
    gene = round(gene, 1)
    if gene < 0.5:
     igwizhe = igwizhe - (mrookde)
     igheal = igheal - (mrookde)
    elif gene > 0.5:
     gene = random()
     gene = round(gene, 1)
     if gene > 0.5:
      igwizhe = igwizhe - 2*mrookde
     else:
      igheal = igheal - 2*mrookde
   else:
    gene = random()
    gene = round(gene, 1)
    if gene < 0.5:
     igwizhe = igwizhe - (mrookde)
    if gene > 0.5:
     igheal = igheal - (mrookde)
  elif command == 'H' or command == 'h':
   if igheal < yourheal:
    igheal = igheal + yourrev
   if igheal >= yourheal:
    igheal = yourheal
   if mrookhe1 > 0 and mrookhe2 > 0:
    igheal = igheal - 26
   elif mrookhe2 > 0 or mrookhe1 > 0:
    igheal = igheal - 13
  elif command == 'I' or command== 'i':
   command = str(input("Type 'me' to view your own stats, or type 'a' to view enemy stats."))
   if command == 'a':
    print("Mini Rookie 1's health:" , mrookhe1)
    print("Mini Rookie 2's health:" , mrookhe2)
    print("Mini Rookie's damage:" , mrookde)
   elif command == 'me':
    print("Your health:" , igheal , "/" , yourheal)
    print("Your damage:" , yourdmg)
    print("Wizard's health:" , igwizhe , "/" , wizhe)
    print("Wizard's damage:" , wizde)
  elif command != 'A' or command != 'H' or command != 'I' or command != 'a' or command != 'h' or command != 'i':
   print("Invalid function!")
  if igheal <= 0 and mrookhe1 > 0 and mrookhe2 > 0:
   igheal = yourheal
   mrookhe1 = mrookhe
   mrookhe2 = mrookhe
  if mrookhe1 <= 0 and mrookhe2 <= 0:
   wins = 6
   print("You win! Congratulations!")