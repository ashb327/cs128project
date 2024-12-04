import matplotlib.pyplot as plt

#introduction code
def introduction():
    print("Welcome to Earlham College, new student. Give us some information about yourself.")
    going = True
    while going:
        user_character=input("Please select your gender (Male/Female):")
        if user_character.lower() == "male" or user_character.lower() == "female":
            going = False
            #do another if statement depending on whether they are male or female that gives them the correct avatar
        else:
            going = True
    
    character_name=input("Please enter character name: ")
    character = str(character_name)
    print(character.capitalize() + ", you are a freshman at Earlham College, ")

total_points = 0


def choice_function(choice):
    global total_points
    if choice == 'A':
        total_points+=2
        #print("current points: ", total_points)
        return total_points
    elif choice == 'B':
        total_points+=1
        #print("current points: ", total_points)
        return total_points
    elif choice == 'C':
        total_points+=0
        #print("current points: ", total_points)
        return total_points

def abc_valid():
    invalid = True
    while invalid:
        answer = input("Answer:")
        if answer.upper() == "A" or answer.upper() == "B" or answer.upper() == "C":
            invalid = False
            return answer.upper()
        else:
            invalid = True

def ab_valid():
    invalid = True
    while invalid:
        answer = input("Answer:")
        if answer.upper() == "A" or answer.upper() == "B": 
            invalid = False
            return answer.upper()
        else:
            invalid = True

#chapter one code
def breakfast():
    print ("It's time to eat breakfast")
    print ("A. Eat breakfast")
    print("B. Skip breakfast.")
    answer = ab_valid()
    choice_function(answer)
    if answer == "A":
        breakfast_open_map()
    if answer == "B":
        print ("You skipped breakfast, now you have no energy for the day.")

crumbl = 0

def breakfast_open_map():
    global crumbl
    print ("Please choose a breakfast")
    print ("A. Eggs with avocado toast")
    print("B. Cereal with milk ")
    print("C. 10 Crumbl cookies")
    answer = abc_valid()
    choice_function(answer)
    if answer == "A":
        print("Good! That is a healthy meal, and you feel energized for the day.")
    elif answer == "B":
        print("This option is okay. You feel moderately energized for the day.")
    else:
        print("You feel awful and sick.")
        crumbl += 1
        #return crumbl
def get_ready(choice):
    if choice == "A":
        print ("Now, you are getting ready for class")
        print ("A. Morning routine (wash face, brush teeth, etc)")
        print("B. Change clothes and scroll on social media. ")
        print("C. Go straight to eating breakfast.")
        print("Please choose A, B, or C.")
        answer=abc_valid()
        choice_function(answer)
        
        if answer == "A":
            print("You are washed up and ready for the day.")
        elif answer == "B":
            print("You scrolled social media.")
        else:
            print("You went straight to breakfast.")
        breakfast()
            
    if choice == "B" or choice =="C":
        print ("Now, you are getting ready for class.")
        print ("A. Change clothes and scroll on social media. ")
        print("B. Go straight to eating breakfast.")
        print("Please choose A or B.")
        answer=ab_valid()
        choice_function(answer)
        if answer == "A":
            print("You scrolled social media.")
            breakfast()
        elif answer == "B":
            print("You went straight to breakfast.")
            breakfast()

def check_weather():
    print("Check the weather")
    print("A. Check the weather")
    print("B. Skip checking the weather")
    answer = ab_valid()
    choice_function(answer)

    if answer == "A":
        print("It's 32 degrees outside")
        print("Choose to wear a jacket?")
        print ("A. Yes")
        print("B. No")
        ans = ab_valid()
        choice_function(answer)
        if ans == "A":
            print("You are warm.")
        else:
            print("You are freezing.")
  
    if answer == "B":
        print("You didn't check the weather, so you did not wear a jacket. It is freezing!")

def chapter_one():
    print ("It's 7:00 AM and you have to wake up for your class")
    print ("A. Wake up")
    print("B. Sleep 5 minutes more")
    print("C. Sleep 30 more minutes")
    print("Please choose A, B, or C.")
    answer = abc_valid()
    choice_function(answer)

    if answer == "A":
        get_ready(answer) 
        check_weather()
        print("You made it to school!")
        chapter_two()
    
    if answer == "B":
        print("You slept for five minutes more.")
        get_ready(answer) 
        check_weather()
        print("You made it to school!")
        chapter_two()
    
    if answer == "C":
        print ("You are going to be late for school unless you leave immediately without being able to properly get ready.")
        chapter_two()


