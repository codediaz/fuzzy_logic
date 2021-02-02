<a href="https://pythonhosted.org/scikit-fuzzy/install.html"><img alt="Robot logo" src="https://pythonhosted.org/scikit-fuzzy/_static/img/logo.png" width = "150px" height = "90px" align= "right"/></a>
# Scikit-Fuzzy

### Fuzzy Control Systems: **The Tipping Problem**
The ‘tipping problem’ is commonly used to illustrate the power of fuzzy logic principles to generate complex behavior from a compact, intuitive set of expert rules.

If you’re new to the world of fuzzy control systems, you might want to check out [the Fuzzy Control Primer](https://pythonhosted.org/scikit-fuzzy/userguide/fuzzy_control_primer.html "the Fuzzy Control Primer") before reading through this worked example.

## The Tipping Problem
Let’s create a fuzzy control system which models how you might choose to tip at a restaurant. When tipping, you consider the service and food quality, rated between 0 and 10. You use this to leave a tip of between 0 and 25%.

We would formulate this problem as:

+ Antecednets (Inputs)
    + service
        + Universe (ie, crisp value range): How good was the service of the waitress, on a scale of 1 to 10?
        + Fuzzy set (ie, fuzzy value range): poor, acceptable, amazing
        
    + food quality
        + Universe: How tasty was the food, on a scale of 1 to 10?
        + Fuzzy set: bad, decent, great

+ Consequents (Outputs)
    + tip
        + Universe: How much should we tip, on a scale of 0% to 25%
        + Fuzzy set (ie, fuzzy value range): poor, acceptable, amazing
        
    + food quality
        + Universe: How tasty was the food, on a scale of 1 to 10?
        + Fuzzy set: low, medium, high


        
+ Rules
    + IF the service was good or the food quality was good, THEN the tip will be high.
    + IF the service was average, THEN the tip will be medium.
    + IF the service was poor and the food quality was poor THEN the tip will be low.

+ Usage
    + If I tell this controller that I rated:
        + the service as 9.8, and
        + the quality as 6.5,
        
    + It would recommend I leave:
        + a 20.2% tip.

## Creating the Tipping Controller Using the skfuzzy control API
We can use the skfuzzy control system API to model this. First, let’s define fuzzy variables.

```python
    import numpy as np
    import skfuzzy as fuzz
    from skfuzzy import control as ctrl
```
For the representation of the graphs we use [Matplotlib](https://matplotlib.org/users/installing.html "matplotlib").
```python
    import matplotlib.pyplot as plt
```
```python
# New Antecedent/Consequent objects hold universe variables and membership
    # functions
    quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')
    service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
    tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')
    
    # Auto-membership function population is possible with .automf(3, 5, or 7)
    quality.automf(3)
    service.automf(3)
    
    # Custom membership functions can be built interactively with a familiar,
    # Pythonic API
    tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])
    tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
    tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])

```  
To help understand what the membership looks like, use the `view` methods.   
```python
# You can see how these look with .view()
quality['average'].view()
```
To see the graphs with matplotlib in [Visual Studio Code](https://code.visualstudio.com/ "Visual Studio Code"), put this at all of end `.view()`
```python
# You can see graphics in vscode
plt.show()
```
## Graphics: 
<a href="https://pythonhosted.org/scikit-fuzzy/_images/plot_tipping_problem_newapi_1.png"><img alt="" src="https://pythonhosted.org/scikit-fuzzy/_images/plot_tipping_problem_newapi_1.png" /></a>
```python
service.view()
plt.show()
```

