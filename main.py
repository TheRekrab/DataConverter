#!/bin/env python3
import sys

# FROM functions (To binary outputs):

def from_bin(msg:str):
    return msg

def from_str(msg:str):
    return " ".join([bin(ord(letter))[2:].zfill(8) for letter in list(msg)])

def from_dec(msg:str):
    nums = msg.split(" ")
    return " ".join([bin(int(num))[2:].zfill(8) for num in nums])

def from_hex(msg:str):
    # See if each code is seperated by a space, or no spaces
    if " " in msg.strip():
        codes = msg.strip().split(" ")
    else:
        codes = [msg[i:i+2] for i in range(0, len(msg), 2)]
    bins = []
    for code in codes:
        res = bin(int(code, 16))[2:].zfill(8)
        bins.append(res)
    return " ".join(bins)

def from_oct(msg:str):
    octs = msg.split(' ') if ' ' in msg else [msg[i:i+3] for i in range(len(msg), 3)]
    digits = []
    for octal in octs:
        digits.append(bin(int(octal, 8))[2:].zfill(8))
    return " ".join(digits)

# TO funtions (From binary inputs):

def to_bin(msg:str):
    return msg

def to_str(msg:str):
    return "".join([chr(int(binary, 2)) for binary in msg.split(" ")])

def to_dec(msg:str):
    bins = msg.split(" ")
    return " ".join([str(int(binary, 2)) for binary in bins])

def to_hex(msg:str):
    return " ".join([hex(int(binary, 2))[2:] for binary in msg.split(" ")])

def to_oct(msg:str):
    return " ".join([oct(int(binary, 2))[2:] for binary in msg.split(" ")])

# Here is the dictionary of functions to call:

froms = {
    "-b": from_bin,
    "-s": from_str,
    "-d": from_dec,
    "-h": from_hex,
    "-o": from_oct
}

tos = {
    "-b": to_bin,
    "-s": to_str,
    "-d": to_dec,
    "-h": to_hex,
    "-o": to_oct
}

names = {
    "-b": "Binary",
    "-s": "String/Plain Text",
    "-d": "Decimal",
    "-h": "Hexidecimal",
    "-o": "Octadecimal"
}

def parse_cmd():
    u_from = sys.argv[1].lower().strip()
    if u_from == "--help":
        print("This is a converter to convert different types of data.\nCommand Structure: convert [INPUT-TYPE] [OUTPUT-TYPE] [DATA]")
        print("Here are the data types you can use:")
        print("------------------------------------")
        print("-b   Binary")
        print("-s   String aka. Plain text")
        print("-d   Decimal")
        print("-h   Hexadecimal")
        print("-o   Octadecimal")
        print("------------------------------------")
        quit()
    elif u_from not in tos:
        print("Unknown data type %s" % u_from)
        quit()

    u_to = sys.argv[2].lower().strip()
    if u_to not in froms:
        print("Unknown data type %s" % u_to)
        quit()

    print("Converting %s to %s..." % (names[u_from], names[u_to]))

    # Perform conversions:
    msg = " ".join(sys.argv[3:])
    to_func = tos[u_to]
    from_func = froms[u_from]
    half_done = from_func(msg) # Should convert given to binary
    converted = to_func(half_done) # Should convert bionary to desired format
    print("Message converted!\nConverted Message: %s" % converted)

if __name__ == "__main__" and len(sys.argv) >= 2:
    parse_cmd()
elif __name__ == "__main__" and len(sys.argv) == 1:
    print("This is a converter to convert different types of data.\nCommand Structure: convert [INPUT-TYPE] [OUTPUT-TYPE] [DATA]")
    print("Here are the data types you can use:")
    print("------------------------------------")
    print("-b   Binary")
    print("-s   String aka. Plain text")
    print("-d   Decimal")
    print("-h   Hexadecimal")
    print("-o   Octadecimal")
    print("------------------------------------")
    quit()
