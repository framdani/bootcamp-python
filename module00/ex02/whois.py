import sys

argc = len(sys.argv)
if argc>1:
    if (argc == 2):
        if (sys.argv[1]==0):
            print("I'm zero");
        elif (int(sys.argv[1])%2==0):
            print("I'm odd")
        elif int(sys.argv[1])%2!=0:
            print("I'm even");
    else:
        print("Error")
