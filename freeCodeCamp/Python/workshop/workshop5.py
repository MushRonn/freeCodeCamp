# BUILD A PIN EXTRACTOR

def pin_extractor(poem):
    secret_code = ''
    lines = poem.split('\n')
    for line in lines:
        words = line.split()
        print(words)
    
poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

pin_extractor(poem)
    