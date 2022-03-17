class Task1(object):
    """
    Define a class which get a name in __init__ and at least two methods:
    print_string: to print the name in lower case
    printString: to print the name in upper case
    """
    def __init__(self, name="Barbara") -> None:
        self.my_name = name

    def print_string_lower(self):
        print(self.my_name.lower())

    def print_string_upper(self):
        print(self.my_name.upper())


class Task2(object):
    """
    Define a class named Circle which can be constructed by a radius. The Circle class has a method which can
    compute the area.
    """
    pass


class Task3(object):
    """
    Class that is model to robot moves starting from the original point (0,0) -- set up in init.
    The robot can move toward UP, DOWN, LEFT and RIGHT with given steps. The trace of robot movement is shown as the following:
    UP 5
    DOWN 3
    LEFT 3
    RIGHT 2

    so there should be two methods: get_current location(), move_instruction().
    """


class Task4(object):
    """
    Create class that works like stack. In init it creates an empty list. And it has two methods pop and push for
    pushing them on this list.
    """
    pass


class Task6(object):
    """
    Define a class named American which has a static method called printNumber and has information about
    how many objects were created.
    """


class Task7(object):
    """
    Write a Fraction class to represent rational numbers like 1/2 and -3/8.
    Fractions should always be stored in reduced form; for example, store 4/12 as 1/3 and 6/-9 as -2/3.
    Hint: A GCD (greatest common divisor) function may help.
    """


class Task8(object):
    """
    Define a class named Shape and its subclass Square. The Square class has an init function which takes a
    length as argument. Both classes have a area function which can print the area of the shape where Shape's
    area is 0 by default. To override a method in super class, we can define a method with the same name in the
    super class.
    """


class Task9(object):
    """
    Define a class Person and its two child classes: Male and Female.
    All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
    Use Parent class to define a child class.
    """


class Task10(object):
    """
    Create cool function to prepare stats on covid (using covid file).
    Let it have name of country and population in contructor and think
    about smart method to store data and present them as plots.

    Here everything is up to you, there are no bad solutions.
    """


if __name__ == '__main__':
    my_object = Task1("Grzegorz")
    other_object = Task1("Anna")

    my_object.print_string_lower()
    other_object.print_string_upper()

    my_object.my_name = "Filip"
    my_object.print_string_upper()

    yet_other_object = Task1()
    yet_other_object.print_string_upper()
