import hashlib


class EllipticCurve():  #Using Elliptic curve over finite field to generate key pair

    # Recommended parameters for using Elliptic Curve Secp236k1

    Prime = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1 
    ACoef = 0
    BCoef = 7
    Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798 
    Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
    GPoint = (Gx, Gy)
    Nparam = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

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
            y2 += mod	
        return y2

    def ECAdd(self, x1, y1, x2, y2):
        if x1 == x2 and y1 == y2:  #Tangent case (Doubling)
            beta = (3*x1**2 + self.ACoef) * self.modular_inverse(2*y1, self.Prime)
        else:  #Addition case 
            beta = (y2 - y1) * self.modular_inverse((x2 - x1), self.Prime)
        x3 = beta**2 - x1 - x2
        y3 = beta*(x1 - x3) - y1
        x3 %= self.Prime
        y3 %= self.Prime
        return x3, y3

    def generate_key(self, private_key):  #ECMultiply
        x0, y0 = self.GPoint
        xt, yt = x0, y0
        binary_key = str(bin(private_key))[2:]
        for i in range (1, len(binary_key)):
            xt, yt = self.ECAdd(xt, yt, xt, yt)  #Doubling
            if binary_key[i] == "1":
                xt, yt = self.ECAdd(xt, yt, x0, y0)
        return xt, yt


if __name__ == "__main__":
    a = EllipticCurve()
    private_key = 0x5c77b75031dc98e7dce5d6cddc0d23e2c357fe4888b9ea54fc05be3a95794d2a
    ecx, ecy = a.generate_key(private_key)
    public_key = hex(ecx)
    print(public_key)
