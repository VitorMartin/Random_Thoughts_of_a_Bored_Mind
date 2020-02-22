def lower_char(char):
    if 'A' <= char <= 'Z':
        return chr(ord(char) + 32)

    else:
        return char


def lower_string(string):
    result = ''

    for i in range(0, len(string)):
        result = result + lower_char(string[i])

    return result

print(lower_string(input('String: ')))