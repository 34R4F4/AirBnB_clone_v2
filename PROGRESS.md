# AirBnB_clone_v2

## Setup

- fork [original repo](https://github.com/justinmajetich/AirBnB_clone.git)
- rename as `AirBnB_clone_v2`

## Primary Test

test orignal repo before start editing:

### Test Execution

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
(hbnb)	#Ctrl+D
/AirBnB_clone$
```
Error in `console.py`

Fix `console.py`

### Test Functionality

#### Create an object

```bash
(hbnb) create BaseModel
0c80c6be-c49e-42e5-9e4e-55f6023e9506
(hbnb)
```

#### Show an object

```bash
(hbnb) show BaseModel 0c80c6be-c49e-42e5-9e4e-55f6023e9506
[BaseModel] (0c80c6be-c49e-42e5-9e4e-55f6023e9506) {'id': '0c80c6be-c49e-42e5-9e4e-55f6023e9506', 'created_at': datetime.datetime(2024, 4, 13, 0, 31, 46, 197307), 'updated_at': datetime.datetime(2024, 4, 13, 0, 31, 46, 197314)}
(hbnb) 
```

#### Destroy an object

```bash
(hbnb) destroy BaseModel 0c80c6be-c49e-42e5-9e4e-55f6023e9506
(hbnb) 
(hbnb) show BaseModel 0c80c6be-c49e-42e5-9e4e-55f6023e9506
** no instance found **
(hbnb) 
```

#### Update an object

```bash
(hbnb) create User
fbc12975-3dbb-46af-8f40-7410f664aed0
(hbnb) all
["[User] (fbc12975-3dbb-46af-8f40-7410f664aed0) {'id': 'fbc12975-3dbb-46af-8f40-7410f664aed0', 'created_at': datetime.datetime(2024, 4, 13, 0, 39, 39, 138315), 'updated_at': datetime.datetime(2024, 4, 13, 0, 39, 39, 138322)}"]
(hbnb)
(hbnb)
(hbnb) update User fbc12975-3dbb-46af-8f40-7410f664aed0 first_name "Arafa"
(hbnb) all
["[User] (fbc12975-3dbb-46af-8f40-7410f664aed0) {'id': 'fbc12975-3dbb-46af-8f40-7410f664aed0', 'created_at': datetime.datetime(2024, 4, 13, 0, 39, 39, 138315), 'updated_at': datetime.datetime(2024, 4, 13, 0, 42, 18, 744639), 'first_name': 'Arafa'}"]
(hbnb) 
```

```bash
(hbnb) User.all()
["[User] (fbc12975-3dbb-46af-8f40-7410f664aed0) {'id': 'fbc12975-3dbb-46af-8f40-7410f664aed0', 'created_at': datetime.datetime(2024, 4, 13, 0, 39, 39, 138315), 'updated_at': datetime.datetime(2024, 4, 13, 0, 42, 18, 744639), 'first_name': 'Arafa'}"]
(hbnb) create User
7f63c502-4cb8-46f4-81b6-4f9dd23b6c07
(hbnb) update User 7f63c502-4cb8-46f4-81b6-4f9dd23b6c07 name "Bonolo"
(hbnb) User.all()
["[User] (fbc12975-3dbb-46af-8f40-7410f664aed0) {'id': 'fbc12975-3dbb-46af-8f40-7410f664aed0', 'created_at': datetime.datetime(2024, 4, 13, 0, 39, 39, 138315), 'updated_at': datetime.datetime(2024, 4, 13, 0, 42, 18, 744639), 'first_name': 'Arafa'}", "[User] (7f63c502-4cb8-46f4-81b6-4f9dd23b6c07) {'id': '7f63c502-4cb8-46f4-81b6-4f9dd23b6c07', 'created_at': datetime.datetime(2024, 4, 13, 0, 45, 15, 449052), 'updated_at': datetime.datetime(2024, 4, 13, 0, 46, 0, 700284), 'name': 'Bonolo'}"]
(hbnb) 
```

```bash
```

```bash
```

```bash
```

```bash
```

```bash
```

```bash
```

```bash
```

```bash
```

```bash
```

```bash
```

```bash
```

```bash
```

```bash
```

```bash
```

```bash
```

