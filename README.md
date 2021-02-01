<a href="https://pythonhosted.org/scikit-fuzzy/install.html"><img alt="Robot logo" src="https://pythonhosted.org/scikit-fuzzy/_static/img/logo.png" width = "225px" height = "115px"/></a>

Scikit-Fuzzy is a collection of fuzzy logic algorithms intended for use in the SciPy Stack, written in the Python computing language.
This SciKit is developed by the SciPy community. Contributions are welcome! Please join us on the mailing list or our persistent chatroom on Gitter.IM.

[![DOI](https://zenodo.org/badge/8872608.svg)](https://zenodo.org/badge/latestdoi/8872608)

## Homepage and package documentation
http://pythonhosted.org/scikit-fuzzy/

## Source, bugs, and development
http://github.com/scikit-fuzzy/scikit-fuzzy

## Gitter IM
https://gitter.im/scikit-fuzzy/scikit-fuzzy

## Mailing List
http://groups.google.com/group/scikit-fuzzy

License
-------
Please read LICENSE.txt in this directory.

IEEE Rounding for Matlab users
------------------------------

It should be noted that Matlab rounds incorrectly. The IEEE standard (which is
how this package behaves) requires rounding to the nearest EVEN number if
exactly between, e.g. 1.5 --> 2; 2.5 --> 2; 3.5 --> 4; 4.5 --> 4, etc. This
minimizes systematic rounding error. Thus, if re-implementing algorithms from
Matlab code, slight inconsistencies in rounded results are expected. These are
not bugs, and will not be fixed.
