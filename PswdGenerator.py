
from random import randint

class PswdGenerator:

    listOfCaract = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
        "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
        "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
        "Y", "Z",
    ]

    def __init__(self, nbCaract):
        self.nbCaract = nbCaract

    def getNbCaract(self):
        return self.nbCaract

    def generatePswd(self):

        print("NbCaractère dans liste", len(self.listOfCaract))

        counterOutput = 0
        password      = ""

        while counterOutput <= self.nbCaract:
            password = password + self.listOfCaract[randint(0, len(self.listOfCaract) - 1)]
            counterOutput = counterOutput + 1

        return password
