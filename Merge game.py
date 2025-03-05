quit = False
print("Oh hello! You seem new...")
print("ever wanted to upgrade new characters?")
print("Well... you are in the right place!")
reqxp = 100
lvl1 = 2
lvl2 = 0
lvl3 = 0
lvl4 = 0
lvl5 = 0
lvl6 = 0
lvl7 = 0
coins = 100
print("Look at these 2 little buddies...")
print(lvl1)
print("look cute, right?")
print("Let's merge them to make a stronger guy!")
command = input(str("Merge!"))
print("Upgraded!")
lvl1 = lvl1 -2
lvl2 = lvl2 +1
print("You currently have one level 2.")
print("This will help you dig out resources and increase your experience level!")
xp = 0
xp = xp + 100
if xp >= 100:
    print("Levelled up!")
    level = 2
    coins = coins + 100
    lvl1 = lvl1 + 1
    xp = xp - 100
while quit == False:
    print("Player Level:", level)
    print("Progress:" , xp ,"/", reqxp)
    command = input(str("Input I to see your inventory, or input S to see the shop! Input E to quit."))
    if command == 'I':
        print("You have:")
        print(lvl1 , "Level 1s.")
        print(lvl2 , "Level 2s.")
        print(lvl3 , "Level 3s.")
        print(lvl4 , "Level 4s.")
        print(lvl5 , "Level 5s.")
        print(lvl6 , "Level 6s.")
        print(lvl7 , "MAX levels.")
        command = input(str("Which level character do you wish to upgrade?Input level number only."))
        if command == '1':
          if lvl1 >= 2:
            print("Merge 2 Level 1s to make a Level 2!")
            command = input(str("Input 'upgrade' to get a new level 2!"))
            if command == 'upgrade':
               lvl1 = lvl1 - 2
               lvl2 = lvl2 + 1
               xp = xp + 100
          else:
            print("Not enough Level 1s.")
        if command == '2':
          if lvl2 >= 3:
            print("Merge 3 Level 2s to make a Level 3!")
            command = input(str("Input 'upgrade' to get a new level 3!"))
            if command == 'upgrade':
               lvl2 = lvl2 - 3
               lvl3 = lvl3 + 1
               xp = xp + 150
          else:
            print("Not enough Level 2s.")
        if command == '3':
          if lvl3 >= 5:
            print("Merge 5 Level 3s to make a Level 4!")
            command = input(str("Input 'upgrade' to get a new level 4!"))
            if command == 'upgrade':
               lvl3 = lvl3 - 5
               lvl4 = lvl4 + 1
               xp = xp + 300
          else:
            print("Not enough Level 3s.")
        if command == '4':
          if lvl4 >= 5:
            print("Merge 5 Level 4s to make a Level 5!")
            command = input(str("Input 'upgrade' to get a new level 5!"))
            if command == 'upgrade':
               lvl4 = lvl4 - 5
               lvl5 = lvl5 + 1
               xp = xp + 500
          else:
            print("Not enough Level 4s.")
        if command == '5':
          if lvl5 >= 5:
            print("Merge 5 Level 5s to make a Level 6!")
            command = input(str("Input 'upgrade' to get a new level 6!"))
            if command == 'upgrade':
               lvl5 = lvl5 - 5
               lvl6 = lvl6 + 1
               xp = xp + 1500
          else:
            print("Not enough Level 5s.")
        if command == '6':
          if lvl6 >= 10:
            print("Merge 10 Level 6s to create a new MAX level character!")
            command = input(str("Input 'upgrade' to get a new MAX level character!"))
            if command == 'upgrade':
               lvl6 = lvl6 - 10
               lvl7 = lvl7 + 1
               xp = xp + 10000
          else:
            print("Not enough Level 6s.")
        if command == '7':
          print("You have ", lvl7 ,"characters at MAX level!")
          print("More levels are coming soon!")
        if level < 5:
          if xp >= 100:
            xp = xp - 100
            level = level + 1
            coins = coins + 100
            lvl1 = lvl1 + 1
            print("Level up!")
            print("Level", level)
        elif level > 5 and level < 10:
          if xp >= reqxp:
            reqxp = 250
            xp = xp - reqxp
            level = level + 1
            coins = coins + 250
            lvl1 = lvl1 + 2
            print("Level up!")
            print("Level", level)
    if command == 'S':
      print("Coins:" ,coins)
      print("1: 10x Level 1s: 50 coins!(2x extra)")
      print("2: 10x Level 2s: 400 coins!(60% value!)")
      print("3: 5x Level 3s: 1000 coins!(5x value)")
      print("4: 1x Level 4: 2000 coins! (80% value)")
      command = input(str("Which offer do you want to buy?"))
      if command == '1':
        if coins < 50:
          print("Not enough coins.")
        else:
          lvl1 = lvl1 + 10
          print("Purchase successful!")
          coins = coins - 50
      elif command == '2':
        if coins < 400:
          print("Not enough coins.")
        else:
          lvl2 = lvl2 + 10
          print("Purchase successful!")
          coins = coins - 400
      elif command == '3':
        if coins < 1000:
          print("Not enough coins.")
        else:
          lvl3 = lvl3 + 5
          print("Purchase successful!")
          coins = coins - 1000
      elif command == '4':
        if coins < 2000:
          print("Not enough coins.")
        else:
          lvl4 = lvl4 + 1
          print("Purchase successful!")
          coins = coins - 2000
      else:
        print("Invalid option!")