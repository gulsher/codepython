secret_word = "dog"

guess =""
guess_count = 0
guess_limit = 3
out_of_guess = False

while guess != secret_word and not(out_of_guess):
    if guess_count < guess_limit:
        guess = input("Enter the Guess:")
        guess_count += 1
    else:
        print("chances are over")
        out_of_guess= True
    
if(out_of_guess):
    print("you lose")
else:
    print("you win")