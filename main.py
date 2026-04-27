# Asha Thomas, Iman Patel, Mishal Siddiqui
# Animal Cafe: a user interactive memorization game where the player is allowed to choose their difficulty level (easy/medium/hard), their own character (cat/dog/monkey/bunny) and complete a various amount of orders with an turn counter. At the end of the day, the user is graded on their accuracy and either wins or loses!
# How to play: All you have to do to play the game is click ‘Play’ on the homescreen, click one of the difficulty buttons (changes the types of orders you will be required to complete), click on your desired chef animal, and start! When a customer appears, click on the ‘!’ by their head where you will see what they want you to make for them. Select the ‘Make Order’ button and click on the cake that’s correct. When you’re done, click on the ‘Done’ button. Depending on if you got it right or wrong, your score will update. Keep going until all 5 customers have been served!

import turtle
import random


s = turtle.getscreen()


# DICTIONARY FOR IMAGES & DESCRIPTIONS
# difficulties listed below (easy, medium, hard)
easy = {
"small plain vanilla cake": "small_plain_vanilla_CROPPED.gif",
"small plain vanilla cake with vanilla frosting": "small_plain_vanilla-vanilla_CROPPED.gif",
"small plain chocolate cake with vanilla frosting": "small_plain_vanilla-chocolate_CROPPED.gif",
"small plain vanilla cake with strawberry frosting": "small_plain_strawberry-vanilla_CROPPED.gif",
"small plain chocolate cake with strawberry frosting": "small_plain_strawberry-chocolate_CROPPED.gif",
"small plain chocolate cake": "small_plain_chocolate_CROPPED.gif",
"small plain vanilla cake with chocolate frosting": "small_plain_chocolate-vanilla_CROPPED.gif",
"small plain chocolate cake with chocolate frosting": "small_plain_chocolate-chocolate_CROPPED.gif",
"small vanilla cake with vanilla frosting and sprinkles": "small_decorated_vanilla-vanilla_CROPPED.gif",
"small chocolate cake with vanilla frosting and sprinkles": "small_decorated_vanilla-chocolate_CROPPED.gif",
"small vanilla cake with strawberry frosting and sprinkles": "small_decorated_strawberry-vanilla_CROPPED.gif",
"small chocolate cake with strawberry frosting and sprinkles": "small_decorated_strawberry-chocolate_CROPPED.gif",
"small vanilla cake with chocolate frosting and sprinkles": "small_decorated_chocolate-vanilla_CROPPED.gif",
"small chocolate cake with chocolate frosting and sprinkles": "small_decorated_chocolate-chocolate_CROPPED.gif"}


medium = {
"large plain vanilla cake with vanilla frosting ": "large_plain_vanilla-vanilla_CROPPED.gif",
"large plain chocolate cake with vanilla frosting": "large_plain_vanilla-chocolate_CROPPED.gif",
"large plain vanilla cake with strawberry frosting": "large_plain_strawberry-vanilla_CROPPED.gif",
"large plain chocolate cake with strawberry frosting": "large_plain_strawberry-chocolate_CROPPED.gif",
"large plain vanilla cake": "large_plain_vanilla_CROPPED.gif",
"large plain chocolate cake": "large_plain_chocolate_CROPPED.gif",
"large vanilla cake and sprinkles": "large_decorated_vanilla_CROPPED.gif",
"large vanilla cake with vanilla frosting and sprinkles": "large_decorated_vanilla-vanilla_CROPPED.gif",
"large chocolate cake with vanilla frosting and sprinkles": "large_decorated_vanilla-chocolate_CROPPED.gif",
"large vanilla cake with strawberry frosting and sprinkles": "large_decorated_strawberry-vanilla_CROPPED.gif",
"large chocolate cake with strawberry frosting and sprinkles": "large_decorated_strawberry-chocolate_CROPPED.gif",
"large chocolate cake and sprinkles": "large_decorated_chocolate_CROPPED.gif",
"large vanilla cake with chocolate frosting and sprinkles": "large_decorated_chocolate-vanilla_CROPPED.gif",
"large chocolate cake with chocolate frosting and sprinkles": "large_decorated_chocolate-chocolate_CROPPED.gif",
"large vanilla cake with chocolate frosting": "large_plain_chocolate-vanilla_CROPPED.gif",
"large chocolate cake with chocolate frosting": "large_plain_chocolate-chocolate_CROPPED.gif"}




