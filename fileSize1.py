import os
dfile=os.stat('people-excercise.txt')
print(dfile.st_size)