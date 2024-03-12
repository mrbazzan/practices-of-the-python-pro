
> My musings from Dane Hillard's **PRACTICES OF THE PYTHON PRO**
> Praxis Peritum Serpentium


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

A language's type system is how it chooses to manage data types of variable,
Python is dynamically typed (data types are determined at runtime). Some
other languages are statically typed (data types are determined at compile
time).

Python raises an **AttributeError** when a method is called but it
does not exist in an instance's class, whereas some other languages fail
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
> An example that helps think about the limitation of hierarchy is in the
> classification of Kangaroo, Human, Cat and Dog to
> (Biped, Mammal, Quadruped, Canine) where each of them can belong to
> more than one group i.e Dog can belong to the group of Canine,
> Quadruped, and anyone else that is true.

An issue occurs when a clear hierarchy is to be implemented between Mammal and
Quadruped. Not all Quadruped are Mammal, and not all Mammal are Quadruped.
How then is the hierarchy defined? Hence, composition.

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
    def roll(self):
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

Changes faster than 100ms to humans are instantenous.
    faster than 100ms == less than 100ms (e.g 50ms, 99ms)?

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
[what do you mean Dan] the initial computation may itself be non-constant,
but if it allows subsequent steps to become constant, great trade-off!.

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

# by using a set to hold all the unique colors, checking for specific
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

def squares(item):
    length = len(item)
    count = 0
    while count < length:
        yield item[count] ** 2
        count += 1

```

[hey, baz] use generators instead of list whenever you can.

Generators introduces this thing called **Lazy evaluation**, producing
one value at a time since consuming code might not need all the values
at once.

Make it work, make it right, make it fast
-----------------------------------------

This should be the goal in each small iteration as code is written.

Martin Fowler's rule of three for when refactoring should be done
> by the time you implement the same thing three times, there is
probably a need to provide an abstraction for that behaviour

Understanding what tools a language has for different activities often
helps to produce shorter/concise code (not always the best, we know).
This is one of the points of "making code right".

The performance of large system transcends code.

Tools
-----

timeit module in Python
CPU profiling (profiling means analyzing to gather metrics about
behaviour)


CHAPTER FIVE
------------

    TESTING YOUR SOFTWARE


Software testing can be loosely defined as the practice of verifying that
software behaves as expected.

Although it's easy to think that more time spent validating code affects
shipping time, testing provides a stable base on which refactoring
can be done (remember refactor? the guy that needs to be taken
care of frequently).


Anatomy of a functional test
----------------------------

Functional test ensures that a piece of code functions correctly. Some of
its steps are listed below:
i) prepare the inputs
ii) identify the expected outputs
iii) obtain the acutal output
iv) compare the actual output to the expected output

This allows test to be read as a specification of how code works.


Forms of functional testing
---------------------------
Manual testing
Automated testing
Acceptance testing - "Can I successfully add a book to my library?"
Unit testing
   In Python, functions can be isolated (given certain inputs, and expect
   certain outputs) so they are considered a unit. Classes contain many
   pieces that can be isolated further, so they are generally bigger than
   a unit, but they can be occasionally treated as one.
Integration testing
   It checks the result of interactions between various unit tests. Think,
   create a database, populate with some fields, perform various CRUD
   operations on it.

   End-to-end tests may be framed from the perspective of the user,
   integration tests focus more on the behaviour of code.
Regression testing
   A regression is a shift to an undesirable (or unexpected) state.
   This is the practice of running your existing suite of tests after
   each code change before shipping to production


Assertions
----------

Assertions are statements of fact


Unit testing with unittest
--------------------------

unittest is Python's built-in testing framework.

Test doubles
------------

In order to write test for codes that interact with other systems, there
might be a need to imitate API calls that have destructive effect on real data.
This can be done in any of the following ways:
- Faking
- Stubbing
- Mocking

Unit testing with pytest
------------------------

pytest is another testing framework in Python


Beyond functional testing
-------------------------

Functional testing precedes testing the speed of your code?

Performance testing
Load testing


Test-driven development (TDD)
-----------------------------

A mindset and a philosophy.
> if awkwardness must be incorporated in a code, it is better for it to
> be in tests than the real code. Never sabotage code only to make testing
> easier (or coverage stronger).


Chapter >5
----------

    PROJECT: bookmark

A multi-tier architecture is frequently used in web and desktop
applications (we use it in this project too).

- Presentation layer: interface for user to interact with software
- Logic layer: connector of the presentation and persistence layer
- Persistence layer: where data is stored for later use

Similar to this is the Model-View-Controller (MVC) pattern — think Django.

Persistence layer
-----------------

Create a ``DatabaseManager`` class to handle direct interaction with the
database through SQL code. A third-party ORM could also be used.

Database tips
-------------

Using cusors to execute statements, this allows iterating
over the result it returns.

Use clauses to limit scope. e.g ``WHERE``

Logic layer
-----------

Although it is tempting to litter the whole codebase with ``if`` blocks
that couples the text presented to the user with actions to be triggered.
Like so,

```python