hard = {
"small plain vanilla cake": "small_plain_vanilla_CROPPED.gif",
"small plain vanilla cake with vanilla frosting": "small_plain_vanilla-vanilla_CROPPED.gif",
"small plain chocolate cake with vanilla frosting": "small_plain_vanilla-chocolate_CROPPED.gif",
"small plain vanilla cake with strawberry frosting": "small_plain_strawberry-vanilla_CROPPED.gif",
"small plain chocolate cake with strawberry frosting": "small_plain_strawberry-chocolate_CROPPED.gif",
"small plain chocolate cake": "small_plain_chocolate_CROPPED.gif",
"small plain vanilla cake with chocolate frosting": "small_plain_chocolate-vanilla_CROPPED.gif",
"small plain chocolate cake with chocolate frosting": "small_plain_chocolate-chocolate_CROPPED.gif",
"small vanilla cake with vanilla frosting and sprinkles": "small_decorated_vanilla-vanilla_CROPPED.gif",
"small chocolate cake with vanilla frosting and sprinkles": "small_decorated_vanilla-chocolate_CROPPED.gif",
"small vanilla cake with strawberry frosting and sprinkles": "small_decorated_strawberry-vanilla_CROPPED.gif",
"small chocolate cake with strawberry frosting and sprinkles": "small_decorated_strawberry-chocolate_CROPPED.gif",
"small vanilla cake with chocolate frosting and sprinkles": "small_decorated_chocolate-vanilla_CROPPED.gif",
"small chocolate cake with chocolate frosting and sprinkles": "small_decorated_chocolate-chocolate_CROPPED.gif",
"large plain vanilla cake with vanilla frosting ": "large_plain_vanilla-vanilla_CROPPED.gif",
"large plain chocolate cake with vanilla frosting": "large_plain_vanilla-chocolate_CROPPED.gif",
"large plain vanilla cake with strawberry frosting": "large_plain_strawberry-vanilla_CROPPED.gif",
"large plain chocolate cake with strawberry frosting": "large_plain_strawberry-chocolate_CROPPED.gif",
"large plain vanilla cake": "large_plain_vanilla_CROPPED.gif",
"large plain chocolate cake": "large_plain_chocolate_CROPPED.gif",
"large vanilla cake and sprinkles": "large_decorated_vanilla_CROPPED.gif",
"large vanilla cake with vanilla frosting and sprinkles": "large_decorated_vanilla-vanilla_CROPPED.gif",
"large chocolate cake with vanilla frosting and sprinkles": "large_decorated_vanilla-chocolate_CROPPED.gif",
"large vanilla cake with strawberry frosting and sprinkles": "large_decorated_strawberry-vanilla_CROPPED.gif",
"large chocolate cake with strawberry frosting and sprinkles": "large_decorated_strawberry-chocolate_CROPPED.gif",
"large chocolate cake and sprinkles": "large_decorated_chocolate_CROPPED.gif",
"large vanilla cake with chocolate frosting and sprinkles": "large_decorated_chocolate-vanilla_CROPPED.gif",
"large chocolate cake with chocolate frosting and sprinkles": "large_decorated_chocolate-chocolate_CROPPED.gif",
"large vanilla cake with chocolate frosting": "large_plain_chocolate-vanilla_CROPPED.gif",
"large chocolate cake with chocolate frosting": "large_plain_chocolate-chocolate_CROPPED.gif"}


# lists for the customer + walk functions
customer_list = ["customer_1.gif", "customer_2.gif", "customer_3.gif", "customer_4.gif", "customer_5.gif"]
ordered_customers = []
current_customer = 0
donePressed = False
customer_order = ""


