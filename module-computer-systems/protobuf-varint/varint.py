import os
import struct

def encode(n: int) -> bytes:
    byte_sequence = []
    while n > 0:
        print(f"n is {n}")
        part = n % 128
        # TODO: add msb
        print(f"part is {part}")
        n >>= 7
        if n > 0:
            part |= 0x80
        byte_sequence.append(part)
    return bytes(byte_sequence)

def decode(value: bytes) -> int:
    pass

def test():
    assert encode(150) == b'\x96\x01'
    assert decode(b'\x96\x01') == 150

    for n in range(1 << 30):
        assert decode(encode(n)) == n


if __name__ == "__main__":
    # with open('150.uint64', 'rb') as f:
    #    print(struct.unpack('>Q', f.read())[0])
    print(encode(150))
