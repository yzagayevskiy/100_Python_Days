# Day 3 Project - Escape Game
print('''
***************************************
                /\                     
               /**\                    
              /****\   /\              
             /      \ /**\             
            /  /\    /    \            
           /  /  \  /      \           
          /  /    \/ /\     \          
         /  /      \/  \/\   \         
      __/__/_______/___/__\___\        
***************************************
''')
print("Welcome to Cabin in the Mountains!")
print("Your mission is to safely escape the freezingly cold cabin. \n")

choice1 = input('You\'ve woken in the freezingly cold cabin that appears to be in the mountains by the view from the window. What do you want to do? Type "nothing" or "explore". \n').lower()
if choice1 == "explore":
  choice2 = input('You\'ve found three doors: red, blue, and green. Which door do you want to open? Type "red", "blue", or "green". \n').lower()
  if choice2 == "red":
    print("It's a fridge room. Game Over.")
  elif choice2 == "blue":
    choice3 = input('This room has a fire place and another door. What do you do? Type "start fire", "check door", or "nothing". \n').lower()
    if choice3 == "start fire":
      print("The fireplace warmth gives you heat for some time, but there are only so many logs. Game Over.")
    elif choice3 == "check door":
      print("It is an exit from the cabin! You Win!")
    elif choice3 == "nothing":
      print("You\'ve got a frost bite. Game Over.")
    else:
      print("You\'ve chosen an option that doesn't exist. Game Over.")
  elif choice2 == "green":
    print('You\'ve got attacked by an angry bear. Game Over.')
  else:
    print("You\'ve chosen an option that doesn't exist. Game Over.")
elif choice1 == "nothing":
  print('You\'ve got a frost bite. Game Over.')
else:
  print("You\'ve chosen an option that doesn't exist. Game Over.")
