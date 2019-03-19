#appropriate solution cube root 
guess=0.0
numberOfGuesses=0
increament=0.0001
epsilon=0.001
cube=int(input("enter the cube to find the cube root"))
while(abs(guess**3-cube)>=epsilon):
    guess+=increament
    numberOfGuesses+=1
print("cube root of ",guess)    
    