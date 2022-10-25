import math

class Rational:
    def __init__(self, numerator=1.00, denominator=1.00):
        self.k = math.gcd(numerator, denominator)
        self.numerator = numerator//self.k
        self.denominator = denominator//self.k
    def fractional_view(self):
        return f"{str(self.numerator)}/{str(self.denominator)}"
    def rational_view(self):
        value = self.numerator / self.denominator
        return value

"""
x = Rational(2, 4)
print(x.fractional_view())
print(x.rational_view())
"""

print("enter the numerator of a fractional number:")
nmr = int(input())
print("enter the denominator of the fractional number:")
dnr = int(input())
rn = Rational(nmr, dnr)
print("enter 1 to display the number in fractional form and 2 to display in rational form:")
if(int(input()) == 1):
    print(rn.fractional_view())
else:
    print(rn.rational_view())