import time
import random
import webbrowser

missed = 0
hardMode = False
alphabet = ('abcdefghijklmnopqrstuvwxyz')
#User difficulty that they choose
#dif = ["easy", "medium", "hard"]
#the list of words in hangman
sports = ["basketball", "archery", "soccer", "baseball", "golf", "tennis", "badminton", "football", "rugby", "hockey", "volleyball", "cricket", "swimming"]
tools = ["hammer", "scissors", "screwdriver", "pitchfork", "saw", "drill", "vacuum", "welder", "hoe"]
Countries = ["Afghanistan", "Albania", "Belgium","Canada", "China", "USA","Denmark","Egypt","Germany","Greece","Iceland","Japan","Norway","Russia","Syria"]

red = "\033[1;31m"
blue = "\033[1;34m"
black = "\033[0m"
green = "\033[1;32m"
yellow = "\033[1;33m"

hangman = [
''' ----------
|    |
|
|
|
|
|
|
|
-------------
''',
''' ----------
|    |
|    O 
|
|
|
|
|
|
|
-------------
''',
''' ----------
|    |
|    O 
|    |
|
|
|
|
|
|
-------------
''',
''' ----------
|    |
|    O 
|  /-|
|
|
|
|
|
|
-------------
''',
''' ----------
|    |
|    O 
|  /-|-\
|  
| 
|
|
|
|
-------------
''',
''' ----------
|    |
|    O 
|  /-|-\
|    |
|
|
|
|
|
-------------
''',
''' ----------
|    |
|    O 
|  /-|-\
|    | 
|   |
|
|
|
|
-------------
''',
''' ----------
|    |
|    O 
|  /-|-\
|    | 
|   | |
|
|
|
|
-------------
''',
''' ----------
|    |
|    O 
|  /-|-\
|    | 
|   | |
|  _| |
| 
|
|
-------------
''',
''' ----------
|    |
|    O 
|  /-|-\
|    | 
|   | |
|  _| |_
| 
|
|
-------------
''',
]

hangmanTwo = [
''' ----------
|    |
|
|
|
|
|
|
|
-------------
''',
''' ----------
|    |
|    O 
|
|
|
|
|
|
|
-------------
''',
''' ----------
|    |
|    O 
|  /-|
|
|
|
|
|
|
-------------
''',
''' ----------
|    |
|    O 
|  /-|-\
|  
| 
|
|
|
|
-------------
''',
''' ----------
|    |
|    O 
|  /-|-\  
|  _|
| 
|
|
-------------
''',
''' ----------
|    |
|    O 
|  /-|-\
|  _| |_
| 
|
|
-------------
''',
]

def ifLetter(guess):
   checkList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
   if guess.lower() in checkList:
       return True
   return False

def menu():
   print('''             _____________________________________
           |                                     |
           |  Welcome User To Hang Man The Game  |
           |_____________________________________|
            \n ''')
   time.sleep(0.25)

   while True:
       print('''-----------------------------------------------------------------

   \t \t \t \t        MENU:     
   \t \t \t \t   A. Instructions
   \t \t \t \t   B. Word List
   \t \t \t \t   C. Play Hangman
   \t \t \t \t   D. Veteran Mode
   \t \t \t \t   E. Secret ;)\n 
-----------------------------------------------------------------
\t\t\t\t  ***** SELECT OPTION ***** \n
>>>>:''')
       user = input().lower()
       if gameChoice(user):
           break

def gameChoice(user):
   if user == "a":
       print('''Hangman is a simple game meant for all ages. This is a one player game but can be shared among a group working together to solve the puzzle.

       \tRules:

       \t\t\t 1. You can pick what you would like to select in the menu including modes, instructions, etc.
       \t\t\t 2. You will be asked if you would like to play so you will have to say “Yes” if you want to play. Do not type anything else that is not yes as you won’t be able to play than.
       \t\t\t 3. Select which set of words you would like from a theme. Example: Sports.
       \t\t\t 4. You are presented with a blank noose.
       \t\t\t 5. You will then be presented with a word covered by dashes.
       \t\t\t 6. You need to guess the letters in the word.
       \t\t\t 7. For every wrong word, a limb will be attached to the man.
       \t\t\t 8. If you run out of turns than the man will die and you lose.
       \t\t\t 9. You can choose whether you would like to play again. \n''')
       time.sleep(1)
       return False
   elif user == "b":
       print('''Sports: basketball, archery, soccer, baseball, golf, tennis, badminton, football, rugby, hockey, volleyball
Tools: hammer, scissors, screwdriver, pitchfork, saw, drill, vacuum, welder, hoe
Countries: Afghanistan, Albania, Belgium, Canada, China, USA, Denmark, Egypt, Germany, Greece, Iceland, Japan, Norway, Russia, Syria \n''')
       time.sleep(1)

       return False

   elif user == "d":
       print(red + '''\t\t\t\t   =====================
\t\t\t\t   |                   |
\t\t\t\t   |  WELCOME TO THE   |
\t\t\t\t   |   DANGER ZONE!!   |
\t\t\t\t   |                   |
\t\t\t\t   =====================
''' + black)
       time.sleep(0.5)
       global hardMode
       hardMode = True
   elif user == "e":
       webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
       quit()
   elif user != "c":
       print(red + "INVALID OPTION")
       quit()
   return True


