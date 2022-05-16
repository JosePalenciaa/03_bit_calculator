# Calculates the  of bits for text (# of character x 8)
def text_bits():

    print()
    # Ask user for a string...
    var_text = input("Enter some text: ")

    # Calculates the # of bits (length of sting x 8)
    var_length = len(   var_text)
    num_bits = 8 * var_length

    # Outputs answer with workingtt
    print()
    print("\'{}\' has {} characters ...". format(var_text, var_length))
    print("# of bits is {} x 8...".format(var_length))
    print("We need {} bits to represent {}".format(num_bits, var_text))
    print()

    return ""


# Main routine goes here
text_bits()