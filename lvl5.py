print("Level 5.")
wave = 1
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
rookde1 = rookde
rookhe1 = rookhe
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
 while wins == 5:
  print(igheal)
  if rookhe1 > 0:
   command = str(input("Type A to hit the rookie, H to heal yourself, or I to check their info!"))
  if command == 'A' or command == 'a':
   rookhe1 = rookhe1 - 25
   igheal = igheal - rookde
   rookhe1 = rookhe1 - yourdmg
  elif command == 'H' or command == 'h':
   if igheal < yourheal:
    igheal = igheal + yourrev
    print(igheal)
   if igheal >= yourheal:
    igheal = yourheal
  elif command == 'I' or command == 'i':
   print("Rookie 1's health:" , rookhe1)
   print("Rookie's damage:" , rookde)
  elif command != 'A' or command != 'H' or command != 'I' or command != 'a' or command != 'h' or command != 'i':
   print("Invalid function!")
  if igheal <= 0 and rookhe1 > 0 and rookhe2 > 0:
   igheal = yourheal
   rookhe1 = rookhe
   rookhe2 = rookhe
  if rookhe1 <= 0:
   wave = wave + 1
   command = str(input("Good start!"))
   command = str(input("But remember, you haven't finished yet! We have to face the second wave of robots!"))
   print("Wave 2")
   command = str(input("Ultra Rook: You've beat these little boys, but you saw nothing..."))
   command = str(input("You will now feel the power of the ultra!"))
   command = str(input("Jerry: Well this clearly won't be easy... but worry not! I found someone who can help!"))
   command = str(input("Ulrea Rookie: You mean this guy? *insert a man stuck in a cage*"))
   command = str(input("Jerry: Oh no! Well we have to destroy the cage first!"))
   cagehealth = 110
   urookhe1 = urookhe
   while wave == 2:
    if cagehealth > 0:
     command = str(input("Type A to hit either the ultra rookie or the cage, H to heal yourself, or I to check their info!"))
    if command == 'A' or command == 'a':
      command = str(input("Input U to hit the ultra rookie, or input C to hit the cage."))
      if command == 'C' or command == 'c':
       cagehealth = cagehealth - 25
      elif command == 'U' or command == 'u':
       urookhe1 = urookhe1- 25
      igheal = igheal - urookde
    elif command == 'H' or command == 'h':
     if igheal < yourheal:
      igheal = igheal + yourrev
      print("Health currently:" , igheal)
     if igheal >= yourheal:
      igheal = yourheal
     igheal = igheal - urookde
    elif command == 'I' or command == 'i':
     print("Ultra Rookie's health:" , urookhe1)
     print("Cage's health:" , cagehealth)
     print("Ultra Rookie's damage:" , urookde)
    elif command != 'A' or command != 'H' or command != 'I' or command != 'a' or command != 'h' or command != 'i':
     print("Invalid function!")
    if cagehealth <= 0:
     command = str(input("WIzard: Unleahing the power of MAGIC!"))
     command = str(input("Ultra Rookie: Wait wait wait wait- NOOOOOOOO-"))
     urookhe1 = 0
     wave = 3
     wins = 6
elif command != 'p' or command != 'P':
 print("invalid option!")
if wins == 6:
 wizhe = 110
 wizde = 21
 print("NEW CHARACTER UNLOCKED!")
 print("Wizard")
 print("Common")
 print("STATS")
 print("Health:" , wizhe)
 print("Damage:" , wizde)