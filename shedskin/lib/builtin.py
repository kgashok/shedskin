class class_:
    def __repr__(self):
        return self.__name__

class int_:
    def __add__(self, b):
        return b
    def __and__(self, b):
        return 1
    def __or__(self, b):
        return 1
    def __xor__(self, b):
        return 1
    def __pow__(self, b):
        return b
    def __rshift__(self, b):
        return 1
    def __lshift__(self, b):
        return 1

    def __mul__(self, b):
        return b
    def __div__(self, b):
        return b
    def __floordiv__(self, b):
        return b
    def __sub__(self, b):
        return b
    def __repr__(self):
        return ''
    def __mod__(self, b):
        return b
    def __divmod__(self, b):
        return (b,)
    def __invert__(self):
        return 1
    def __neg__(self):
        return 1
    def __pos__(self):
        return 1
    def __hash__(self):
        return 1
    def __abs__(self):
        return 1

    def __copy__(self):
        return self
    def __deepcopy__(self):
        return self

    def __with_float__(self):
        return 1.0

class float_:
    def __add__(self, b):
        return b.__with_float__()
    def __sub__(self, b):
        return b.__with_float__()
    def __mul__(self, b):
        return b.__with_float__()
    def __div__(self, b):
        return b.__with_float__()
    def __floordiv__(self, b):
        return b.__with_float__()
    def __pow__(self, b):
        return b.__with_float__()
    def __neg__(self):
        return 1.0
    def __pos__(self):
        return 1.0
    def __mod__(self, b):
        return b.__with_float__()
    def __divmod__(self, b):
        return (b.__with_float__(),)

    def __repr__(self):
        return ''
    def __hash__(self):
        return 1
    def __abs__(self):
        return 1.0
    def __copy__(self):
        return self
    def __deepcopy__(self):
        return self

    def __with_float__(self):
        return 1.0

class none:
    def __hash__(self):
        return 1

class pyiter:
    def __init__(self, i=None):
        pass
    def __inititer__(self, i):
        self.unit = iter(i).next()

    def __iter__(self):
        return __iter(self.unit)
    def __copy__(self): # XXX to base class
        return self
    def __deepcopy__(self):
        return self

class pyseq(pyiter):
    pass

class list(pyseq):
    def append(self, f):
        self.unit = f
    def index(self, idx, s=0, e=0):
        return 1
    def count(self, a):
        return 1

    def __getitem__(self, i):
        return self.unit
    def __setitem__(self, i, e):
        self.unit = e
    def __delitem__(self, i):
        pass

    def __len__(self):
        return 1
    def __contains__(self, x):
        return 1
    def __add__(self, b):
        return self
        return b
    def __mul__(self, b):
        return self
    def __iadd__(self, b):
        self.unit = b.unit
        return self
    def __imul__(self, n):
        return self
    def __slice__(self, x, l, u, s):
        return self
    def __delslice__(self, a, b):
        pass
    def __setslice__(self, x, l, u, s, r):
        self.unit = r.unit
    def __delete__(self, x, a=1, b=1, s=1):
        pass
    def __repr__(self):
        self.unit.__repr__()
        return ''
    def __str__(self):
        return self.__repr__()
    def extend(self, u):
        self.unit = u.unit

    def pop(self, m=0):
        return self.unit
    def remove(self, e):
        pass
    def insert(self, m, e):
        self.unit = e

    def reverse(self):
        pass
    def sort(self, cmp=0, key=0, reverse=0):
        elem = self.unit
        cmp(elem, elem)
        elem.__cmp__(elem)
        key(elem)

class tuple(pyseq):
    def __len__(self):
        return 1
    def __repr__(self):
        self.unit.__repr__()
        return ''
    def __str__(self):
        return self.__repr__()

    def __add__(self, b):
        a = self.unit
        a = b.unit
        return (a,)
    def __mul__(self, b):
        return self

    def __getitem__(self, i):
        a = self.unit
        return a

    def __slice__(self, x, l, u, s):
        return self
    def __hash__(self):
        return 1

