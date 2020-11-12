from Particle import Particle 
import math
import numpy as np 

class Solar_System: 
    """ This class, named Solar_System, uses the Particle class to form a structure of n-bodies to simulate our Solar System 
    where the variables of each object (a body in the system) can be updated and other quantities calculated for a given time.
    """
    deltaT=1
    bodies = []
    def __init__(self, listOfBodies):
        """ This constructs an object that conatins a list of bodies."""
        self.bodies = listOfBodies

    def accelerations(self):   
        """ This calculates the acceleration for each body in the list of bodies.
        It uses two loops so that the acceleration calculated for a body is the summation of all of the accelerations 
        between itself and all of the other bodies excluding itself.
        """
        for body1 in self.bodies:
            myAcc = np.array([0.,0.,0.])
            for body2 in self.bodies:
                if body2 != body1:
                    G = 6.67e-11
                    m = body2.mass
                    r = body1.position - body2.position
                    r_mag = np.linalg.norm(r)
                    newAcc = ((-G*m*r)/(r_mag**3))
                    myAcc += newAcc
            body1.acceleration = myAcc
         
    def update_bodies_v_and_x(self,deltaT):
        """ This method updates the velocity and position variables of a body using the Euler-Cromer approximations from the Particle class when called."""
        for body in self.bodies:  
            body.update_v_and_x(deltaT)

    def update_K(self):
        """ This method updates the kinetic energy variable of a body in the list using the method from the Particel class when called."""
        for body in self.bodies:  
            body.update_KE()

    def get_PE(self):
        """ This method calculates the total potential energy of the system by adding up the potential energies of each body in the list when called."""
        for body1 in self.bodies:
            myPotenitalE = 0.
            for body2 in self.bodies:
                if body2 != body1:
                        G = 6.67e-11
                        m = body2.mass
                        m_i = body1.mass
                        r = body1.position - body2.position
                        r_mag = np.linalg.norm(r)
                        newPotentialE = (G*m*m_i)/(r_mag)
                        myPotenitalE += newPotentialE
            return myPotenitalE         

    def get_K_total(self):
        """ This method calculates the total kinetic energy of the system by adding up the individual kinetic energies of the bodies in the list of bodies when called."""
        myKinE = 0.
        for body1 in self.bodies:            
            myKinE += body1.KinE
        return myKinE         

    def update_momentum(self):
        """ This method updates the momentum variable for each body in the list using the method which calcuates the momentum of a body from the Particle class when called."""
        for body in self.bodies:  
            body.update_p()

    def get_momentums(self):
        """ This method calculates the total momentum of the system by adding up the individual momentums of each body in the list of bodies when called  and will only work if update_momentum is also called."""
        mymomentums = 0.
        for body1 in self.bodies:            
            mymomentums += body1.Momentum
        return mymomentums     

    def Virial_Theorem(self): 
        """ This method calculates the Virial Theorem energy of the sysytem when called. The get_K_total() and get_PE() must also be called for this to work."""
        self.update_K()
        VE = 2.*(self.get_K_total()) - self.get_PE() 
        return VE

