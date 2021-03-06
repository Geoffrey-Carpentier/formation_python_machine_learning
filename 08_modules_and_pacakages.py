#coding:utf-8

"""
modules and pacakges
-------------------------------"""

# personal modules
import modules.module1 as m1

print(m1.addition(1, 2, 3))


# needed modules for machine learning
import math
import random
import statistics
import os
import glob

# display the path of the current working directory
print(os.getcwd())

# get all files in the working directory (list)
print(glob.glob('*'))

# get all files with filter (list)
print(glob.glob('*.py'))


# display all the py files from the directory on the screen
filenames = glob.glob('*.py')

for file in filenames:
	with open(file, 'r') as f:
		print(f.read())
	print('--------------------------------')

"""
ex
----------------"""
# record the content of each .py file from the directory in a file.txt
filenames = glob.glob('*.py')

for file in filenames:
	with open(file, 'r') as f:
		with open(f'records/{f.name}.txt', 'w') as txt:
			txt.write(f.read())


"""
correction
--------------------"""
# record each file in a dictionnary wich each key is a file name
filenames = glob.glob('*.py')
d = {}
for file in filenames:
	with open(file, 'r') as f:
		d[file] = f.read().splitlines()
print(d)