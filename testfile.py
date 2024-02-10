print("Have you already played the tutorial before?")
package = str(input("Type yes to skip it, or type no to play it."))
if package == 'no':
 wins = 0 ## wins determine how many battles you have won. 
 print("hello")
 print("my name is omer")
 name = str(input("wHAT IS YOUR NAME?")) ## str is the declearation for string data type in python
 print("nice to meet you," , name )
 print("I hope we could get along.")
 print("WAIT! WHAT WAS THAT NOISE?!")
 print("Great... it is the menancing robotic duo, Larry and Lawrie! We have to defeat them. GO!")
 yourdmg = 7 
 yourheal = 50 
 igheal = yourheal
 attack2 = 3
 health2 = 17
 print("LARRY: Well, I can't believe I have to do this... anyways... let's go!")
 print("Larry is the first robot you have to defeat. You have to input hit to attack them. ")
 while health2 > 0:
  print("Your current health is:" , igheal)
  print("Your turn!")
  command = str(input("Type hit to attack Larry."))
  if command == 'hit':
   health2 = health2 - yourdmg
   print("Larry's health is" , health2)
   print("Larry's turn!")
   igheal = igheal - attack2
  elif command != 'hit':
   print("Type hit to attack!")
 print("Congratulations! You won with" , igheal ,"health left.") 
 wins = wins + 1
 print("OMER: Well great job! Though you still have to deal with lawrie...")
 print("Lawrie: DON'T THINK YOU GOT THE HANG OF THIS TOO EARLY. HE IS JUST AN INNOCENT LAD. I AM THE REAL THREAT TO YOUR EXISTANCE.")
 print("OMER: You can upgrade your gear with the help of coins! Here, let me donate you some!")
 coins = 50 ## coins is the currency for the game.
 print("You got" , coins , "coins!")
 print("YOUR INVENTORY")
 print("Your offense gear: 7 damage.")
 up = 10
 dmgle = 1 ## dmgle is the way to prevent gaining infinite damage
 heale = 1 ## heale is the way to prevent gaining infinite health
 command = str(input("Upgrade costs 10 coins. Type yes to upgrade damage by +18."))
 while command == 'yes' and dmgle < 2:
   coins == coins - up
   yourdmg = yourdmg + 18 
   dmgle = dmgle + 1
   print("Damage has been upgraded. Your offense gear now deals 25 damage.")
 print("Your defense gear: 50 health.")
 command = str(input("Upgrade costs 10 coins. Type yes to upgrade health by +147."))
 while command == 'yes' and heale < 2:
  coins == coins - up
  yourheal = yourheal + 147
  heale = heale + 1
  print("health has now been upgraded. Your defense gear now keeps you alive with 197 health.")
 print("OMER: THAT IS MORE LIKE IT! NOW LET'S GO KICK LAWRIE OUTTA HERE AND SHOW HIM SOME STREGNTH!")
 print("LAWRIE: AW LOOK WHO'S HERE. YOU THINK SOME ADOPTION WILL GIVE YOU SO CALLED 'STREGNTH'?! HAHAHAHAHAHAHA")
 print("OMER: don't let his insults get you carried away. Stay focused brothers, STAY FOCUSED!")
 lawrihe = 312
 lawride = 34
 igheal = yourheal
 print("Lawrie's health is" , lawrihe)
 print("Lawrie's damage is" , lawride)
 print("OMER:Oh well... seems like this might not have been as easy as we would have thought...")
 print("OMER: But fear not! I forgot to tell you something... level 2 health gear unlocks the ability to heal yourself!")
 yourrev = 25/100*yourheal
 lo = 1
 while lo < 2:
  print("your current health is" , igheal)
  print("Lawrie's current health is" , lawrihe)
  print("Your turn!")
  command = str(input("Type 'heal' to heal yourself, or type 'hit' to attack!"))
  if command == 'hit' and igheal > 0 and lawrihe > 0:
   lawrihe = lawrihe - yourdmg
   print("Lawrie's turn!")
   igheal = igheal - lawride
  elif command == 'heal' and igheal > 0 and lawrihe > 0:
   igheal = igheal + yourrev
   print("Lawrie's turn!")
   igheal = igheal - lawride
  elif command != 'heal' and command != 'hit' and igheal > 0 and lawrihe > 0:
   print("Type hit to attack, or type heal to heal yourself!")
  if lawrihe <= 0 and igheal <= 0:
   lo = lo + 2
  elif igheal <= 0:
   lo = lo + 1
  elif lawrihe <= 0:
   lo = lo + 2
 if lo == 3:
  wins = wins + 1
  print("LAWRIE: CURSE YOU! YOU WILL PAY FOR THIS! I AM TELLING YOU... THI- THI- TH-")
  print("OMER: FINALLY! We defeated them and got him out of here. Now we can focus more on our own skills. Come and join forces with me as we go on to explore the outside world of cruel robots abusing their power to take over the world. The struggle is endless, but is sure going to be worth it!")
 elif lo == 2:
  print("LAWRIE: HAHAHAHAHAHAHA! YOU'RE. NOT. MOVING. ANYWHERE!")
  print("GAME OVER")
  print("Battles won:" , wins)
  print("MADE BY OMER ARFAN")
  print("EXECUTE THE FILE AGAIN TO RETRY AND HAVE A SECOND CHANCE")
  command = str(input("Input anything to quit."))
  exit
 if wins == 2:
  print("You found a crate!")
  print("A crate is of a random rarity... the chances start from Super Common rarity and can go up to Cosmic rarity.")
  print("The higher the rarity, the better the rewards!")
 elif wins != 2:
  exit
 LUCKIE = 0
 from random import random
 prime = random() ## PRIME IS THE GEMERATED VALUE
 gene = prime*1000000 ## GENE IS SHORT FOR GENERATION. GENERATION WILL DEFINE THE RARITY OF THE CRATE.
 gene = gene - LUCKIE
 if gene <= 1000000 and gene >= 500000:
  rarity = 'Super Common'
  LUCKIE = LUCKIE + 10
 elif gene < 500000 and gene >= 250000:
  rarity = 'Common'
  LUCKIE = LUCKIE + 10
 elif gene < 250000 and gene >= 125000:
  rarity = 'Rare'
  LUCKIE = LUCKIE + 10
 elif gene < 125000 and gene >= 62500:
  rarity = 'Super Rare'
  LUCKIE = LUCKIE + 10
 elif gene < 62500 and gene >= 31250:
  rarity = 'Ultra Rare'
  LUCKIE = LUCKIE + 10
 elif gene < 31250 and gene >= 15625:
  rarity = 'Epic'
  LUCKIE = LUCKIE + 10
 elif gene < 15625 and gene >= 7815:
  rarity = 'Mythic'
  LUCKIE = LUCKIE + 10
 elif gene < 7815 and gene >= 3910:
  rarity = 'Exotic'
  LUCKIE = LUCKIE + 10
 elif gene < 3910 and gene >- 1955:
  rarity = 'Legendary!'
  LUCKIE = LUCKIE + 4
 elif gene < 1955 and gene >= 391:
  rarity = 'Champion!'
  LUCKIE = LUCKIE + 3
 elif gene < 391 and gene >= 78:
  rarity = 'Galactic!'
  LUCKIE = LUCKIE + 2
 elif gene < 78 and gene >= 1:
  rarity = 'UNIVERSAL!'
  LUCKIE = LUCKIE + 1
 elif gene < 1:
  rarity = 'COSMIC!!!'
  LUCKIE = 0
 command = str(input("Input anything for to reveal your crate rarity!"))
 print(rarity)
 if rarity == 'Super Common':
  rew = 4
  print(rew)
  coins = coins + rew
  print(coins)
  command = str(input("Input anything to continue..."))
 elif rarity == 'Common':
  rew = 9
  print(rew)
  coins = coins + rew
  print(coins)
  command = str(input("Input anything to continue..."))
 elif rarity == 'Rare':
  rew = 20
  print(rew)
  coins = coins + rew
  print(coins)
  command = str(input("Input anything to continue..."))
 elif rarity == 'Super Rare':
  rew = 45
  print(rew)
  coins = coins + rew
  print(coins)
  command = str(input("Input anything to continue..."))
 elif rarity == 'Ultra Rare':
  rew = 102
  print(rew)
  coins = coins + rew
  print(coins)
  command = str(input("Input anything to continue..."))
 elif rarity == 'Epic':
  rew = 207
  print(rew)
  coins = coins + rew
  print(coins)
  command = str(input("Input anything to continue..."))
 elif rarity == 'Mythic':
  rew = 431
  print(rew)
  coins = coins + rew
  print(coins)
  command = str(input("Input anything to continue..."))
 elif rarity == 'Exotic':
  rew = 902
  print(rew)
  coins = coins + rew
  print(coins)
  command = str(input("Input anything to continue..."))
 elif rarity == 'Legendary!':
  rew = 2001
  print(rew)
  coins = coins + rew
  print(coins)
  command = str(input("Input anything to continue..."))
 elif rarity == 'Champion!':
  rew = 4391
  print(rew)
  coins = coins + rew
  print(coins)
  command = str(input("Input anything to continue..."))
 elif rarity == 'Galactic!':
  rew = 9772
  print(rew)
  coins = coins + rew
  print(coins)
  command = str(input("Input anything to continue..."))
 elif rarity == 'UNIVERSAL!':
  rew = 21134
  print(rew)
  coins = coins + rew
  print(coins)
  print("Dang you really feeling that luck eh?")
  command = str(input("Input anything to continue..."))
 elif rarity == 'COSMIC!!!':
  rew = 50000
  print(rew)
  coins = coins + rew
  print(coins)
  print("YOU HIT THE GOLDEN TICKET BABY!")
  command = str(input("Input anything to continue..."))
 print("Seems good!")
 command = str(input("Now well, you have a clear image of the basics of your journey..."))
 command = str(input("It is all on you to continue and conquer all the evil robots of this society..."))
 command = str(input("But don't worry! I'll still be there to help when there's something new!"))
