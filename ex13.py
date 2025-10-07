from sys import argv

script, arg1, arg2, arg3, arg4 = argv

print(f"This is the script called {script}")
note="The {} argument is {}"
print(note.format('first', arg1))
print(note.format('second', arg2))
print(note.format('third', arg3))
print(note.format('fourth', arg4))
