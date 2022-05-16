# Calculates the  of bits for text (# of character x 8)
def text_bits():

    print()
    # Ask user for a string...
    var_text = input("Enter some text: ")

    # Calculates the # of bits (length of sting x 8)
    var_length = len(   var_text)
    num_bits = 8 * var_length