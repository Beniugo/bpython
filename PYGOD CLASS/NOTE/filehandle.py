from pprint import pprint   
""" 
'a' ---> append mode. this would open up the file append changes (read, write).
i craete a file i fit doesn't exist

'w' --- write mode. this allows to write to a file. if the file already contains content,
it will overwrite. it create a file if it doesnt exist.

'r'---- read mode. this is just used to read the file. This is the default mode.


"""
fhand = open("message.txt").readlines()
num_lines = 0
frequency = {}
for line in fhand:
    for word in line.split():
        frequency.setdefault(word, 0)
        frequency[word] += 1
print(frequency)