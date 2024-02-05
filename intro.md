## Prelude to Learning Python

1. What do you know about Python?
2. What is python used for?
3. What can python do? Are there limits?
 
***

Python is an object orientated, general-purpose, indentation-based, dynamically typed, garbage collected,
interprete programming and scripting language.

<h3>Object Orientated</h3>
What this means is that everything in python is an object. Any data created is an object.
An object can either be something logical, such as my GroceryStore program having a Milk Object,
or it can be something abtract, such as an object that represents an open file.
Every object has:

1. Data - This can be numbers, words...

2. Methods - Things you can do to / with the object (Perhaps Milk object could have a method 'add_to_cart')

3. The option for inheritance - Perhaps a Truck object may inherit the 'Vehicle' class, and shares data and methods that the
'Vehicle' abtract can do (Such as entering, turning on, refueling...)

It is a little more complex than this, but this is all that is needed right now


<h3> General-purpose </h3>
Sometimes people create languages with a certain purpose in mind. For example, R is made specifically for data scientists.
Python has no specific purpose, and is therefore geeralized as a general-purpose programming language

<h3> Indentation-Based </h3>
A code block is a snippet of code that is executed together. Many languages will use curly braces to define
different code blocks, python uses different indentations.
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

<h3>Garbage Collected</h3>
In all computer programs, random access memory (RAM) is used to store things, such as variables. (Think of spotify storing the name of
the current song somewhere.) In some programming languages, you need to explicitly create, and drop these values in memory.
Many languages, including python, have what's called a Garbage collector, which essentially does the memory management automatically,
at the cost of performance.

<h3>Interpreted</h3>
This is one of two ways for the computer to turn your code into binary instructions for the CPU.
The interpreter will go down line by line and execute each line. So if line 4 deletes a file, and line 5 causes
the program to crash, line 4 will still delete that file, regardless of what happens after it.
You might wonder, what is the other option than reading each line? Well, it is compiled.
The language will get compiled (Usually by external tools) and executed. The main difference is that each file has to produce no
errors before executing. So if line 4 delets a file, and line 5 causes an error, it will not delete the file.

<h3>Programming and Scripting Language</h3>
Usually different languages are categorized into either being meant for programming (Like creating apps such as spotify, or Chrome), or
meant for creating quick scripts (Such as searching a directory for text inside a file)
Python is good at, and can do both of these things. And the specific distinction between a language that CAN
do scripting actions, and a language that is commonly defined as a scripting language, is if it is easy and quick to
make the script

***

The python file extention is `.py`
