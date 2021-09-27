print("What?")
a = [1, 2, 3]
a = [1, 2, 3,
     4, 5, 6,
     7, 8, 9]
a = [1,  # item 1
     2, ]

print("See Print")

a
[1, 2, 3]
a
(1, 2, 3)

a = {'key1': 1 #value for key 1
     ,'key 2': 2 #value foe key 2
     }

def my_func(a, #this is used to indicate....
            b, # comment
            c):
     print(a,b,c)

my_func(10,20,30)

my_func(10, #Comment
        20, #comment
        30 #comment
        )
a = 10
b = 20
c = 30

if a > 5 \
    and b > 10 \
        and c > 20:
     print('yes')


a = 'this\nis a string'
print(a)

a = '''this
    is a string
       that is created over multiple lines'''
print (a)