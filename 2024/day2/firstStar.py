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


# reduce the numbers to their difference values.
def parseDifference(input):
    output = []
    for sequence in input:
        aux = []
        sequence = sequence.split(" ")
        for i in range(0, len(sequence) -1):
            diff = int(sequence[i+1]) - int(sequence[i]) 
            aux.append(diff)
        output.append(aux)
    return output
    
def isSafe(sequence):
    dampner = 0 # default first start problem
    signal = "+"
    if sequence[0] < 0:
        signal = "-"
        
    for n in sequence:
        if ( abs(n) > 3 or abs(n) < 1 ):
            dampner = dampner - 1
            
        if( (n > 0 and signal == "-") or (n < 0 and signal == "+")  ):
            dampner = dampner -1
        
        if (dampner < 0):
            return False
            break
    #

    return True
    

def main():
    results = {
        "safe" : 0,
        "unsafe" : 0
    }
    
    input = parseDifference(getInput())
    
    for sequence in input:
        if isSafe(sequence):
            results["safe"] += 1
        else:
            results["unsafe"] += 1
    
    print(results)
    
    return
    
main()