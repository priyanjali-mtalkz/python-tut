class Test:
    def __init__(self):
        a = 10
    def foo(self):
        return "Hello"
    def loo(self):
        self.foo()
        return "foo and loo called"

x = Test
print(x.loo())