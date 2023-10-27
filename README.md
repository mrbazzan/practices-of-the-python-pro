
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
