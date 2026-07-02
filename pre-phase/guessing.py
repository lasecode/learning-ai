#Number Guessing Game
import random

def guess(choice, difficult):
    count = 1
    while True:
        if choice != difficult:
            count += 1
            print("Fail")
            value = try_again()
            if value == False:
                break
            else:
                choice = value
        else:
            print("Correct")
            print(f"It took {count} attempt(s)")
            break
    

def try_again():
    retry = input("Do you want to try again(Y/n): ")
    if retry.lower() == 'y':
        choice = int(input("guess: "))
        return choice
    elif retry.lower() == "n":
        print("Goodbye")
        return False
        

def main():
    print("\nNumber Guessing Game")
        
    difficulty = input("\nChoose Difficulty(E/M/H): ")

    if difficulty.lower() == "e":
        easy = random.randint(0,10)
        choice = int(input("1-10: "))
        guess(choice, easy)
    elif difficulty.lower() == "m":
        medium = random.randint(0,50)
        choice = int(input("1-50: "))
        guess(choice, medium)
    if difficulty.lower() == "h":
        hard = random.randint(0,100)
        choice = int(input("1-100: "))
        guess(choice, hard)
    
        
    
if __name__ == "__main__":
    main()