#variables/flag/list for the dance party
customersAndChefs = ["customer_1.gif", "customer_2.gif", "customer_3.gif", "customer_4.gif", "customer_5.gif", "chef_bunny_CROPPED.gif", "chef_monkey_CROPPED.gif", "chef_cat_CROPPED.gif", "chef_dog_CROPPED.gif"]
random_colors = None
flag = True


# user character when playing the game
selectedAnimal = None


# cake images
cakeGIF = ""
randomCake1 = ""
randomCake2 = ""
randomCake3 = ""


# set the difficulty of the game
difficulty = ""


#scoring
rating = 100
turn = 0


# -------------- FUNCTIONS BELOW --------------


# screen for the outside cafe/welcome screen
def outside_cafe(x,y):
   t.clear()
   s.clear()
   s.bgpic("SCREEN-outside_cafe-6.png")
   flag = False
   random_colors = turtle.Turtle()
   random_colors.clear()
   characters = turtle.Turtle()
   characters.clear()
   customersAndChef_gif = turtle.Turtle()
   customersAndChef_gif.clear()
  
   #turtle play button
   turtle.addshape("button_play-CROPPED.gif")
   playButton = turtle.Turtle()
   playButton.penup()
   playButton.hideturtle()
   playButton.goto(100, -310)
   playButton.shape("button_play-CROPPED.gif")
   playButton.showturtle()
   playButton.onclick(playGameSelectDifficulty)


   #turtle about button
   turtle.addshape("button_about-CROPPED.gif")
   aboutButton = turtle.Turtle()
   aboutButton.penup()
   aboutButton.hideturtle()
   aboutButton.goto(290, -310)
   aboutButton.shape("button_about-CROPPED.gif")
   aboutButton.showturtle()
   aboutButton.onclick(aboutGame)


   #turtle exit button
   turtle.addshape("button_exit-CROPPED.gif")
   exitButton = turtle.Turtle()
   exitButton.penup()
   exitButton.hideturtle()
   exitButton.goto(485, -310)
   exitButton.shape("button_exit-CROPPED.gif")
   exitButton.showturtle()
   exitButton.onclick(exitGame)


# screen for selecting difficulty
def playGameSelectDifficulty(x,y):
   global difficulty
   s.clear()
   s.bgpic("SCREEN_difficulty.png")


   #easy select button
   turtle.addshape("button_easy.gif")
   selectEasy = turtle.Turtle()
   selectEasy.penup()
   selectEasy.hideturtle()
   selectEasy.goto(-450, 50)
   selectEasy.shape("button_easy.gif")
   selectEasy.showturtle()
   selectEasy.onclick(selectedEasy)


   #medium select button
   turtle.addshape("button_medium.gif")
   selectMedium = turtle.Turtle()
   selectMedium.penup()
   selectMedium.hideturtle()
   selectMedium.goto(0, 50)
   selectMedium.shape("button_medium.gif")
   selectMedium.showturtle()
   selectMedium.onclick(selectedMedium)


   #hard select button
   turtle.addshape("button_hard.gif")
   selectHard = turtle.Turtle()
   selectHard.penup()
   selectHard.hideturtle()
   selectHard.goto(450, 50)
   selectHard.shape("button_hard.gif")
   selectHard.showturtle()
   selectHard.onclick(selectedHard)


# game difficulties + selected chef
def selectedEasy(x,y):
   global difficulty
   difficulty = "easy"
   playGameSelectChef(x,y)
   difficultySelected = True


def selectedMedium(x,y):
   global difficulty
   difficulty = "medium"
   playGameSelectChef(x,y)


def selectedHard(x,y):
   global difficulty
   difficulty = "hard"
   playGameSelectChef(x,y)


