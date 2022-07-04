"""
전승원: addition, maintainer
양정윤: subtract
조성현: multiplication
"""
class Complex:
    def __init__(self, re=0, im=0):
        # For a complex number 1 + 2i, re = 1 and im = 2
        self.re = re
        self.im = im

    def __str__(self):
        return str(self.re) + "+" + str(self.im) + "i"

c1 = Complex(1, 2)
print(c1)