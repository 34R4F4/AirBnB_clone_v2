# AirBnB_clone_v2

## Setup

- fork [original repo](https://github.com/justinmajetich/AirBnB_clone.git)
- rename as `AirBnB_clone_v2`

## Primary Test

test orignal repo before start editing:

```bash
/AirBnB_clone$ ./console.py

./console.py:76: SyntaxWarning: "is" with a literal. Did you mean "=="?
  if pline[0] is '{' and pline[-1] is'}'\
./console.py:76: SyntaxWarning: "is" with a literal. Did you mean "=="?
  if pline[0] is '{' and pline[-1] is'}'\
./console.py:275: SyntaxWarning: "is" with a literal. Did you mean "=="?
  if args and args[0] is '\"':  # check for quoted arg
./console.py:283: SyntaxWarning: "is not" with a literal. Did you mean "!="?
  if not att_name and args[0] is not ' ':
./console.py:286: SyntaxWarning: "is" with a literal. Did you mean "=="?
  if args[2] and args[2][0] is '\"':
(hbnb) 
```
Error in `console.py`

```bash
(hbnb)	#CTRL+C
(hbnb) Traceback (most recent call last):
  File "./console.py", line 324, in <module>
    HBNBCommand().cmdloop()
  File "/usr/lib/python3.8/cmd.py", line 126, in cmdloop
    line = input(self.prompt)
KeyboardInterrupt
```
Error in `cmd.py`
