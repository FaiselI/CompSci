#U4_M4_PS13
#Problem Set 13
# F.Ismail on 2-21-21

# Task 1- Order of the Rainbows
print("Task 1- Order of the Rainbows")
print()
#create rainbow file
colorFile = open("rainbow.txt",'w')
#write the colors of the rainbow
colorFile.write("red\norange\nyellow\ngreen\nblue\npurple")
#close when finished
colorFile.close( )
#open in readmode
rainbowFile = open('rainbow.txt','r')
#read as a list variable
rainbowColors = rainbowFile.readlines()
#sort the colors
rainbowColors.sort()
#iterate through the list
for color in rainbowColors:
  print(color.upper().strip())
#close the file
rainbowFile.close()
print()

#task 2 - The weather
print("Task 2: The Weather")
print()
#open the file in readmode
meanTemps = open('meantemp.txt','r')
#read the first line
headings = meanTemps.readline()
print(headings)
#use strip to turn into list
print(headings.split(','))
#use while loop
while meanTemps:
  cityTemp = meanTemps.readline().strip().split(',')
  if cityTemp != ['']:
    print(cityTemp[:3])
#close the file 
meanTemps.close( )
print()

#task3- Random Pi Guessing
print("Task 3: Random Pi Guessing")
print()
#open the pi file
pi = open("pi.txt",'r')
#input for user name
variableName = input("What is your name: ")
#find the length of input
seed = len(variableName)
#read the file and use seek
pi.seek(seed)
#initialize variable digit to the value of reading one character from pi file
digit = pi.read(1)
#initialize guess variable
guess = input("Enter a single digit guess or q to quit: ")
#initialize incorrect and correct
wrong = 0
correct = 0
#while loop 
while True:
  #check if guess is a number before running the rest of the loop
  if guess.isdigit() == False:
    break
  #check if the digit is a period
  if digit == '.':
    #if true move the digit one more
    digit = pi.read(1)
  else:
    #check if digit is a newline
    if digit == '\n':
      #add one to seed
      seed = seed + 1
      #then move the cursor to the index of seed
      pi.seek(seed)
  #if the guess is equal to the digit the cursor is one
  if guess == digit:
    #print correct and add one to the correct variable
    print("Correct!!!!")
    correct += 1
    guess = input("Enter a single digit guess or q to quit: ")
  else:
    #if they are not equal print incorrect and add one to the wrong variable
    print("Incorrect.")
    wrong += 1
    guess = input("Enter a single digit guess or q to quit: ")
#print statement for how many digits wrong and right
print("You got",correct,"number of digit correct and",wrong,'number of digits incorrect.')
#close the file
pi.close()