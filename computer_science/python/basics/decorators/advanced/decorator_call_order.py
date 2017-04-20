import functools
import inspect
 
class ClassBased:
    def __init__(self, *args, **kwargs):
        print("Args for ClassBased.__init__:", args, kwargs)
        self.args = args
        self.kwargs = kwargs
 
    def __call__(self, *args, **kwargs):
        print("Args for ClassBased.__call__", args, kwargs)
        @functools.wraps(args[0])
        def wrapped(*inner_args, **inner_kwargs):
            print("Args for ClassBased's wrapped function:", inner_args, inner_kwargs)
            print("Signature: ", repr(inspect.signature(args[0])), "Name: ", args[0].__name__)
            return args[0](*inner_args, **inner_kwargs)
        return wrapped
 
def dec1(func):
    print("Wrapping for dec1")
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        print("in dec1")
        func(*args, **kwargs)
        print("leaving dec1")
    print("done dec1")
    return wrapped
 
def dec2(func):
    print("wrapping in dec2")
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        print("in dec2")
        print("Signature",repr(inspect.signature(func)))
        func(*args, **kwargs)
        print("leaving dec2")
    print("wrapped")
    return wrapped

@ClassBased("mark")
@ClassBased("jim")
@dec2
def spam(inner_arg):
    print("in spam")
    print("inner arg is", inner_arg)
 
spam("Innermost arg")
