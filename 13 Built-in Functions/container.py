x = (1,2,3,45,6,)
y = len(x)
y = list(reversed(x))
for i in y:
    print(i)

print(sum(x, 10))
print(max(x))

print(any((0,0,0,1,0,1,0,))) # any 1(True) gives True 0|0|1|0
print(all((0,0,0,1,0,1,0,))) # only all 1s (True) gives True 0&0&10

a = (1,2,3,4,5,6)
b = (9,5,6,7,8,2)
c = zip(a,b)
for aa, bb in c:
    print(f'{aa} - {bb}: {aa - bb}')

p = ('cat', 'dog', 'rabbit', 'velociraptor')
for i,v in enumerate(p): print(i,v)