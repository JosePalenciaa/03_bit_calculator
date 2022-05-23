def num_check(question, low):
    valid = False
    while not valid:
        
        error = "Please enter a number that is more than "
        "(or equal to) {}".format(low)
        print()
        
        try:
        
            # ask user to enter a number
            response = int(input(question))
            
            # checks number is more than zero
            if response >= low:
                return response
            
            # outputs error if input is invalid
            else:
                print(error)
                print()
                
        except ValueError:
            print(error)   

# converts decimals to binary and states how many
# bits are needed to represent the original integer
def int_bits():

    # gets integer (must be >=0)
    var_integer = num_check("Please eneter an integer: ", 0)

    # source for code below is
    # https://stackoverflow.com/questions/8928240/convert-base-2-binary-number-string-to-int

    var_binary = "{0:b}".format(var_integer)

    # calculate # of bits (length of string above)
    num_bits = len(var_integer)

    # output answer with working
    print()
    print("{} in binary is {}".format(var_integer, var_binary))
    print("# of bits is {}".format(num_bits))
    print()

    return""

# main routine 
int_bits()