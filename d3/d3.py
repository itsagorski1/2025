import sys

def getJoltage(line):
    lineLen = len(line)
    firstDigitIndex = line.index(max(line[:(lineLen-1)]))
    firstDigit = max(line[:(lineLen-1)])
    lastDigitIndex = line.index(max(line[(firstDigitIndex+1):]))
    lastDigit = max(line[(firstDigitIndex+1):])
    return (firstDigitIndex, firstDigit, lastDigitIndex, lastDigit)