total_grades = []

#chapter two code
def math_hw1():
    math_grade = 0
    user_input = input("2+1= ")
    if user_input == '3':
        print("Correct.")
        math_grade += 25
    else:
        print("Incorrect.")

    user_input = input("3+5= ")
    if user_input == '8':
        print("Correct.")
        math_grade += 25
    else:
        print("Incorrect.")

    user_input = input("7*3= ")
    if user_input == '21':
        print("Correct.")
        math_grade += 25
    else:
        print("Incorrect.")

    user_input = input("4*8= ")
    if user_input == '32':
        print("Correct.")
        math_grade += 25
    else:
        print("Incorrect.")
    
    print("Here is your homework grade: ", math_grade)
    total_grades.append(math_grade)

def math_hw2():
    math_grade = 0
    user_input = input("4+9= ")
    if user_input == '13':
        print("Correct.")
        math_grade += 25
    else:
        print("Incorrect.")

    user_input = input("9*8= ")
    if user_input == '72':
        print("Correct.")
        math_grade += 25
    else:
        print("Incorrect.")

    user_input = input("4*6= ")
    if user_input == '24':
        print("Correct.")
        math_grade += 25
    else:
        print("Incorrect.")

    user_input = input("3+10= ")
    if user_input == '13':
        print("Correct.")
        math_grade += 25
    else:
        print("Incorrect.")
    
    print("Here is your homework grade: ", math_grade)
    total_grades.append(math_grade)


def english_homework1():
    grade = 0
    print("Retype these sentences with proper grammar.")
    
    #problem 1
    print("Problem 1:")
    print("The old man was very funny but he did not make me laugh")
    user_correction = input("Your correction: ")
    if user_correction == "The old man was very funny, but he did not make me laugh.":
        print("Correct!")
        grade += 50
    else:
        print("Incorrect.")

    #problem 2
    print("Problem 2:")
    print("he was angry at her, he hated it.")
    user_correction2 = input("Your correction: ")
    if user_correction2 == "He was angry at her, and he hated it." or user_correction2 == "He was angry at her. He hated it.":
        print("Correct!")
        grade += 50
    else:
        print("Incorrect.")
    print("Here is your homework grade: ", grade)
    total_grades.append(grade)

    

#def math_lab():
    

def math_lab_choice():
    print("It is time for your math lab. What do you do?")
    print("A. Go to the lab session.")
    print("B. Skip it.")
    answer = ab_valid()
    choice_function(answer)

    if answer == "A":
        print("You go to the math lab.")
        print("Time for your math exercises!")
        math_hw2()

    if answer == "B":
        print("You did not go to the math lab.")
        
def lunch_options():
    global crumbl
    print("Here are your choices:")
    print("A. Sandwich")
    print("B. Cereal")
    print("C. 10 crumbl cookies")
    answer = abc_valid()
    choice_function(answer)
    if answer == "A":
        print("The sandwich was yummy. You are energized.")
    if answer == "B":
        print("The cereal was alright, but you're not very energized from it.")
    if answer == "C": 
        crumbl += 1
            #print("You died from eating 20 crumbl cookies in one day. Game over.")
            #endscreen function
        print("You feel sick and awful.")
    math_lab_choice()

def lunch():
    
    print("It is now noon. It is lunch time! What do you do?")
    print("A. Eat lunch.")
    print("B. Skip lunch.")
    answer = ab_valid()
    choice_function(answer)
    if answer == "A":
        lunch_options()
    if answer == "B":
        print("You are extremely tired.")
        math_lab_choice()
       

def history_class():
    print("Oh, it turns out your history professor is sick today and there will be no class. What do you do?")
    print("A. Study for your exams.")
    print("B. Get on your phone.")
    print("C. Email your teacher that he should have been here.")
    answer = abc_valid()
    choice_function(answer)

    if answer == "A":
        print("You studied for your exams and will be very prepared!")
    if answer == "B":
        print("You spent your time on your phone, but you could have spent more time studying.")
    if answer == "C":
        print("Your teacher will not be pleased with you.")
    lunch()
def english_class():
    print("You arrived at english class. Time to do your in-class exercises.")
    english_homework1()
    print("Good job. You finished your exercises. It is currently 10:50am.")
    history_class()

