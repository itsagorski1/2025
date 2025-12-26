import sys

def getJoltage(line):
    lineLen = len(line)
    firstDigitIndex = line.index(max(line[:(lineLen-1)]))
    firstDigit = max(line[:(lineLen-1)])
    lastDigitIndex = line.index(max(line[(firstDigitIndex+1):]))
    lastDigit = max(line[(firstDigitIndex+1):])
    return str(firstDigit) + str(lastDigit)

def parseLines():
    with open(sys.argv[1], 'rt') as input_file:
        input_lines = [x.strip() for x in input_file.readlines()]
    for line in input_lines:
        totalJoltage = int(getJoltage(line))
    return totalJoltage

if __name__ == '__main__':
    print(parseLines())