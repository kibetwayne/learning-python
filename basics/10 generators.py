'''Unlike list comprehensions that produce a full list in memory, generators produce items one at a time and on demand.
They are memory-efficient and ideal for working with large datasets.
Generators are a type of iterator, meaning they implement the __iter__() and __next__() methods automatically.
They use the yield keyword instead of return statement
Generators wait for you to ask for the next result
Generators are preferred more than list as they dont use mem space. They compute items only as needed, rather than storing the entire sequence.
Generators can handle infinite sequences without running out of memory.

uses +>
        reading large files line by line without loading them into memory
        Stream data from APIs or DBs in chunks
        Generate infinite sequences(prime numbers, prime numbers from Pi)'''

#!================================================================
#?generator functions
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

gen = count_up_to(5)
print(next(gen)) # Output: 1
print(next(gen)) # Output: 2
print(list(gen)) #output: [3, 4, 5] (remaining values)
def square(n):
    for i in range(n+1):
        yield i * i
    

for result in square(3):
    if result != 0:
        print(result)
        
#!================================================================
#?generator expressions
# similar to list compressions but using parentheses()
gen2 = (x**2 for x in range(5))
print(next(gen2)) #output: 0
print(next(gen2)) #output: 1
print(list(gen2)) #output: [4, 9, 16](remaining values)

#!================================================================
#?generator methods

#next(generator) retrieves the next value from the generator
gen3 = (x**2 for x in range(3))
print(next(gen3)) #output: 0
print(next(gen3)) #output: 1

#!================================================================
#.send(value) resumes the generator and sends external values to it. It passes the given value to the generator at the point where it is paused (at a yield statement).
def echo():
    while True:
        received = yield
        print(f'received: {received}')

gen4 = echo()
next(gen4) #start the generator
gen4.send('hello')



#!================================================================
#.close() #stops the generator
gen.close()