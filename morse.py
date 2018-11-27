# morse.py
# pylint: disable=missing-docstring

class Morse:
    morse_dict = {
        '.-':   'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..':  'D',
        '.':    'E',
        '..-.': 'F',
        '--.':  'G',
        '....': 'H',
        '..':   'I',
        '.---': 'J',
        '-.-':  'K',
        '.-..': 'L',
        '--':   'M',
        '-.':   'N',
        '---':  'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.':  'R',
        '...':  'S',
        '-':    'T',
        '..-':  'U',
        '...-': 'V',
        '.--':  'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z',
        '/':    ' '
    }

    def decode(self, message):
        decoded_message = ''
        if message == '':
            return ''
        message_tab = message.split(' ')
        for message_elem in message_tab:
            decoded_message = decoded_message+self.decode_letter(message_elem)

        return decoded_message

    def decode_letter(self, message_elem):
        return self.morse_dict[message_elem]
