Pcurve = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 -1 
Acurve = 0
Bcurve = 7
Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798 
Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
GPoint = (int(Gx),int(Gy))
Nparam = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

class Point():

    def __init__(self, x, y):  
        self.x = x
        self.y = y


class EllipticCurve():

    def __init__(self, a_coef, b_coef, mod, gpoint):
        self.a_coef = a_coef
        self.b_coef = b_coef
        self.mod = mod
        self.gpoint = gpoint
    
    def modInverse(self, num, mod) : 
        num %= mod; 
        for i in range(1, mod) : 
            if (num * i) % mod == 1:
                return i
        return 1
  

    def ECAdd(self, first, second):
        lam = (second.y - first.y) * self.modInverse(second.x - first.x, self.mod)
        x_r = (lam**2 - first.x - second.x) % self.mod
        y_r = (lam * (first.x - x_r) - first.y) % self.mod
        return Point(x_r, y_r)

    def ECDouble(self, first):
        lam = (3 * first.x**2 + self.a_coef) * self.modInverse(2 * first.y, self.mod)
        x_r = (lam**2 - 2 * first.x) % self.mod
        y_r = (lam * (first.x - x_r) - first.y) % self.mod
        return Point(x_r, y_r)

    def ECMultiply(self, private_key):
        binary_key = str(bin(private_key))[2:]
        point = self.gpoint
        for i in range (1, len(binary_key)):
            point = self.ECDouble(point); 
            if binary_key[i] == "1":
                point = self.ECAdd(point, self.gpoint)
        return point



a = EllipticCurve(0, 7, Pcurve, Point(Gx, Gy))

private_key = 583

public_key = a.ECMultiply(private_key)
print(public_key.x, public_key.y)