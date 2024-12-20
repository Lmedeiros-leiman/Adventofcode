from pathlib import Path


# fetch the input from the file
def getInput():
    fileInput = open(Path(__file__).parent / "input.txt",'r').read()
    return fileInput.split()


def main():
    a = getInput()

    print(a)
    pass
main()