class tuple2(pyseq):
    def __len__(self):
        return 1
    def __repr__(self):
        self.first.__repr__()
        self.second.__repr__()
        return ''
    def __str__(self):
        return self.__repr__()

    def __add__(self, b):
        a = self.unit
        a = b.unit
        return (a,)

    def __mul__(self, b):
        return (self.unit,)

    def __getitem__(self, i):
        return self.unit

    def __getfirst__(self, i):
        return self.first
    def __getsecond__(self, i):
        return self.second

    def __hash__(self):
        return 1

class str_(pyseq):
    def strip(self, chars=''):
        return ''
    def lstrip(self, chars=''):
        return ''
    def rstrip(self, chars=''):
        return ''

    def istitle(self):
        return 1
    def splitlines(self, c=0):
        return ['']
    def partition(self, sep):
        return ['','','']
    def rpartition(self, sep):
        return ['','','']
    def rsplit(self, sep='', c=-1):
        return ['']
    def split(self, sep='',c=-1):
        return ['']
    def join(self, l):
        return self
    def __getitem__(self, i):
        return ' '
    def __mul__(self, n):
        return ''
    def __contains__(self, s):
        return 1
    def __repr__(self):
        return ''
    def __mod__(self, a=None):
        a = a.unit
        a.__str__()
        a.__repr__()
        return ''
    def __add__(self,be):
        return ''
    def __len__(self):
        return 1

    def upper(self):
        return ''
    def lower(self):
        return ''
    def title(self):
        return ''
    def capitalize(self):
        return ''

    def find(self, sub, s=0, e=0):
        return 1
    def rfind(self, sub, s=0, e=0):
        return 1
    def index(self, sub, s=0, e=0):
        return 1
    def rindex(self, sub, s=0, e=0):
        return 1

    def isdigit(self):
        return 1
    def islower(self):
        return 1
    def isupper(self):
        return 1
    def isalpha(self):
        return 1
    def isspace(self):
        return 1
    def isalnum(self):
        return 1

    def zfill(self, width):
        return ''
    def ljust(self, width, chars=''):
        return ''
    def rjust(self, width, chars=''):
        return ''
    def expandtabs(self, width=8):
        return ''

    def count(self, e, start=0, end=0):
        return 1
    def startswith(self, e, start=0, end=0):
        return 1
    def endswith(self, e, start=0, end=0):
        return 1

    def replace(self, a, b, c=0):
        return ''

    def translate(self, table, delchars=''):
        return ''

    def swapcase(self):
        return ''
    def center(self, w, fill=''):
        return ''

    def __slice__(self, x, l, u, s):
        return self
    def __hash__(self):
        return 1

class dict(pyiter):
    def __initdict__(self, other):
        self.__setunit__(other.unit, other.value)

    def __inititer__(self, other):
        item = iter(other).next()
        self.__setunit__(item[0], item[1])

    def __repr__(self):
        self.unit.__repr__()
        self.value.__repr__()
        return ''
    def __str__(self):
        return self.__repr__()

    def __key__(self, k):
        k.__hash__()
        k.__eq__(k)

    def __setunit__(self, k, v):
        self.__key__(k)
        self.unit = k
        self.value = v

    def __setitem__(self, k, v):
        self.__setunit__(k, v)
    def __getitem__(self, k):
        self.__key__(k)
        return self.value
    def __delitem__(self, k):
        self.__key__(k)

    def setdefault(self, k, v=None):
        self.__setunit__(k, v)
        return v

    def keys(self):
        return [self.unit]
    def values(self):
        return [self.value]
    def items(self):
        return [(self.unit, self.value)]

    def has_key(self, k):
        self.__key__(k)
        return 1

    def __len__(self):
        return 1

    def clear(self):
        pass
    def copy(self):
        return {self.unit: self.value}
    def get(self, k, default=None):
        self.__key__(k)
        return self.value
        return default
    def pop(self, k):
        self.__key__(k)
        return self.value
    def popitem(self):
        return (self.unit, self.value)
    def update(self, d):
        self.__setunit__(d.unit, d.value)

    def __delete__(self, k):
        self.__key__(k)

    def fromkeys(l, b=None):
        return {l.unit: b}
    fromkeys = staticmethod(fromkeys) # XXX classmethod

    def iterkeys(self):
        return __iter(self.unit)
    def itervalues(self):
        return __iter(self.value)
    def iteritems(self):
        return __iter((self.unit, self.value))

