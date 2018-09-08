"""
"""


def count_to(count):
    # our list
    
    numbers_in_german = ["eins" , "zwei", "drei", "vier" , "funf"]
    
    iterator = zip(range(count), numbers_in_german)
    
    for position, number in iterator:
        yield number
    
for num in count_to(3):
    print(num)

for num in count_to(4):
    print(num)