def options():
   print('''\t \t \t \t     THEME OF WORDS:     
   \t \t \t \t   A. Sports
   \t \t \t \t   B. Tools
   \t \t \t \t   C. Countries \n   
-----------------------------------------------------------------
''')

   words = input("\t\t\t\t  ***** SELECT WORD LIST ***** \n"
                ">>>>: \n").lower()

   return words

def error(guess, message):
  print(message)
  return guess + 1

while True:
   menu()
   time.sleep(0.25)

   listChoice = options()
   if listChoice == "a":
       listOfWords = sports
   elif listChoice == "b":
       listOfWords = tools
   elif listChoice == "c":
       listOfWords = Countries
   else:
       print(red + "INVALID OPTION")
       break
   time.sleep(0.25)

   while True:
      if hardMode:
          guess = 5
          hangman = hangmanTwo
      else:
          guess = 10
      missed = 0

      secretword = random.choice(listOfWords).lower()
      wordList = []
      for x in range(len(secretword)):
          wordList.append(secretword[x])
      dashes = ['-'] * len(wordList)
      lettersGuess = []

      while guess >= 0:

          print(hangman[missed])
          print(green + "WORD:" + black,)
          for x in range(len(dashes)):
              print(dashes[x], end = "")
          print("\nYou have", guess,"turns")
          userGuess = input(yellow + "\nWhat letter do you guess?\n" + black)
          guess -= 1
          missed += 1

          if ifLetter(userGuess) == False:
               guess = error(guess, red + "invalid character" + black)
               time.sleep(0.5)
               missed -= 1
          else:
              if len(userGuess) == 1:
                  if userGuess in lettersGuess:
                       guess = error(guess,red + "already in" + black)
                       time.sleep(0.5)
                       missed -= 1
                  else:
                      lettersGuess.append(userGuess)
                      trial = False
                      for x in range(len(wordList)):
                          if wordList[x] == userGuess:
                              dashes[x] = userGuess
                              trial = True
                      if trial:
                          guess += 1
                          missed -= 1

              elif userGuess.isalpha():
                   guess = error(guess, red + "string" + black)
                   time.sleep(0.5)

          correct = True
          for x in range(len(dashes)):
               if dashes[x] == '-':
                   correct = False

          if correct:
               time.sleep(0.75)
               print("\nThe Secret Word Was=",blue + secretword + black, "\n")
               webbrowser.open("https://d1u5p3l4wpay3k.cloudfront.net/fortnite_gamepedia/1/1d/Victory_royale_2.png", new=0, autoraise=True)
               break
          if guess == 0:
               if missed == 5:
                   print(hangman[5])
               if missed == 10:
                   print(hangman[9])
               time.sleep(0.5)
               print("_____________________________________________________________")
               print("\nThe Secret Word Was:", blue + secretword + black, "\n")
               print("_____________________________________________________________")
               webbrowser.open("https://i.ytimg.com/vi/eV2LjonGVIE/maxresdefault.jpg", new=0, autoraise=True)
               break

      user = input("_________________________________________________________________ \n"
                   "\n Would You Like To Play Again?")
      if user != "yes":
           webbrowser.open("https://www.askideas.com/media/07/Thank-You-Goodbye.jpg")
           quit()





# I imported the necessary modules to complete important functions. For example I need random to choose a random word from my list. Time is used as a way to add breaks and pauses between my code. Webbrowser is used to access the webbrowser by opening a new tab of an image.
import time
import random
import webbrowser

#missed is a counter for how many times the user inputted an incorrect letter. This does not count an invalid input like an interger.
#hardMode is the variable that represents a harder difficulty level. I made it equal False until the user picks it which makes it True. It is just a quicker way to access hardMode.
missed = 0
hardMode = False