def english_choose():
    print("A. Go to your english class.")
    print("B. Go get coffee from the coffee shop ten minutes away.")
    print("C. Skip class.")
    answer = abc_valid()
    choice_function(answer)

    if answer == "A":
        english_class()
    if answer == "B":
        print("You are a little late to class.")
        english_class()
    if answer == "C":
        print("You skipped class. It is now 10:50am.")
        history_class()

def math_class():
    print("You made it to math class. Time to do in-class exercises.")
    math_hw1()
    print("Class is over. It is 9:50am. What will you do?")
    english_choose()
    


def chapter_two():
    print("Here is your class schedule for today:")
    print("9am: Math")
    print("10am: English")
    print("11am: History")
    print("12pm: Lunch")
    print("2:30pm: Math Lab")

    print("It is 8:50am. What will you do?")
    print("A. Go to your math class.")
    print("B. Talk to friends.")
    print("C. Skip class.")
    answer = abc_valid()
    choice_function(answer)

    if answer == "A":
        print("You are on time!")
        math_class()
    if answer == "B":
        print("You are late to class.")
        math_class()
    if answer == "C":
        print("You didn't go to class.")
        print("It is now 9:50am. What do you do?")
        english_choose()
        
def end():
    print ("CONGRADUATION!YOU HAVE COMPLETED YOUR DAY!!!!")
    
    print ("Here is your total points: " + str(total_points)+"/32")
    if total_points >=25:
        print("Your choices, at least for the most part, were good choices. You are a good student, and you will be successful!")
    elif total_points>15 and total_points<25:
        print("Your choices, at least for the most part, were okay choices. You are an average student, and you will probably do fine in life.")
    else:
        print("Your choices, at least for the most part, were bad choices. You are not a very good student. You will probably fail in life.")
    print("Here is the summary for your performance from the classes for the day.")
    fig, ax = plt.subplots()
    x = ["math hw1","english hw", "math hw2"]
    y = total_grades
    
    fig = plt.figure(figsize=(10,5))
    
    ax.bar(x, y, color = "maroon", width=0.8)
    ax.set_title("Random bar plot")
    ax.set_xlabel("Random x")
    ax.set_ylabel("Random y")
    plt.show()
    print

def night_routine():
    print("It is almost time for bed. How will you end off your night?")
    print("A. Brush your teeth and do your skincare routine.")
    print("B. Brush your teeth.")
    print("C. Slowly fall asleep while looking at your phone and not preparing for bed.")
    answer = abc_valid()
    choice_function(answer)
    if answer == "A":
        print("You feel amazing and peaceful as you fall asleep. You have splendid dreams.")
    if answer == "B":
        print("You fall asleep fine.")
    if answer == "C":
        print("Your sleep is dreadful and you feel very unrested.")
    end()
def after_dinner():
    print("Now you have a few options on what to do next.")
    print("A. Study for your exams")
    print("B. Take a shower")
    print("C. Play videogames")
    answer = abc_valid()
    choice_function(answer)

    if answer == "A":
        print("You are going to ace those exams!")
    if answer == "B":
        print("You feel refreshed and relaxed, but a bit sleepy now.")
    if answer == "C":
        print("You wasted your night.")
    night_routine()
def dinner():
    global crumbl
    print("You open the fridge and decide what to eat...")
    print("A. Steak with asparagus")
    print("B. Cereal")
    print("C. 10 crumbl cookies...")
    answer = abc_valid()
    choice_function(answer)

    if answer == "A":
        print("You feel well fed and ready to study for the night.")
        after_dinner()  
    if answer == "B":
        print("You are okay, but it makes you want to snack more throughout the night.")
        after_dinner()  
    if answer == "C":
        crumbl += 1
        print("You are going to die from a heart attack in a few days.")
        if crumbl ==3:
            print ("You chose to eat 30 crumbl cookies during the days and END UP GOING TO THE HOSPITAL. GAME OVER!!!!")
        else:
            after_dinner()  




def chapter_three():
    print("You just finished your day at school, and now you have come back to your dorm for the night.")
    print("Do you eat dinner?")
    print("A. Yes")
    print("B. No")
    answer = ab_valid()
    choice_function(answer)

    if answer == "A":
        dinner()
    else:
        print("You starve.")
        after_dinner()

introduction()
chapter_one()
chapter_three()
