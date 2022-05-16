# checks input is a number more than a given value
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

# Main routine goes here

Keep_going = ""
while Keep_going =="":
    print()
# Ask user for integer (must be more / equal to 0)
var_integer = num_check("Enter an integer: ", 0)
print()

# Ask for width & hieght of an image
# (must be more / equal to 1)
image_width = num_check("Image Width? ", 1)
print()
image_width = num_check("Image Height? ", 1)
print()