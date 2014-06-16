from threading import Thread
import time

def memoize_args(name="undefined"):
    def wrapper(func):
        '''decorator to cache a setter function'''
        global _memoized_args
        _memoized_args = {}

        def decorator(self, *args, **kwargs):
            # see if "force" parameter is set
            if "force" in kwargs:
                force = kwargs["force"]
                del kwargs["force"]
            else:
                force = False

            if (not force) and (name in _memoized_args) and ((args, kwargs) == _memoized_args[name]):
                return True # TODO: use original return value
            else:
                # call function and save parameters
                ret_val = func(self, *args, **kwargs)
                _memoized_args[name] = (args, kwargs)

                return ret_val
        return decorator
    return wrapper

################################################################################

class ThreadMethodTimeoutError(Exception): pass

################################################################################

class ThreadMethodThread(Thread):
    "ThreadMethodThread, daemonic descendant class of threading.Thread which " \
    "simply runs the specified target method with the specified arguments."

    def __init__(self, target, args, kwargs):
        Thread.__init__(self)
        self.setDaemon(True)
        self.target, self.args, self.kwargs = target, args, kwargs
        self.start()

    def run(self):
        try:
            self.result = self.target(*self.args, **self.kwargs)
        except Exception, e:
            self.exception = e
        except:
            self.exception = Exception()
        else:
            self.exception = None

################################################################################

def threadmethod(timeout = None):
    "@threadmethod(timeout), decorator function, returns a method wrapper " \
    "which runs the wrapped method in a separate new thread."

    def threadmethod_proxy(method):

        if hasattr(method, "__name__"):
            method_name = method.__name__
        else:
            method_name = "unknown"

        def threadmethod_invocation_proxy(*args, **kwargs):
            worker = ThreadMethodThread(method, args, kwargs)
            if timeout is None:
                return worker
            worker.join(timeout)
            if worker.isAlive():
                raise ThreadMethodTimeoutError("A call to %s() has timed out"
                                               % method_name)
            elif worker.exception is not None:
                raise worker.exception
            else:
                return worker.result

        threadmethod_invocation_proxy.__name__ = method_name

        return threadmethod_invocation_proxy

    return threadmethod_proxy