# sets chef to the users desired one
def playGameSelectChef(x,y):
   global selectedAnimal
   s.clear()
   s.bgpic("SCREEN_select_characters.png")


   #monkey select button
   turtle.addshape("button_select-monkey_CROPPED.gif")
   selectMonkey = turtle.Turtle()
   selectMonkey.penup()
   selectMonkey.hideturtle()
   selectMonkey.goto(-520, -240)
   selectMonkey.shape("button_select-monkey_CROPPED.gif")
   selectMonkey.showturtle()
   selectMonkey.onclick(selectedMonkey)


   #cat select button
   turtle.addshape("button_select-cat_CROPPED.gif")
   selectCat = turtle.Turtle()
   selectCat.penup()
   selectCat.hideturtle()
   selectCat.goto(-180, -240)
   selectCat.shape("button_select-cat_CROPPED.gif")
   selectCat.showturtle()
   selectCat.onclick(selectedCat)


   #bunny select button
   turtle.addshape("button_select-bunny_CROPPED.gif")
   selectBunny = turtle.Turtle()
   selectBunny.penup()
   selectBunny.hideturtle()
   selectBunny.goto(180, -243)
   selectBunny.shape("button_select-bunny_CROPPED.gif")
   selectBunny.showturtle()
   selectBunny.onclick(selectedBunny)


   #dog select button
   turtle.addshape("button_select-dog_CROPPED.gif")
   selectDog = turtle.Turtle()
   selectDog.penup()
   selectDog.hideturtle()
   selectDog.goto(515, -240)
   selectDog.shape("button_select-dog_CROPPED.gif")
   selectDog.showturtle()
   selectDog.onclick(selectedDog)


# sets screen to the about page
def aboutGame(x,y):
   s.clear()
   s.bgpic("SCREEN_about_page.png")
  
   # instructions
   t.goto(10,-95)
   t.pencolor("#7d2746")
   t.write("Begin by choosing your desired difficulty along with a \ncharacter to be your chef and begin serving customers!\nMemorize orders to correctly select cakes & serve all\ncustomers for the day! Make sure to correctly select\nthe cakes per order, otherwise your rating goes down!",align="center",font=("Monospace", 25, "normal","bold",))
  
   # mini logo
   turtle.addshape("logo_mini.gif")
   mini_logo = turtle.Turtle()
   mini_logo.penup()
   mini_logo.hideturtle()
   mini_logo.goto(-80, -100)
   mini_logo.shape("logo_mini.gif")
   mini_logo.showturtle()
   mini_logo.onclick(dance_party)
  
   # calls the menu button
   menuButton(x,y)


# sets screen to the exit page
def exitGame(x,y):
   s.clear()
   s.bgpic("SCREEN_exit_page.png")
   t.goto(0,10)
  
   # text
   t.pencolor("#554796")
   t.write("Goodbye, come again soon!", align="center", font=("Monospace", 40, "normal","bold",))
  
   # logo
   turtle.addshape("logo.gif")
   logo = turtle.Turtle()
   logo.penup()
   logo.hideturtle()
   logo.goto(20, -180)
   logo.shape("logo.gif")
   logo.showturtle()
   logo.onclick(dance_party)
  
   # calls the menu button
   menuButton(x,y)


# displays menu button
def menuButton(x,y):
   global flag
   # adds the menu button to the screen
   turtle.addshape("button_menu_CROPPED.gif")
   menuButton = turtle.Turtle()
   menuButton.penup()
   menuButton.hideturtle()
   menuButton.goto(600,-330)
   menuButton.shape("button_menu_CROPPED.gif")
   menuButton.showturtle()
   menuButton.onclick(outside_cafe)


   # clears the dance party
   random_colors = turtle.Turtle()
   random_colors.clear()
   characters = turtle.Turtle()
   characters.clear()
   customersAndChef_gif = turtle.Turtle()
   customersAndChef_gif.clear()


# select bunny chef
def selectedBunny(x,y):
   global selectedAnimal
   selectedAnimal = "chef_bunny_CROPPED.gif"
   insideCafe(x,y)
 # select cat chef
def selectedCat(x,y):
   global selectedAnimal
   selectedAnimal = "chef_cat_CROPPED.gif"
   insideCafe(x,y)
 # select dog chef
