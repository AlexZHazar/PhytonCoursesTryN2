import math
class MyFractal:
    def __init__ (self, num, denum):
        self.num = num
        self.denum = denum
    def __str__(self):
        return f"{self.num}/{self.denum}"
    def simplify (self):
        common_denum = math.gcd(self.num, self.denum)
        self.num //= common_denum
        self.denum //= common_denum
    def __add__ (self, other):
        if isinstance(other, MyFractal):
            common_def = self.denum * other.denum
            second_num = other.num * self.denum
            first_num = self.num * other.denum
            result=MyFractal(first_num + second_num,common_def)
            result.simplify()
            return result
        elif isinstance(other, int):
            second = MyFractal(other,1)
            common_def = self.denum * second.denum
            second_num = second.num * self.denum
            first_num = self.num * second.denum
            result=MyFractal(first_num + second_num,common_def)
            result.simplify()
            return result
    def __sub__ (self, other):
        if isinstance(other, MyFractal):
            common_def = self.denum * other.denum
            second_num = other.num * self.denum
            first_num = self.num * other.denum
            result=MyFractal(first_num - second_num,common_def)
            result.simplify()
            return result
        elif isinstance(other, int):
            second = MyFractal(other,1)
            common_def = self.denum * second.denum
            second_num = second.num * self.denum
            first_num = self.num * second.denum
            result=MyFractal(first_num - second_num,common_def)
            result.simplify()
            return result
    def __mul__ (self, other):
        if isinstance(other, MyFractal):
            result=MyFractal(self.num * other.num, self.denum * other.denum)
            result.simplify()
            return result
        elif isinstance(other, int):
            result=MyFractal(self.num * other, self.denum )
            result.simplify()
            return result
    def __truediv__ (self, other):
        if isinstance(other, MyFractal):
            result=MyFractal(self.num * other.denum, self.denum * other.num)
            result.simplify()
            return result
        elif isinstance(other, int):
            result=MyFractal(self.num, self.denum * other)
            result.simplify()
            return result

    