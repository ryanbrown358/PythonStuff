"""
Opening and closing a file

File Mode - 
r - open an existing file to read
w - open am exostomg file to write.  Creates a new file if none exist or opens an existing file and discards all its previous contects
a - appends text. Opens or creates a text filew for writting at the end of the file. 
r+ - Open a text file to write to or read from a file
w+ - Opens a text file to write to or read from 
a+ - open or creates a text file to read from or write to at the end of file

Once the file is open and you have a file opject you can get different details about the file utilizing its properties 

"""
"""
name - Name of the opened file
mode - Mode in which the file was opened 
closed - Satus boolean value of Treu or False 
readable() - Read permission boolean value True or False 
writeable() - Write Permission boolean value of True or False


"""
"""file = open('example.txt', 'w')

print('File Name:', file.name)
print('File Open Mode:', file.mode)
"""

#Next add two statements to display the file access permissions
"""
print('Readable:', file.readable())
print('Writable:', file.writable())


def status(x):
    if (x.closed != False):
        return 'Closed'
    else:
        return 'Open'


print('File Status:', status(file))

file.close()

print('File Status: ', status(file))
"""

story = "Once upon a time\n"
story += "a dog who loved to play blass\n"
story += "This dog could run as fast as the wind"
print(story)

file = open('story.txt', 'w')
file.write(story)
file.close()

file = open('story.txt', 'r')

for line in file:
    print(line, end='')
file.close()

file = open('story.txt', 'a')
file.write('\n- Written by: Andrew')
file.close()