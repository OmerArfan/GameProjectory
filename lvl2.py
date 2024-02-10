yourheal = 197
igheal = 197
lawrihe = 312
lawride = 34
yourdmg = 197
yourrev = 25/100*yourheal
lo = 1
wins = 1
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
 if igheal <= 0:
  lo = lo + 1
 elif lawrihe <= 0:
  lo = lo + 2

if lo == 1:
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
 print("never gonna give you up!")