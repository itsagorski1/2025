import sys

def check_validity(number):
    str_of_num = str(number)
    for i in range(1,(len(str_of_num) // 2)+1):
        if str_of_num[:i] * (len(str_of_num) // i) == str_of_num:
            return True
    return False
    

def check_range(start, end):
    invalid_number_total = 0
    for number in range(start, end + 1):
        if check_validity(number):
            invalid_number_total += number
    return invalid_number_total

def parse_range():
    with open(sys.argv[1], 'r') as input_file:
        input_lines = [x.strip() for x in input_file.readlines()]
    bad_number_total = 0
    numbers = input_lines[0].split(',')
    for i in range(len(numbers)):
        bad_number_total += check_range(int(numbers[i-1].split('-')[0]), int(numbers[i-1].split('-')[1]))
    return bad_number_total

if __name__ == '__main__':
    print(parse_range())