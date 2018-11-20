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
#The game
MM= True
guesstimes=0
#numbers of white of red feedback
white=0
whitechecker=0
codepool = [1,2,3,4,5,6,7,8]
stopcount=0
f= open("guru99.txt","w+")
while stopcount <5:
    while MM:
        #ocode=codegeneate(input("Length:"),input("Pool:"))
        ocode = codegeneate(4, 8)
        stopcount= stopcount+1
        f.write("OCODE:")
        f.write(str(ocode))
        #print(ocode)
        individual = True
        while individual:
            guesstimes+=1
            #guess=aspt() remove input function because PC will autamatic generate
            if guesstimes >0 and guesstimes<5:
                guess = (guesstimes,guesstimes+1,guesstimes+2,guesstimes+3)
                print ("your guess is",guess)
                f.write("\n Guess"+str(guesstimes)+":"+str(guess))
            else:
                MM= False
                individual = False
                f.write("Roundcomplete")
                #guess = aspt()
                #guess = ("1 1 1 1")
                #print ("your guess is", guess)
            FB = check(guess)
            f.write("\n"+FB)
            #white checking sysmtem to determine the word length change, to determine the change in feedback
            if guesstimes == 1:
                white+=len(FB)
                print (white)
            else:
                if white > len(FB):
                    #Removed number is better
                    whitechecker = -1
                    print (whitechecker,"Bad New Number")
                    codepool[guesstimes+2] = 0
                    print (codepool)
                elif white < len(FB):
                    #Removed number is bad
                    whitechecker = 1
                    print (whitechecker,"Good new number")
                    codepool[guesstimes - 2] = 0
                    print (codepool)
                else:
                    #Both number have the same trait.
                    whitechecker = 0
                    print (whitechecker,"They have the same trait!")

                white = len(FB)
                print (white)
            if FB=="RRRR" :
                print("Yes!! you've nailed it!")
                MM= False
                individual= False
            if guesstimes >10:
                print("Well, you did dont get the anwser. The answer is ",ocode)
                MM= False
                individual = False
        if MM==False:
            MM=True
            individual= True
            guesstimes =0
            codepool = [1, 2, 3, 4, 5, 6, 7, 8]
        if stopcount >5:
            break
    if stopcount >5:
        break
f.close
