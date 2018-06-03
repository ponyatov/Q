import sys
sys.stdout = open('log.log','w')
 

class Qbject:
    def __init__(self, V):
        # tag type with class name in lowercase
        self.type = self.__class__.__name__.lower()
        # single value
        self.value = V
	def __repr__(self): return 'xxxxx' # self.dump()
	def dump(self): return '<%s:%s>' % (self.type, self.value)

print '%s'%Qbject('test')

