## @file
## @brief Symbolic data type system

## @defgroup sym Symbolic data type system
## @ingroup quora
## - https://ponyatov.quora.com/On-computer-language-design-Symbolic-data-type-system
## @{

## base class
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
    
class Primitive(Qbject): pass

print Primitive('object')

## @}
