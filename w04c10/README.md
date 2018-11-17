# W04c10 Basic Input and output

* User input with input()
* Reading and writing files
* Structured files
* Shelf
* csv

Next Class
* JSON and SQLite
* Begin flow control discussion

## TOC

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [W04c10 Basic Input and output](#w04c10-basic-input-and-output)
	- [TOC](#toc)
	- [User input with input()](#user-input-with-input)
- [note that print automatically includes a seperator space, but we can change](#note-that-print-automatically-includes-a-seperator-space-but-we-can-change)
- [that behavior if needed](#that-behavior-if-needed)
- [or, we could concatenate the string](#or-we-could-concatenate-the-string)
	- [Reading and writing files](#reading-and-writing-files)
		- [Plaintext ("Text") files](#plaintext-text-files)
			- [Writing Text Files](#writing-text-files)
			- [Using With statement](#using-with-statement)
			- [Reading Text Files](#reading-text-files)
		- [Binary files](#binary-files)
		- [Structured files](#structured-files)
			- [Shelf files](#shelf-files)
			- [CSV](#csv)

<!-- /TOC -->

## User input with input()

We've already seen how we can a program input via command line arguments, now let's look at Python's input function

The input function in Python allows us to get user input.

```python
uname = input("Hello, what is your name: ")
print("Hello", uname)
# note that print automatically includes a seperator space, but we can change
# that behavior if needed
print("Hello ", uname, " nice to meet you.", sep='')
# or, we could concatenate the string
print("Hello" + uname + "nice to meet you.")
```

We can also get numbers, or other data format, but we need to be careful:
```python
mpg = input("Enter your car's mpg rating: ")
gallons = input("Enter the number of gallon's you think you have in your gas tank: ")
print("You could drive ", mpg*gallons, " miles with this amount of gas. What are your waiting for!")
```

> __NOTE:__ Python allows you to format strings in a very similar fashion to the printf statement found in C, C++, and Java. But Python also a and advance "PyFormat" option as well (see: https://pyformat.info/, and also see https://docs.python.org/3/tutorial/inputoutput.html)

## Reading and writing files

Files are typically text, or binary, and structured or unstructured.

### Plaintext ("Text") files

Plaintext files only contain basic text characters and do not include information on font, size, or color. We typically see text files having the .txt extension, but Python script files ending with the .py extension are also examples of plaintext files. These text files can be opened with Windows’s Notepad or OS X’s TextEdit application. Using Python you can read the contents of plaintext files and treat them as an ordinary string values.

#### Writing Text Files

```python
file = open("test.txt", "w") # open file, create if new and overwrite it exists
file.write("Hello world!")
file.write("...and yadda yadda yadda.")
file.close()
```

Using the command prompt we can run this script and view it's results.
```
$ cat test.txt
Hello world!...and yadda yadda yadda.
```

To append to the file
```python
file = open("test.txt", "a")
file.write("Hello World again")
file.close()
```

Now, we find the text appended to our file
```
cat test.txt
Hello world!...and yadda yadda yadda.Hello World again
```

Let's start adding some new lines:

```python
file = open("test.txt", "a")
file.write("\n\nHello World again, and again\n")
file.close()
```

...And the output:

```
$ cat test.txt
Hello world!...and yadda yadda yadda.Hello World again

Hello World again, and again
```

#### Using With statement

It's good to develop the habit of using the with statement. Using the with statement we don't have to remember to close the file, it will be automatically closed for us.

```python
with open("test.txt", "a") as file:
  for x in range(0, 10):
    file.write(str(x) + "\n")
```

...and the output of which is:

```
$ cat test.txt
Hello world!...and yadda yadda yadda.Hello World again

Hello World again, and again
0
1
2
3
4
5
6
7
8
9
```

#### Reading Text Files

Reading text files is similar to the write. We'll use the with statement for our examples here.

If you want to read the entire file contents into a string, use the read function
```python
with open("test.txt", "r") as file:
  content = file.read()
print(content)
```

The output of which would be our entire text file:

```
$ python text_file5.py
Hello world!...and yadda yadda yadda.Hello World again

Hello World again, and again
0
1
2
3
4
5
6
7
8
9
```

__NOTE1__: Files and filepaths. When referencing a file that is in the current directory of the script, we only need to provide the filename. There are times, however, when we will need to reference a file that is located in another directory. In such cases we will need to provide the path along with the filename. There are differences between Windows and MacOS in how file paths are expressed. We will be using the Windows version in this course, which uses the drive letter and backslash format (i.e. "C:\folder\subfolder\filename.txt"). MacOS and Linus use forward slash, and may not use drive letter references - for instance, in MacOS "/Volumes" folder, and in Linus, "/mnt". If you are using one of these other platforms, you will need to translate these path references to your particular platform.

__NOTE2__: Since the backslash character (used in windows filepaths) is and escape character used in string formatting, we need to double the backslash as in the following example: "c:\\users\\bob\\file.txt"

__NOTE3__: If you're doing much work in this area, I'd suggest reading further on the [os.path module](https://docs.python.org/3/library/os.path.html). There are many useful functions in this module; ie. checking current working directory, the validity of a path, etc.

__SIDEBAR__ One very useful facility/function in Python is regular the expressions package, re. We'll probably revisit this in greater detail in the "data wrangling" portion of the course later, but for now, you can look into this powerful concept by reading this intro [here](https://developers.google.com/edu/python/regular-expressions), and the interactive exercise [here](https://regexone.com/lesson/introduction_abcs)

### Binary files

Unlike plaintext files, binary files contain information that is not constrained to just text. Binary files store information as binary data, and the interpretation of this data is generally very proprietary, or context specific. We will not be dealing much with binary files in this course, but you should be aware of them and how to deal with them when needed. Also, some file formats, such as Pythons "shelve" format (used to store Python objects) also use a binary format.  

### Structured files

Structured files require some extra information in order for them to be interpreted. These can be binary, or text, and they conform to some structure -- be it proprietary or to some standard.

#### Shelf files

With the "shelf" modules, we can save python objects from memory into binary shelf files.

```python
import shelve
shelfie = shelve.open('mydata')
pets = ['Fluffy', 'Pookems', 'Killa']
shelfie['pets'] = pets
shelfie.close()
```

```python
import shelve
shelfie = shelve.open('mydata')
print(list(shelfie.keys()))
print(list(shelfie.values()))
shelfie.close()
```

...and the output of which looks like:

```
$ python shelfie2.py
['pets']
[['Fluffy', 'Pookems', 'Killa']]
```
__NOTE__: For information on Python object persistence and shelve, read more [here](https://docs.python.org/3.4/library/shelve.html).

#### CSV

CSV file functions in Python:
* [official Python documentation](https://docs.python.org/3/library/csv.html)

Each line in a CSV file is a "row" (or record, observation, etc.), and the commas within the file indicate a new field (or cell, attribute, etc.).

CSV files are simple text files, making them convenient and well supported across many different applications. The downside to these files is that there don't contain any extra information such as Type of the values seen, don't indicate any formatting information (color, highlighting, ect.), don't have multiple worksheets, no specified width of the fields, etc.


```python
import csv
with open('sample.csv', newline='') as csvfile:
    sampleReader = csv.reader(csvfile)
    sampleData = list(sampleReader)
    print(sampleData)
```

Now, if you csv file has a header (which our example does), we can view it as follow:

```python
import csv
with open('sample.csv', newline='') as csvfile:
    sampleReader = csv.reader(csvfile)
    sampleData = list(sampleReader)
    print(sampleData[0][0:])
```
We can also load this data into a tuple structure:

```python
import csv
with open('sample.csv', newline='') as csvfile:
    sampleReader = csv.reader(csvfile)
    sampleData = tuple(sampleReader)
print(sampleData[0][0], ": ", sampleData[1][0], sep='')
print(sampleData[0][1], ": ", sampleData[1][1], sep='')
```

```python
import csv
with open('sample.csv', newline='') as csvfile:
    sampleReader = csv.reader(csvfile)
    sampleData = tuple(sampleReader)
print(sampleData[0][0], ": ", sampleData[1][0], sep='')
print(sampleData[0][1], ": ", sampleData[1][1], sep='')
```

Reading data using for Loop

```python
import csv
csvFile = open('sample.csv')
sampleReader = csv.reader(csvFile)
for row in sampleReader:
    print('Row #' + str(sampleReader.line_num) + ": " + str(row[0]))
```

Now, let's look at writing to a CSV file:

```python
import csv
csvFile = open('sample2.csv', 'w')
sampleWriter = csv.writer(csvFile)
sampleWriter.writerow(['Bob', 'Jones', '1234 Elm Street'])
sampleWriter.writerow(['Jill', 'Green', '4321 Pine Avenue'])
```

```
$ cat sample2.csv
Bob,Jones,1234 Elm Street
Jill,Green,4321 Pine Avenue
```
If we wanted to edit a values. Let's change Bob to Robert.

```python
import csv
with open('sample2.csv', newline='') as csvfile:
    sampleReader = csv.reader(csvfile)
    sampleData = list(sampleReader)

print(sampleData)
sampleData[0][0] = "Robert"
csvFile = open('sample2.csv', 'w')
sampleWriter = csv.writer(csvFile)
sampleWriter.writerows(sampleData)
```
