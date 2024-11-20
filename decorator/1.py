import functools

def print_name(func):
    @functools.wraps(func)
    def wrapper():
        func()
    # similar to react HOC which should change component`s displayName after wrap origin component
    # wrapper.__name__ = func.__name__
    return wrapper

@print_name
def test():
    print(f"the name of test func is {test.__name__}")


test()