def selectedDog(x,y):
   global selectedAnimal
   selectedAnimal = "chef_dog_CROPPED.gif"
   insideCafe(x,y)


# select monkey chef
def selectedMonkey(x,y):
   global selectedAnimal
   selectedAnimal = "chef_monkey_CROPPED.gif"
   insideCafe(x,y)


# function for the dance party
def dance_party(x,y):
   global flag
   s.clear()
   s.bgpic("SCREEN-inside_cafe.png")
   menuButton(x,y)
  
   # run infinitely until the user hits the 'menu' button which sets the flag
   flag = True
   while flag:
       # goes through various colors
       random_colors = turtle.Turtle()
       random_colors.hideturtle()
       random_colors.penup()
       random_colors.goto(-230, 300)
       #colors = ["medium purple", "blue", "medium sea green", "royal blue", "medium violet red"]
       colors = ["#FF6EC7", "#FFFF00", "#FF3F34", "#39FF14", "#00FFFF", "#1B03A3", "#A500FF", "#FF5E00", "#FF00FF", "#00FF7F", "#FF1493", "#7FFF00", "#FF4500", "#8A2BE2", "#FFD700", "#FFB6C1"]
       for i in range(5):
           random_color = random.choice(colors)
           random_colors.clear()
           random_colors.pencolor(random_color)
           random_colors.write("DANCE PARTY!",font=("Papyrus", 50, "normal","bold"))


       # add shapes for customer + chefs combined into one list
       for customersAndChef_gif in customersAndChefs:
           turtle.addshape(customersAndChef_gif)


       # makes the characters do a dance at random positions
       for i in range(len(customersAndChefs)):
           a = random.randint(-500, 500)
           b = random.randint(-200, 100)
           characters = turtle.Turtle()
           characters.penup()
           characters.hideturtle()
           characters.goto(a,b)


           characters.shape(customersAndChefs[i])
           characters.showturtle()
           characters.speed(3)


           # makes the character move in a star shap pattern
           sz = 25
           ang = 60
           for i in range(0, int(360/ang), 1):
               characters.forward(sz)
               characters.backward(sz)
               characters.right(ang)   
          


       flag = False


# changes the screen to inside the cafe
def insideCafe(x,y):
   global current_customer, ordered_customers
   s.clear()
   s.bgpic("SCREEN-inside_cafe.png")
   chef(selectedAnimal)
  
# turns the customer into a turtle
   for customer_gif in customer_list:
       turtle.addshape(customer_gif)


# checks if there are customers in the list
   if current_customer < len(customer_list):
       animal_customer = turtle.Turtle()
       animal_customer.penup()
       animal_customer.hideturtle()
       animal_customer.goto(-570,100)
       animal_customer.shape(customer_list[current_customer])
       animal_customer.showturtle()
       animal_customer.speed(1)


# adds the customer to a new list
       ordered_customers.append(animal_customer)


# move the customer down
       move_down(animal_customer)
       current_customer +=1


# function to move the customer down to order
def move_down(animal_customer):
   animal_customer.goto(-570,100)
   animal_customer.speed(1)
   animal_customer.goto(-570,-100)


# display the order button
   clickForOrder(-530, -90)


# displays the chef inside the cafe
def chef(selectedAnimal):
   turtle.addshape(selectedAnimal)
   chef = turtle.Turtle()
   chef.penup()
   chef.hideturtle()
   chef.goto(-570, -300)
   chef.shape(selectedAnimal)
   chef.showturtle()


# shows the order buttons for customers
def clickForOrder(x,y):
   turtle.addshape("button_!.gif")
   orderButton = turtle.Turtle()
   orderButton.penup()
   orderButton.hideturtle()
   orderButton.goto(-500, -90)
   orderButton.shape("button_!.gif")
   orderButton.showturtle()


# if clicked, it will go to the display order screen
   orderButton.onclick(displayOrder)


