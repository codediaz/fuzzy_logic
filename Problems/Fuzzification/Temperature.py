import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt


# DEFINE FUZZY VARIABLES
temperatura = ctrl.Antecedent(np.arange(0, 51, 1), 'temperatura')
motor = ctrl.Consequent(np.arange(0, 301, 1), 'motor')

# FUNCTION POPULATION
temperatura['fría'] = fuzz.trapmf(temperatura.universe, [0, 0, 8, 16])
temperatura['fresca'] = fuzz.trimf(temperatura.universe, [8, 16, 21])
temperatura['adecuada'] = fuzz.trimf(temperatura.universe, [16, 21, 30])
temperatura['calor'] = fuzz.trimf(temperatura.universe, [21, 30, 35])
temperatura['tórrida'] = fuzz.trapmf(temperatura.universe, [30, 35, 50, 50])  

motor['parar'] = fuzz.trapmf(motor.universe, [0, 0, 50, 100])
motor['despacio'] = fuzz.trimf(motor.universe, [50, 100, 150])
motor['medio'] = fuzz.trimf(motor.universe, [100, 150, 200])
motor['rápido'] = fuzz.trimf(motor.universe, [150, 200, 250])
motor['muy rápido'] = fuzz.trapmf(motor.universe, [200, 250, 300, 300])

# VISUALIZATION
temperatura['adecuada'].view()
plt.show()

motor.view()
plt.show()

# FUZZY RULES 
rule1 = ctrl.Rule(temperatura['calor'], motor['rápido'])
rule2 = ctrl.Rule(temperatura['tórrida'], motor['muy rápido'])
rule3 = ctrl.Rule(temperatura['fría'], motor['parar'])
rule4 = ctrl.Rule(temperatura['fresca'], motor['despacio'])

# RULES VISUALIZATION
rule1.view()
rule2.view()
rule3.view()
rule4.view()
plt.show()


# Control System Creation and Simulation
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])

tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

tipping.input['temperatura'] = 32

tipping.compute()

print(tipping.output['motor'])
motor.view(sim=tipping)
plt.show()

