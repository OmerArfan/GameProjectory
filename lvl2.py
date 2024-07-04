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
 print("S. U. 's current health is" , lawrihe)
 print("Your turn!")
 command = str(input("Type 'heal' to heal yourself, or type 'hit' to attack!"))
 if command == 'hit' and igheal > 0 and lawrihe > 0:
  lawrihe = lawrihe - yourdmg
  print("S. U. 's turn!")
  igheal = igheal - lawride
 elif command == 'heal' and igheal > 0 and lawrihe > 0:
  igheal = igheal + yourrev
  print("S. U.'s turn!")
  igheal = igheal - lawride
 elif command != 'heal' and command != 'hit' and igheal > 0 and lawrihe > 0:
  print("Type hit to attack, or type heal to heal yourself!")
 if lawrihe <= 0 and igheal <= 0:
  lo = 3
 elif igheal <= 0:
  lo = 3
 elif lawrihe <= 0:
  lo = 2
if lo == 3:
 wins = wins + 1
 print("S. U. : Oh wow... surely I underestimated you...")
 print("S. U. : Well... you are free to explore around now, but be careful!")
 print("Jerry: Wait, there are more robots out here? Well not complaining! Who doesn't love a fun challenge?")
elif lo == 2:
 print("Try again!")