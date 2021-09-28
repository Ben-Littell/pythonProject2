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


# file_sum = sum_all('sum_all.txt')
# print(file_sum)

def read_column(filename, column_num=0):
    column_list_in = []
    file = open_file(filename, 'readlines')
    for line in file:
        split_line = line.split()
        column_list_in.append(split_line[column_num])
    return column_list_in


# column_list = read_column('numb_6.txt', 5)
# print(column_list)

# single word
def count_word(filename, word='is'):
    counter = 0
    new_word = ''
    file = open_file(filename).lower().split()
    word_l = word.lower()
    for item in file:
        for char in item:
            if char.isalpha():
                new_word += char
        if new_word == word_l:
            counter += 1
            new_word = ''
        else:
            new_word = ''

    return counter


# word_counts = count_word('zenofpython.txt')
# print(word_counts)

def count_words(filename, words):
    word_dict = {}
    new_word = ''
    file = open_file(filename).lower().split()
    for word in words:
        counter = 0
        word_l = word.lower()
        for item in file:
            for char in item:
                if char.isalpha():
                    new_word += char
            if new_word == word_l:
                counter += 1
                new_word = ''
            else:
                new_word = ''
        word_dict.update({word: counter})

    return word_dict


# words_counter = count_words('zenofpython.txt', ['purity', 'is', 'never'])
# print(words_counter)
