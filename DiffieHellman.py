import math


class DiffieHellman:

    def __init__(self, private_key):
        self.private_key = private_key
        self.generator = 5
        self.modulus = 23

    def calculate_public_key(self):
        public_key = (self.generator ** self.private_key) % self.modulus
        return public_key

    def convert_public_to_private(self, public_key):
        private_key = (public_key ** self.private_key) % self.modulus
        return private_key

a = DiffieHellman(438)
a_public = a.calculate_public_key()
print('Alices public key: ' + str(a_public))

b = DiffieHellman(358)
b_public = b.calculate_public_key()
print('Bobs public key: ' + str(b_public))

b_private = a.convert_public_to_private(b_public)
print(b_private)

a_private = b.convert_public_to_private(a_public)
print(a_private)