class pyset(pyiter):
    def __inititer__(self, i):
        self.__setunit__(iter(i).next())

    def __setunit__(self, unit):
        self.unit = unit
        unit.__hash__()
        unit.__eq__(unit)

    def issubset(self, b):
        return 1
    def issuperset(self, b):
        return 1

    def intersection(self, b):
        return self

    def difference(self, b):
        return self
    def symmetric_difference(self, b):
        return self
        return b

    def __sub__(self, b):
        return self
    def __and__(self, b):
        return self
    def __or__(self, b):
        return self
    def __xor__(self, b):
        return self

    def union(self, b):
        return self
        return set(b)

    def copy(self):
        return self

    def __hash__(self):
        return 1

    def __len__(self):
        return 1
    def __repr__(self):
        self.unit.__repr__()
        return ''

class frozenset(pyset):
    pass

class set(pyset):
    def add(self, x):
        self.__setunit__(x)
    def __isub__(self, b):
        return self
    def discard(self, x):
        pass
    def remove(self, x):
        pass
    def pop(self):
        return self.unit
    def clear(self):
        pass
    def update(self, b):
        self.unit = b.unit
    def difference_update(self, b):
        pass
    def symmetric_difference_update(self, b):
        self.__setunit__(b.unit)
    def intersection_update(self, b):
        pass

class complex:
    def __init__(self, real=None, imag=None):
        real.__float__()
        self.real = 1.0
        self.imag = 1.0

    def __add__(self, c):
        return self

    def __sub__(self, c):
        return self

    def __mul__(self, c):
        return self

    def __div__(self, c):
        return self

    def __floordiv__(self, b):
        return self

    def __mod__(self, b):
        return self

    def __divmod__(self, b):
        return (self,)

    def __pos__(self):
        return self

    def __neg__(self):
        return self

    def __abs__(self):
        return 1.0

    def __pow__(self, b):
        return self

    def conjugate(self):
        return self

    def __repr__(self):
        return ''

    def __with_float__(self):
        return self

    def __hash__(self):
        return 1

class object: pass

class Exception:
    def __init__(self, msg=None):
        self.msg = msg

class AssertionError(Exception): pass
class EOFError(Exception): pass
class FloatingPointError(Exception): pass
class IndexError(Exception): pass
class IOError(Exception): pass
class KeyboardInterrupt(Exception): pass
class KeyError(Exception): pass
class MemoryError(Exception): pass
class NameError(Exception): pass
class NotImplementedError(Exception): pass
class OSError(Exception): pass
class OverflowError(Exception): pass
class RuntimeError(Exception): pass
class StopIteration(Exception): pass
class SyntaxError(Exception): pass
class SystemError(Exception): pass
class SystemExit(Exception): pass
class TypeError(Exception): pass
class ValueError(Exception): pass
class ZeroDivisionError(Exception): pass

__exception = OSError('') # XXX remove
__exception.errno = 0
__exception.filename = ''
__exception.message = ''
__exception.strerror = ''

def str(x=None):
    x.__str__()
    x.__repr__()
    return ''

def int(x=None, base=1):
    x.__int__()
    return 1

def float(x=None):
    x.__float__()
    return 1.0

def hex(x):
    x.__hex__()
    return ''

