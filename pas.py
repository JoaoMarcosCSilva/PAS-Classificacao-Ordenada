import sys

filename = sys.argv[1]

def toNumber (s):
    if (s[0].isdigit()):
        return float(s)
    if (s == 'AUS' or s == '--' or s == 'N.A'):
        return -1

def isNumber (s):
    if (s[0].isdigit()):
        return True
    if (s == 'AUS' or s == '--' or s == 'N.A'):
        return True
    return False

class Entry:
    def __init__(self, s):
        entry = s.split()
        
        self.id = entry[0]
        self.name = ''
        
        firstNumber = 0
        
        for wordNumber in range(1, len(entry)):
            if not isNumber(entry[wordNumber]):
                self.name += entry[wordNumber] + ' '
            else:
                firstNumber = wordNumber
                break
        
        self.conhGerais = toNumber(entry[firstNumber + 0])
        self.lingPort   = toNumber(entry[firstNumber + 1])
        self.linEstr    = toNumber(entry[firstNumber + 2])
        self.red        = toNumber(entry[firstNumber + 3])
        self.total      = toNumber(entry[firstNumber + 4])
        self.aprovado   = entry      [firstNumber + 5]
    
        
def isEntry(s):
    for i in range(0,9):
        if s[i].isdigit() == False:
            return False
    if s[9] != '-':
        return False
    if s[10].isdigit() == False:
        return False
    return True
    
file = open(filename, 'r')
database = sorted([Entry(s) for s in file.read().split('\n') if isEntry(s)], key = lambda entry: entry.total, reverse = True)

results = ''

for index, entry in enumerate(database):
    results += str(index + 1) + ';'
    results += str(entry.id) + ';'
    results += str(entry.name) + ';'
    results += str(entry.conhGerais) + ';'
    results += str(entry.lingPort) + ';'
    results += str(entry.linEstr) + ';'
    results += str(entry.red) + ';'
    results += str(entry.total) + ';'
    results += str(entry.aprovado) + '\n'

fileOut = open('pas output.txt','w')
fileOut.write(results)
fileOut.close()