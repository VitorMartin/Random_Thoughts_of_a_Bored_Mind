def validate_input(test):
    # Validate size of input
    t = len(test.split())
    if t < 2:
        print('Input too short')
        return False
    elif t > 3:
        print('Input too long')
        return False

    elif t == 2:    # So pode o formato '## END'
        t = test.split()    # '45, END'

        try:
            int(t[0])
        except ValueError:
            print('First char must be INT')
            return False

        if t[1] != 'END':
            print('Input with 2 commands expect an INT and \'END\' command')
            return False

    else:   # Input com 3 elementos '10 GOTO 45'
        t = test.split()    # [10, GOTO, 45]
        if t[1] != 'GOTO':
            print('\'GOTO\' command not found')
            return False

        try:
            int(t[0])
        except ValueError:
            print('First char must be INT')
            return False

        try:
            int(t[2])
        except ValueError:
            print('Last char must be INT')
            return False

    return True


def get_basic():
    prog = []
    while True:
        inp = input('Define line as \'## GOTO ##\' or \'## END\' to finish input: ')
        inp = inp.upper()    # string

        test = validate_input(inp)
        if test is False:
            continue
        else:
            prog.append(inp)

        if inp.split()[1].endswith('END'):
            print('Your input:', prog)
            return prog


def find_line(prog, target):    # INPUT(['10 GOTO 21', '21 END'], '21') –> OUTPUT(2)
    target = str(target)

    for i in range(len(prog)):
        label = prog[i].split()
        label = label[0]    # Seleciona o label da linha de comando: '10 GOTO 21' –> 10

        if label == target:
            return i


def execute(prog):
    location = 0
    visited = [False] * len(prog)

    while True:
        if prog[location].endswith('END'):    # Se o comando termina em END –> 'success'
            return "success"

        if visited[location] is True:         # Se o comando ja foi visitado –> 'infinite loop'
            return 'infinite loop'

        visited.insert(location, True)    #
        visited.remove(False)             # Troca o False por True na ordem crescente

        T = prog[location].split()
        T = T[len(T) - 1]           # T = target

        location = find_line(prog, T)


while True:
    print(execute(get_basic()))
    print('--------------------')
