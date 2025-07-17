#!/usr/bin/env python3

# Student ID: [seneca_id]



def function1():

    # This object 'a' is local to function1

    a = 'object_function1'

    print('print() call in function1 on a:', a)



def function2():

    # This object 'a' is local to function2

    a = 'function2_object'

    print('print() call in function2 on a:', a)



# Object 'a' in main script

a = 'object_in_main'

print('print() call in main on a:', a)



# Call function1 (does not affect main's 'a')

function1()

print('print() call in main on a:', a)



# Call function2 (does not affect main's 'a')

function2()

print('print() call in main on a:', a)


