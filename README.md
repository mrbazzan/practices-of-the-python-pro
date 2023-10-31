
> My musings from Dane Hillard's **PRACTICES OF THE PYTHON PRO**

CHAPTER THREE
-------------

Abstraction helps reduce cognitive load, and allow focus on
making sure software works

Decomposition enables abstraction. Decomposition is breaking down
software into smaller parts.

Encapsulation (basis for OOP). This allows related functions and
data to be grouped into a larger construct. Constructs in Python
that allow encapsulation to be achieved are listed below in increasing
order of encapsulation?
> functions
> classes and methods
> modules
> packages

Privacy in Python.

Python has no real support for private methods or data. The burden is
placed on the developers. Thus, a common convention is to begin private
variables, method, clases with an underscore in Python (this is not set
in stones by any means, it's just a convention).

In order to achieve loosely coupled classes, it is imperative that other
classes don't depend on the internals (private variable, methods etc.) of
a class.

Encapsulation + Abstraction allows information hiding to be achieved (hi-
ding parts that don't really matter to the users).

Programming Styles
------------------

- Procedural: using procedure calls (functions).
- Functional: program as compositions of functions (as arguments or
              return value). Think conventional interfaces
- Declarative: Think how matplotlib.pyplot is used. ??! HTML too.

Typing, Inheritance and Polymorphism
------------------------------------

A language's type system is how it choose to manage data types of variable,
Python is dynamically typed (data types are determined at runtime). Some
other languages are statically typed (data types are determined at compile
time).

Python raises an **AttributeError** when a method is called, but it
does not exist in an instance's class whereas some other languages fail
to even compile if this happens. This allows Python to be great for
*Polymorphism*, a language feature that allows utilizing a method on
objects of different types to provide varying behavious (or in the words
of Hillard, A PROGRAMMING LANGUAGE FEATURE WHERE OBJECTS OF DIFFERENT TYPES
PROVIDE SPECIALIZED BEHAVIOUR VIA A CONSISTENT METHOD NAME)

At the advent of OOP,
> ConsolePrinter < Printer < Buffer < BytesHandler

Today (when did he write the book?), the preference has shifted to
"composing behaviours into an object). Composition.

Inheritance forces hierarchy. Composition frees one from the limitations
of hierarchy while providing the relation.
> An example that helps think about this, is the classification of
> Kangaroo, Human, Cat and Dog to (Biped, Mammal, Quadruped, Canine) where
> each of them can belong to more than one group i.e Dog can belong to the
> group of Canine, Quadruped, and anyone else that is true.

Composition is achieved through a language feature called *Interface*.
Interfaces are formal definition of methods and data that a class must
implement

NOTE TO SELF:
    Python lacks interfaces? What about "abstractmethod" module. Perhaps
    what he meant is that Python, the language, doesn't by default provide
    interfaces? Isn't "abstractmethod" a core library though?

A make-shift interface can be built in Python, this is referred to as
*Mixin*. Creating a model for animals that can speak and roll becomes:

```python

class SpeakMixin:
    def speak(self):
        ...

class RollMixin:
    def speak(self):
        ...

# e.g for Dog

class Dog(SpeakMixin, RollMixin):
    pass

```

This allows dog to display a couple of tricks (page 56).

NOTE TO SELF:
    FIND TIME TO STUDY PARADIGMS

An *Adapter* in software is when an abstraction is created over an external
software (e.g a third-party package) to make it easier to use.


CHAPTER FOUR
------------

    DESIGNING FOR HIGH PERFORMANCE


In large systems, if something feels instanteous, it might be fast enough.
If your software requires storage on a disk or in a database, minimizing the
amount of storage saves money (how? well, you wouldn't have to pay the
external services: Amazon, Google etc. a huge sum because you are not
saving a lot of data.

[my note] Software that depend on databases have to worry about
fetch-and-get time.

Changes lower than 100ms to humans are instantenous.

Time and Space complexity is not an exact measurement, rather it helps
understand the worst case scenario for a software.
[note] complexity measurement are used to contrast(evaluate) ways of
achieving a particular task; they aren't so useful for unrelated tasks.
e.g you can compare the complexity of differing algorithms for finding
an element in a sorted list, not so much comparing the recursive solution
of finding the nth fibonacci number to an iterative (or even recursive)
solution of finding the factorial of a number.

Time complexity
---------------

It measures how fast a code can perform a task in relation to its inputs.

- Linearity O(n)
[note] even though a particular activity may be steeply linear, other, more
complex operations can still outpace it if the inputs are sufficiently many.
Wow! there are cases in which O(n^2) might be slower than O(n).

- Square Proportionality O(n^2)
Think nested loops (a loop in another loop)

- Constant Time O(1)
Doesn't depend on the input! Nothing is better than constant time.
[what do you mean Dan] the initial computation may itself be nonconstant,
but if it allows subsequent steps to become constanct, great trade-off!.

Space complexity
----------------

It measures the disk space or memory usage of a code as input grows.
Python has the added advantage of automatic garbage collection.

[hey baz] be careful about the way you deal with files, you don't always
have to load everything in memory!

Try to find opportunities to shift from a higher-order complexity to a
lower-order one, this will almost always yield better performance.

Performance and data types
--------------------------

Understanding Python's existing datatypes is important because new
software written in Python will build on the existiing data types.

Time
----

- For constant time
adding, removing and accessing items from a ``set`` and ``dict``

```python

# by using a set to hod all the unique colors, checking for specific
# color in the set takes only constant time.
colors = set()
with open('all-favorite-colors.txt') as favorite_colors_file:
    for color in favorite_colors_file:
        colors.add(color.strip())

```

- For linear time
most operations on a ``list`` datatype.
adding or removing from the end of a list takes O(1) time.

``tuples`` too, but they can't be modified.

Space
-----

A list of 10 elements takes roughly 10 times more space in memory than
a list with single element. i.e space complexity == O(n)

The trick is to use ``generators`` (they produce single value at a time
pausing until the next value is requested). e.g ``range(start, stop, step)``.

How do generators work in Python? Generators make use of the ``yield``
keyword. ``yield`` yields a value, and then yields execution (execution goes
back to the calling code)

```python

def range(args):
    assert len(args) < 4

    if len(args) == 1:
        start = 0
        stop = args[0]
    else:
        start = args[0]
        stop = args[1]

    current = start
    step = args[2] if len(args) == 3 else 1

    while current < stop:
        yield current
        current += step

```
