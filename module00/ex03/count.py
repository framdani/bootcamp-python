import string

def text_analyzer(*text):
    if (len(text) == 0):
        print("What is the text to analyse?")
        return
    if (len(text)>1):
        print("Error")
    else:
        upper = 0
        lower = 0
        space = 0
        marks = 0
        print("The text contains " + str(len(text)) + " characters:")
        for c in text[0]:
            if c.islower():
                lower = lower + 1
            elif c.isupper():
                upper = upper + 1
            elif c.isspace():
                space = space + 1
            elif c in string.punctuation:
                marks = marks + 1
        print("- "+ str(upper) +" upper letters")
        print("- "+ str(lower) +" lower letters")
        print("- "+ str(marks ) +" punctuation marks")
        print("- "+ str(space) +" spaces")
    return
