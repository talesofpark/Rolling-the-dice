import random

playing = True
while playing: 
    choice = input("Roll the dice? (y/n): ").lower() #to always treat the result as lower case
    if choice == "y": 
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f"({die1}, {die2})")
    elif choice == "n": 
        print("Thank you for playing")
        break
    else: 
        print("Invalid Choice!")





    
