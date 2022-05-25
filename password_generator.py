import string
import random


def generate_password(size):
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    password = []
    for char in range(size):
        random.shuffle(characters)
        password += random.choice(characters)
        random.shuffle(password)
    print("".join(password))


def text2morse(text):
    translation_dictionary = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', " ":"/"}
    translated = []
    for character in text.upper():
        translated.append(translation_dictionary.get(character.upper()))
    return " ".join(translated)

generate_password(18)