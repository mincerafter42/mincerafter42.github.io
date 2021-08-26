# gonna make a horoscope generator
import random
def RFL(LIST): # Random From List (shortened because I'm going to be using this a lot)
    selected = LIST[random.randint(0,len(LIST)-1)] # pick a random item from the list
    if type(selected) in (str,int): return selected # if it's a string or integer literal, return it
    else: return selected() # else it is a function, evaluate then return

planets = ("Mercury","Venus","Mars","Jupiter","Saturn","Uranus","Neptune")
planetLocations = ("in SPACE","REALLY far away","somewhere I think","hidden behind a smudge on my telescope","over there! No wait, that's a star","really pretty","still not habitable","AWESOME","not relevant to the discussion, but I will pretend it is","probably still existing","round","quite big","composed of various molecules","spinning around a lot")
planetStatements = lambda:RFL(planets)+" is "+RFL(planetLocations)

actions = ("avoid","stay away from","beware of","run away screaming if you encounter","look for","seek","benefit from","get uncomfortably close to")
actionTargets = ("school, if you go to it","buildings with a roof","animals with three legs","cats that have colours","your keys",lambda:RFL(planets),"horoscopes","symmetrical patterns","breakfast cereal","those awesome shoes with wheels on them","typing lessons","flat things","bodies of water","the colour yellow","high-voltage electricity","musical instruments","dwarf planets","composite numbers","the letter M","non-scrambled eggs","vehicles with more than three wheels","low-voltage electricity","maths questions","maths questions involving electricity")
advice = lambda:RFL(actions)+" "+RFL(actionTargets)

concatenators = (", meaning you should ",". This means you should ",". I strongly recommend that you ")
adviceVariants = (lambda:advice()+" and "+advice()+".",lambda:advice()+", and "+advice()+", and also "+advice()+".",lambda:adviceVariants[0]()+" "+advice().capitalize()+".")

luckyNumbers = (2,3,5,7,11,13,21,23,29,31,37,41,42)
def getLuckyNumbers(): # return between 3 and 5 lucky numbers
    howMany = random.randint(3,5)
    numbers = []
    while len(numbers)<howMany:
        luckyNumber = RFL(luckyNumbers)
        if luckyNumber not in numbers: numbers.append(luckyNumber)
    return "Lucky numbers: "+str(numbers)[1:-1]

horoscope = lambda:planetStatements()+RFL(concatenators)+RFL(adviceVariants)+"\n"+getLuckyNumbers()

print(" The HOROSCOPE GENERATOR! ".center(80,"=")+"\nUsing the totally real science of predicting the future based on planet locations, and definitely\nnot randomness, find out what YOU should do by pressing the easy-to-press Enter button!")
input()
numberOfHoroscopes=0
again="y"
while again=="y":
    print(horoscope())
    numberOfHoroscopes+=1
    if numberOfHoroscopes==1:
        print('Want to go again? Then type "y". I can make many predictions.')
    elif numberOfHoroscopes<10:
        print('Type "y" for another horoscope.')
    else:
        print("That's a lot of horoscopes. I think you're looking at too many horoscopes. Stop looking at horoscopes.")
        input()
        print("Nope, no more horoscopes for you.")
        input()
        exit()
    again=input()
