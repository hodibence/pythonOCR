# Bank OCR

## Environment
I was using PyCharm IDE from JetBrains. The python version I was using is 3.8 and as my OS I am using windows 10.

## Requirements
Make sure you have python 3+ installed, you can run the following command and if you get back any version number higer than 3.0 you are good to go.
```shell
$ python --version
```

## Directory Structure
    data - sample files
    src  - all the .py files
    venv - libraray root

## Commands
### To run the program you have to pass the file path as an argument 
```shell
$ python main.py ..\data\one_to_9.txt
```
### To run tests the program
```shell
$ python -m unittest
```
### For more detailed tests add -v (verbose)
```shell
$ python -m unittest -v
```

## Result
    There is going to be a result.txt within the src folder which is containing the output
    based on the input file you provided, this file is going to expand as you are running
    the program over and over again, each account number is going to be represented in a single line.

 
