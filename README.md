# An-n-body-Simulation
Written in Python code, this project contains the files used to simulate an ‘n –body’ system evolving over time, acting under the influence of gravity. Data used is from the Horizons data base (at the time of creation) to model the kinematics and dynamics of the solar system. This project was created for the module 'Scientific Programming and Modelling Project' (PHYS281) at Lancaster University.

Particle.py contains a class called Particle which forms the basic structure of the bodies used to simulate how bodies in a gravitational system interact.

Solar_System contains a class called Solar_System which contains methods that can be used to update the variables of an object from a list.

Simulation uses the two classes created in combination with loops to update the variables at a given time, and it also saves the data as an .npy file.

Analysis uses the .npy file created to plot graphs.

How to run:
1. Choose the bodies to plot by adding or removing them from the list on line 25 in the Simulation file by running the Simulationfile in the terminal.
2. Open the Analysis file, change the file's name that is being loaded to the appropriate file and then edit which plt. lines to and run the Analysis file in the
   terminal to produce graphs.
