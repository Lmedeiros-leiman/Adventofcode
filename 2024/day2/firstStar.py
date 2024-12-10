#
#
#
from pathlib import Path
import os


# fetch the input from the file
def getInput():
    fileInput = open(Path(__file__).parent / "input.txt",'r').read()
    #fileInput = open(Path(__file__).parent / "dummy.txt",'r').read()
    return fileInput.split("\n")


def main():
    results = {
        "safe" : 0,
        "unsafe" : 0
    }
    input = getInput()
    
    for r in input:
        sucess = True
        sequence = r.split(" ")
        
        
        for i in range(1,len(sequence) -1): 
            
            prevDiff = int(sequence[i-1]) - int(sequence[i])
            currDiff = int(sequence[i]) - int(sequence[i+1])
            #
            # Check if the ammount that changed is greater than the allowed (3)
            if (abs(prevDiff) > 3 or abs(currDiff) > 3):
                sucess = False
                print("Broke rule 1")
                results["unsafe"] += 1
                break
            #
            # Checks if they have the same path (are both increasing or decreasing)
            if ( (prevDiff > 0) != (currDiff > 0) ):
                sucess = False
                print("Broke rule 2")
                results["unsafe"] += 1
                break
            #
            # Check if any of then is 0
            if (prevDiff == 0 or currDiff == 0):
                sucess = False
                print("Broke rule 3")
                results["unsafe"] += 1
                break
            
            
        #
        if (sucess):
            results["safe"] += 1
        
        print(f" {r} => {sucess}  | { results }")

    #
    print(results)
    pass
main()