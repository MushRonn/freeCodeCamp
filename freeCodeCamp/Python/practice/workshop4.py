# Building a Caesar Cipher

shift = 5
alphabet = 'abcdefghijklmnopqrstuvwxyz'
shifted_alphabet = alphabet[shift:] + alphabet [:shift]

translation_table = str.maketrans(alphabet, shifted_alphabet)
print(translation_table)

text = 'hello world'
encrypted_text = text.translate(translation_table)
print(encrypted_text)