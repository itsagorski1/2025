import sys

def getJoltage(s):
    digits = list(s)
    remove = len(digits) - 12

    while remove > 0:
        for i in range(len(digits) - 1):
            if digits[i] < digits[i + 1]:
                del digits[i]
                break
        else:
            digits.pop()
        remove -= 1

    return ''.join(digits)

def parseLines():
    totalJoltage = 0
    with open(sys.argv[1], 'rt') as input_file:
        input_lines = [x.strip() for x in input_file.readlines()]
    for line in input_lines:
        totalJoltage += int(getJoltage(line))
    return totalJoltage

if __name__ == '__main__':
    print(parseLines())