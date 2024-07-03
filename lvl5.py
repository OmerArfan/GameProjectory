print("Level 5.")
yourrev = 49
yourdmg = 25
yourheal = 197
igheal = 197
yourrev = 25/100*yourheal
yourrev = round(yourrev, 0)
heale = 2
dmgle = 2
wins = 4
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
rookde1 = rookde
rookde2 = rookde
rookhe1 = rookhe
rookhe2 = rookhe
print("UPCOMING ROBOTS")
print("Rookie's damage:" , rookde)
print("Rookie's health:" , rookhe)
print("Ulrea Rookie's damage" , urookde)
print("Ultra Rookie's health" , urookhe)
command = str(input("Input p to play!"))
if command == 'p' or command == 'P':
 command = str(input("You now have to go through waves of battles!"))
 command = str(input("In the first wave, robots will attack you, but once you defeat them, another set of robots will come to attack you, which you have to defeat!"))
 print("Wave 1")
 while wins == 4:
  if rookhe1 > 0 and rookhe2 > 0:
   command = str(input("Type A to hit one of the mini rookies, H to heal yourself, or I to check their info!"))
  elif rookhe1 <= 0 or rookhe2 <= 0:
   command = str(input("Type A to hit the remaining mini rookie, H to heal yourself, or I to check his info!"))
  if command == 'A' or command == 'a':
   if rookhe1 > 0 and rookhe2 > 0:
    command = str(input("Input 1 to hit Mini Rookie 1, or input 2 to hit Mini Rookie 2."))
    if command == '1':
     rookhe1 = rookhe1 - 25
    elif command == '2':
     rookhe2 = rookhe2 - 25
    elif rookhe1 <= 0:
     rookhe2 = rookhe2 - 25
    elif rookhe2 <= 0:
     rookhe1 = rookhe1 - 25
   if rookhe1 > 0 and rookhe2 > 0:
    igheal = igheal - 26
   elif rookhe2 <= 0 or rookhe1 <= 0:
    igheal = igheal - 13
    rookhe1 = rookhe1 - yourdmg
  elif command == 'H' or command == 'h':
   if igheal < yourheal:
    igheal = igheal + yourrev
   if igheal >= yourheal:
    igheal = yourheal
   if rookhe1 > 0 and rookhe2 > 0:
    igheal = igheal - 26
   elif rookhe2 > 0 or rookhe1 > 0:
    igheal = igheal - 13
  elif command == 'I' or command == 'i':
   print("Mini Rookie 1's health:" , rookhe1)
   print("Mini Rookie 2's health:" , rookhe2)
   print("Mini Rookie's damage:" , rookde)
  elif command != 'A' or command != 'H' or command != 'I' or command != 'a' or command != 'h' or command != 'i':
   print("Invalid function!")
  if igheal <= 0 and rookhe1 > 0 and rookhe2 > 0:
   igheal = yourheal
   rookhe1 = rookhe
   rookhe2 = rookhe
  if rookhe1 <= 0 and rookhe2 <= 0:
   command = str(input("Good start!"))
   command = str(input("But remember, you haven't finished yet! We have to face the second wave of robots!"))
   print("Wave 2")
   print("Ultra Rook: You've beat these little boys, but you saw nothing...")
   print("You will now feel the power of the ultra!")
   