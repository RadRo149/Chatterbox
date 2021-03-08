#Chatterbox
import time
name = input("Enter name: ")
print(f"\n Hello {name.title()}! Welcome to chatterbox! Answer the questions below to continue!")
no = input("Enter a number from 0-9: ")
no = int(no)
if no % 2 != 0:
    print(f"\nOk {name.title()}, now choose between 0, 1, 16, or 25.")
    odd_no = input("So, what number?: ")
    odd_no = int(odd_no)
    if odd_no == 0:
        print("Wanna play rock paper scissors?\n")
        from random import randint
        go = ["r", "p", "s"]
        computer = go[randint(0,2)]
        test = False
        while test == False:
            player = input("Rock (r), Paper (p), Scissors (s), Quit (q)?: ")
            if player == computer:
                print("It is a tie")
            elif player == "r":
                if computer == "p":
                    print("You lose!", computer, "covers", player)
                else:
                    print("You win!", player, "smashes", computer)
            elif player == "p":
                if computer == "s":
                    print("You lose!", computer, "cuts", player)
                else:
                    print("You win!", player, "covers", computer)
            elif player == "s":
                if computer == "r":
                    print("You lose...", computer, "smashes", player)
                else:
                    print("You win!", player, "cuts", computer)
            elif player == "q":
                test = True
            else:
                print("That is not valid. Pls check your spelling!")
            player = False
    elif odd_no == 1:
        print("Hangman time!")
        import random
        print(f"\nGood Luck, {name.title()}!")
        words = ['mathematics', 'music', 'languages', 'service', 
                'humanities', 'science', 'english', 'lifeskills', 
                'art', 'drama', 'physicaleducation', 'designtechnology', 'advisory', 'itp'] 
        word = random.choice(words)
        print("\nGuess the characters in the word")
        print("\nHint: all are school subjects")
        guesses = ''
        turns = 9
        while turns > 0:
            failed = 0
            for char in word: 
                if char in guesses: 
                    print(char)
                else: 
                    print("_")
                    failed += 1
            if failed == 0:
                print("You Win") 
                print(f"\nThe word is {word}!") 
                break
            guess = input("\nGuess a character:")
            guesses += guess 
            if guess not in word:
                turns -= 1
                print("\nWrong")
                print("You have", + turns, 'more guesses')
                if turns == 0:
                    print(f"\nYou Lose. The word was {word}")
    elif odd_no == 16:
        print("\nYou now have a choice to go to the fortune teller! If you want to do it, type '11', but if not, type in '00'.")
        choice = input("Whaddya say?: ")
        if choice == "11":
            print("\nOk, now stare into the imaginary ball and wait: ")
            time.sleep(4.91)
            print("\nYou will get some new pants!\n")
        elif choice == "00":
            print("\nYou are a radical rockstar and you are very talented and smart!")
        else:
            print("\nYou lose.")
    elif odd_no == 25:
        choc = input("Enter the amount of chocolate you have or want to have in a week (1-9): ")
        choc = int(choc)
        born = input("what year were you born?: ")
        born = int(born)
        year = input("What year is it?: ") 
        year = int(year)
        ifyou = input("Enter 1757 if you had your birthday this year, if not, enter 1756: ")
        ifyou = int(ifyou)
        haha = input("Just say if you are amazed with the number that will show up, ok?: ")
        num1 = input("Age: ")
        num1 = int(num1)
        num2 = input("Birth date (eg. 24 of December 2008, you just put 24): ")
        num2 = int(num2)
        num3 = input("Birth Month Number: ")
        num3 = int(num3)
        num5 = input("Any number (1-10): ")
        num5 = int(num5)
        num6 = input("Previous computer number/2-didget number: ")
        num6 = int(num6)
        num7 = input("Lucky Number (<100 & >0): ")
        num7 = int(num7)
        num4 = input("Enter a 3-didget number that is 900-999: ")
        num4 = int(num4)
        result = (choc * 2 + 5) * 50 + ifyou - born + (year - 2007)
        spec_no = num1 - num2 - num3 - num5 - num6 - num7 + born - result - num4
        print(f"\nHi {name.title()}! Your number is {result}. The first diget is the amount of chocolate you want to eat, and the last two are your age! Also, your ultra lucky number this year is {spec_no}! If that number is not a 3-diget number (or maybe a 2-diget for the youngsters), you were just messing with me. I know when you do mess with me anyway, it comes on my record, so I can track you. But if you got a 3-diget number, you're fine, right? \n{haha.title()} \nExactly! Ok, gotta go now, bye!")
    else:
        print("\nYou lose.")
