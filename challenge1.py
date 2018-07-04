#!/usr/bin/env python
'''Convert hex to base64'''

import base64

def main():
    b16 = bytearray('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'.decode('hex'))
    print bytearray('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'.decode('dec'))
    b64 = base64.b64encode(b16)

    print b64
    assert(b64 == 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')

if __name__ == "__main__":
    main()
