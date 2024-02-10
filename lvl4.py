print("Level 4.")
yourrev = 49
yourdmg = 25
yourheal = 197
igheal = 197
yourrev = 25/100*yourheal
yourrev = round(yourrev, 0)
heale = 2
dmgle = 2
wins = 3
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
print("Mini Rookie's damage:" , mrookde)
print("MIni Rookie's health:" , mrookhe)
mrookhe1 = mrookhe
mrookhe2 = mrookhe
command = str(input("To play the level enter p."))
if command == 'p' or command == 'P':
 command = str(input("DOUBLE ROOKS!"))
 command = str(input("Now it is time that we enhance our skills to the point that we could tackle multiple opponents at once!"))
 command = str(input("You have to choose which rook you want to attack, if you choose the hit function."))
 command = str(input("You know, this feature reminds me of something..."))
 while wins == 3:
  print("Your health:" , igheal)
  print("Mini Rookie 1's health:" , mrookhe1)
  print("Mini Rookie 2's health:" , mrookhe2)
  if mrookhe1 > 0 and mrookhe2 > 0:
   command = str(input("Type A to hit one of the mini rookies, H to heal yourself, or I to check their info!"))
  elif mrookhe1 <= 0 or mrookhe2 <= 0:
   command = str(input("Type A to hit the remaining mini rookie, H to heal yourself, or I to check his info!"))
  if command == 'A' or command == 'a':
   if mrookhe1 > 0 and mrookhe2 > 0:
    command = str(input("Input 1 to hit Mini Rookie 1, or input 2 to hit Mini Rookie 2."))
    if command == '1':
     mrookhe1 = mrookhe1 - 25
    elif command == '2':
     mrookhe2 = mrookhe2 - 25
   elif mrookhe1 <= 0:
    mrookhe2 = mrookhe2 - 25
   elif mrookhe2 <= 0:
    mrookhe1 = mrookhe1 - 25
   if mrookhe1 > 0 and mrookhe2 > 0:
    igheal = igheal - 26
   elif mrookhe2 <= 0 or mrookhe1 <= 0:
    igheal = igheal - 13
    mrookhe1 = mrookhe1 - yourdmg
  elif command == 'H' or command == 'h':
   if igheal < yourheal:
    igheal = igheal + yourrev
   if igheal >= yourheal:
    igheal = yourheal
   if mrookhe1 > 0 and mrookhe2 > 0:
    igheal = igheal - 26
   elif mrookhe2 > 0 or mrookhe1 > 0:
    igheal = igheal - 13
  elif command == 'I' or command == 'i':
   print("Mini Rookie 1's health:" , mrookhe1)
   print("Mini Rookie 2's health:" , mrookhe2)
   print("Mini Rookie's damage:" , mrookde)
  elif command != 'A' or command != 'H' or command != 'I' or command != 'a' or command != 'h' or command != 'i':
   print("Invalid function!")
  if igheal <= 0 and mrookhe1 > 0 and mrookhe2 > 0:
   igheal = yourheal
   mrookhe1 = mrookhe
   mrookhe2 = mrookhe
  if mrookhe1 <= 0 and mrookhe2 <= 0:
   command = str(input("Level 4 cleared!"))
   wins = 4
  if igheal <= 0 and mrookhe1 != 0 or mrookhe2 != 0:
   igheal = yourheal
   mrookhe1 = mrookhe
   mrookhe2 = mrookhe
   command = str(input("Level failed! Try again!"))
elif command != 'P' or command != 'p':
 print("Input P to play!")