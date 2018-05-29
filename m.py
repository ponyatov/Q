class O:
    def __init__(self,V): self.val = V
    def __repr__(self): return '<%s>'%self.val
    def __add__(self,o): return self.__class__(self.val + o.val)

A = O(123) ; print A
B = O(4.56) ; print B

print A+B

class S(O):
    def __init__(self,V): O.__init__(self, V) ; self.nest = []
    def __lshift__(self,o): self.nest.append(o) ; return self
    def __repr__(self):
        S = O.__repr__(self)
        for i in self.nest: S += '\n\t%s'%i
        return S

D = S('DATA')
print D

print D << A << B

print D