# generates a random customer order based on the difficulty selected by the user
def generateOrder(difficulty):
   global customer_order, cakeGIF, randomCake1, randomCake2, randomCake3
   no_matches = False


   while not no_matches:
       if difficulty == "easy":     
           index = random.randint(0, len(easy)-1)
           customer_order = list(easy.keys())[index]


           cakeGIF = easy.get(customer_order)
           randomIndex1 = random.randint(0, len(medium)-1)
           random_order1 = list(medium.keys())[randomIndex1]
           randomIndex2 = random.randint(0, len(medium)-1)
           random_order2 = list(medium.keys())[randomIndex2]
           randomIndex3 = random.randint(0, len(hard)-1)
           random_order3 = list(hard.keys())[randomIndex3]
           randomCake1 = medium.get(random_order1)
           randomCake2 = medium.get(random_order2)
           randomCake3 = hard.get(random_order3)


           if randomCake1 != cakeGIF and randomCake2 != cakeGIF and randomCake3 != cakeGIF:
               if randomCake1 != randomCake2 and randomCake1 != randomCake3 and randomCake2 != randomCake3:
                   no_matches = True
      
          
       elif difficulty == "medium":
           index = random.randint(0, len(medium)-1)
           customer_order = list(medium.keys())[index]
           cakeGIF = medium.get(customer_order)


           randomIndex1 = random.randint(0, len(easy)-1)
           random_order1 = list(easy.keys())[randomIndex1]
           randomIndex2 = random.randint(0, len(easy)-1)
           random_order2 = list(easy.keys())[randomIndex2]
           randomIndex3 = random.randint(0, len(hard)-1)
           random_order3 = list(hard.keys())[randomIndex3]
           randomCake1 = easy.get(random_order1)
           randomCake2 = easy.get(random_order2)
           randomCake3 = hard.get(random_order3)


           if randomCake1 != cakeGIF and randomCake2 != cakeGIF and randomCake3 != cakeGIF:
               if randomCake1 != randomCake2 and randomCake1 != randomCake3 and randomCake2 != randomCake3:
                   no_matches = True


       elif difficulty == "hard":
           index = random.randint(0, len(hard)-1)
           customer_order = list(hard.keys())[index]
           cakeGIF = hard.get(customer_order)


           randomIndex1 = random.randint(0, len(easy)-1)
           random_order1 = list(easy.keys())[randomIndex1]
           randomIndex2 = random.randint(0, len(medium)-1)
           random_order2 = list(medium.keys())[randomIndex2]
           randomIndex3 = random.randint(0, len(medium)-1)
           random_order3 = list(medium.keys())[randomIndex3]
           randomCake1 = easy.get(random_order1)
           randomCake2 = medium.get(random_order2)
           randomCake3 = medium.get(random_order3)


           if randomCake1 != cakeGIF and randomCake2 != cakeGIF and randomCake3 != cakeGIF:
               if randomCake1 != randomCake2 and randomCake1 != randomCake3 and randomCake2 != randomCake3:
                   no_matches = True
    
# displays cakes on the plates in random spots
def displayOnPlates(userCake, cake_turtles):
   all_cakes = [userCake] + cake_turtles
   plates = [(-540,-50),(-310,-50),(-85,-50),(150,-50)]
   random.shuffle(all_cakes)
   random.shuffle(plates)
 # specifically places them on a random plate
   for i in range (len(all_cakes)):
       cake_turtle = all_cakes[i]
       cake_turtle.goto(plates[i])
       cake_turtle.showturtle()


# displays the customers order
def displayOrder(x,y):
   s.clear()
   s.bgcolor("white")
   t.goto(0, 0)
   t.speed(8)


# customer order text
   t.pencolor("black")
   generateOrder(difficulty)
   t.write((f"\"I want a {customer_order}!\""), align="center", font=("Monospace", 23, "normal","bold"))
   turtle.addshape("button_make-order.gif")


# make order button below
   makeOrderButton = turtle.Turtle()
   makeOrderButton.penup()
   makeOrderButton.hideturtle()
   makeOrderButton.goto(-45, -90)
   makeOrderButton.shape("button_make-order.gif")
   makeOrderButton.showturtle()
  
