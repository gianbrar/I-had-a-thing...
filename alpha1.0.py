import time
from random import randint
print("Welcome to excuse generator 1.0. Generating excuse...")
noun0 = (randint(0, 25))
verb0 = (randint(1, 9))
adjective1 = (randint(1, 3))
if noun0 == 0:
    nouncorrespondent0 = "cat"
elif noun0 == 1:
    nouncorrespondent0 = "sandwich"
elif noun0 == 2:
    nouncorrespondent0 = "house plant"
elif noun0 == 3:
    nouncorrespondent0 = "mother"
elif noun0 == 4:
    nouncorrespondent0 = "father"
elif noun0 == 5:
    nouncorrespondent0 = "computer"
elif noun0 == 6:
    nouncorrespondent0 = "best friend"
elif noun0 == 7:
    nouncorrespondent0 = "younger brother"
elif noun0 == 8:
    nouncorrespondent0 = "older brother"
elif noun0 == 9:
    nouncorrespondent0 = "younger sister"
elif noun0 == 10:
    nouncorrespondent0 = "older sister"
elif noun0 == 11:
    nouncorrespondent0 = "identical twin"
elif noun0 == 12:
    nouncorrespondent0 = "nonidentical twin"
elif noun0 == 13:
    nouncorrespondent0 = "phone"
elif noun0 == 14:
    nouncorrespondent0 = "tv"
elif noun0 == 15:
    nouncorrespondent0 = "book"
elif noun0 == 16:
    nouncorrespondent0 = "kindle"
elif noun0 == 17:
    nouncorrespondent0 = "ebook"
elif noun0 == 18:
    nouncorrespondent0 = "mp3 player"
elif noun0 == 19:
    nouncorrespondent0 = "iPod"
elif noun0 == 20:
    nouncorrespondent0 = "Zune"
elif noun0 == 21:
    nouncorrespondent0 = "iPad"
elif noun0 == 22:
    nouncorrespondent0 = "excuse generator"
elif noun0 == 23:
    nouncorrespondent0 = "mac&cheese"
elif noun0 == 24:
    nouncorrespondent0 = "ceiling"
elif noun0 == 25:
    nouncorrespondent0 = "floor"

if verb0 == 1:
    verbcorrespondent0 = "be watered"
elif verb0 == 2:
    verbcorrespondent0 = "be destroyed"
elif verb0 == 3:
    verbcorrespondent0 = "go to their soccer game"
elif verb0 == 4:
    verbcorrespondent0 = ""
elif verb0 == 5:
    verbcorrespondent0 = "talking"
elif verb0 == 6:
    verbcorrespondent0 = "kinder to others"
elif verb0 == 7:
    verbcorrespondent0 = "eat"
elif verb0 == 8:
    verbcorrespondent0 = "befriending others"
elif verb0 == 9:
    verbcorrespondent0 = "go to their martial arts lesson"

if adjective1 == 1:
    adjectivecorrespondent0 = "red"
elif adjective1 == 2:
    adjectivecorrespondent0 = "needy"
elif adjective1 == 3:
    adjectivecorrespondent0 = "deadly"


print("I would love to, but my "+ nouncorrespondent0 , "needs to "+ verbcorrespondent0+", because it's "+ adjectivecorrespondent0+".")
