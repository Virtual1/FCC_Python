## FCC_Python

[FreeCodeCamp](https://www.freecodecamp.com) is building a Python curriculum and I want to help.  

My main focus for now is writing code challenges and lessons that focus on Python basics.

The challenge_recipe.py file contains a template for the code challenges.  

I am currently working on lessons for operators and operations.  

### [Curriculum Outline and Organization](https://github.com/freeCodeCamp/python-coding-challenges/issues/8)

In the root directory of the project there will exist a directory: **challenges**, and a file called **classroom_settings.json**

The **challenges** directory will contain each lesson directory title like so: `[C#].[L#].<name>` i.e. 2.1.Addition (means the Addition lesson is Lesson 1 of Chapter 2).
Due note that chapter and lesson numbers is for our organization purposes and will not be reflected in the Repl.it Classroom.

Each lesson directory will contain four files:

1. lesson_code.py
2. lesson_tests.py
3. lesson.md
4. lesson_settings.json  

lesson_code.py will be loaded into the initial-code section (top left container) of the classroom.

lesson_tests.py will be loaded into a hidden unittest file (behind the scenes).

lesson.md will be loaded into the markdown section (bottom right container) of the classroom.

lesson_settings.json will be used to store information such as Title, Chapter, Lesson number, ID(?). This will mainly be for FCC, but repl will be able to utilize the Title property and maybe the ID property.

Each Repl.it Classroom lesson url will be added to the challenges.json file in the project root directory.
