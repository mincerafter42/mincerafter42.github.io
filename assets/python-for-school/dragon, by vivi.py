import time

game = ("You are a dragon! You live in a dragon cave with your treasure. But now, you find a human has entered your cave!\nType 1 to share some treasure with the human.`Type 2 to eat the human.",
 ('You share some treasure with the human.\n"Wow, thanks," the human says. "I have a gift for you too, if you want it.\n1 to take the gift.`2 to not take the gift.',
  ('The human gives you a beautiful chalice, which is a sort of cup if you didn\'t know. You place it in your chalice collection.\n"Well, I\'ll be going now," says the human, "unless you want me to stay."\n1 to let the human leave.`2 to ask the human to stay.',
   ('The human leaves your cave and gives your cave an awesome review on Google Maps. You now have a cool chalice. You can drink stuff out of it. Probably water.\nTHE END',()),
   ('"Oh, cool!" says the human. "So what do you want to do?"\n1 to ask the human about their interests.`2 to tell the human about your interests.`3 to play Monopoly with the human.',
    ('The human tells you about knitting. You don\'t knit, but knitted clothes sound fun and cozy.\n1 to ask the human if they want to knit you some clothes.`2 to tell the human about your interests.',
     ('"I\'d love to knit you some clothes!" replies the human. "I think they\'ll look great on you! Is there any design you want?"\n1 to ask for a scaly design like your dragon scales.`2 to ask for a solid purple design.`3 to ask for a surprise.',
      ('The human takes your measurements, and comes back a month later with a box.\nYou open the box to find a lovely sweater with pictures of devices that measure mass. Scales.\n"Just kidding!" says the human, and gives you another box containing a second lovely sweater with an awesome pattern of brightly coloured scales.\nThis human is a great friend. They have an excellent sense of humour too. You have made a new friend!\nTHE END',()),
      ('The human takes your measurements, and comes back one week later with a box.\nYou open the box to find a lovely sweater that\'s a wonderful shade of purple.\nThis human is very kind. And friendly. In fact they are so friendly that they are a friend!\nYou made a new friend! THE END',()),
      ('The human takes your measurements, and comes back two weeks later with a box.\nYou open the box to find a lovely sweater with a simple picture of a human hugging a dragon on the front.\nThis is an awesome sweater.\n1 to thank the human for the sweater.`2 to thank the human for the sweater and also hug them.',
       ('You thank the human for the awesome sweater, and they are fine that you don\'t want a hug.\nThe fact that you like the sweater is good enough for them and they have plenty of friends to hug. This human is a great friend.\nTHE END',()),
       ('You hug the human. The human hugs back.\nIt is snug.\nIt would probably be more snug if you were wearing your awesome sweater.\n\nThis human is a great friend. In fact you think they are your new best friend!\nTHE END',()))),
     ('You tell the human about your love of computer programming, and the programming classes you took in high school.\nThe human likes programming too!\nThe two of you decide to work on programming projects together over the Internet.\nTHE END',())),
    ('You tell the human about your love of computer programming, and the programming classes you took in high school.\nThe human likes programming too!\nThe two of you decide to work on programming projects together over the Internet.\nTHE END',()),
    ('You show the human your limited edition dragon-themed Monopoly board, which definitely exists even though I did no research into the history of Monopoly boards.\nThe human doesn\'t particularly like Monopoly, but plays with you anyway. The human now thinks of you as an acquaintance and promises to tell you if anyone they know wants to play Monopoly.\nTHE END',()))),
  ('You politely decline. "That\'s OK," the human replies, "I can find somebody else to give this gift to." The human leaves, giving your cave a nice review on Google Maps.\nTHE END',())),
 ("You are now digesting a human. The human thinks you are very rude. The human leaves a terrible review of your cave on Google Maps and then dies.\nTHE END",()))

def askQuestion(question):
    # gonna print the text with some time delay
    texts = question[0].split("\n")
    for message in range(len(texts)):
        if message > 0:
            time.sleep(1.4) # sleep before any message that isn't the first
        print(texts[message].replace("`","\n")) # this is how we can have newlines without a time delay
    answers = len(question)-1 # determine number of answers
    if answers > 1: # only continue if it's not the end
        choice = input() # get input
        while type(choice)!=int: # being sure input is an int
            try:
                choice = int(choice) # try to make choice an int
                if choice < 1 or choice > answers: # then check if it's in the correct range
                    print("No, it has to be between 1 and "+str(answers)+". Try again")
                    choice = input()
            except:
                print("No, it has to be a number! Try again")
                choice = input()
        askQuestion(question[choice]) # once the choice is made, continue with it
    # if no answers, just end
doAgain = "y"
while doAgain == "y":
    askQuestion(game)
    time.sleep(2)
    print("Type \"y\" to play again.")
    doAgain = input()
        
