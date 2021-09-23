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