elif no % 2 == 0:
    print(f"\nOk {name.title()}, now choose between 4, 9, 36, or 49")
    eve_no = input("So, what number?: ")
    eve_no = int(eve_no)
    if eve_no == 4:
        print(f"\nHey, {name.title()}, wanna calculate?.")
        done = False
        while not done:
            import time
            print("|A)Addition                |")
            print("|S)Subtraction             |")
            print("|M)Multiplication          |")
            print("|D)Division                |")
            print("|E)Exponents               |")
            print("|Q)Quit                    |")
            usr_choice = input(">>")
            if usr_choice == "A" or usr_choice == "a":
                print("What is A?")
                a = input(">>")
                a = int(a)
                print("What is B?")
                a2 = input(">>")
                a2 = int(a2)
                print("PROCESSING DATA...")
                time.sleep(1.49)
                print(a+a2)
            elif usr_choice == "S" or usr_choice == "s":
                print("What is A?")
                s = input(">>")
                s = int(s)
                print("What is B?")
                s2 = input(">>")
                s2 = int(s2)
                print("PROCESSING DATA...")
                time.sleep(1.49)
                print(s-s2)
            elif usr_choice == "M" or usr_choice == "m":
                print("What is A?")
                m = input(">>")
                m = int(m)
                print("What is B?")
                m2 = input(">>")
                m2 = int(m2)
                print("PROCESSING DATA...")
                time.sleep(1.49)
                print(m*m2)
            elif usr_choice == "D" or usr_choice == "d":
                print("What is A?")
                d = input(">>")
                d = int(d)
                print("What is B?")
                d2 = input(">>")
                d2 = int(d2)
                if d2 == ZeroDivisionError:
                    print("That is an invalid sum, please do not divide by 0!")
                else:
                    print("PROCESSING DATA...")
                    time.sleep(1.49)
                    print(d/d2)
            elif usr_choice == "E" or usr_choice == "e":
                print("What is A?")
                e = input(">>")
                e = int(e)
                print("What is B?")
                e2 = input(">>")
                e2 = int(e2)
                print("PROCESSING DATA...")
                time.sleep(1.49)
                print(e**e2)
            elif usr_choice == "49":
                print("Wow, you are really smart!")
                time.sleep(1.49)
                print("WHY DID YOU DO THAT?!")
            print("\nTry Again?")
            if usr_choice == "Q" or usr_choice == "q":
                done = True
                print("\nOk, cya!")
            else:
                print("\n|A)Addition                |")
                print("|S)Subtraction             |")
                print("|M)Multiplication          |")
                print("|D)Division                |")
                print("|E)Exponents               |")
                print("|Q)Quit                    |")
                usr_choice = input(">>")
    elif eve_no == 9:
        coun = input("Where are you from?: ")
        on = input("Choose, 8 or 9: ")
        on = int(on)
        if on == 8:
            print(f"\nYou are being crushed by {coun.title()}.")
        elif on == 9:
            print(f"\nYou can lift {coun.title()}.")
        else:
            print("\nYou lose.")
    elif eve_no == 36:
        print("Hello, welcome to Roan's trivium quiz (not trivial)!")
        ans0 = input("Are you ready to play (yes/no): ")
        score = 0
        totalq = 4
        if ans0.lower() == "yes":
            ans = input("1. What is my name?: ")
            if ans.lower() == "roan":
                score += 1
            ans2 = input("2. What is my favourite colour?: ")
            if ans2.lower() == "red":
                score += 1
            ans3 = input("3. What is my age?: ")
            if ans3 == "12":
                score += 1
            ans4 = input("4. What is my favourite band?: ")
            if ans4.lower() == "trivium":
                score += 1
            print("Thank you for playing", score, "questions correct")
            mark = (score/totalq)*100
            print("Mark:", mark, "%")
        print("Good game!")
    elif eve_no == 49:
        print("\nYou have entered a guessing game, so continue...")
        guess_count = 0
        guess_count = int(guess_count)
        guess_limit = 9
        outofguesses = False
        guess = ""
        secret_word = "stop"
        while guess != secret_word and not (outofguesses):
            if guess_count < guess_limit:
                guess = input("Enter Guess: ")
                guess_count += 1
                if guess != "stop":
                    print("Wrong! You have", 9 - guess_count,"turns left.")
            else:
                outofguesses = True
        if outofguesses:
            print("\nYou lose.")
        else:
            print("\nYou win! The word was 'stop'")
    else:
        print("\nYou lose.")
else:
    print("\nYou lose.")