#The three themes of words that the user can pick from.
sports = ["basketball", "archery", "soccer", "baseball", "golf", "tennis", "badminton", "football", "rugby", "hockey", "volleyball", "cricket", "swimming"]
tools = ["hammer", "scissors", "screwdriver", "pitchfork", "saw", "drill", "vacuum", "welder", "hoe"]
Countries = ["Afghanistan", "Albania", "Belgium","Canada", "China", "USA","Denmark","Egypt","Germany","Greece","Iceland","Japan","Norway","Russia","Syria"]

red = "\033[1;31m"
blue = "\033[1;34m"
black = "\033[0m"
green = "\033[1;32m"
yellow = "\033[1;33m"
magenta = "\033[1;35m"
cyan = "\033[1;36m"

hangman = [
''' ----------
|    |
|
|
|
|
|
|
|
-------------
''',
''' ----------
|    |
|    O 
|
|
|
|
|
|
|
-------------
''',
''' ----------
|    |
|    O 
|    |
|
|
|
|
|
|
-------------
''',
''' ----------
|    |
|    O 
|  /-|
|
|
|
|
|
|
-------------
''',
''' ----------
|    |
|    O 
|  /-|-\
|  
| 
|
|
|
|
-------------
''',
''' ----------
|    |
|    O 
|  /-|-\
|    |
|
|
|
|
|
-------------
''',
''' ----------
|    |
|    O 
|  /-|-\
|    | 
|   |
|
|
|
|
-------------
''',
''' ----------
|    |
|    O 
|  /-|-\
|    | 
|   | |
|
|
|
|
-------------
''',
''' ----------
|    |
|    O 
|  /-|-\
|    | 
|   | |
|  _| |
| 
|
|
-------------
''',
''' ----------
|    |
|    O 
|  /-|-\
|    | 
|   | |
|  _| |_
| 
|
|
-------------
''',
]

hangmanTwo = [
''' ----------
|    |
|
|
|
|
|
|
|
-------------
''',
''' ----------
|    |
|    O 
|
|
|
|
|
|
|
-------------
''',
''' ----------
|    |
|    O 
|  /-|
|
|
|
|
|
|
-------------
''',
''' ----------
|    |
|    O 
|  /-|-\
|  
| 
|
|
|
|
-------------
''',
''' ----------
|    |
|    O 
|  /-|-\  
|  _|
| 
|
|
-------------
''',
''' ----------
|    |
|    O 
|  /-|-\
|  _| |_
| 
|
|
-------------
''',
]

def ifLetter(guess):
   checkList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
   if guess.lower() in checkList:
       return True
   return False

def menu():
   print('''             _____________________________________
           |                                     |
           |  Welcome User To Hang Man The Game  |
           |_____________________________________|
            \n ''')
   time.sleep(0.25)

   while True:
       print('''-----------------------------------------------------------------

   \t \t \t \t        MENU:      \n''',
blue + "\t \t \t \t \t  A. Instructions\n" + black,
green + "\t \t \t \t \t  B. Word List\n" + black,
magenta + "\t \t \t \t \t  C. Play Hangman\n" + black,
yellow + "\t \t \t \t \t  D. Veteran Mode\n" + black,
red + "\t \t \t \t \t  E. Secret ;)\n" + black,
'''-----------------------------------------------------------------
\t\t\t\t   ***** SELECT OPTION ***** \n
>>>>:''')
       user = input().lower()
       if gameChoice(user):
           break

def gameChoice(user):
   if user == "a":
       print('''\t\t\tHangman is a simple game meant for all ages. This is a one player game but can be shared among a group working together to solve the puzzle.

       \tRules:

       \t\t\t 1. You can pick what you would like to select in the menu including modes, instructions, etc.
       \t\t\t 2. You will be asked if you would like to play so you will have to say “Yes” if you want to play. Do not type anything else that is not yes as you won’t be able to play than.
       \t\t\t 3. Select which set of words you would like from a theme. Example: Sports.
       \t\t\t 4. You are presented with a blank noose.
       \t\t\t 5. You will then be presented with a word covered by dashes.
       \t\t\t 6. You need to guess the letters in the word.
       \t\t\t 7. For every wrong word, a limb will be attached to the man.
       \t\t\t 8. If you run out of turns than the man will die and you lose.
       \t\t\t 9. You can choose whether you would like to play again. \n''')
       time.sleep(1)
       return False
   elif user == "b":
       print('''Sports: basketball, archery, soccer, baseball, golf, tennis, badminton, football, rugby, hockey, volleyball
Tools: hammer, scissors, screwdriver, pitchfork, saw, drill, vacuum, welder, hoe
Countries: Afghanistan, Albania, Belgium, Canada, China, USA, Denmark, Egypt, Germany, Greece, Iceland, Japan, Norway, Russia, Syria \n''')
       time.sleep(1)

       return False

   elif user == "d":
       print(red + '''\t\t\t\t   =====================
\t\t\t\t   |                   |
\t\t\t\t   |  WELCOME TO THE   |
\t\t\t\t   |   DANGER ZONE!!   |
\t\t\t\t   |                   |
\t\t\t\t   =====================
''' + black)
       time.sleep(0.5)
       global hardMode
       hardMode = True
   elif user == "e":
       webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
       return False
   elif user != "c":
       print(red + "INVALID OPTION")
       quit()
   return True

