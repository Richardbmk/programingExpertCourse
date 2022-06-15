class A:
    pass

class B:
    pass

class C(A, B):
    pass

class D(C):
    pass


a = C()

print(isinstance(a, B))
print(isinstance(a, A))
print(isinstance(a, C))
print(isinstance(a, D))