def oct(x):
    x.__oct__()
    return ''

def bin(x):
    x.__index__()
    return ''

def isinstance(a, b):
    return 1

def range(a, b=1, s=1):
    return [1]

def raw_input(msg=''):
    return ''

class file(pyiter):
    def __init__(self, name, flags=None):
        self.unit = ''
        self.closed = 0
        self.name = ''
        self.mode = ''

    def read(self, size=0):
        return ''
    def readline(self, n=-1):
        return ''
    def readlines(self):
        return ['']

    def write(self, s):
        pass
    def writelines(self, it):
        pass

    def seek(self, i, w=0):
        pass
    def tell(self):
        return 1

    def flush(self):
        pass
    def close(self):
        pass

    def fileno(self):
        return 1

    def __repr__(self):
        return ''

    def next(self):
        return ''

def open(name, flags=None):
    return file(name, flags)

def ord(c):
    return 1

def chr(i):
    return 'c'

def round(x, n=0):
    return 1.0

def divmod(a, b):
    return a.__divmod__(b)

def bool(x):
    x.__nonzero__()
    x.__len__()
    return 1

def repr(x):
    return x.__repr__()

def hash(x):
    return x.__hash__()

def len(w):
    return w.__len__()

def pow(a, b, c=1):
    return a.__pow__(b)

def abs(x):
    return x.__abs__()

def sorted(it, cmp=0, key=0, reverse=0):
    elem = iter(it).next()
    cmp(elem, elem)
    elem.__cmp__(elem)
    key(elem)
    return [elem]

def reversed(l):
    return iter(l)

def enumerate(x):
    return __iter((1, iter(x).next()))

class __xrange:
    def __init__(self):
        self.unit = 1
    def __iter__(self):
        return __iter(1)
    def __len__(self):
        return 1

def xrange(a, b=1, s=1):
    return __xrange()

def zip(*args):
    return [(iter(args).next(),)]
def __zip2(arg1, arg2):
    return [(iter(arg1).next(), iter(arg2).next())]

def max(__kw_key=0, *arg): # XXX 0
    arg.__cmp__(arg)
    __kw_key(arg)
    return arg
def __max1(arg, __kw_key=0):
    elem = iter(arg).next()
    elem.__cmp__(elem)
    __kw_key(elem)
    return elem

def min(__kw_key=0, *arg): # XXX 0
    arg.__cmp__(arg)
    __kw_key(arg)
    return arg
def __min1(arg, __kw_key=0):
    elem = iter(arg).next()
    elem.__cmp__(elem)
    __kw_key(elem)
    return elem

def sum(l, b):
    b.unit = l.unit.unit # XXX
    return sum(l)
    return b
def __sum1(l):
    elem = iter(l).next()
    elem.__add__(elem)
    return elem

def cmp(a, b):
    a.__cmp__(b)
    return 1

def any(a):
    return 1

def all(a):
    return 1

class __iter(pyiter):
    def __init__(self, a):
        self.unit = a
    def next(self):
        return self.unit
    def __iter__(self):
        return self
    def __len__(self): # xrange and such
        return 1

def iter(a):
    return a.__iter__()

def exit(code=0):
    pass

def quit(code=0):
    pass

def map(func, *iter1):
    return [func(*iter(iter1).next())]
def __map3(func, iter1, iter2):
    return [func(iter(iter1).next(), iter(iter2).next())]
def __map4(func, iter1, iter2, iter3): # XXX
    return [func(iter(iter1).next(), iter(iter2).next(), iter(iter3).next())]

def filter(func, iter1):
    if func(iter(iter1).next()):
        return [iter(iter1).next()]
def __filter(func, iter1):
    func(iter(iter1).next())
    return iter1

def reduce(func, iter1, init=None):
    elem = iter(iter1).next()
    return func(elem, elem)

def next(iter1, fillvalue=None):
    return iter1.next()
    return fillvalue
