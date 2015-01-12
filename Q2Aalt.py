#imports
import sys
import fileinput

# Counter, maybe there is a better way
count = 0

# Iterieration of Input
for line in fileinput.input():
    
    # Selection of Header
    if count == 0 :
        
        #Format the Header
        newL = '>' + line.replace('@' , '')
        
        # Print the Header without newline
        sys.stdout.write(newL)
        
    # Selection of Sequence
    elif count == 1 :
        
        # Print the Sequence
        sys.stdout.write(line)
        
    # Up's the Counter
    count += 1
    count = count % 4
    

