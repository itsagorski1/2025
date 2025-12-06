import sys

def parseCommand(s):
    return s[0], int(s[1:])

def rotateDial(current_position, rotation_command):
    direction, distance = parseCommand(rotation_command)
    if direction == "R":
        new_position = (current_position + distance) % 100
    elif direction == "L":
        new_position = (current_position - distance) % 100
    return new_position

def main():
    dial = 50
    password = 0
    with open(sys.argv[1], 'r') as input_file:
        input_lines = [x.strip() for x in input_file.readlines()]
        for line in input_lines:
            direction, distance = parseCommand(line)
            for i in range(distance):
                dial = rotateDial(dial, line[0]+"1")
                if dial == 0:
                    password += 1
    print(password)

if __name__ == '__main__':
    main()