mp_bin = {'0': "0000", '1': "0001", '2': "0010", '3': "0011", '4': "0100", '5': "0101", '6': "0110", '7': "0111", '8': "1000", '9': "1001", 'A': "1010", 'B': "1011", 'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"}
mp_hex = {"0000": '0', "0001": '1', "0010": '2', "0011": '3', "0100": '4', "0101": '5', "0110": '6', "0111": '7', "1000": '8', "1001": '9', "1010": 'A', "1011": 'B', "1100": 'C', "1101": 'D', "1110": 'E', "1111": 'F'}

def hex2bin(s):
    bin  =""
    for char in s:
        bin = bin + mp_bin[char]
    return bin

def bin2hex(s):
    hex_string = ""
    for i in range(0, len(s), 4):
        bin_chunk = s[i:i+4]    
        hex_string += mp_hex[bin_chunk]
    
    return hex_string

def bin2dec(binary):
    return int(binary)

def dec2bin(num):
    return bin(num)

def permute(k, arr, n):
    permutation = ""
    for i in range(0, n):
        permutation = permutation + k[arr[i] - 1]
    return permutation

def shift_left(k, n):
    s = ""
    for i in range(n):
        for j in range(1, len(k)):

            s = s + k[j]
        s = s + k[0]
        k = s
        s = ""
    
    return k

def xor(a, b):
    return a ^ b

