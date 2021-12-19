import random
print('Hello. What is your name?')
name=input()
num=random.randint(1,20)
print('DEBUG: The guessed number is : ' + str(num))
print('Well, '+ name+ ' , I am thinking of a number between 1 to 20')

#Ask player to guess 6 times

for guessesTaken in range(1,7): # or we can use range(6)
    print('Take a guess.')
    try:
        guess = int(input())
        if guess < num:
            print('Your guess is too low')
        elif guess > num:
            print('Your guess is too high')
        else:
            break # for correct guess
    except ValueError:
        print('You did not enter a number')

if guess == num:
    print('Good job, ' + name + '! You guessed my number correctly in ' + str(guessesTaken) + ' guesses!')
    # if range(6) is used in for loop, we have to use str(guessesTaken + 1)
else:
    print('Nope. The number I was thinking of was ' + str(num))
    
