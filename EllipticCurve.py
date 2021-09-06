import hashlib


class EllipticCurve():  #Using Elliptic curve over finite field to generate key pair

    def __init__(self, a_coef, b_coef, mod, gpoint):
        self.a_coef = a_coef
        self.b_coef = b_coef
        self.mod = mod
        self.gpoint = gpoint
    
    def modular_inverse(self, num, mod):  #Extended Euclidian Algorithm for modular inverse
        while(num < 0):  #Later found out built-in pow(a, -1, b) does the same
            num += mod
        x1, x2, x3 = 1, 0, mod
        y1, y2, y3 = 0, 1, num
        q = x3 // y3
        t1 = x1 - q*y1
        t2 = x2 - q*y2
        t3 = x3 - q*y3
        while(y3 != 1):
            x1, x2, x3 = y1, y2, y3
            y1, y2, y3 = t1, t2, t3
            q = x3 // y3
            t1 = x1 - q*y1
            t2 = x2 - q*y2
            t3 = x3 - q*y3
        while(y2 < 0):
            y2 = y2 + mod	
        return y2

    def ECAdd(self, x1, y1, x2, y2):
        if x1 == x2 and y1 == y2:  #Tangent case (Doubling)
            beta = (3*x1**2 + self.a_coef) * self.modular_inverse(2*y1, self.mod)
        else:  #Addition case 
            beta = (y2 - y1) * self.modular_inverse((x2 - x1), self.mod)
        x3 = beta**2 - x1 - x2
        y3 = beta*(x1 - x3) - y1
        x3 = x3 % self.mod
        y3 = y3 % self.mod
        return x3, y3

    def ECMultiply(self, private_key):
        x0, y0 = self.gpoint
        xt, yt = x0, y0
        binary_key = str(bin(private_key))[2:]
        for i in range (1, len(binary_key)):
            xt, yt = self.ECAdd(xt, yt, xt, yt)  #Doubling
            if binary_key[i] == "1":
                xt, yt = self.ECAdd(xt, yt, x0, y0)
        return xt, yt

# Recommended parameters for using Elliptic Curve Secp236k1
Pcurve = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 -1 
Acurve = 0
Bcurve = 7
Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798 
Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
Nparam = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

a = EllipticCurve(0, 7, Pcurve, (Gx, Gy))  #Initialise with essential variables

private_key = 0xa4f228d49910e8ecb53ba6f23f33fbfd2bad442e902ea20b8cf89c473237bf9f
ecx, ecy = a.ECMultiply(private_key)
public_key = hex(ecx)
print(public_key)
