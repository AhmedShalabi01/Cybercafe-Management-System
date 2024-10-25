# Cybercafe management system
> This repository contains the implementation of the cyber cafe management system which is a terminal-based application built using Python, pandas, and JSON as a course project

## Table of Contents
* [Requirements and Specifications](#requirements-and-specifications)
* [Libraries and Frameworks Used](#libraries-and-frameworks-used)
* [Application Usage](#application-usage)
* [Target Audience](#target-audience)
* [Room for Improvement](#room-for-improvement)

## Requirements and Specifications
here are the project requirements and specifications as received from the instructor: [Cybercafe Management System Requirements](docs/Cyper%20cafe%20management%20System.pdf)

<!-- and here is the complete system analysis pdf document: [Car Rental Business System Report](Car%20Rental%20Business%20System.pdf). -->

## Libraries and Frameworks Used
- [pandas - Python Data Analysis Library](https://pandas.pydata.org)
<br>pandas is a fast, powerful, flexible, and easy-to-use open-source data analysis and manipulation tool, built on top of the Python programming language.

<br>We have used pandas for creating, updating, and deleting computers and session information stored in an excel sheet that is used as a database for computers and session information.

- [JavaScript Object Notation (JSON)](https://www.json.org/json-en.html)
<br>JSON is a lightweight data-interchange format. It is easy for humans to read and write. It is easy for machines to parse and generate. It is based on a subset of the JavaScript Programming Language Standard ECMA-262 3rd Edition - December 1999. JSON is a text format that is completely language-independent but uses conventions that are familiar to programmers of the C family of languages, including C, C++, C#, Java, JavaScript, Perl, Python, and many others. These properties make JSON an ideal data-interchange language.

<br>We have used JSON for creating, updating, and deleting users' information stored in a JSON file that is used as a database for users' information.

## Application Usage
to run that terminal-based application, you need to do the following: 
1. clone that repository into your machine
2. create a python virtual environment in the cloned project directory and activate that virtual environment
3. download pandas library
4. download the JSON library
5. download the termcolor library
6. use your compiler to find all occurrences of the path `/Users/ahmedkhaled/Desktop/Ahmed Khalid/MSA University/Computer Engineering/Third Year/First Semester/Concepts of Programming Languages/project/CybercafeManagementSystem` and change it to the path of your project directory, e.g., `C:\Documents\Projects\project-directory`

## Target Audience
That project is best suited for introductory python programming courses as it uses basic programming concepts, e.g., functions, loops, variables, scoping, classes, and inheritance. That project does not use advanced OOP concepts like Polymorphism, abstract, or interface classes. Therefore, Developers who are in their first year learning python programming will apply most of their theoretical knowledge after studying that easy yet structured project.

## Room for Improvement
The project was delivered as a course project that we have to finish in a relatively short time. So if you want to improve it further, you can use a library like Tkinter to build a Graphical User Interface (GUI) as an interactive version of that application. Moreover, you can also create that application as Software As A Service (SAAS).
