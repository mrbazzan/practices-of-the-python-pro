
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
