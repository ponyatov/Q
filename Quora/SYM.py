## @file
## @brief Symbolic data type system

## @defgroup sym Symbolic data type system
## @ingroup quora
## - https://ponyatov.quora.com/On-computer-language-design-Symbolic-data-type-system
## ![](https://qph.fs.quoracdn.net/main-qimg-f435ceb356cf3741282d6d4c6c444d9b)
## @{

## base class
## ![](https://qph.fs.quoracdn.net/main-qimg-4954ac185d215be92c344efff57662c7)
class Qbject:
    ## construct object in form `<type:value>`
    def __init__(self,V):
        ## tag type with class name in lowercase
        self.type = self.__class__.__name__.lower()
        ## single value
        self.value = V
    ## print object
    def __repr__(self): return self.dump()
    ## dump object in tree form
    def dump(self): return '<%s:%s>' % (self.type, self.value)

## primitive objects represented in low-level code or computer hardware
## ![](https://qph.fs.quoracdn.net/main-qimg-ba5e715684d728708dd449b3acc65f5c)
class Primitive(Qbject): pass

## symbols names other objects like variables, classes, functions, constants,.
class Symbol(Primitive): pass

## in computing string can be universal data type,
## look on [REFAL](http://en.wikipedia.org/wiki/Refal) language
class String(Primitive):
    ## dump with escape characters
    def dump(self):
        S = '<%s:\'' % self.type
        for char in self.value:
            if   char == '\n': S += '\\n'
            elif char == '\r': S += '\\r'
            elif char == '\t': S += '\\t'
            else: S += char
        return S+'\'>'
    
## floating point number as mostly used in real applications
class Number(Primitive):
    ## we must override constructor to make `float(value)`
    def __init__(self,V):
        Primitive.__init__(self, V)
        ## forced floating point value
        self.value = float(V)

print Number(3.1415), Number(-1), Number('3e5')

## @}

