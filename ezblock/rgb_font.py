class Alphabet(object):
    _normal = {
        'A': [
            '0110',
            '1001',
            '1001',
            '1111',
            '1001',
            '1001',
            '0000',],
        'B': [
            '1110',
            '1001',
            '1110',
            '1001',
            '1001',
            '1110',
            '0000',],
        'C': [
            '0110',
            '1001',
            '1000',
            '1000',
            '1001',
            '0110',
            '0000',],
        'D': [
            '1110',
            '1001',
            '1001',
            '1001',
            '1001',
            '1110',
            '0000',],
        'E': [
            '1111',
            '1000',
            '1110',
            '1000',
            '1000',
            '1111',
            '0000',],
        'F': [
            '1111',
            '1000',
            '1110',
            '1000',
            '1000',
            '1000',
            '0000',],
        'G': [
            '0110',
            '1001',
            '1000',
            '1011',
            '1001',
            '0110',
            '0000',],
        'H': [
            '1001',
            '1001',
            '1111',
            '1001',
            '1001',
            '1001',
            '0000',],
        'I': [
            '111',
            '010',
            '010',
            '010',
            '010',
            '111',
            '000',],
        'J': [
            '0001',
            '0001',
            '0001',
            '1001',
            '1001',
            '0110',
            '0000',],
        'K': [
            '1001',
            '1010',
            '1010',
            '1100',
            '1010',
            '1001',
            '0000',],
        'L': [
            '1000',
            '1000',
            '1000',
            '1000',
            '1000',
            '1111',
            '0000',],
        'M': [
            '10001',
            '11011',
            '10101',
            '10001',
            '10001',
            '10001',
            '00000',],
        'N': [
            '1001',
            '1001',
            '1101',
            '1011',
            '1001',
            '1001',
            '0000',],
        'O': [
            '0110',
            '1001',
            '1001',
            '1001',
            '1001',
            '0110',
            '0000',],
        'P': [
            '1110',
            '1001',
            '1001',
            '1110',
            '1000',
            '1000',
            '0000',],
        'Q': [
            '01110',
            '10001',
            '10001',
            '10001',
            '10101',
            '01110',
            '00001',],
        'R': [
            '1110',
            '1001',
            '1001',
            '1110',
            '1010',
            '1001',
            '0000',],
        'S': [
            '0110',
            '1001',
            '0100',
            '0010',
            '1001',
            '0110',
            '0000',],
        'T': [
            '11111',
            '00100',
            '00100',
            '00100',
            '00100',
            '00100',
            '00000',],
        'U': [
            '1001',
            '1001',
            '1001',
            '1001',
            '1001',
            '0110',
            '0000',],
        'V': [
            '1001',
            '1001',
            '1001',
            '1001',
            '1010',
            '0100',
            '0000',],
        'W': [
            '10001',
            '10001',
            '10001',
            '10101',
            '10101',
            '01010',
            '00000',],
        'X': [
            '1001',
            '1001',
            '0110',
            '1001',
            '1001',
            '1001',
            '0000',],
        'Y': [
            '10001',
            '10001',
            '01010',
            '00100',
            '00100',
            '00100',
            '00000',],
        'Z': [
            '1111',
            '0001',
            '0010',
            '0100',
            '1000',
            '1111',
            '0000',],
        'a': [
            '0111',
            '1001',
            '1001',
            '0111',
            '0000',],
        'b': [
            '1000',
            '1110',
            '1001',
            '1001',
            '1110',
            '0000',],
        'c': [
            '011',
            '100',
            '100',
            '011',
            '000',],
        'd': [
            '0001',
            '0111',
            '1001',
            '1001',
            '0111',
            '0000',],
        'e': [
            '0110',
            '1011',
            '1100',
            '0110',
            '0000',],
        'f': [
            '001',
            '010',
            '111',
            '010',
            '010',
            '000',],
        'g': [
            '0111',
            '1001',
            '1001',
            '0111',
            '0001',
            '0110',],
        'h': [
            '1000',
            '1110',
            '1001',
            '1001',
            '1001',
            '0000',],
        'i': [
            '1',
            '0',
            '1',
            '1',
            '1',
            '0',],
        'j': [
            '01',
            '00',
            '01',
            '01',
            '01',
            '10',
            '00',],
        'k': [
            '1000',
            '1001',
            '1010',
            '1110',
            '1001',
            '0000',],
        'l': [
            '1',
            '1',
            '1',
            '1',
            '1',
            '0',],
        'm': [
            '11110',
            '10101',
            '10101',
            '10101',
            '00000',],
        'n': [
            '1110',
            '1001',
            '1001',
            '1001',
            '0000',],
        'o': [
            '0110',
            '1001',
            '1001',
            '0110',
            '0000',],
        'p': [
            '0110',
            '1001',
            '1001',
            '1110',
            '1000',],
        'q': [
            '0110',
            '1001',
            '1001',
            '0111',
            '0001',],
        'r': [
            '101',
            '110',
            '100',
            '100',
            '000',],
        's': [
            '0111',
            '1100',
            '0011',
            '1110',
            '0000',],
        't': [
            '010',
            '111',
            '010',
            '010',
            '001',
            '000',],
        'u': [
            '1001',
            '1001',
            '1001',
            '0111',
            '0000',],
        'v': [
            '1001',
            '1001',
            '1010',
            '0100',
            '0000',],
        'w': [
            '10101',
            '10101',
            '01010',
            '01010',
            '00000',],
        'x': [
            '101',
            '010',
            '010',
            '101',
            '000',],
        'y': [
            '1001',
            '1001',
            '0111',
            '0001',
            '0110',
            '0000',],
        'z': [
            '1111',
            '0010',
            '0100',
            '1111',
            '0000',],
        'ERROR_CHAR': [
            '1111',
            '1001',
            '1001',
            '1001',
            '1001',
            '1111',
            '0000',],
        ' ': [
            '00',
            '00',
            '00',
            '00',
            '00',],
        '!': [
            '1',
            '1',
            '1',
            '1',
            '0',
            '1',
            '0',],
        '?': [
            '110',
            '001',
            '010',
            '010',
            '000',
            '010',
            '000',],
        ',': [
            '01',
            '10',],
        '.': [
            '1',
            '0',],
        ':': [
            '1',
            '0',
            '0',
            '1',
            '0',
            '0',],
        ';': [
            '01',
            '00',
            '00',
            '01',
            '10',
            '00',],
        "'": [
            '1',
            '1',
            '0',
            '0',
            '0',
            '0',
            '0',],
        '"': [
            '101',
            '101',
            '000',
            '000',
            '000',
            '000',
            '000',],
        '(': [
            '01',
            '10',
            '10',
            '10',
            '10',
            '01',
            '00',],
        ')': [
            '10',
            '01',
            '01',
            '01',
            '01',
            '10',
            '00',],
        '`': [
            '10',
            '01',
            '00',
            '00',
            '00',
            '00',
            '00',],
    }
    all_on = [
        0xFF,0xFF,0xFF,
        0xFF,0xFF,0xFF,
        0xFF,0xFF,0xFF,
        0xFF,0xFF,0xFF,
        0xFF,0xFF,0xFF,
        0xFF,0xFF,0xFF,
        0xFF,0xFF,0xFF,
        0xFF,0xFF,0xFF]


    def __init__(self):
        pass

    def normal(self, s):
        if s not in self._normal:
            s = 'ERROR_CHAR'
        return self._normal[s]

