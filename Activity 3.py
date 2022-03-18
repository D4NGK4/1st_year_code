import random as rand

print("stuff")

print("Submitted By; Dan Joshua M. Tagaan_IT1R12")

lives = 3

# ans = 
while True:
    try:
        while lives != 0:
            num1 = rand.randint(1, 500)
            num2 = rand.randint(1, 500)
            sum = num1 + num2

            print("Lives {}".format(lives))
            ans=int(input(f"{num1} + {num2}="))
            if ans != sum:
                lives -= 1
            else:
                print("Correct!")
                break

            if lives == 0:
                print("You Lose!")
        break
    except ValueError:
        print("Wrong Value, please try again.")
