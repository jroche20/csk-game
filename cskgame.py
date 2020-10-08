

import random
import sys
import time
from art import *

# This fancy code prints out the cool header art! Don't worry if you don't understand it.
header = text2art("2020")
print(header)

# This magical code defines a function slow_type that prints text slowly, as if it's being typed! Don't worry if you don't understand it.
typing_speed = 350
def slow_type(msg):
    for letter in msg:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')

################################################
# ~ Intro ~

# Below is an example of calling a function.
slow_type("Welcome to 2020: The Pandemic The Game.")

slow_type("Congratulations. \
You're living in the year of toilet paper, mask, and hand sanitizer shortages. \
After your city issues quarantine restrictions, you decide to pick up a new hobby. \
Answer these questions to find the best hobby for you!\n")

print()

def island_options(item):
    slow_type("Item: " + item[0])
    slow_type("Description - " + item[1])
    slow_type("Drawbacks - " + item[2])

cooking = ["cooking tools", "some seasoning, utensils, a whisk", "depends on the ingredients on the island"]
phone = ["a phone", "Netflix, games, a camera", "there's no internet connection, but maybe you downloaded a movie beforehand?"]
raft = ["a raft", "pretty self explanatory but you can try escaping the island", "who knows how far the nearest people are..."]
survive = ["survival tools", "knife, fishing net, matches", "you can't account for every challenge on a deserted island"]

slow_type("If you were stranded on a deserted island (like being quarantined...), which item would you want with you?")
island_options(cooking)
island_options(phone)
island_options(raft)
island_options(survive)

recipes = ["pasta", "chocolate cake", "pancakes", "ramen"]

# Functions strip and lower help clean the input answer so that it matches our expected answer, such as simply "amy".
print()
choice = (input("Type which item you would want - cooking, phone, raft, tools: ")).strip().lower()
print()

if choice == "cooking":
    slow_type("An aspiring chef! \
Quarantine is the perfect time to pick up some cooking skills. \
There are endless recipes to choose from. \n")
    print()
    your_item = cooking
    slow_type("But now you may ask... what should I cook? \
Answer these questions to find the recipe you should try out. \n")
    print()
    slow_type("If you could have any kind of food for the rest of your life, what would it be? ")
    recipechoice = (input("Type which item you would want - pasta, chocolate cake, pancakes, ramen: ")).strip().lower()
    print()
    if recipechoice == "pasta":
        slow_type("Carbs are always a great option! Which kind of carb would you prefer - pasta or bread? ")
        carbchoice = (input()).strip().lower()
        if carbchoice == "pasta":
            slow_type("Why not try making some homemade pasta while in quarantine? \
            Here's a link to get you started: https://leitesculinaria.com/40229/recipes-homemade-pasta-dough.html \n")
        else:
            slow_type("Hop on the bandwagon and make some bread! \
Sourdough's a great option, but you better get started on that starter: https://www.feastingathome.com/sourdough-bread/ \n")
    elif recipechoice == "chocolate cake":
        slow_type("There's always room for dessert! ")
        dessertchoice = (input("Would you consider yourself a baker already? y/n--> ")).strip().lower()
        if dessertchoice == "y":
            slow_type("Already a baker? Try some challenging recipes, like macarons (https://tasty.co/recipe/macarons). ")
        else:
            slow_type("Go with a classic, like chocolate chip cookies, or just a good 'ol chocolate cake. ")
    elif recipechoice == "pancakes":
        slow_type("Breakfast IS the most important meal of the day! Do you prefer a sweet or savory breakfast? ")
        breakfastchoice = (input("Type sweet or savory: ")).strip().lower()
        if breakfastchoice == "sweet":
            slow_type("Get up early tomorrow morning and make some crepes! ")
        else:
            slow_type("Why not try making an eggs benedict? ")
    else:
        slow_type("Ramen is always there, but why not try some similar recipes? ")
        print()
        soupchoice = (input("Are you a soup person? y/n ")).strip().lower()
        if soupchoice == "y":
            slow_type("Ramen's good, but try out different recipes, like pho. ")
        else:
            slow_type("If you want some more Asian food, try out making some homemade sushi or poke bowls. ")
