# codingforkids (Copyright of Zujiang)

## Popular Python functions:
* print( ): print an output message
* input( ): to take an input from the user (in string format even the input is a number)
* range( ): return a list of a sequence of integers, you can define start, stop, step
* abs( ): return an absolute value of a numeric value
* round( ): return an rounded value of a numeric value
* min( ) and max( ): return a smallest/biggest item of a list 
* pow(x, y): returns the value of x to the power of y (same as x**y)
* sorted( ): sort a list in ascending order
* sum( ): sum a list with numeric numbers
* len( ): return the number of characters in string, or the number of elements in a list
* open(file name, mode): open a file in mode r, w, x, a
* type( ): return the type of the variable  
* help(other function): display the help message of a given function

## Other useful functions
* str.format( ): output a formatted string with variables
* randint(a, b): return a random integer in range [a, b] including both ends (need to import random)
* random( ): return a random value between 0 to 1 (need to import random)
* list.index(“abc”): return the position at the first occurrence of “abc” in list
* list.append(item), list.insert(index, item), list.remove(item): add/insert/remove a item in a list
* list.clear( ): clear the entire list
* list.sort( ): sort the list
* list.count(“abc”): return the number of times “abc” appears in the list
* list.reverse( ): reverse the order of the list
* dict.values( ): returns a list of all the values in the dictionary
* dict.keys( ): returns a list of all the keys in the dictionary
* dict.clear( ): clear the entire dictinary
* dict.get(key ): get the value by key.  dict.get(key, defaultvalue): return the value by key if found, or return the      default value
* myValue = myDictionary[“mykey”]: retrieve your value in dictionary by providing the key
* set.add(item): add a new item into a set
* set.remove(item): remove a item from a set
* list(myset): copy the data in a set to a list
* datetime.now( ):  get the current date (need to: from datetime import datetime)

## create an empty python built-in object
* a = []: create a empty list 
* a = (): create a empty tuple
* a = {}: create a empty dictionary
* a = set(): create a empty set

## File Manipunation
* Use Python built-in function to open a file:
	```python
    open(file, mode, encoding)
    ```
    > file: the file name (with path)

    > mode: read/write/append + binary/text
    
    > encoding: only for text (for example: utf-8)
* Write some text to a file:
    ```python
	f = open('myfile.txt', mode='wt', encoding='utf-8')
    f.write("my name is greggy\n")                                              #write a string to the file
    f.writelines(['my first line\n', 'my second line\n', 'my third line\n'])    #write multiple lines
    f.close()           #always close your file after you finish to use it
    ```
* Read some text from a file:
    ```python
    f = open('myfile.txt', mode='rt', encoding='utf-8')	
    s = f.readline()		#read one line of text
    lineList = f.readlines()	#read all lines of text into a list	
    f.seek(0)			#go back to the beginning of the file so we can read it again
    f.close()           #always close your file after you finish to use it
    ```


## Some tips
* use help(math) function to get all the methods in math package
* use help(math.factorial) function to get the info on how to use factorial()  
* Use import this to see the full list of The Zen of Python
* Use ctrl + z, then enter to exit Python REPL
* Use ctrl + c to break the infinite loop in REPL

## Data for practices:
* 7316717653133062491922511967442657474235534912493496353520312774506326239578318016944807958478851843





