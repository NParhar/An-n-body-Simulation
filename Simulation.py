from Solar_System import Solar_System 
from Particle import Particle
import matplotlib.pyplot as plt
import math
import copy
import numpy as np 

""" Each object from line 13 to 23 represents a body in our Solar System which is then used in the system, Sol_System, which uses the n_body class and
Particle class to create a list of bodies where each body's variables can be updated. 
The data in the variables, used as the inital values, are from the Horizons database: 'https://ssd.jpl.nasa.gov/horizons.cgi', and the initial values
are taken from the day '2018-Nov-25'. These values have been converted to appropriate units.
"""
Sun = Particle(np.array([0.,0.,0.]), np.array([0.,0.,0.]), np.array([0.,0.,0.]),'Sun', 1988500e24, 0., 0.)
Mercury = Particle(np.array([0.2010056011166326*149597870700,0.2405381641244316*149597870700,0.001215319644815392*149597870700]), np.array([-0.02717021227155681*149597870700/86400, 0.01920474190026218*149597870700/86400 , 0.004061830215553290*149597870700/86400]), np.array([0.,0.,0.]),'Mercury', 3.302e23, 0., 0.)
Venus = Particle(np.array([0.1241488157626241*149597870700,0.7094836337699391*149597870700,0.002570611198339732*149597870700]), np.array([-0.01999193985646372*149597870700/86400, 0.003385691037584677*149597870700/86400 , 0.001200144446707753*149597870700/86400]), np.array([0.,0.,0.]),'Venus', 48.685e23, 0., 0.)  
Earth = Particle(np.array([0.4573952905847123*149597870700,0.8747952996605530*149597870700,-3.966563168994176e-5*149597870700]), np.array([-1.551939358195390e-2*149597870700/86400, 7.906277729451943e-3*149597870700/86400 , -8.856576917652236e-7*149597870700/86400]), np.array([0.,0.,0.]),'Earth', 5.97219e24, 0., 0.)
Mars = Particle(np.array([1.332426864378202*149597870700,4.740674750235996e-1*149597870700,-2.276116685310531e-2*149597870700]), np.array([-4.156646447387024e-3*149597870700/86400, 1.437967228831893e-2*149597870700/86400 , 4.033080484129075e-4*149597870700/86400]), np.array([0.,0.,0.]),'Mars', 6.4171e23, 0., 0.)
Jupiter = Particle(np.array([-2.384248186205534*149597870700,-4.800514525924035*149597870700,0.07328707718796308*149597870700]), np.array([0.006673389171273721*149597870700/86400, -0.003003264551429833*149597870700/86400 , -0.0001368253270294736*149597870700/86400]), np.array([0.,0.,0.]),'Jupiter', 1898.13e24, 0., 0.)
Saturn = Particle(np.array([1.767822582270580*149597870700,-9.904649529382823*149597870700,0.1018025920886717*149597870700]), np.array([5.193155139536926e-3*149597870700/86400, 9.608185430991238e-4*149597870700/86400 , -2.234294594450944e-4*149597870700/86400]), np.array([0.,0.,0.]),'Saturn', 5.6834e26, 0., 0.)
Uranus = Particle(np.array([1.709149992145677e1*149597870700,1.012504564096667e1*149597870700,-1.837198325944810e-1*149597870700]), np.array([-2.026882375843751e-3*149597870700/86400,3.197658949118317e-3*149597870700/86400 , 3.814276996387383e-5*149597870700/86400]), np.array([0.,0.,0.]),'Uranus', 86.813e24, 0., 0.)  
Neptune = Particle(np.array([2.895362406874241e1*149597870700,-7.601650919379489*149597870700,-5.107993578634304e-1*149597870700]), np.array([7.836626899057624e-4*149597870700/86400, 3.053184996874008e-3*149597870700/86400 , -8.095750876147414e-5*149597870700/86400]), np.array([0.,0.,0.]),'Neptune', 102.413e24, 0., 0.)
Pluto = Particle(np.array([1.177085805209303e1*149597870700,-3.156444373542071e1*149597870700,-2.782691017722837e-2*149597870700]), np.array([3.017994862824241e-3*149597870700/86400, 4.400420905674778e-4*149597870700/86400 , -9.055950942675726e-4*149597870700/86400]), np.array([0.,0.,0.]),'Pluto', 1.307e22, 0., 0.)
Moon = Particle(np.array([4.575772055610683e-1*149597870700,8.772449963736652e-1*149597870700,-1.563739702290773e-4*149597870700]), np.array([-1.613512463572199e-2*149597870700/86400, 7.942693574496635e-3*149597870700/86400 , 4.622545710464050e-5*149597870700/86400]), np.array([0.,0.,0.]),'Moon', 7.349e22, 0., 0.) 

listOfBodies = [Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, Moon]
Sol_System = Solar_System(listOfBodies)

""" Using the initial values, all of the variables of a body can be predicted for given times using deltaT as the time step for
N number of steps to create a simulation of our Solar System..
"""

time = 0
deltaT = 0
Data2 = [] 
N = 1
for i in range(0,N):
    time = time + i*deltaT
    Sol_System.accelerations()
    Sol_System.update_bodies_v_and_x(deltaT)
    Sol_System.update_K()
    Sol_System.update_momentum()
    initial_VE = Sol_System.Virial_Theorem()
    initial_KE = Sol_System.get_K_total()
    initial_p = Sol_System.get_momentums()

""" The data calculated above is the intital values, where previously the acceleration, kinetic energy, and momentum for the bodies in the system
were set to be zero. This also creates values for the initial kinetic energy of the system, the initial momentum of the system, and the initial Virial 
Theorem energy, which can then be used to calculate the fractional change of kinetic energy of the system, the fractional change of the momentum
of the system, and the fraction change of the Virial Theorem energy, which is done on line 63 as the 17th, 15th, and 13th items in the list, item, respectively.
"""

time = 0
deltaT = 86400
Data = [] 
N = 100000
for i in range(0,N):
    time = time + i*deltaT
    Sol_System.accelerations()
    Sol_System.update_bodies_v_and_x(deltaT)
    Sol_System.update_K()
    Sol_System.update_momentum()
    print("Time: %6.3f, %s"%(time, Sun.position))
    item = [ time, copy.deepcopy(Sun), copy.deepcopy(Mercury), copy.deepcopy(Venus), copy.deepcopy(Earth), copy.deepcopy(Mars), copy.deepcopy(Jupiter), copy.deepcopy(Saturn), copy.deepcopy(Uranus), copy.deepcopy(Neptune), copy.deepcopy(Pluto), copy.deepcopy(Moon), copy.deepcopy(Sol_System.Virial_Theorem()), copy.deepcopy(np.abs(1-(1/initial_VE)*Sol_System.Virial_Theorem())), copy.deepcopy(Sol_System.get_momentums()), copy.deepcopy(np.abs(1-(1/initial_p)*Sol_System.get_momentums())) , copy.deepcopy(Sol_System.get_K_total()), copy.deepcopy(np.abs(1-(1/initial_KE)*Sol_System.get_K_total()))]
    Data.append(item) 
np.save("Bodies_deltaT_1day",Data)
""" The data produced here uses a large number of steps and initial values created in the loop before that ends on line 44. It calls 
the methods from the class Solar_System in the correct order so that the values of the variables calculated use the variables calculated before the time step"""


