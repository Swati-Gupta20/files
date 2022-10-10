# from pathlib import Pathq
# dfile=Path('people.txt')
# print(dfile.stat().st_size)



from pathlib import Path
user=input('file name:-')
dfile=Path(user)
print(dfile.stat().st_size)