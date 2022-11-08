#copy test
a = 10
b = a
print(id(a),id(b))

a += 1
print('a값',a,+id(a), 'b값', b, id(b))

print(a)
print(b)

print(type(a))
print(type(b))

# twotimes(2)
# def twotimes(x):
#     y = 2 * x
#     return y
# print(y)