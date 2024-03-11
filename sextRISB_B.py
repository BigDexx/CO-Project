
def sextRISB(n):
   binary_string = bin(n & ((1 << 12) - 1))[2:].zfill(12)
   return binary_string


def sextB(n):
    binary_string = bin(n & ((1 << 13) - 1))[2:].zfill(13)
    return binary_string
