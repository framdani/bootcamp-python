import sys
l = len(sys.argv)
if l != 3:
    print("ERROR")
else:
    new_words=[]
    if sys.argv[2].isdigit()==False or sys.argv[1].isdigit():
        print("ERROR")
    else:
        new_words=sys.argv[1].split(' ')
        return_value=[]
        for i in new_words:
            if len(i)>int(sys.argv[2]):
                return_value.append(i)
        print(return_value)