elif choice == "phone":
    slow_type("Can't let go of your phone? \
Well, Netflix, Hulu, and Disney+ are always there to help you through those hours of boredom. \
Binge all the shows you want while in quarantine.\n")
    print()
    your_item = phone
    slow_type("Bored already? Let's see which show you should binge next... ")
    print()
    slow_type("You have 3 books in front of you, each with a different genre -- sci-fi, action, or drama.")
    print()
    bookchoice = (input("Which would you choose? ")).strip().lower()
    if bookchoice == "sci-fi":
        print("Sci-Fi... Why not trying out The Mandalorian on Disney+ or Umbrella Academy on Netflix? ")
    elif bookchoice == "action":
        print("Action... You can go for a classic, like Indiana Jones, or go with a more recent movie, like Spider-Man: Into the Spider-Verse. ")
    else:
        print("Drama... Try out The Crown on Netflix or This is Us on Hulu. ")
elif choice == "tools":
    slow_type("Very smart choice. Since you're a practical person, try picking up a practical skill while in quarantine. ")
    slow_type("Answer these questions to see which skill you should learn. ")
    print()
    move = (input("If you had the means, would you pick up your things this instant and move to somewhere you've always wanted to live? y/n--> ")).strip().lower()
    craft = (input("Would you consider yourself a crafty person? y/n--> "))
    speak = (input("Would you consider yourself an outgoing person? y/n--> "))
    #knit = (input("Have you always wante"))

    if move == "y" and speak == "y":
        slow_type("As an adventurous and spontaneous person, you should learn a new language! Might come in handy when you do get to live in your dream location! ")
    elif move =="n" and speak == "n":
        slow_type("As more of a cautious and quiet person, you should try improving your public speaking skills! Practice in front of a mirror! ")
    elif move == "y" and speak == "y":
        slow_type("As more of an outgoing person, try learning how to sing! Youtube is always there for random tutorials. ")
    elif move == "n" and craft == "n":
        slow_type("Since you aren't crafty... why not learning how to craft? Try DIY'ing something and starting different projects!")
    elif move == "y" and craft == "y":
        slow_type("Try learning a new instrument!")
    else:
        slow_type("Why not slow down and learn how to knit/embroider? Make some clothes for yourself!")

else:
    your_item = raft
    slow_type("Ah yes, trying to escape. \
Well the bad thing is, you can't escape quarantine. \
But maybe you should try getting some physical exercise. \n")
    print()
    print("Let's see which activity you should try next. ")
    print()
    slow_type("If you were to go on vacation (not right now of course), where would you go - the outdoors or a new city? ")
    vacationchoice = (input("Type outdoors or city: ")).strip().lower()
    if vacationchoice == "outdoors":
        print("Fresh air is always nice. Go on a hike or a run on a local trail, but remember to social-distance and wear a mask! ")
    else:
        slow_type("If you were visiting this new city, would you rather walk and see all the sights, or visit a museum/exhibition? ")
        citychoice = (input("Type walk or museum: ")).strip().lower()
        if citychoice == "walk":
            slow_type("Physical exercise is always good. Get started by looking up 20 min workout videos on Youtube. ")
        else:
            slow_type("If you're more of a relaxed and calm person, try out yoga to ease the stress of quarantine. ")

print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()

slow_type("Now that you have suggestions for what to do, let's make sure you're ready to get through this pandemic. ")
house = (input("What should you never leave your house without? ")).strip().lower()

if house == "keys":
    slow_type("Well yes, but there's something else... a mask! ")
elif house == "a mask":
    slow_type("CORRECT. Please wear a mask!")
elif house == "mask":
    slow_type("CORRECT. Please wear a mask!")
else:
    slow_type("Don't forget to always... bring a mask!!")

print()
chin = (input("Next, if you were trying to drink water, would you pull your mask down under your chin? y/n--> ")).strip().lower()
if chin == "y":
    slow_type("Please don't pull your mask under your chin to your neck. You should instead have a clean paper bag with you to put your mask in! ")
else:
    slow_type("Good job! The best practice is to put your mask in a clean paper bag. ")

print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()

slow_type("Like Groundhog Day, let's see if you'll have good luck for the rest of the year!")
dice = int(input("Pick a number from 1-4. "))
slow_type("Rolling the dice...")
rand = random.randint(1,4)
if dice == rand:
    slow_type("Yay! You will have good luck for the rest of 2020! :)")
else:
    slow_type("Well, you didn't roll good luck, but at least everyone's in the same boat, so it'll be bad for everyone! :)")


print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
slow_type("2020 has been a crazy year. But if you remember to continue practicing good habits, you will get through the year! \
Don't forget to social-distance ALWAYS and don't wear your mask under your nose because that's just counterintuitive. \n")
footer = text2art("!!!")
print(footer)
slow_type("You wake up and realize it was all a nightmare... or is it?")
