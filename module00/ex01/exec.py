import sys

#counter = 0
#argc = len(sys.argv)
#reversedString = ""
#revAlpha = ""
#if argc > 1:
 #   for c in (range(1, argc)):
  #      counter = len(sys.argv[c])
   #     while counter>0:
    #        counter = counter - 1
     #       if sys.argv[c][counter].islower():
      #          reversedString+=sys.argv[c][counter].upper()
       #     else:
        #       reversedString+=sys.argv[c][counter].lower()
        #reversedString += " "
    #print(reversedString)
argv = sys.argv
reverse_str=""
new_str=""
if len(argv)>1:
    for i in argv[::-1][:-1]:
        reverse_str+="".join(reversed(i))
    [c.upper() if c.islower() else c.lower() for c in reverse_str]
    print(reverse_str)

