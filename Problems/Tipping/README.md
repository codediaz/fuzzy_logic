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