if user_action == 'add':
    # add bookmark
elif user_action == 'delete':
    # delete bookmark

```

The problem lies in that:
- every new action has to get an ``elif`` statement (what if we have
20 actions?)
- what if a user action wants to trigger two actions
simultaneously (e.g add and delete)?

Rather, the logic of each action should be encapsulated as a command object
such that the presentation layer only points to command not caring how it
works. DECOUPLING.

The pattern described above is called a ``COMMAND PATTERN``.

Presentation layer
------------------

**bookmark** is a CLI application.

An ``Option`` class is created to provide user-facing functionalities.
Every option presented to the user is an instance of this class.
It is responsible for presenting an option to the user, handling
the corresponding input and triggering the associated Command class.


CHAPTER SEVEN
-------------

    EXTENSIBILITY AND FLEXIBILITY


What is extensible code? A code is said to be extensible when you
can add new features without editing/changing existing code.
Basically, implement new features to an existing codebase without
the need to revamp the whole project.
It only requires adding new code that encapsulate the new feature.

Chrome, Firefox and other browsers were not built specifically for
a particular add-on/extension, rather, they were designed to allow
for generic extensions to be built later.

A way to identify inextensible code is when you have to
perform ``shotgun surgery`` to get in new featrures.
In programming words, this means editing and modifying little
nuggets in the existing code.

Duplicating a copy of code, and updating it to suite the intended new
feature is also a form of extension. This provides the advantage
of finding out how to make the original code more extensible.

"Duplication is better than wrong abstraction"

Since real world systems are not ideal, it is quite possible that
editing existing code might occur when introducing a new feature.
This is where system flexibility applies.

There are couple of reasons why an existing code might require
modification; some of which are:
- to fix a bug
- refactoring to make it easy to work with
etc.

Since flexibility measures code's resistance to change, an ideal
flexible code would allow changes to occur without much hassle.

7.1: Example of a poorly flexible code
--------------------------------------

This code contains a rigid mapping of user choice to outcome

```python
if choice == "A":
    print("A is for apples")
elif choice == "B":
    print("B is for bags")

```

7.2: Example of a flexible code
-------------------------------

This is a flexible mapping of choices to outcome such that adding
new choices is achieved by adding the choice and outcome as key-value
pair in the dictionary. This mapping acts like a
configuration — information a program uses to determine how to execute.

Configuration is often easier to understand than conditional logic.

```python

choices = {"A": "apples", "B": "bags"}
print(f"{choice} is for {choices[choice]}")