# when clicked, takes you to the create food screen
   makeOrderButton.onclick(create_food)


#takes user to the inside of the kitchen and the cakes appear
def create_food(x,y):
   global cakeGIF, randomCake1, randomCake2, randomCake3
   s.clear()
   s.bgpic("SCREEN_create-food.png")
   turtle.addshape(cakeGIF)
   turtle.addshape(randomCake1)
   turtle.addshape(randomCake2)
   turtle.addshape(randomCake3)


  # user cake turtle
   userCake = turtle.Turtle()
   userCake.penup()
   userCake.hideturtle()
   userCake.shape(cakeGIF)
   #userCake.showturtle()
   userCake.onclick(checkWin)


  #random cake turtles
   Cake1 = turtle.Turtle()
   Cake1.penup()
   Cake1.hideturtle()
   Cake1.shape(randomCake1)
   #Cake1.showturtle()
   Cake1.onclick(checkLoseCake1)


   Cake2 = turtle.Turtle()
   Cake2.penup()
   Cake2.hideturtle()
   Cake2.shape(randomCake2)
   #Cake2.showturtle()
   Cake2.onclick(checkLoseCake2)


   Cake3 = turtle.Turtle()
   Cake3.penup()
   Cake3.hideturtle()
   Cake3.shape(randomCake3)
   #Cake3.showturtle()
   Cake3.onclick(checkLoseCake3)


   cake_turtles = [Cake1,Cake2,Cake3]


   displayOnPlates(userCake, cake_turtles)
  
   userCake.showturtle()
   Cake1.showturtle()
   Cake2.showturtle()
   Cake3.showturtle()
  
   instruction(x,y)
   displayRating(x,y)
   done(x,y)


#check if the user lost and put the selected cake on the cakeplate
def checkLoseCake1(x,y):
   global turn, rating
   print("Lose Cake 1")
  
   Cake1 = turtle.Turtle()
   Cake1.penup()
   Cake1.hideturtle()
   Cake1.shape(randomCake1)
   Cake1.showturtle()
   Cake1.goto(475,-52)
  
   lose = True
   if True:
       turn += 1
       rating -= 20
   if turn == 5 and rating < 80:
       s.clear()
       turtle.addshape("button_lose.gif")
       losePopup = turtle.Turtle()
       losePopup.penup()
       losePopup.hideturtle()
       losePopup.goto(0, 0)
       losePopup.shape("button_lose.gif")
       losePopup.showturtle()
       losePopup.onclick(outside_cafe)


       reset_game_stats()
      
#check if the user lost and put the selected cake on the cakeplate
def checkLoseCake2(x,y):
   global turn, rating
   print("Lose Cake 2")
   Cake2 = turtle.Turtle()
   Cake2.penup()
   Cake2.hideturtle()
   Cake2.shape(randomCake2)
   Cake2.showturtle()
   Cake2.goto(475,-52)
   lose = True
   if True:  
       turn += 1
       rating -= 20
   if turn == 5 and rating < 80:
       s.clear()
       turtle.addshape("button_lose.gif")
       losePopup = turtle.Turtle()
       losePopup.penup()
       losePopup.hideturtle()
       losePopup.goto(0, 0)
       losePopup.shape("button_lose.gif")
       losePopup.showturtle()
       losePopup.onclick(outside_cafe)


       reset_game_stats()


#check if the user lost and put the selected cake on the cakeplate
def checkLoseCake3(x,y):
   global turn, rating
   print("Lose Cake 3")
   Cake3 = turtle.Turtle()
   Cake3.penup()
   Cake3.hideturtle()
   Cake3.shape(randomCake3)
   Cake3.showturtle()
   Cake3.goto(475,-52)


   lose = True
   if True:
      
       turn += 1
       rating -= 20
   if turn == 5 and rating < 80:
       s.clear()
       turtle.addshape("button_lose.gif")
       losePopup = turtle.Turtle()
       losePopup.penup()
       losePopup.hideturtle()
       losePopup.goto(0, 0)
       losePopup.shape("button_lose.gif")
       losePopup.showturtle()
       losePopup.onclick(outside_cafe)


       reset_game_stats()


