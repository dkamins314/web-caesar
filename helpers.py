#rotates a single character by rot positions
def rotate_character(char,rot):
    rot=int(rot)                                     # ensure that the rotation is an integer
    if char.isalpha()== False:                       # if the character is not a letter, ...
        c = char                                     # don't manipulate it
    else:                                            # if it is a letter
        if char.isupper():                           # if the character to rotate is upper case
            ec = (alphabet_position(char)+rot)%26+65 # the Encrypted Char is the  value of symbol+rotation limited to 0-25
            c = chr(ec)                              # ensure that we are going to return a character
        else:                                        # if it is not an upper and it is not a non-character, it must be a lower case character
            ec = (alphabet_position(char)+rot)%26+97 # the encrypted i- is the  value of i+rotation
            c = chr(ec)                              # ensure that the item we are returning is a character
    return c                                         # return the character


# return the position of the given letter in the alphabet from 0 to 25
def alphabet_position(letter):
    letter = letter.lower()                 # force the letter to lower case
    number = ord(letter) - 97               # get the ASCII code and subtract the letter 'a' which will bring the value to between 0 and 25
    return number                           # return the number to the calling function
