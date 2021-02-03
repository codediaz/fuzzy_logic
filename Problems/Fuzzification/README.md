<a href="https://pythonhosted.org/scikit-fuzzy/install.html"><img alt="Robot logo" src="https://pythonhosted.org/scikit-fuzzy/_static/img/logo.png" width = "150px" height = "90px" align= "right"/></a>
# Scikit-Fuzzy

### Fuzzy Control Systems: **The Tipping Problem**
The ‘tipping problem’ is commonly used to illustrate the power of fuzzy logic principles to generate complex behavior from a compact, intuitive set of expert rules.

If you’re new to the world of fuzzy control systems, you might want to check out [the Fuzzy Control Primer](https://pythonhosted.org/scikit-fuzzy/userguide/fuzzy_control_primer.html "the Fuzzy Control Primer") before reading through this worked example.

## Graphics 
### Quality:
```python
quality['average']
plt.show()
```
<a href="https://pythonhosted.org/scikit-fuzzy/_images/plot_tipping_problem_newapi_1.png"><img alt="" src="https://pythonhosted.org/scikit-fuzzy/_images/plot_tipping_problem_newapi_1.png" /></a>

### Service:
```python
service.view()
plt.show()
```
<a href="https://pythonhosted.org/scikit-fuzzy/_images/plot_tipping_problem_newapi_2.png"><img alt="" src="https://pythonhosted.org/scikit-fuzzy/_images/plot_tipping_problem_newapi_2.png" /></a>

### Service:
```python
tip.view()
plt.show()
```
<a href="https://pythonhosted.org/scikit-fuzzy/_images/plot_tipping_problem_newapi_3.png"><img alt="" src="https://pythonhosted.org/scikit-fuzzy/_images/plot_tipping_problem_newapi_3.png" /></a>

## Homepage and package documentation
http://pythonhosted.org/scikit-fuzzy/

## Source, bugs, and development
http://github.com/scikit-fuzzy/scikit-fuzzy

## Gitter IM
https://gitter.im/scikit-fuzzy/scikit-fuzzy

## Mailing List
http://groups.google.com/group/scikit-fuzzy

IEEE Rounding for Matlab users
------------------------------
It should be noted that Matlab rounds incorrectly. The IEEE standard (which is
how this package behaves) requires rounding to the nearest EVEN number if
exactly between, e.g. 1.5 --> 2; 2.5 --> 2; 3.5 --> 4; 4.5 --> 4, etc. This
minimizes systematic rounding error. Thus, if re-implementing algorithms from
Matlab code, slight inconsistencies in rounded results are expected. These are
not bugs, and will not be fixed.



