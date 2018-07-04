#!/usr/bin/env python
'''Fixed XOR'''

def xor_strings(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))

def main():
    binary_a = bytearray('1c0111001f010100061a024b53535009181c'.decode('hex'))
    binary_b = bytearray('686974207468652062756c6c277320657965'.decode('hex'))
    #print binary_a
    print binary_b
    xored = xor_strings(binary_a, binary_b).encode("hex")
    assert(xored == '746865206b696420646f6e277420706c6179')


if __name__ == "__main__":
    main()
