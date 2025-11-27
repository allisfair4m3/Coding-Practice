# Coding-Practice
Practicing Python3 coding questions

Starting with DSA and Pandas Practice Questions

`master` is the main branch 
**RULE**: Development changes from `dev` branch pushed to this branch on biweekly Sundays

`dev` is the development branch
**RULE**: You're allowed to mess up here BUT only push clean working code changes to `master`.

# Python

## DSA - Data Structures and Algorithms

### Lists 
    - Solved 2 problems with difficulty level Easy

## OOP - Object Oriented Programming

### Introduction to Classes and Objects
    -   Created multiple classes like Book and Song to create its instances/objects, 
        assigned attributes (variables for example name, author/artist, pages, year, genre) 
        and methods (functions associated with each class like playing song, stopping)

### Class variables
    -   Created Class like Employee with class variables joining_year and num_employees,
        checked how these class variables are shared with instances of this class and 
        what happens when we modify it by accessing it through Class name vs its instance.

### What is __str__ and __repr__ ?

    -   Understood the difference between both, where `\_\_str\_\_` is used for user readability 
        compared to `\_\_repr\_\_` which is used for debugging purposes and represented in the 
        same manner as the object would be created while coding.

### Instance Method vs Static Method vs Class Method

    -   Instance Method: accessed using instance of the class for operating on instances of the class
    -   Static Method (Decorator `@staticmethod`): utility function accessed using Class but does not require instance/class data and can be used independently without `self` or `cls`
    -   Class Method (Decorator `@classmethod`): accessed using Class to access or modify class variables