#check if the user won by seeing if the user has gone through 5 turns and if the rating is above 80%
def checkWin(x,y):
   global turn, rating
   print("win")
   userCake = turtle.Turtle()
   userCake.penup()
   userCake.hideturtle()
   userCake.shape(cakeGIF)
   userCake.showturtle()
   userCake.goto(475,-52)
   win = True
   if win:
       turn += 1
   if turn == 5 and rating >= 80:  
       s.clear()
       turtle.addshape("button_win.gif")
       winPopup = turtle.Turtle()
       winPopup.penup()
       winPopup.hideturtle()
       winPopup.goto(0, 0)
       winPopup.shape("button_win.gif")
       winPopup.showturtle()
       winPopup.onclick(outside_cafe) 


       reset_game_stats()


# fixes the customers, rating, and turns so that when the game is run again they work
def reset_game_stats():
   global customeer_list, ordered_customers, current_customer, donePressed, turn, rating
   customer_list = ["customer_1.gif", "customer_2.gif", "customer_3.gif", "customer_4.gif", "customer_5.gif"]
   ordered_customers = []
   current_customer = 0
   donePressed = False
   turn = 0
   rating = 100


#creates "done" button which takes user to the inside of the cafe
def done(x,y):
   global current_customer, donePressed


   turtle.addshape("button_done_CROPPED.gif")
   doneButton = turtle.Turtle()
   doneButton.penup()
   doneButton.hideturtle()
   doneButton.goto(580 , -330)
   doneButton.shape("button_done_CROPPED.gif")
   doneButton.showturtle()
   doneButton.onclick(insideCafe)


   donePressed = True
  
#write out instructions for game
def instruction(x,y):
   t = turtle.Turtle()


   t.penup()
   t.goto(-10,-280)
   t.color("white")
   t.speed(3)
   t.pendown()
   t.write("Instruction: Click the correct cake and select done(you can only select one)!", align="center", font=("Monospace", 21, "normal","bold"))
   t.hideturtle()


#this function changes the rating and updates user's turns
def displayRating(x,y):
   global rating, turn


   t.goto(-660, -335)
   t.clear()
   t.color("cornflower blue")
   t.write((f"Rating: {rating}% Turns: {turn}"),font=("Monospace", 23, "normal","bold"))


#resize to 72% of the original (1382 X 778px)
s.bgpic("SCREEN-outside_cafe-6.png")


#write welcome message
t = turtle.Turtle()
t.penup()
t.pencolor("#C11C84")
t.goto(-645, 30)
t.speed(8)
t.write("Welcome to the Animal Café!",font=("Monospace", 30, "normal","bold"))




#TURTLE BUTTONS: -----------------------------


#turtle play button
turtle.addshape("button_play-CROPPED.gif")
playButton = turtle.Turtle()
playButton.penup()
playButton.hideturtle()
playButton.goto(100, -310)
playButton.shape("button_play-CROPPED.gif")
playButton.showturtle()
playButton.onclick(playGameSelectDifficulty)




#turtle about button
turtle.addshape("button_about-CROPPED.gif")
aboutButton = turtle.Turtle()
aboutButton.penup()
aboutButton.hideturtle()
aboutButton.goto(290, -310)
aboutButton.shape("button_about-CROPPED.gif")
aboutButton.showturtle()
aboutButton.onclick(aboutGame)     




#turtle exit button
turtle.addshape("button_exit-CROPPED.gif")
exitButton = turtle.Turtle()
exitButton.penup()
exitButton.hideturtle()
exitButton.goto(485, -310)
exitButton.shape("button_exit-CROPPED.gif")
exitButton.showturtle()
exitButton.onclick(exitGame)


turtle.done()
s.listen()
s.mainloop()