class Icons(object):
    """docstring for emotions"""
    _icons = {
        "heart" : [
            '0,0,0,0,0,0,0,0',
            '0,1,1,0,1,1,0,0',
            '1,1,1,1,1,1,1,0',
            '1,1,1,1,1,1,1,0',
            '1,1,1,1,1,1,1,0',
            '0,1,1,1,1,1,0,0',
            '0,0,1,1,1,0,0,0',
            '0,0,0,1,0,0,0,0',],
        "small heart" : [
            '0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0',
            '0,0,1,0,1,0,0,0',
            '0,1,1,1,1,1,0,0',
            '0,1,1,1,1,1,0,0',
            '0,0,1,1,1,0,0,0',
            '0,0,0,1,0,0,0,0',
            '0,0,0,0,0,0,0,0',],
        "yes" : [
            '0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,1',
            '0,0,0,0,0,0,1,0',
            '0,0,0,0,0,1,0,0',
            '1,0,0,0,1,0,0,0',
            '0,1,0,1,0,0,0,0',
            '0,0,1,0,0,0,0,0',],
        "no" : [
            '1,0,0,0,0,0,0,1',
            '0,1,0,0,0,0,1,0',
            '0,0,1,0,0,1,0,0',
            '0,0,0,1,1,0,0,0',
            '0,0,0,1,1,0,0,0',
            '0,0,1,0,0,1,0,0',
            '0,1,0,0,0,0,1,0',
            '1,0,0,0,0,0,0,1',],
        "happy" : [
            '0,0,0,0,0,0,0,0',
            '0,1,1,0,0,1,1,0',
            '0,1,1,0,0,1,1,0',
            '0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0',
            '1,0,0,0,0,0,0,1',
            '0,1,0,0,0,0,1,0',
            '0,0,1,1,1,1,0,0',],
        "sad" : [
            '0,0,0,0,0,0,0,0',
            '0,1,1,0,0,1,1,0',
            '0,1,1,0,0,1,1,0',
            '0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0',
            '0,0,1,1,1,1,0,0',
            '0,1,0,0,0,0,1,0',
            '1,0,0,0,0,0,0,1',],
        "confused" : [
            '0,0,0,0,0,0,0,0',
            '0,1,1,0,0,1,1,0',
            '0,1,1,0,0,1,1,0',
            '0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0',
            '0,0,1,0,0,0,1,0',
            '0,1,0,1,0,1,0,1',
            '1,0,0,0,1,0,0,0',],
        "angry" : [
            '0,0,0,0,0,0,0,0',
            '1,1,0,0,0,0,1,1',
            '0,1,1,0,0,1,1,0',
            '0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0',
            '1,1,1,1,1,1,1,1',
            '1,0,0,1,1,0,0,1',
            '1,0,0,1,1,0,0,1',],
        "asleep" : [
            '0,0,0,0,0,0,0,0',
            '1,1,1,0,0,1,1,1',
            '1,1,1,0,0,1,1,1',
            '0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0',
            '0,0,1,1,1,1,0,0',
            '0,0,1,1,1,1,0,0',
            '0,0,0,0,0,0,0,0',],
        "surprised" : [
            '0,0,0,0,0,0,0,0',
            '0,1,1,0,0,1,1,0',
            '0,1,1,0,0,1,1,0',
            '0,0,0,0,0,0,0,0',
            '0,0,0,1,1,0,0,0',
            '0,0,1,0,0,1,0,0',
            '0,0,1,0,0,1,0,0',
            '0,0,0,1,1,0,0,0',],
        "silly" : [
            '0,0,0,0,0,0,0,0',
            '0,1,1,0,0,1,1,0',
            '0,1,1,0,0,1,1,0',
            '0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0',
            '1,1,1,1,1,1,1,1',
            '0,0,0,0,0,0,1,1',
            '0,0,0,0,0,0,1,1',],
        "meh" : [
            '1,1,1,0,0,1,1,1',
            '1,1,1,0,0,1,1,1',
            '0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0',
            '0,0,0,0,1,1,0,0',
            '0,0,0,1,1,0,0,0',
            '0,0,1,1,0,0,0,0',
            '0,1,1,0,0,0,0,0',],
        "t-shirt" : [
            '1,1,1,0,0,1,1,1',
            '1,1,1,1,1,1,1,1',
            '0,1,1,1,1,1,1,0',
            '0,1,1,1,1,1,1,0',
            '0,1,1,1,1,1,1,0',
            '0,1,1,1,1,1,1,0',
            '0,1,1,1,1,1,1,0',
            '0,1,1,1,1,1,1,0',],
        "rollerskate" : [
            '0,0,0,0,0,1,1,1',
            '0,0,0,0,0,1,1,1',
            '0,0,0,0,0,1,1,1',
            '0,0,0,0,0,1,1,1',
            '1,1,1,1,1,1,1,1',
            '1,1,1,1,1,1,1,1',
            '1,1,1,1,1,1,1,1',
            '0,1,1,0,0,1,1,0',],
        "duck" : [
            '0,0,0,0,0,0,0,0',
            '0,1,1,0,0,0,0,0',
            '1,1,1,0,0,0,0,0',
            '0,1,1,1,1,1,1,1',
            '0,1,1,1,1,1,1,1',
            '0,1,1,1,1,1,1,0',
            '0,0,1,1,1,1,0,0',
            '0,0,0,0,0,0,0,0',],
        "house" : [
            '0,0,0,1,1,0,0,0',
            '0,0,1,1,1,1,0,0',
            '0,1,1,1,1,1,1,0',
            '1,1,1,1,1,1,1,1',
            '0,1,1,1,1,1,1,0',
            '0,1,1,1,1,1,1,0',
            '0,1,1,0,0,1,1,0',
            '0,1,1,0,0,1,1,0',],
        "butterfly" : [
            '1,1,1,0,0,1,1,1',
            '1,1,1,0,0,1,1,1',
            '1,1,1,1,1,1,1,1',
            '0,0,0,1,1,0,0,0',
            '0,0,0,1,1,0,0,0',
            '1,1,1,1,1,1,1,1',
            '1,1,1,0,0,1,1,1',
            '1,1,1,0,0,1,1,1',],
        "umbrella" : [
            '0,0,0,1,1,0,0,0',
            '0,0,1,1,1,1,0,0',
            '0,1,1,1,1,1,1,0',
            '1,1,1,1,1,1,1,1',
            '0,0,0,1,1,0,0,0',
            '1,1,0,1,1,0,0,0',
            '1,1,1,1,1,0,0,0',
            '1,1,1,1,1,0,0,0',],
        "skull" : [
            '0,0,0,0,0,0,0,0',
            '0,0,1,1,1,1,0,0',
            '0,1,0,1,1,0,1,0',
            '0,1,1,1,1,1,1,0',
            '0,0,1,1,1,1,0,0',
            '0,0,1,1,1,1,0,0',
            '0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0',],
        
        
    }
    def __init__(self):
        pass

    def __call__(self, name):
        try:
            return self._icons[name]
        except:
            return "This emotion not found"
