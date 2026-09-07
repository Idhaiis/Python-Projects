#Used stackoverflow, w3schools and google images (for mors alphabet)
#Only used ai for making README.md
import keyboard, time
import os

MorsList = [""]
Sentence = ""
Counter = 0

MorsDict = {
    "": " ",
    ".": "E",
    "..": "I",
    "...": "S",
    "....": "H",
    "._": "A",
    ".._": "U",
    "..._": "V",
    ".__": "W",
    ".___": "J",
    "._.": "R",
    "._..": "L",
    ".._.": "F",
    ".__.": "P",
    "_": "T",
    "__": "M",
    "___": "O",
    "_.": "N",
    "__.": "G",
    "__..": "Z",
    "__._": "Q",
    "_..": "D",
    "_...": "B",
    "_._": "K",
    "_._.": "C",
    "_.__": "Y",
    "_.._": "X",
    ".____": "1",
    "..___": "2",
    "...__": "3",
    "...._": "4",
    ".....": "5",
    "_....": "6",
    "__...": "7",
    "___..": "8",
    "____.": "9",
    "_____": "0"                                            
}

def clear():
    os.system('cls')
    print(MorsList)
    print(Sentence)
    
clear()

while True:
    a = keyboard.read_event()     #Reading the key
    if a.name == "esc":break      #Loop will break on pressing esc, you can remove that
    elif a.event_type == "down":  #If any button is pressed (Not talking about released) then wait for it to be released
        t = time.time()           #Getting time in sec
        b = keyboard.read_event() 
        while not b.event_type == "up" and b.name == a.name:  #Loop till the key event doesn't matches the old one
            b = keyboard.read_event()
        if b.name == "enter":
            try:
                Sentence += MorsDict[MorsList[Counter]]
                MorsList.append("")
                Counter += 1
                clear()
            except:
                MorsList[Counter] = ""
                clear()
                print("\n This morse code doesn't includes at dictionary")
        else:
            if time.time()-t <= 0.1:
                MorsList[Counter] = MorsList[Counter] + "."
                clear()
            else:
                MorsList[Counter] = MorsList[Counter] + "_"
                clear()