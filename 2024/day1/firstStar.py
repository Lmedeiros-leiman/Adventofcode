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
    l1 = []
    l2 = []
    
    for i,n in enumerate(input):
        if (i % 2 == 0):
            l1.append(int(n))
        else:
            l2.append(int(n))
    #
    distance = 0
    l1.sort()
    l2.sort()
    for i,n in enumerate(l1):
        if (l1[i] > l2[i]):
            distance += (l1[i] - l2[i])
        else:
            distance += (l2[i] - l1[i])
    
    print(distance)
    
    pass
main()