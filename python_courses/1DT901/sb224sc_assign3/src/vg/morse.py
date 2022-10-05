morse_dict = {
    'a': '.-', 'k': '-.-', 'u': '..-',
    'b': '-...',  'l': '.-..',  'v': '...-',
    'c': '-.-.',  'm': '--',    'w': '.--',
    'd': '-..',   'n': '-.',    'x': '-..-',
    'e': '.',     'o': '---', 'y': '-.--',
    'f': '..-.',  'p': '.--.',  'z': '--..',
    'g': '--.',   'q': '--.-', 'å': '.--.-',
    'h': '....',  'r': '.-.',   'ä': '.-.-',
    'i': '..',    's': '...',   'ö': '---.',
    'j': '.---', 't': '-'
}


msg = input('Write a message: ').lower()
print('Message in Morse code:')
for letter in msg:
    if letter == ' ':
        print(' ', end=' ')
    else:
        print(morse_dict[letter], end=' ')
print('')

morse_dict = dict([(value, key) for key, value in morse_dict.items()])

msg = input('Write in Morse code: ')
print('Message in plain language:')
for i in msg.split(' '):
    if i == '':
        print('', end='')
    else:
        print(morse_dict[i], end=' ')
print('')
