## Prelude to Learning Python

1. What do you know about Python?
2. What is python used for?
3. What can python do? Are there limits?
<details>
<summary>4. Do you know what an environment is?</summary>
An environment is a way to describe the logical state of a computer, typically where code is ran, or programs are executed. Your computer has it's own unique environment. Environment characteristics are usually software based, but can be affected by
hardware, such as what CPU artitecture, or how much RAM it has. Environments have their own variables, called environmental variables. These variables can affect how code is ran, and how the user interacts with their environment.

Examples of environmental variables being used:

1. Using `win` + `r` and typing `%appdata%`. `%appdata%` is an environmental variable.
2. An online game using hardware serial numbers to ban cheaters / rule breakers.
3. A program using another program to perform some action. Here is an example of python calling a program called `ffmpeg`:
```python
import subprocess
subprocess.run(["ffmpeg", "i", "input.mp4", "output.mp4"])
```
This program will only run without error if the user has `ffmpeg.exe` as an environmental variable

</details>
<details>
<summary>5. What about a virtual environment?  </summary>

A virtual environment is an environment, but it is created with software. It simulates running code in a different computer. It is a type of virtualization. The purpose is to create
isolated environments so you can test and develop code separately from your system environment. It is commonly used to see what actions are required (such as installing a program) to make
a certain application work. (Such as the `ffmpeg` example above)

</details>

<details>
  
  <summary>What is python:</summary>
  
 Python is an object orientated, general-purpose, indentation-based, dynamically typed, garbage collected,
 interprete programming and scripting language.

<h3>Object Orientated</h3>
What this means is that everything in python is an object. Any data created is an object.
An object can either be something logical, such as my GroceryStore program having a Milk Object,
or it can be something abtract, such as an object that represents an open file.
Every object has:

1. Data - This can be numbers, words... it just needs to be associated with that object.

2. Methods - Things you can do to / with the object (Perhaps a Milk object could have a method 'add_to_cart')

3. The option for inheritance - Perhaps a Truck object may inherit the 'Vehicle' class, and shares data and methods that the
'Vehicle' abtract can do (Such as entering, turning on, refueling...)

Object orientated programming often has it's own course in university studies, but this is all that is needed right now


<h3> General-purpose </h3>
Sometimes people create languages with a certain purpose in mind. For example, R is made specifically for data scientists, Swift for building applications for Apple systems, or SQL, for interacting
with databases. (SQL is technically a query language, but you get the point)


The attribute of 'general purpose' is usually only given to languages that have a mature ecosystem, and lots of libraries to do vastly different tasks.


Python has no specific purpose, and is often referred to as a general-purpose programming language. 


<h3> Indentation-Based </h3>
A code block is a snippet of code that is executed together. Many languages will use curly braces to define
different code blocks, python uses a different method for code blocks: indentations.
<h5>Curly braces:</h5>

```
group_1
group_1
group_1 
{
  group_2
  group_2
  group_2
}
{
  group_3
  group_3
}
group_1
group_1
```
<h5>Indentation:</h5>

```
group_1
group_1
group_1
  group_2
  group_2
  group_2
    group_3
    group_3
  group_2
group_1
```
You don't need to worry about why or how code blocks are made, that will come later. Just know that python uses indentation.

<h3>Dynamically Typed</h3>
Some programming languages need you to define what type a variable is before allowing you to create it.
They also require you to define what types are passed in and returns from functions.
Python does not require you to explicitly define what type your variable is. The interpreter will know.

```
Static typing:
x: integer = 10;

Dynamic Typing:
x = 10;
```

<h3>Garbage Collected</h3>
In all computer programs, random access memory (RAM) is used to store things, such as variables. (Think of spotify storing the name of
the current song somewhere.) In some programming languages, you need to explicitly create, and drop these values in memory.
A majority of languages, including python, have what's called a Garbage collector, which essentially does the memory management automatically,
at the cost of performance.

<h3>Interpreted</h3>
Though interpretation vs compiling is not an inherant trait of the language, it is how the code gets executed. And technically, python's code is 'compiled' to bytecode, then interpreted.
But for the sake of running code, and how it acts, we'll call it interpreted.


This is one of two ways for the computer to turn your code into binary instructions for the CPU.
The interpreter will go down line by line and execute each line. So if line 4 deletes a file, and line 5 causes
the program to crash, line 4 will still delete that file, regardless of what happens after it.


You might wonder, what is the other option than reading each line? Well, it is compiled.
The language will get compiled (Usually by external tools) and executed. The main difference is that each file has to produce no
errors before executing. So if line 4 delets a file, and line 5 has a compilation error, it will not delete the file.

<h3>Programming and Scripting Language</h3>
Usually different languages are categorized into either being meant for programming (Like creating apps such as spotify, or Chrome), or
meant for creating quick scripts (Such as searching a directory for text inside a file)
Python is good at, and can do both of these things. And the specific distinction between a language that CAN
do scripting actions, and a language that is commonly defined as a scripting language, is if it is easy and quick to
make the script. Since all programming languages are scripting languages, but not all scripting languages are programming languages, we just refer to the useful, and easy to work with
languages as 'scripting languages'. And python fits that category.

  
  </details>

***

The python file extention is `.py`

You may also see file extention `.pyc`. This is the bytecode that is generated when a python file is executed. If deleted, python will generate a new one, next time the relevant script is ran.

