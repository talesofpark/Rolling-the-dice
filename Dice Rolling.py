import random

playing = True
while playing: 
    choice = input("Roll the dice? (y/n): ").lower() #to always treat the result as lower case
    if choice == "y":
        num_of_iterations = input("How many times? ")
        n=0
        while n <= int(num_of_iterations): 
            die1 = random.randint(1,6)
            print(f"({die1})")
            n +=1 
    elif choice == "n": 
        print("Thank you for playing")
        break
    else: 
        print("Invalid Choice!")





    
