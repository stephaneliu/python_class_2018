#!/usr/bin/python3

def cleanup(dirty):
    clean = []
    for word in dirty:
        clean.append(word.strip().lower())
    return clean

spam = [
    "Spam", 
    "eggs  ",
    "   spam    ",
    "     spam spam     ", 
    "SPAM	", 
    "       SPAM and eggs    ",
    "Spam",
    "   Spam,    spam, spam,    spam, spam, eggs, and spam      ",
]

print(cleanup(spam))

