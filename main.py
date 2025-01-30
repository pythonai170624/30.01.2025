from typing import override


class A:
    @override
    def __hash__(self) -> int:
        super.__hash__()

def len_(instance):
    if instance.__len__:
        return instance.__len__()
    raise TypeError(f"object of type {type(instance)} has no len()")

a = A()
o = object()
print(len(o))
print(a.__class__)
a.x = 1
print(a.__dir__())
print(a)