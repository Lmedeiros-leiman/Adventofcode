# list of locations to check is empty.
# receives a text file with two lists (split by \n and tab space)
# need to split it into 2 lists
# needs to calculate the distance between the nth smallest number of each list.
#

from pathlib import Path
import os


# fetch the input from the file
def getInput():
    fileInput = open(Path(__file__).parent / "firstStarInput.txt",'r').read()
    return fileInput.split()

# splits the input into arrays 

def main():
    input = getInput()
    l1 = {}
    l2 = []
    
       
    for i,n in enumerate(input):
        if (i % 2 == 0):
            l1[n] = 0
        else:
            l2.append(n)
    
    
    similarity = 0
    for n in l2:
        if (l1.get(n) != None):
            l1[n] += 1
    
    for key in l1.keys():
        similarity += l1[key] * int(key)
    
    print(similarity)
    
    pass
main()