# import hello
# print hello.hello.__doc__
# print hello.hello('test')#,1,2.3)

import LL
print LL
print LL.hello
print LL.Hello
print

print LL.Module, LL.Module.__dict__

module = LL.Module('Hello','arm-none-eabi') # can make directory with files 
print module

print
print LL.Type

print LL.Int
print LL.Int(8)

print LL.Float
print LL.Float(8),LL.Float(48)#,LL.Float(120),LL.Float(1024)

print
i8 = LL.Int(8) ; print 'i8',i8
i16 = LL.Int(0x10); print 'i16',i16
i32 = LL.Int(0x20); print 'i32',i32

print LL.Int(17)
print

print LL.Void
void = LL.Void() ; print 'void',void

print module