def options():
   print("\t \t \t \t     THEME OF WORDS:\n",
cyan + "\t \t \t \t   A. Sports\n" + black,
green + "\t \t \t \t   B. Tools\n" + black,
yellow + "\t \t \t \t   C. Countries \n"+ black,
"-----------------------------------------------------------------")

   words = input("\t\t\t\t  ***** SELECT WORD LIST ***** \n"
                ">>>>: \n").lower()

   return words

def error(guess, message):
  print(message)
  return guess + 1

while True:
   menu()
   time.sleep(0.25)

   listChoice = options()
   if listChoice == "a":
       listOfWords = sports
   elif listChoice == "b":
       listOfWords = tools
   elif listChoice == "c":
       listOfWords = Countries
   else:
       print(red + "INVALID OPTION")
       break
   time.sleep(0.25)

   while True:
      if hardMode:
          guess = 5
          hangman = hangmanTwo
      #elif
      else:
          guess = 10
      missed = 0

      secretword = random.choice(listOfWords).lower()
      wordList = []
      for x in range(len(secretword)): # get the lenght ot the word
          wordList.append(secretword[x]) # gets each letter and adds it to the letter list. Ex: gold = G O L F
      dashes = ['-'] * len(wordList)
      lettersGuess = []

      while guess >= 0:

          print(hangman[missed])
          time.sleep(0.5)
          print(green + "WORD:" + black,)
          for x in range(len(dashes)):
              print(dashes[x], end = "")#make sure it stays in the same line
          print("\nYou have", guess,"Lives Left")
          userGuess = input(yellow + "\nWhat letter do you guess?\n" + black).lower()
          guess -= 1
          missed += 1

          if ifLetter(userGuess) == False:
               guess = error(guess, red + "invalid character" + black)
               time.sleep(0.5)
               missed -= 1
          else:
              if len(userGuess) == 1:
                  if userGuess in lettersGuess:
                       guess = error(guess,red + "already in" + black)
                       time.sleep(0.5)
                       missed -= 1
                  else:
                      lettersGuess.append(userGuess)
                      trial = False
                      for x in range(len(wordList)):
                          if wordList[x] == userGuess:
                              dashes[x] = userGuess
                              trial = True
                      if trial:
                          guess += 1
                          missed -= 1

              elif userGuess.isalpha():
                   guess = error(guess, red + "string" + black)
                   time.sleep(0.5)

          correct = True #assume all dashes are gone
          for x in range(len(dashes)): # checks if any letter in the word is still a dash
               if dashes[x] == '-': #If dashes are still in the word
                   correct = False # you will change the (correct) assumption from true to false

          if correct: # if the assumption that
               time.sleep(0.75)
               print("\nThe Secret Word Was:",blue + secretword + black)
               webbrowser.open("https://d1u5p3l4wpay3k.cloudfront.net/fortnite_gamepedia/1/1d/Victory_royale_2.png", new=0, autoraise=True)
               break #
          if guess == 0:
               if missed == 5:
                   print(hangman[5])
               if missed == 10:
                   print(hangman[9])
               time.sleep(0.5)
               print("_____________________________________________________________")
               print("\nThe Secret Word Was:", blue + secretword + black)
               webbrowser.open("https://i.ytimg.com/vi/eV2LjonGVIE/maxresdefault.jpg", new=0, autoraise=True)
               break

      user = input("_______________________________________________________________\n"
                   "\n***** Would You Like To Play Again? *****\n").lower()
      time.sleep(1)

      if user != "yes":
           webbrowser.open("https://www.askideas.com/media/07/Thank-You-Goodbye.jpg")
           quit()