```

**7.2** is an example of a loosely-coupled system. It is flexible,
and makes extension easily achieved.


Rigidity in code and possible solutions
---------------------------------------

Rigidity in code make it hard to introduce changes. A rigid code
is one in which the flexibility is quite low. The developer should
always look out for ways to make rigid code become flexible
by refactoring.

Some of the ways to reduce rigidity are:

Inversion of control
--------------------

One of the basic rules of OOP is that a system is defined as a couple
of small classes where each class is focused on a concern. The system
is then defined by writing a class that uses instances of those smaller
classes.

Inversion of control is concerned with how these small classes are used
by the larger class. The creation of instances of the smaller classes
should not happen when the larger class is being instantiated rather the
control of creation is placed on the code creating the system.

    ... instead of creating instances of dependencies in your class,
    you can pass in existing instances for the class to use.

For code example, check *inverison_of_control.py*

Relying on Interfaces
---------------------

Whenever large classes are too focused on the details
of smaller classes dependencies, rigidity manifests.

    Bicycle class doesn't really care about a specific tire
    or frame. It only cares that tire has certain attributes
    and methods.

Shared-upon interfaces allow for substitution of implementations
as long as the attributes and behaviours (methods) are consistent.

    This is why CarbonFiberFrame class could be used in-place of
    Frame class.

The robustness principle
------------------------

Entropy is the tendency for organization to dissolve into
disorganization over time.

Code often starts out small and understandable but it tends toward
complexity over time becauase it has to accommodate different kinds
of input.

To reduce rigidity, the robustness principle embodies the spirit of
providing only the behaviour required to achieve the desired
outcome while being open to array of inputs i.e the developer
has to think deeply about the kind of inputs the software
would accept over time.

An example in Python is the **int()** function which takes integers,
strings, bytes and floats as input. It acts as a funnel, chanelling
these various inputs into a single output type.

"Be conservative in what you do, be liberal in what you accept from
others"


CHAPTER EIGHT
-------------

    THE RULES (AND EXCEPTIONS) OF INHERITANCE


Classes can inherit from other classes, ending up with the
inherited classes' data and behaviour.

Inheritance of programming past
-------------------------------

Many applications sought to model real world systems as hierarchy of
objects, in the hopes of achieving a neat
structure (this is done with inheritance). Inheritance was so
entwined into object-oriented programming that the concepts
were nearly inseperable.

The problem lies in the use of inheritance as a
"silver bullet" (magical solution to a complicated problem).
The excessive use of the paradigm in OOP lead to a lot of people
getting frustrated and renouncing OOP altogther (this does not mean
that OOP and Inheritance donot have the capability for modelling
the right hierarchies).

What are some of the frustrations of class inheritance?
-------------------------------------------------------

- As software grows, it becomes harder to keep parent-child relationship
between classes straight.

    Inheritance introduces probably the tightest coupling in programming.
    A class inherits all the superclass's data and methods, and
    can then override them. When class hierarchies grow, it becomes
    quite difficult to see this coupling because looking at a
    particular class, it isn't obvious whether another class is
    inheriting from it or not.

    e.g Shape < Polygon < Quadrilateral < Rectangle < Square

    A change in `Shape` class could affect `Square` which is
    four levels away (like a propagating constraint?). This could
    pose a big danger in software.


"As developers, we should increase our understanding and reduce
cognitive load"

What is inheritance for?
------------------------

Inheritance is for **specialization of behaviour**, don't use it
only to reuse code.

    Create a subclass to make a method return a different value or
    perform different operation under the hood.

Substitutability
----------------

Liskov substitution principle states that ...

    in any program, any instance of a class must be replaceable by
    an instance of one of its subclasses without affecting the
    correctness of the program.

The ideal use case for inheritance
----------------------------------

- problem with shallow, narrow hierarchy: keep the hierarchy and
the number of subclass small.

    Iterable < (List, String, Dict, Set)

- subclasses are at the leaves of the object graph: a class may point
to other objects, but its subclasses generally shouldn't have any
further dependencies.

- subclasses use all the behaviour of their superclass: if a subclass
doesn't use all of its superclass's behaviour, is it really an
instance of the superclass?

    what does it mean to compose a behaviour into a class that needs
    it?


Inheritance in Python
---------------------

Python provides the following tools to check the "situation" of an object.
- `type()`
- `isinstance()`
- `issubclass()`
- `super()`: check **teller.py()**
