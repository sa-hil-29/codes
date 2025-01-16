from random import randint

num = randint(1,100)
guesses = []
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

while True:
    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))
    guesses.append(guess)
    if (guess<1 or guess > 100):
        print("OUT OF BOUNDS! Please try again:")
    else:
        if(len(guesses) == 1):
            if(guess == num):
                print("Congratulations! you won")
                print("It took {} guesses for you to guess correct number.".format(len(guesses)))
                break
            elif( abs(num - guess) <= 10 ):
                print("WARM!")
            else:
                print("COLD!")
        else:
            if(guess == num):
                print("Congratulations! you won")
                print("It took {} guesses for you to guess correct number.".format(len(guesses)))
                break
            elif( abs(num - guess) <= abs(num- guesses[-2])):
                print("WARMER!")
            else:
                print("COLDER!")
        
    
