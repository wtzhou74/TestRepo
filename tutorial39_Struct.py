from struct import *

# store as bytes data
packed_data = pack('iif', 5, 29, 4.9)
print(packed_data)

print(calcsize("i"))
print(calcsize("ii"))
print(calcsize("iif"))

# convert the bytes data back to normal
original_data = unpack("iif", packed_data)
print(original_data)

print(unpack("iif", b'\x05\x00\x00\x00\x1d\x00\x00\x00\xcd\xcc\x9c@'))