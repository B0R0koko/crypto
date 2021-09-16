from src.crypto.KeysGenerator import EllipticCurve
import hashlib


with open('pic.png', 'rb') as file:
    b = bytes(file.read())

h = hashlib.sha256(b)
private_key = h.hexdigest()
private_key = int(private_key, 16)
print(private_key)

a = EllipticCurve()
public_key = a.generate_key(private_key)
print(hex(public_key[0]))



