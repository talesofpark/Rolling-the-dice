import random

playing = True
times = 0
while playing: 
    choice = input("Roll the dice? (y/n): ").lower() #to always treat the result as lower case
    if choice == "y":
        num_of_iterations = (input("How many times? "))
        n=1
        if num_of_iterations == type(int):
            print("Invalid Choice!")
        else: 
            while n <= int(num_of_iterations): 
                die1 = random.randint(1,6)
                print(f"({die1})")
                n +=1 
        times += int(num_of_iterations)
    elif choice == "n": 
        print(f"Thank you for playing! You have played {times} times!")
        break
    else: 
        print("Invalid Choice!")





    
