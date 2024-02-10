yourdmg = 25
yourheal = 197
igheal = 197
yourrev = 25/100*yourheal
wins = 2
lo = 0
rook = '1'
rookde1 = 17 ## ROOKDE IS ROOKIE'S MORE COMMON DAMAGE POTENTIAL.
rookhe = 149 ## ROOKHE IS ROOKIE'S HEALTH.
while rookhe > 0:
 command = str(input("Input A to attack the enemy, H to heal yourself, or I to check the enemy stats!"))
 if command == 'A':
  rookhe = rookhe - 25
  print(rookhe)
  igheal = igheal - 17
  print(igheal)
 elif command == 'H':
  igheal = igheal + yourrev
  if igheal > yourheal:
   igheal = 197
  print(rookhe)
  igheal = igheal - 17
  print(igheal)
 elif command == 'I':
  print("Rookie's stats:")
  print("Damage:" , rookde1)
  print("Health:" , rookhe)
print("Victory!")
