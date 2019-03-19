#square root by bisection method

x=float(input("enter no. whose square root you want to find"))
low=1.0
high=x
guess=(high+low)/2.0
epsilon=0.001
steps=0

if x>1:
    while abs(guess**2-x)>=epsilon:
        steps+=1
        if abs(guess**2)<x:
            low=guess
        else :
            high=guess
        guess=(high+low)/2.0
        print("low "+str(low)+", high "+str(high)+", guess "+str(guess))

else:
    low=x
    high=1
    guess=(high+low)/2
    while abs(guess**2-x)>=epsilon:
        steps+=1
        if abs(guess**2)>x:
            high=guess
        else:
            low=guess
        guess=(high+low)/2    
        print("low "+str(low)+", high "+str(high)+", guess "+str(guess))

print("square root of x "+str(guess))   
print("no. of steps taken "+str(steps)) 
    