#imports
import sys


#number of args
numArgs = len(sys.argv)

#ERROR if not enough args were committed
if numArgs <= 1:
    sys.exit("Not enough arguments!")

#naming input file from args
Input = sys.argv[1]

#opening files
try:
        fastQ = open(Input , 'r')
except IOError, e:
        sys.exit(e)

#parsing through file
while 1:
      
        #saving the lines
        firstL = fastQ.readline()
        secondL = fastQ.readline()
      
        #you could maybe skip these  lines to save ram
        fastQ.readline()
        fastQ.readline()
      
        #make sure that there are no blank lines in the file
        if firstL == "" or  secondL == "":
            break
      
        #edit the Header to begin with '>'
        firstL = '>' + firstL.replace('@' , '')
      
        sys.stdout.write(firstL)
        sys.stdout.write(secondL)

#close both files
fastQ.close()


