my_dictionary = {
'kittens': 'cute animals'
}
my_dictionary['kittens'] = 'delicious'
print my_dictionary
##The second line adds kittens into the dictionary as cute animals.

my_dictionary = {}
my_dictionary['puppies'] = 'baby dogs'
print my_dictionary
##the second line adds puppies to the dictionary with is meaning as baby dogs.

my_dictionary = {
    'hello': 'hola',
    'goodbye': 'adios'
    }
print my_dictionary.pop('foo', None)
# None
print my_dictionary
# {'goodbye': 2}
my_dictionary = {
    'hello': 'hola',
    'goodbye': 'adios'
    }
print my_dictionary.pop('foo')
print my_dictionary
##The difference between them is that print just prints out whatever folows after it on the same line.
