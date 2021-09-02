from flask import Flask
app = Flask(__name__)


@app.route('/hi')
def hi():
    return "Nice work"

@app.route('/sayhito $name')
def print_hi(name):
    return "Hi, {0}".format(name)

@app.route('/count')
def count(*items):
    return str(len(items))

@app.route('/exit')
def exit():
    import sys
    sys.exit(0)

@app.route('/Entry')
def Entry(name):
    return f"Welcome you {name}"

@app.route('/Exit')
def Exit(name):
    return f"Have A Nice Day ! {name}"

@app.route('/add')
def add(num1,num2):
    return num1 + num2 

@app.route('/subtract')
def subtract(num1,num2):
    return num1 - num2

@app.route('/multiply')
def multiply(num1,num2):
    return num1 * num2 

@app.route('/divide')
def divide(num1,num2):
    return num1 / num2

@app.route('/guessgame')
def guessgame():
    import random
    number = random.randint(1, 10)

    player_name = input("Hello, What's your name?")
    number_of_guesses = 0
    print('okay! ' + player_name + ' I am Guessing a number between 1 and 10:')

    while number_of_guesses < 5:
        guess = int(input())
        number_of_guesses += 1
        if guess < number:
            print('Your guess is too low')
        if guess > number:
            print('Your guess is too high')
        if guess == number:
            break
    if guess == number:
        print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
    else:
        print('You did not guess the number, The number was ' + str(number))

@app.route('/BMI_Calculator')
def BMI_Calculator():
    Height=float(input("Enter your height in centimeters: "))
    Weight=float(input("Enter your Weight in Kg: "))
    Height = Height/100
    BMI=Weight/(Height*Height)
    print("your Body Mass Index is: ",BMI)
    if(BMI>0):
	    if(BMI<=16):
		    print("you are severely underweight")
	    elif(BMI<=18.5):
		    print("you are underweight")
	    elif(BMI<=25):
		    print("you are Healthy")
	    elif(BMI<=30):
		    print("you are overweight")
	    else: print("you are severely overweight")
    else:
        ("enter valid details")

@app.route('/Rock_Paper_Scissors')
def Rock_Paper_Scissors():
    import random
    choices = ["Rock", "Paper", "Scissors"]
    computer = random.choice(choices)
    player = False
    cpu_score = 0
    player_score = 0
    while True:
        player = input("Rock, Paper or  Scissors?").capitalize()
    
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
                cpu_score+=1
            else:
                print("You win!", player, "smashes", computer)
                player_score+=1
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
                cpu_score+=1
            else:
                print("You win!", player, "covers", computer)
                player_score+=1
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose...", computer, "smashes", player)
                cpu_score+=1
            else:
                print("You win!", player, "cut", computer)
                player_score+=1
        elif player=='End':
            print("Final Scores:")
            print(f"CPU:{cpu_score}")
            print(f"Plaer:{player_score}")
            break
