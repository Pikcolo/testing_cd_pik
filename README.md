# Testing Code
## Hello
> My name is Sirawich Noipa

> student id: 6610110327

## How to Run Testing
- Linux 
``` 
python3 -m unittest -v tests/<test_file_name.py>
```
- OSX
``` 
python -m unittest -v tests/<test_file_name.py>
```
- Windows
``` 
python -m unittest -v tests/<test_file_name.py>
```
``` 
py -m unittest -v tests/<test_file_name.py>
```

## How to Test Coverage

- Install coverage and nosetest package
```
pip install coverage nose2
```
- Try run nose2 with coverage
```
nose2 -v --with-coverage
```
```
nose2 -v --with-coverage --coverage-report html
```
```
nose2 -v –with-coverage --coverage <package_name>
```
