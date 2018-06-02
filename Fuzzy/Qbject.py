# -*- coding: utf8 -*-
## @file
## @brief Q system core elements used in Fuzzy
## <br>копия элементов ядра Qsystem использованных в Fuzzy

## @defgroup qfuzzy Qbject class tree
## @ingroup fuzzy
## @brief Q system core elements used in Fuzzy
## <br>копия элементов ядра Qsystem использованных в Fuzzy
## @{

## generic Object class (the name was chosen not to interfere with Python3)
class Qbject:
    ## construct with given value
    def __init__(self, V, token=None):
        ## <type:value> must be compatible with PLY library token objects
        self.type = self.__class__.__name__.lower()
        ## single value
        self.value = V
        ## `nest[]`ed elements /ordered/
        self.nest = []
        ## `attr{}`ibutes /associative array, unordered/
        self.attr = {}
        # process lexeme data
        if token:
            ## lexeme char position in source code
            self.lexpos = token.lexpos
            ## lexeme line number in source code
            self.lineno = token.lineno
            ## lexeme length
            try: self.toklen = token.toklen
            except AttributeError: self.toklen = len(token.value)
    ## by default all objects `execute`s in itself
    def __call__(self): D << self ; return self
    ## `object[key]` operator
    def __getitem__(self,key): return self.attr[key]
    ## `object[key]=val` operator
    def __setitem__(self,key,o): self.attr[key] = o ; return self
    ## text dump (tree form)
    def __repr__(self): return self.dump()
    ## dump any object in tree form
    def dump(self, depth=0,prefix=''):
        S = self.pad(depth) + self.head(prefix=prefix)
        for i in self.attr:
            try:
                S += self.attr[i].dump(depth+1,prefix='%s = '%i)
            except AttributeError:
                S += self.pad(depth+1) + '%s = %s'%(i,self.attr[i])
        for j in self.nest: S += j.dump(depth+1)
        return S
    ## pad tree element
    def pad(self,N): return '\n' + '\t' * N
    ## dump object in short form (header only)
    def head(self,prefix=''):
        return '%s<%s:%s>' % (prefix,self.type, self.value)

## @}