elif package == 'yes':
 yourrev = 49
 yourdmg = 25
 yourheal = 197
 igheal = 197
 yourrev = 25/100*yourheal
 yourrev = round(yourrev, 0)
 wins = 0
 heale = 2
 dmgle = 2
 while wins < 2:
  wins = int(input("Input the number of wins you have.(2 to 3)"))
 coins = 30
 LUCKIE = 0
 from random import random
 prime = random() ## PRIME IS THE GEMERATED VALUE
 gene = prime*1000000 ## GENE IS SHORT FOR GENERATION. GENERATION WILL DEFINE THE RARITY OF THE CRATE.
 gene = gene - LUCKIE
 if gene <= 1000000 and gene >= 500000:
  rarity = 'Super Common'
  LUCKIE = LUCKIE + 10
 elif gene < 500000 and gene >= 250000:
  rarity = 'Common'
  LUCKIE = LUCKIE + 10
 elif gene < 250000 and gene >= 125000:
  rarity = 'Rare'
  LUCKIE = LUCKIE + 10
 elif gene < 125000 and gene >= 62500:
  rarity = 'Super Rare'
  LUCKIE = LUCKIE + 10
 elif gene < 62500 and gene >= 31250:
  rarity = 'Ultra Rare'
  LUCKIE = LUCKIE + 10
 elif gene < 31250 and gene >= 15625:
  rarity = 'Epic'
  LUCKIE = LUCKIE + 10
 elif gene < 15625 and gene >= 7815:
  rarity = 'Mythic'
  LUCKIE = LUCKIE + 10
 elif gene < 7815 and gene >= 3910:
  rarity = 'Exotic'
  LUCKIE = LUCKIE + 10
 elif gene < 3910 and gene >- 1955:
  rarity = 'Legendary!'
  LUCKIE = LUCKIE + 4
 elif gene < 1955 and gene >= 391:
  rarity = 'Champion!'
  LUCKIE = LUCKIE + 3
 elif gene < 391 and gene >= 78:
  rarity = 'Galactic!'
  LUCKIE = LUCKIE + 2
 elif gene < 78 and gene >= 1:
  rarity = 'UNIVERSAL!'
  LUCKIE = LUCKIE + 1
 elif gene < 1:
  rarity = 'COSMIC!!!'
  LUCKIE = 0
 if rarity == 'Super Common':
  rew = 4
  coins = coins + rew
 elif rarity == 'Common':
  rew = 9
  coins = coins + rew
 elif rarity == 'Rare':
  rew = 20
  coins = coins + rew
 elif rarity == 'Super Rare':
  rew = 45
  coins = coins + rew
 elif rarity == 'Ultra Rare':
  rew = 102
  coins = coins + rew
 elif rarity == 'Epic':
  rew = 207
  coins = coins + rew
 elif rarity == 'Mythic':
  rew = 431
  coins = coins + rew
 elif rarity == 'Exotic':
  rew = 902
  coins = coins + rew
 elif rarity == 'Legendary!':
  rew = 2001
  coins = coins + rew
 elif rarity == 'Champion!':
  rew = 4391
  coins = coins + rew
 elif rarity == 'Galactic!':
  rew = 9772
  coins = coins + rew
 elif rarity == 'UNIVERSAL!':
  rew = 21134
  coins = coins + rew
 elif rarity == 'COSMIC!!!':
  rew = 50000
  coins = coins + rew
