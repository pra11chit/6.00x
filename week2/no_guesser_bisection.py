# guess the secret number
print("Please think of a number between 0 and 100!")
low=0
high=100
guess=int((high+low)/2)
guessed=False
print("Is your secret number 50?")
userInput=str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))

if userInput=='h' or userInput=='l' or userInput=='c':

    while not guessed:
        if userInput=='c' or userInput=='h' or userInput=='l':
            if userInput=='c':
                print("Game over. Your secret number was: ",guess)
                guessed = True
                break
            if userInput=='h':
                high=guess
            if userInput=='l':
                low=guess
            guess=int((high+low)/2)
            
            print("Is your secret number ",guess,"?")    
            userInput=str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))
                
            
        else:
            print("Sorry, I did not understand your input.")
            print("Is your secret number ",guess,"?")    

            userInput=str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))

               
#the while line logic is important