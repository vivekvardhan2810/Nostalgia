import time

def introduction():
    print("Welcome to the Nostalgic Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious place.")
    time.sleep(1)
    print("Your goal is to explore and uncover the secrets of this place.")
    time.sleep(1)

def choose_path():
    print("Choose your path:")
    print("1. Go left")
    print("2. Go right")
    print("3. Go straight")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        print("You went left and discovered an old library.")
        time.sleep(1)
        print("Inside the library, you find a dusty book.")
        time.sleep(1)
        print("The book reveals the history of the mysterious place.")
    elif choice == "2":
        print("You went right and stumbled upon a hidden garden.")
        time.sleep(1)
        print("In the garden, you find a well with a ladder leading down.")
        time.sleep(1)
        print("Do you want to climb down the ladder? (yes/no)")
        decision = input()
        if decision.lower() == "yes":
            print("You descend into a forgotten underground chamber.")
            time.sleep(1)
            print("The chamber is filled with ancient artifacts.")
        else:
            print("You decide not to climb down the ladder.")
    elif choice == "3":
        print("You went straight and entered a dark cave.")
        time.sleep(1)
        print("Inside the cave, you hear mysterious echoes.")
        time.sleep(1)
        print("You feel a sense of adventure as you explore deeper into the cave.")
    else:
        print("Invalid choice. Please enter a valid number.")
        choose_path()

def main():
    introduction()
    choose_path()

if __name__ == "__main__":
    main()