elif package != 'yes' or package != 'no':
 print("Pick either one of these options.")
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
while exit == False:
 print("Input P to play!")
 print("Input I to have a look at your inventory!")
 print("Input E to quit!")
 command = str(input("Enter an option here..."))
 if command == 'P':
  while levelexit == False:
   print("The map you are playing:")
   if wins < 9:
    print("THE ROOTLESS JUNGLE")
    if wins == 2:
     print("Your stats:")
     lo = 0
     print(yourdmg)
     print(yourheal)
     print("Rookie's stats:")
     print(rookde)
     print(rookhe)
     gaco = str(input("To play level 3, input play."))
     if gaco == 'play':
      win = False
      lose = False
      while win == False:
       igheal == 197
       while win == False or lose == False and rookhe <= 0 or igheal <= 0:
        command = str(input("Input A to attack the enemy, H to heal yourself, or I to check the enemy stats!"))
        if command == 'A':
         rookhe = rookhe - yourdmg
         print("Rookie's health is:" , rookhe)
         igheal = igheal - rookde
         print("Your current health is:" , igheal)
        elif command == 'H':
         igheal = igheal + yourrev
         igheal = round(igheal, 0)
         if igheal > yourheal:
          igheal = 197
         print(rookhe)
         igheal = igheal - rookde
         print(igheal)
        elif command == 'I':
         print("Rookie's stats:")
         print("Damage:" , rookde)
         print("Health:" , rookhe)
        if rookhe <= 0:
         win == True
         command = str(input("Level 3 cleared!"))
         wins = 3
        elif igheal <= 0:
         lose == True
         igheal = 197
         igheal == yourheal
         print("Level failed!")
         print("Try again for a second chance!")
         command = str(input("Input anything to continue..."))
    if wins == 3:
     print("Level 4.")
     print("Mini Rookie's damage:" , mrookde)
     print("MIni Rookie's health:" , mrookhe)
     mrookhe1 = mrookhe
     mrookhe2 = mrookhe
     gaco = str(input("To play the level enter p."))
     if gaco == 'p' or gaco == 'P':
      win = False
      lose = False
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
       if igheal <= 0 and (mrookhe1 >= 0 or mrookhe2 >= 0):
        igheal = yourheal
        mrookhe1 = mrookhe
        mrookhe2 = mrookhe
        command = str(input("Level failed! Try again!"))
 if command == 'I':
  command == str(input("Type D to check your damage upgradability, or type H to check you health upgradability."))
  Upexit == False
  if command == 'D':
   while Upexit == False:
    print("Your current damage:" , yourdmg)
    print("Coins remaining:" , coins)
    print("Damage level:" , dmgle) 
    if dmgle < 3:
     dmgup = yourdmg*0.1
     command = str(input("The upgrade will cost 20 coins. Type anything else to cancel the upgrade, or type U to upgrade damage by " , dmgup))
     if command == 'U' and coins >= 20:
      yourdmg == yourdmg + dmgup 
      dmgle = dmgle + 1
      coins = coins - 20
      print("Damage upgraded!")
     elif command == 'U' and coins < 20:
      print("Not enough coins!")
      Upexit == True
     elif command != 'U':
      Upexit == True
    if dmgle < 4 and coins >= 50:
     dmgup = yourdmg*0.1
     command = str(input("The upgrade will cost 50 coins. Type anything else to cancel the upgrade, or type U to upgrade damage by " , dmgup))
     if command == 'U' and coins >= 20:
      yourdmg == yourdmg + dmgup 
      dmgle = dmgle + 1
      coins = coins - 50
      print("Damage upgraded!")
     elif command == 'U' and coins < 50:
      print("Not enough coins!")
      Upexit == True
     elif command != 'U':
      Upexit == True
    if dmgle < 5 and coins >= 200:
     dmgup = yourdmg*0.1
     command = str(input("The upgrade will cost 200 coins. Type anything else to cancel the upgrade, or type U to upgrade damage by " , dmgup))
     if command == 'U' and coins >= 200:
      yourdmg == yourdmg + dmgup 
      dmgle = dmgle + 1
      coins = coins - 200
      print("Damage upgraded!")
     elif command == 'U' and coins < 200:
      print("Not enough coins!")
      Upexit == True
     elif command != 'U':
      Upexit == True
    if dmgle < 6 and coins >= 500:
     dmgup = yourdmg*0.1
     command = str(input("The upgrade will cost 500 coins. Type anything else to cancel the upgrade, or type U to upgrade damage by " , dmgup))
     if command == 'U' and coins >= 500:
      yourdmg == yourdmg + dmgup 
      dmgle = dmgle + 1
      coins = coins - 500
      print("Damage upgraded!")
     elif command == 'U' and coins < 500:
      print("Not enough coins!")
      Upexit == True
     elif command != 'U':
      Upexit == True
    if dmgle < 7 and coins >= 1000:
     dmgup = yourdmg*0.1
     command = str(input("The upgrade will cost 1000 coins. Type anything else to cancel the upgrade, or type U to upgrade damage by " , dmgup))
     if command == 'U' and coins >= 1000:
      yourdmg == yourdmg + dmgup 
      dmgle = dmgle + 1
      coins = coins - 1000
      print("Damage upgraded!")
     elif command == 'U' and coins < 1000:
      print("Not enough coins!")
      Upexit == True
     elif command != 'U':
      Upexit == True
    if dmgle < 8 and coins >= 2000:
     dmgup = yourdmg*0.1
     command = str(input("The upgrade will cost 2000 coins. Type anything else to cancel the upgrade, or type U to upgrade damage by " , dmgup))
     if command == 'U' and coins >= 2000:
      yourdmg == yourdmg + dmgup 
      dmgle = dmgle + 1
      coins = coins - 2000
      print("Damage upgraded!")
     elif command == 'U' and coins < 2000:
      print("Not enough coins!")
      Upexit == True
     elif command != 'U':
      Upexit == True
    if dmgle < 9 and coins >= 3000:
     dmgup = yourdmg*0.1
     command = str(input("The upgrade will cost 3000 coins. Type anything else to cancel the upgrade, or type U to upgrade damage by " , dmgup))
     if command == 'U' and coins >= 3000:
      yourdmg == yourdmg + dmgup 
      dmgle = dmgle + 1
      coins = coins - 3000
      print("Damage upgraded!")
     elif command == 'U' and coins < 3000:
      print("Not enough coins!")
      Upexit == True
     elif command != 'U':
      Upexit == True
    if dmgle < 10 and coins >= 4000:
     dmgup = yourdmg*0.1
     command = str(input("The upgrade will cost 4000 coins. Type anything else to cancel the upgrade, or type U to upgrade damage by " , dmgup))
     if command == 'U' and coins >= 4000:
      yourdmg == yourdmg + dmgup 
      dmgle = dmgle + 1
      coins = coins - 4000
      print("Damage upgraded!")
     elif command == 'U' and coins < 4000:
      print("Not enough coins!")
      Upexit == True
     elif command != 'U':
      Upexit == True
    if dmgle < 11 and coins >= 5000:
     dmgup = yourdmg*0.1
     command = str(input("The upgrade will cost 5000 coins. Type anything else to cancel the upgrade, or type U to upgrade damage by " , dmgup))
     if command == 'U' and coins >= 5000:
      yourdmg == yourdmg + dmgup 
      dmgle = dmgle + 1
      coins = coins - 5000
      print("Damage upgraded!")
      print("Damage gear at MAX level!")
     elif command == 'U' and coins < 5000:
      print("Not enough coins!")
      Upexit == True
     elif command != 'U':
      Upexit == True
    if dmgle == 11:
     print("Already at MAX level!")
     Upexit == True
  if command == 'H':
   while Upexit == False:
    print("Your current health:" , yourheal)
    print("Coins remaining:" , coins)
    print("Health level:" , heale) 
    if heale < 3:
     heup = yourheal*0.1
     command = str(input("The upgrade will cost 20 coins. Type anything else to cancel the upgrade, or type U to upgrade health by " , dmgup))
     if command == 'U' and coins >= 20:
      yourheal == yourheal + heup 
      heale = heale + 1
      coins = coins - 20
      print("Health upgraded!")
     elif command == 'U' and coins < 20:
      print("Not enough coins!")
      Upexit == True
     elif command != 'U':
      Upexit == True
    if heale < 4 and coins >= 50:
     heup = yourheal*0.1
     command = str(input("The upgrade will cost 50 coins. Type anything else to cancel the upgrade, or type U to upgrade health by " , dmgup))
     if command == 'U' and coins >= 20:
      yourheal == yourheal + heup 
      heale = heale + 1
      coins = coins - 50
      print("Health upgraded!")
     elif command == 'U' and coins < 50:
      print("Not enough coins!")
      Upexit == True
     elif command != 'U':
      Upexit == True
    if heale < 5 and coins >= 200:
     heup = yourheal*0.1
     command = str(input("The upgrade will cost 200 coins. Type anything else to cancel the upgrade, or type U to upgrade health by " , dmgup))
     if command == 'U' and coins >= 200:
      yourheal == yourheal + heup 
      heale = heale + 1
      coins = coins - 200
      print("Health upgraded!")
     elif command == 'U' and coins < 200:
      print("Not enough coins!")
      Upexit == True
     elif command != 'U':
      Upexit == True
    if heale < 6 and coins >= 500:
     heup = yourheal*0.1
     command = str(input("The upgrade will cost 500 coins. Type anything else to cancel the upgrade, or type U to upgrade health by " , dmgup))
     if command == 'U' and coins >= 500:
      yourheal == yourheal + heup 
      heale = heale + 1
      coins = coins - 500
      print("Health upgraded!")
     elif command == 'U' and coins < 500:
      print("Not enough coins!")
      Upexit == True
     elif command != 'U':
      Upexit == True
    if heale < 7 and coins >= 1000:
     heup = yourheal*0.1
     command = str(input("The upgrade will cost 1000 coins. Type anything else to cancel the upgrade, or type U to upgrade health by " , dmgup))
     if command == 'U' and coins >= 1000:
      yourheal == yourheal + heup 
      heale = heale + 1
      coins = coins - 1000
      print("Health upgraded!")
     elif command == 'U' and coins < 1000:
      print("Not enough coins!")
      Upexit == True
     elif command != 'U':
      Upexit == True
    if heale < 8 and coins >= 2000:
     heup = yourheal*0.1
     command = str(input("The upgrade will cost 2000 coins. Type anything else to cancel the upgrade, or type U to upgrade health by" , dmgup))
     if command == 'U' and coins >= 2000:
      yourheal == yourheal + heup 
      heale = heale + 1
      coins = coins - 2000
      print("Health upgraded!")
     elif command == 'U' and coins < 2000:
      print("Not enough coins!")
      Upexit == True
     elif command != 'U':
      Upexit == True
    if heale < 9 and coins >= 3000:
     heup = yourheal*0.1
     command = str(input("The upgrade will cost 3000 coins. Type anything else to cancel the upgrade, or type U to upgrade health by " , dmgup))
     if command == 'U' and coins >= 3000:
      yourheal == yourheal + heup 
      heale = heale + 1
      coins = coins - 3000
      print("Health upgraded!")
     elif command == 'U' and coins < 3000:
      print("Not enough coins!")
      Upexit == True
     elif command != 'U':
      Upexit == True
    if heale < 10 and coins >= 4000:
     heup = yourheal*0.1
     command = str(input("The upgrade will cost 4000 coins. Type anything else to cancel the upgrade, or type U to upgrade health by " , dmgup))
     if command == 'U' and coins >= 4000:
      yourheal == yourheal + heup 
      heale = heale + 1
      coins = coins - 4000
      print("Health upgraded!")
     elif command == 'U' and coins < 4000:
      print("Not enough coins!")
      Upexit == True
     elif command != 'U':
      Upexit == True
    if heale < 11 and coins >= 5000:
     heup = yourheal*0.1
     command = str(input("The upgrade will cost 5000 coins. Type anything else to cancel the upgrade, or type U to upgrade health by " , dmgup))
     if command == 'U' and coins >= 5000:
      yourheal == yourheal + heup 
      heale = heale + 1
      coins = coins - 5000
      print("Health upgraded!")
      print("Health gear at MAX level!")
     elif command == 'U' and coins < 5000:
      print("Not enough coins!")
      Upexit == True
     elif command != 'U':
      Upexit == True
    if heale == 11:
     print("Already at MAX level!")
     Upexit == True
  
  if command != 'H' or command != 'D':
   command = str(input("Input H or D to check inventory. Or to quit, type Q."))
   if command == 'Q':
    Upexit == True
 if command == 'E':
  command = str(input("Are you sure you want to quit? Type yes to quit."))
  if command == 'yes':
   exit = True