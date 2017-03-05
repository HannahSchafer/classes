"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   a.) Abstraction
       Abstraction is a great design advantage of object orientation in that we 
       are able to use an object from a class without needing to understand the 
       underlying code. This enables efficiency. 

   b.) Encapsulation
       Encapsulation is another great design advantage of object orientation in 
       that the code be readable and maintanable. All the functionality
       and data of a particular class is kept neatly together.

   c.) Polymorphism
       Finally, Polymorphism is the third great design advantage of object 
       orientation in that we can treat different components in similar ways.
       This also enables efficiency, for example when I can make a single 
       'speak' method for all animals, (since all animals speak), and simply
       alter slightly how each sub-animal speaks.

2. What is a class?
   A class is a data structure that is like a smarter dictionary. A class stores
   data, is somewhat flexible, is highly structured, nad has its own stored
   behaviors/functionality.

3. What is an instance attribute?
   An instance attribute is a piece of data about that particular instance of a 
   class. 

4. What is a method?
   A method is an internal function or behavior to a specific class.

5. What is an instance in object orientation?
   An instance is the same thing as an object. Instantiation is the process by 
   which one makes a new, unique object within a class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   A class attribute should apply to ALL the instances/objects within the class.
   An instance attribute only applies to a unique object, once it is instantiated
   within the class.
   For example, a class attribute of the class HackbrightStudents would be 'women',
   since ALL Hackbright Students share this attribute. However, 'name' would be
   an instance attribute, since each student would have a unique instance of a name.
"""


# Parts 2 through 5:
# Create your classes and class methods

"""PART 2: Classes and Init Methods"""

class Student(object):
    """Stores student data: firstname, lastname, address.
    """

    def __init__(self, first_name, last_name, address):
        self. first_name = first_name
        self.last_name = last_name
        self. address = address


class Questions(object):
    """Stores a question and a correct answer. 
    """

    def __init__(self, question, answer):
        self.question = questions
        self.answer = answer


class Exam(object):
    """Stores exam data (questions and answers). 
    """

    def __init__(self, name, questions):
        self.name = name
        self.questions = []


"""PART 3: Methods"""


















