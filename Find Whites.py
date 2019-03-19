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
white= 0
#numbers of white of red feedback
pathway= 0
path = 0
reseter = 0
codepool = [1,2,3,4,5,6,7,8]

while MM:
    #ocode=codegeneate(input("Length:"),input("Pool:"))
    #ocode = codegeneate(4, 8)
    ocode= [1,2,3,5]
    #print(ocode)
    individual = True
    while individual:
        guesstimes+=1
        guess = aspt()
        #guess=[1,1,1,1]
        print ("your guess is", guess)
        FB = check(guess)
        Wcheck = len(FB)
        if Wcheck == 4:
            print("Good Job, you finished the first step.")
        else:
            print("Round" + str(guesstimes))
            if guesstimes == 1:
                white += Wcheck
                print(white)
            else:
                #Case of 4 non-equals:
                if guesstimes == 2 and white != Wcheck:
                    pathway = 1
                    print("You've chosen path 1")

                elif guesstimes == 2 and white == Wcheck:
                    pathway = 2
                    print("You've chosen path 2")
                #print("White is",white)
                #print("Wcheck is", Wcheck)
                if pathway == 1:
                    path += pathway
                    print("you are on Pathway", str(pathway))
                    print("You've guessed:" + str(guesstimes) + "times")
                    # Removed number is good
                    if white > Wcheck:
                        whitechecker = -1
                        reseter +=1
                        print(whitechecker, "Bad New Number")
                        codepool[guesstimes + 2] = 0
                        print(guesstimes)
                        print(codepool)
                        #path +=pathway
                        white = Wcheck
                        #print(path)
                        #4 < > <> path
                        if guesstimes == 5 and path == 4:
                            codepool = list(filter((0).__ne__, codepool))
                            print(codepool)
                            print("Great! You've found the secret four digits! But what's the order?")
                            MM = False
                            individual = False
                            break
                        elif guesstimes == 4 and path == 3:
                            print("You are on 4 of <s and >s pathd")
                            print(codepool)
                        else:continue



                    # Removed number is bad
                    elif white < Wcheck:
                        whitechecker = 1
                        reseter += 1
                        print(whitechecker, "Good new number")
                        codepool[guesstimes - 2] = 0
                        print(codepool)
                        white = Wcheck
                        print(path,"path")
                        #guesstimes
                        # 4 < > <> path
                        if guesstimes == 5 and path == 4:
                            codepool = list(filter((0).__ne__, codepool))
                            print(codepool)
                            print("Great! You've found the secret four digits! But what's the order?")
                            MM = False
                            individual = False
                        elif guesstimes == 4 and path == 3:
                            print("You are on 4 of <s and >s pathsss")
                        else:continue

                    # > = path
                    #added a nuetral number
                    elif white == Wcheck:
                        print("You are on 2 <&>s + 2 =s path")
                        print("suggest guess",str(guesstimes - 1)+str(guesstimes - 1)+str(guesstimes + 3)+str(guesstimes + 3))
                        suggestion = [guesstimes - 1,guesstimes - 1,guesstimes + 3,guesstimes + 3]
                        print (suggestion)
                        FB =check(suggestion)
                        print(FB)
                        #If the pair are both in the code
                        print("resetor is", reseter)
                        # <> = good and = bad
                        if reseter == 2 and len(FB) > 0:
                            print(str(guesstimes - 1), str(guesstimes + 3), "are good numbers")
                            print("removed", str(codepool[guesstimes - 1]) + str(codepool[guesstimes + 3]))
                            print(codepool)
                            codepool[guesstimes + 3] = 0
                            codepool[guesstimes - 1] = 0
                            codepool = list(filter((0).__ne__, codepool))
                            print(codepool)
                            print("Great! You've found the secret four digits! But what's the order?")
                            MM = False
                            individual = False
                            white = Wcheck
                        # <> = bad and = good
                        if reseter == 2 and len(FB) == 0:
                            print(str(guesstimes - 1), str(guesstimes + 3), "are bad numbers")
                            print("removed", str(codepool[guesstimes - 2]) + str(codepool[guesstimes + 2]))
                            codepool[guesstimes + 2] = 0
                            codepool[guesstimes - 2] = 0
                            codepool = list(filter((0).__ne__, codepool))
                            print(codepool)
                            print("Great! You've found the secret four digits! But what's the order?")
                            MM = False
                            individual = False
                            white = Wcheck
                        # < = path
                        elif len(FB) > 0:
                            print(str(guesstimes - 1),str(guesstimes + 3),"are good numbers")
                            guess = aspt()
                            FB = check(guess)
                            Wcheck = len(FB)
                            guesstimes+=1
                            # < = > path
                            if white > Wcheck:
                                whitechecker = -1
                                print(whitechecker, "Bad New Number")
                                print("removed", str(codepool[guesstimes + 2]) + str(codepool[guesstimes - 1]) + str(codepool[guesstimes + 3]))
                                codepool[guesstimes + 2] = 0
                                codepool[guesstimes - 1] = 0
                                codepool[guesstimes + 3] = 0
                                print(guesstimes)
                                codepool= list(filter((0).__ne__, codepool))
                                print(codepool)
                                print("Great! You've found the secret four digits! But what's the order?")
                                MM = False
                                individual = False
                                white = Wcheck

                            # Removed number is bad
                            # < = < path
                            elif white < Wcheck:
                                whitechecker = 1
                                print(whitechecker, "Good new number")
                                print("removed", str(codepool[guesstimes - 2])+str(codepool[guesstimes - 1])+str(codepool[guesstimes + 3]))
                                codepool[guesstimes - 2] = 0
                                codepool[guesstimes - 1] = 0
                                codepool[guesstimes + 3] = 0
                                codepool= list(filter((0).__ne__, codepool))
                                print(codepool)
                                print("Great! You've found the secret four digits! But what's the order?")
                                MM = False
                                individual = False
                                white = Wcheck

                            # < = 0 <> path
                            elif white == Wcheck:
                                print("removed", str(codepool[guesstimes - 2]) + str(codepool[guesstimes + 2]),"dsadasdas")
                                codepool[guesstimes - 2] = 0
                                codepool[guesstimes + 2] = 0
                                guesstimes +=1
                                guess = aspt()
                                FB = check(guess)
                                Wcheck = len(FB)
                                if white > Wcheck:
                                    whitechecker = -1
                                    print(whitechecker, "Bad New Number")
                                    print("removed", str(codepool[guesstimes + 2]))
                                    codepool[guesstimes + 2] = 0
                                    codepool = list(filter((0).__ne__, codepool))
                                    print(codepool)
                                    print("Great! You've found the secret four digits! But what's the order?")
                                    MM = False
                                    individual = False
                                elif white < Wcheck:
                                    whitechecker = 1
                                    print(whitechecker, "Good new number")
                                    print("removed", str(codepool[guesstimes -2]))
                                    codepool[guesstimes - 2] = 0
                                    codepool = list(filter((0).__ne__, codepool))
                                    print(codepool)
                                    print("Great! You've found the secret four digits! But what's the order?")
                                    MM = False
                                    individual = False

                        elif len(FB) == 0:
                            print(str(guesstimes - 1), str(guesstimes + 3), "are bad numbers")
                            print("removed",str(guesstimes - 1), str(guesstimes + 3) )
                            codepool[guesstimes + 2] = 0
                            codepool[guesstimes - 2] = 0
                            print(codepool)
                            guess = aspt()
                            FB = check(guess)
                            Wcheck = len(FB)
                            guesstimes += 1
                            # print("White is",white)
                            # print("Wcheck is", Wcheck)
                            # Removed number is good
                            if white > Wcheck:
                                whitechecker = -1
                                print(whitechecker, "Bad New Number")
                                print("removed", str(codepool[guesstimes + 2]))
                                codepool[guesstimes + 2] = 0
                                print(guesstimes)
                                codepool = list(filter((0).__ne__, codepool))
                                print(codepool)
                                print("Great! You've found the secret four digits! But what's the order?")
                                MM = False
                                individual = False
                                white = Wcheck


                            # Removed number is bad
                            elif white < Wcheck:
                                whitechecker = 1
                                print(whitechecker, "Good new number")
                                print("removed", str(codepool[guesstimes - 2]))
                                codepool[guesstimes - 2] = 0
                                codepool = list(filter((0).__ne__, codepool))
                                print(codepool)
                                print("Great! You've found the secret four digits! But what's the order?")
                                MM = False
                                individual = False
                                white = Wcheck




                            elif white == Wcheck:
                                print( str(codepool[guesstimes - 2]) + str(codepool[guesstimes + 2])," are good numbers")
                                guess = aspt()
                                guesstimes += 1
                                FB = check(guess)
                                Wcheck = len(FB)
                                if white > Wcheck:
                                    whitechecker = -1
                                    print(whitechecker, "Bad New Number")
                                    print("removed", str(codepool[guesstimes + 2]))
                                    codepool[guesstimes + 2] = 0
                                    codepool = list(filter((0).__ne__, codepool))
                                    print(codepool)
                                    print("Great! You've found the secret four digits! But what's the order?")
                                    MM = False
                                    individual = False
                                elif white < Wcheck:
                                    whitechecker = 1
                                    print(whitechecker, "Good new number")
                                    print("removed", str(codepool[guesstimes - 2]))
                                    codepool[guesstimes - 2] = 0
                                    codepool = list(filter((0).__ne__, codepool))
                                    print(codepool)
                                    print("Great! You've found the secret four digits! But what's the order?")
                                    MM = False
                                    individual = False

                    #print("pain in th a")


                elif pathway == 2:
                    # Both number have the same trait.
                    print("you are on Pathway", str(pathway))
                    print("You've guessed:" + str(guesstimes) + "times")
                    whitechecker = 0
                    print(whitechecker, "They have the same trait!")
                    print(FB)
                    print(Wcheck,"dasdsadasdas")
                    if Wcheck != 2:
                        print("you are on a 2<>s and 2=s path.")
                        print("suggest guess",str(guesstimes - 1) + str(guesstimes - 1) + str(guesstimes + 3) + str(guesstimes + 3))
                        suggestion = [guesstimes - 1, guesstimes - 1, guesstimes + 3, guesstimes + 3]
                        print(suggestion)
                        FB = check(suggestion)
                        print(FB)
                        if len(FB) > 0:
                            print(str(guesstimes - 1), str(guesstimes + 3), "are good numbers")
                            guess = aspt()
                            FB = check(guess)
                            Wcheck = len(FB)
                            print(Wcheck)
                            print(white,"123")
                            guesstimes += 1
                            if white > Wcheck:
                                whitechecker = -1
                                reseter += 1
                                print(whitechecker, "Bad New Numbert")
                                codepool[guesstimes + 2] = 0
                                #print(guesstimes)
                                print(codepool)
                                white = Wcheck
                                guess = aspt()
                                guesstimes += 1
                                FB = check(guess)
                                Wcheck = len(FB)
                                print(Wcheck,"and",white)
                                #guesstimes += 1
                                if white > Wcheck:
                                    print(whitechecker, "Bad New Number")
                                    print(guesstimes, "Guesssew")
                                    print("removed",str(codepool[guesstimes + 2]) + str(codepool[guesstimes - 1]) + str(codepool[guesstimes + 3]))
                                    codepool[guesstimes + 2] = 0
                                    codepool[guesstimes - 1] = 0
                                    codepool[guesstimes + 3] = 0
                                    print(guesstimes)
                                    codepool = list(filter((0).__ne__, codepool))
                                    print(codepool)
                                    print("Great! You've found the secret four digits! But what's the orde2r?")
                                    MM = False
                                    individual = False
                                    white = Wcheck
                                    break

                                elif white < Wcheck:
                                    whitechecker = 1
                                    print(whitechecker, "Good new number")
                                    print(guesstimes,"dad")
                                    print("removed",str(codepool[guesstimes - 2]) + str(codepool[guesstimes - 1]) + str(codepool[guesstimes + 3]))
                                    codepool[guesstimes - 2] = 0
                                    codepool[guesstimes - 1] = 0
                                    codepool[guesstimes + 3] = 0
                                    print(codepool)
                                    codepool = list(filter((0).__ne__, codepool))
                                    print(codepool)
                                    print("Great! You've found the secret four digits! But what's the order?")
                                    MM = False
                                    individual = False
                                    white = Wcheck
                                elif  white == Wcheck:
                                    print("removed", str(codepool[guesstimes - 2]) + str(codepool[guesstimes + 2]),"dsadasdas")
                                    codepool[guesstimes - 2] = 0
                                    codepool[guesstimes + 2] = 0
                                    guesstimes += 1
                                    guess = aspt()
                                    FB = check(guess)
                                    Wcheck = len(FB)
                                    if white > Wcheck:
                                        whitechecker = -1
                                        print(whitechecker, "Bad New Number")
                                        print("removed", str(codepool[guesstimes + 2]))
                                        codepool[guesstimes + 2] = 0
                                        codepool = list(filter((0).__ne__, codepool))
                                        print(codepool)
                                        print("Great! You've found the secret four digits! But what's the order?")
                                        MM = False
                                        individual = False
                                    elif white < Wcheck:
                                        whitechecker = 1
                                        print(whitechecker, "Good new number")
                                        print("removed", str(codepool[guesstimes - 2]))
                                        codepool[guesstimes - 2] = 0
                                        codepool = list(filter((0).__ne__, codepool))
                                        print(codepool)
                                        print("Great! You've found the secret four digits! But what's the order?")
                                        MM = False
                                        individual = False

                                # path +=pathway

                            elif white < Wcheck:
                                whitechecker = 1
                                reseter += 1
                                print(whitechecker, "Good new numbert")
                                codepool[guesstimes - 2] = 0
                                print(codepool)
                                white = Wcheck
                                guess = aspt()
                                guesstimes += 1
                                FB = check(guess)
                                Wcheck = len(FB)
                                print(Wcheck, "and", white)
                                # guesstimes += 1
                                if white > Wcheck:
                                    print(whitechecker, "Bad New Number")
                                    print(guesstimes, "Guesssew")
                                    print("removed",
                                          str(codepool[guesstimes + 2]) + str(codepool[guesstimes - 1]) + str(
                                              codepool[guesstimes + 3]))
                                    codepool[guesstimes + 2] = 0
                                    codepool[guesstimes - 1] = 0
                                    codepool[guesstimes + 3] = 0
                                    print(guesstimes)
                                    codepool = list(filter((0).__ne__, codepool))
                                    print(codepool)
                                    print("Great! You've found the secret four digits! But what's the order?")
                                    MM = False
                                    individual = False
                                    white = Wcheck
                                    break

                                elif white < Wcheck:
                                    whitechecker = 1
                                    print(whitechecker, "Good new number")
                                    print(guesstimes, "dad")
                                    print("removed",
                                          str(codepool[guesstimes - 2]) + str(codepool[guesstimes - 1]) + str(
                                              codepool[guesstimes + 3]))
                                    codepool[guesstimes - 2] = 0
                                    codepool[guesstimes - 1] = 0
                                    codepool[guesstimes + 3] = 0
                                    print(codepool)
                                    codepool = list(filter((0).__ne__, codepool))
                                    print(codepool)
                                    print("Great! You've found the secret four digits! But what's the order?")
                                    MM = False
                                    individual = False
                                    white = Wcheck
                                elif white == Wcheck:
                                    print("removed", str(codepool[guesstimes - 2]) + str(codepool[guesstimes + 2]),
                                          "dsadasdas")
                                    codepool[guesstimes - 2] = 0
                                    codepool[guesstimes + 2] = 0
                                    guesstimes += 1
                                    guess = aspt()
                                    FB = check(guess)
                                    Wcheck = len(FB)
                                    if white > Wcheck:
                                        whitechecker = -1
                                        print(whitechecker, "Bad New Number")
                                        print("removed", str(codepool[guesstimes + 2]))
                                        codepool[guesstimes + 2] = 0
                                        codepool = list(filter((0).__ne__, codepool))
                                        print(codepool)
                                        print("Great! You've found the secret four digits! But what's the order?")
                                        MM = False
                                        individual = False
                                    elif white < Wcheck:
                                        whitechecker = 1
                                        print(whitechecker, "Good new number")
                                        print("removed", str(codepool[guesstimes - 2]))
                                        codepool[guesstimes - 2] = 0
                                        codepool = list(filter((0).__ne__, codepool))
                                        print(codepool)
                                        print("Great! You've found the secret four digits! But what's the order?")
                                        MM = False
                                        individual = False

                                #print(path, "path")
                            #elif white == Wcheck:


                    #print("suggest guess",str(guesstimes - 1) + str(guesstimes - 1) + str(guesstimes + 3) + str(guesstimes + 3))
                    #suggestion = [guesstimes - 1, guesstimes - 1, guesstimes + 3, guesstimes + 3]
                    #print(suggestion)
                    #FB = check(suggestion)
                    print(FB)
                    print(ocode)



                #print(white)




        if FB=="RRRR" :
            print("Yes!! you've nailed it!")
            MM= False
            individual= False
        if guesstimes >10:
            print("Well, you did not get the anwser. The answer is ",ocode)
            MM= False
            individual = False
    #if MM==False:
        #MM=True
        #individual= True
        #guesstimes =0
        #codepool = {1, 2, 3, 4, 5, 6, 7, 8}

