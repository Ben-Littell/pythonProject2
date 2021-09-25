def write_file(filename, a_string):
    with open(filename, 'a') as file:
        file.write(a_string)


# write_file("test.txt", 'Test\n')


def open_file(filename, mode='read'):
    with open(filename, 'r') as file:
        if mode == 'read':
            text = file.read()
        elif mode == 'readlines':
            text = file.readlines()
        elif mode == 'readline':
            text = file.readline()
        return text


# open_ = open_file('test.txt', 'readlines')

def printfile(filename):
    file = open_file(filename)
    print(file)


# printfile('first_file.txt')

def sum_column(filename):
    total = 0
    lines = open_file(filename, 'readlines')
    for line in lines:
        total += int(line)
    return total


# sum_text = sum_column('sum_numbers.txt')
# print(sum_text)

def sum_all(filename):
    numb = 0
    total = 0
    file = open_file(filename)
    for char in file:
        if char.isdigit():
            numb += int(char)
        else:
            total += numb
            numb = 0
    return total



file_sum = sum_all('sum_all.txt')
print(file_sum)