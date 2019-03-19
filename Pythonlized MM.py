import random
#Define a Function that Gnerates a x# code from a y# code pool
def codegeneate (y,x):
    y=int(y)
    x=int(x)
    ocode = random.sample(range(1, x), y)
    print ("A code is encripted and waiting for you to solve!")
    return ocode

#a = [int(x) for x in input().split()]
### Define Ask for input guess
def aspt():
    guess1 = [int(x) for x in input("What's your guess?(four digits with space between)").split()]
    return guess1

# Define the checking system
def check(guesses):
    FBposition = ''
    FBcolor = ''
    replicatecheck = 0
    time= 0
    for i in range(4):
        time+=1
        if guesses[i] == ocode[i]:
            FBposition+= "R"
            replicatecheck = guesses[i]
        if guesses[i] != ocode[i] and guesses[i] in ocode:
            if time==1:
                FBcolor +="W"
                replicatecheck = guesses[i]
            if time >1:
                if replicatecheck == guesses[i]:
                    FBcolor =FBcolor
                    replicatecheck = guesses[i]
                elif replicatecheck != guesses[i]:
                    replicatecheck = guesses[i]
                    FBcolor +="W"
    FB=FBposition+FBcolor
    print(FB)
    return FB
    
    MM= True
guesstimes=0
while MM:
    #ocode=codegeneate(input("Length:"),input("Pool:"))
    ocode = codegeneate(4, 8)
    #print(ocode)
    individual = True
    while individual:
        guesstimes+=1
        guess=aspt()
        print ("your guess is",guess)
        FB=check(guess)
        if FB=="RRRR" :
            print("Yes!! you've nailed it!")
            MM= False
            individual= False
        if guesstimes >10:
            print("Well, you did dont get the anwser. The answer is ",ocode)
            MM= False
            individual = False
    if MM==False:
        feedback = input("\nGo Again?(0/1)")
        guesstimes = 0
        feedback=int(feedback)
        if feedback == 0:
            print("bye")
        elif feedback == 1:
            MM=True
            individual= True
            print ("Yeah! Challenge begins!")
