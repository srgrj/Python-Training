"""
for i in ['a', 'b', 'c']:
    try:
        print(i ** 2)
    except TypeError:
        print("Power operation cannot be used for strings")
    finally:
        print("All done")


x = 5
y = 0
try:
    z = x / y
except:
    print('division by zero is not allowed')
finally:
    print('all done')
"""


# i = 0
# print(type(i) == int)



def ask():
    while True:
        try:
            n = int(input('Input an integer: '))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            break

    print('Thank you, your number squared is: ', n ** 2)


ask()
