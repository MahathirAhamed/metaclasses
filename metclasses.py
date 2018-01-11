'''
Created on Jan 11, 2018

@author: mahathir.ahamed
'''
from _pyio import __metaclass__
class SuperMeta(type):
    
    def __call__(meta, classname, supers, classdict):
        print('In SuperMeta.call: ', classname, supers, classdict)
        return type.__call__(meta, classname, supers, classdict)
    
    def __init__(Class, classname, supers, classdict):
        print('In SuperMeta init:', classname, supers, classdict)
        print('...init class object:', list(Class.__dict__.keys()))
        
print('making metaclass') 
class SubMeta(type,):
    __metaclass__= SuperMeta
    def __new__(meta, classname, supers, classdict):
        print('In SubMeta.new: ', classname, supers, classdict)
        return type.__new__(meta, classname, supers, classdict)
    def __init__(Class, classname, supers, classdict):
        print('In SubMeta init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))
        
class Eggs:    pass
print('making class') 
class Spam(Eggs ):        # Invoke SubMeta, via SuperMeta.__call__    
     __metaclass__=SubMeta    
    data = 1   
    def meth(self, arg):
        return self.data + arg
print('making instance')

if __name__=="__main__":
    X = Spam() 
    print('data:', X.data, X.meth(2)) 

