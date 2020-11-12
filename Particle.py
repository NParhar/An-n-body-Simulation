import numpy
class Particle:
    """ This class, named Particle, forms the structure used to hold the information about the bodies used in the system (Sol_System) that is modelled to
    be our Solar System. The structure for each body specifies the position, velocity, acceleration, mass, name, kinetic energy and momentum.    
    """
    position=numpy.array([0.,0.,0.])
    velocity=numpy.array([0.,0.,0.])
    acceleration=numpy.array([0.,0.,0.])
    mass=0.
    Name='Particle_default'
    KinE=0.
    Momentum=0.

    def __init__(self, initialPosition, initialVelocity, initialAcceleration, Name, mass, kinetic_energy, momentum):
        """ This allows an object representing a body in the system to be constructed.
        Each object has 7 key variables: position, velocity, acceleration, mass, name, kinetic energy and momentum. 
        """
        self.position=initialPosition
        self.velocity=initialVelocity
        self.acceleration=initialAcceleration
        self.Name=Name
        self.mass=mass
        self.KinE=kinetic_energy    
        self.Momentum=momentum

    def __repr__(self):
        return 'Particle: %10s, Mass: %.5e, Position: %s, Velocity: %s, Acceleration:%s'%(self.Name,self.mass,self.position, self.velocity,self.acceleration)

    def update_v_and_x(self, deltaT):
        #update(deltaT) is then used to update each body's velocity and position
        """ This method uses Euler-Cromer approximation so that the velocity and position of a body in the system can be updated depending on the arguement, deltaT. """
        self.velocity= self.velocity + self.acceleration*deltaT
        self.position= self.position + self.velocity*deltaT

    def update_KE(self):
        """ This method calculates KinE, the variable that represent the kinetic energy of a body when called to do so. It depends on 2 variables: mass and velocity."""
        self.KinE = 0.5*self.mass*numpy.dot(self.velocity,self.velocity)

    def update_p(self):
        """ This method calculates Momentum, the variable that represent the momentum of a body when called to do so. It depends on 2 variables: mass and velocity."""
        self.Momentum = self.mass*numpy.linalg.norm(self.velocity)
    
    


  
    

       
       
