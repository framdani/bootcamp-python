import sys
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
argc = len(sys.argv)
def valid_argv():
    for i in range(1, argc):
        for c in sys.argv[i]:
            if c.isalnum()==False and c!=' ':
                return (-1)
    return (0)

if argc!=1:
    if valid_argv() == -1:
        print("ERROR")
    else:
        encoded = ""
        morse = ""
        for i in range(1, argc):
            for c in sys.argv[i]:
                    encoded+=c
            if i != argc-1:
                encoded+=' '
        for c in encoded:
            if c!=' ':
                morse+=MORSE_CODE_DICT[c.upper()]+' '
            else:
                morse+='/ '
        print(morse)
