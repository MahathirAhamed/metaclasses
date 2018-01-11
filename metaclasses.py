'''
Created on Dec 29, 2017

@author: mahathir.ahamed
'''
#from _pyio import __metaclass__
import re
from _pyio import __metaclass__
#from __future__ import print_function
'''class MetaClass(type):
    def __init__(cls,name,bases,attrs):
         print('Defining %s' % cls)
         print('Name: %s' % name)
         print('Bases: %s' % (bases,))
         print('Attributes:')
         for (name, value) in attrs.items(): 
             print('    %s: %r' % (name, value))
    def __call__(cls,*args,**kwargs):
        print "I am getting Instantiated"
        return type.__call__(cls, *args, **kwargs)

class SubClass(object):
    __metaclass__ = MetaClass
    spam = 'eggs'


class _TemplateMetaclass(type):
    pattern = r"""
    %(delim)s(?:
      (?P<escaped>%(delim)s) |   # Escape sequence of two delimiters
      (?P<named>%(id)s)      |   # delimiter and a Python identifier
      {(?P<braced>%(id)s)}   |   # delimiter and a braced identifier
      (?P<invalid>)              # Other ill-formed delimiter exprs
    )
    """

    def __init__(cls, name, bases, dct):
        super(_TemplateMetaclass, cls).__init__(name, bases, dct)
        if 'pattern' in dct:
            pattern = cls.pattern
        else:
            pattern = _TemplateMetaclass.pattern % {
                'delim' : re.escape(cls.delimiter),
                'id'    : cls.idpattern,
                }
        cls.pattern = re.compile(pattern, re.IGNORECASE | re.VERBOSE)

class Template:
    """A string class for supporting $-substitutions."""
    __metaclass__ = _TemplateMetaclass
    
    delimiter = '$'
    idpattern = r'[_a-z][_a-z0-9]*'

    def __init__(self, template):
        self.template = template


class MyParent(object):
    def __init__(self):
        print "Initializing"
        self.x=0
class MyChild(MyParent):
    def __init__(self):
        super(MyChild,self).__init__()
        self.data = [1,2,3,4,5,6,7,8]
        print "Initialized"
    def __getitem__(self,x):
        return self.data[x]

class Squares(object):
    def __init__(self,start,stop):
        import pdb;pdb.set_trace()
        self.value = start -1
        self.stop = stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2

def gsquares(start, stop):   
    for i in range(start, stop + 1):
        import pdb;pdb.set_trace()
        yield i ** 2

class SubclassTracker(type): 
    def __init__(cls, name, bases, attrs): 
        try:
            print "Creating",cls,name,bases,attrs
            if TrackedClass not in bases:
                return 
        except NameError:
            return 
        TrackedClass._registry.append(cls)


class TrackedClass(object):
      __metaclass__= SubclassTracker
      _registry = []

def extra(self,arg):
    return arg
class ClassOne: 
    pass

class MetaTwo(type):    
    def __new__(meta, classname, supers, classdict):        
        print('In MetaTwo.new: ', meta,classname, supers, classdict)        
        return type.__new__(meta, classname, supers, classdict)
    def __init__(Class, classname, supers, classdict):        
        print('In MetaTwo.init:', Class,classname, supers, classdict)        
        print('...init class object:', list(Class.__dict__.keys()))
        

class SuperMeta(type):
    def __call__(meta, classname, supers, classdict):
        print('In SuperMeta.call: ', classname, supers, classdict)
        return type.__call__(meta, classname, supers, classdict)
    def __init__(Class, classname, supers, classdict):
        print('In SuperMeta init:', classname, supers, classdict)
        print('...init class object:', list(Class.__dict__.keys()))

class SubMeta(type, ):
    __metaclass__= SuperMeta
    def __new__(meta, classname, supers, classdict):
        print('In SubMeta.new: ', classname, supers, classdict)
        return type.__new__(meta, classname, supers, classdict)
    def __init__(Class, classname, supers, classdict):
        print('In SubMeta init:', classname, supers, classdict)
        print('...init class object:', list(Class.__dict__.keys()))

class Eggs(object):
    # One of the "object" optional
    pass
print('making metaclass') 
class Spam(Eggs, object):   
     __metaclass__ = SubMeta
    class SuperMeta(type):
    def __call__(meta, classname, supers, classdict):
        # By name, not built-in
        print('In SuperMeta.call:', classname)
        return type.__call__(meta, classname, supers, classdict)
class SubMeta(SuperMeta):
    # Created by type default
    def __init__(Class, classname, supers, classdict):
        # Overrides type.__init__
        print('In SubMeta init:', classname)
        
class small():
      def __init__(cls,val):
          cls.val= 10
          print cls.val '''

class MetOne(type):
    def __init__(Class, classname, supers, classdict):
        print('In SuperMeta init:', classname, supers, classdict)
        print('...init class object:', list(Class.__dict__.keys()))
    def toast(self):
        return "toast"

class NormalClass(object):
    __metaclass__ = MetOne
    
    def spam(self):
        return "spam"

class D: 
    def __get__(self, instance, owner): print('__get__')
    #def __set__(self, instance, value): print('__set__')

class C: 
     d = D() 
 
 


    

if __name__ == "__main__":
    #import pdb;pdb.set_trace()
    #val=Template("$String")
    #val = MyChild()[1:5]
    #for i in Squares(1,5):
    #    print (i)
    #for i in val:
    #    print i 
    #for i in gsquares(1,5):
    #    print (i)
    #:wq
    #val = SubClass()
    #x=ClassOne()
    #ClassOne.extra= extra
    #s = NormalClass()
    I = C() 
    
    I.d
    #I.__dict__['d']='spam'
    I.__dict__['d'] = 'spam'
    print I.__class__
    val = [x.__name__ for x in C.__mro__]
    print val 
    #print s.spam()
    #print s.toast()
    #print NormalClass.toast()
    """print(SubMeta.__class__)
    print([n.__name__ for n in SubMeta.__mro__])
    print() 
    print(SubMeta.__call__)                   # Not a data descriptor if found by name 
    print() 
    SubMeta.__call__(SubMeta, 'xxx', (), {})  # Explicit calls work: class inheritance 
    print() 
    SubMeta('yyy', (), {})                    # But implicit built-in calls do not: type
    c = small(10)"""
