import random
def guess_num():
    num = random.randint(1, 100)
    counter = 0

    while True:
        guess = int(input("Enter your guess "))
        counter += 1
        if guess <num:
            print("Too Low!")
        elif guess >num:
            print("Too High!")
        else:
            print("Congratulations! You guessed the number.")
            print("Number of attempts", counter)
            break