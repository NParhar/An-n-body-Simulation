from Particle import Particle
import matplotlib.pyplot as plt 
import math
import numpy as np 
""" this plots GRAPHS OF SOLAR SYSTEM"""
data = np.load("Bodies_deltaT_1day.npy")
Time = []
x_Mercury = []
y_Mercury = []
x_Venus = []
y_Venus = []
x_Earth = []
y_Earth = []   
x_Mars = []
y_Mars = []
x_Jupiter = []
y_Jupiter = []   
x_Saturn = []
y_Saturn = []
x_Uranus = []
y_Uranus = []
x_Neptune = []
y_Neptune = []   
x_Pluto= []
y_Pluto = []
x_Moon = []
y_Moon = []
x_Sun = []
y_Sun = []

p_Sun = []
p_Mercury = []
p_Venus = []
p_Earth = []
p_Mars = []
p_Jupiter = []   
p_Saturn = []
p_Uranus = []
p_Neptune = []
p_Pluto = [] 
p_Moon = []   
p_total = []
p_frac = []

k_Sun = []
k_Mercury = []
k_Venus = []
k_Earth = []
k_Mars = []
k_Jupiter = []   
k_Saturn = []
k_Uranus = []
k_Neptune = []
k_Pluto = [] 
k_Moon = []
k_total = []
k_frac = []

VE = []
VE_frac = []

for line in data:
    time = line[0]
    Sun = line[1]
    Mercury = line[2]
    Venus = line[3]
    Earth = line[4]
    Mars = line[5]
    Moon = line[11]
    Jupiter = line[6]
    Saturn = line[7]
    Uranus = line[8]
    Neptune = line[9]
    Pluto = line[10]
    p_sys = line[14]    
    VEn = line[12]
    VEn_frac = line[13]
    k_sys = line [16]
    p_sys_frac = line[15]
    k_sys_frac = line[17]

    Time.append(time)
    x_Sun.append(Sun.position[0])
    y_Sun.append(Sun.position[1])
    x_Mercury.append(Mercury.position[0])
    y_Mercury.append(Mercury.position[1])
    x_Venus.append(Venus.position[0])
    y_Venus.append(Venus.position[1])
    x_Earth.append(Earth.position[0])
    y_Earth.append(Earth.position[1])
    x_Mars.append(Mars.position[0])
    y_Mars.append(Mars.position[1])
    x_Moon.append(Moon.position[0])
    y_Moon.append(Moon.position[1])
    x_Jupiter.append(Jupiter.position[0])
    y_Jupiter.append(Jupiter.position[1])
    x_Saturn.append(Saturn.position[0])
    y_Saturn.append(Saturn.position[1])
    x_Uranus.append(Uranus.position[0])
    y_Uranus.append(Uranus.position[1])
    x_Neptune.append(Neptune.position[0])
    y_Neptune.append(Neptune.position[1])
    x_Pluto.append(Pluto.position[0])
    y_Pluto.append(Pluto.position[1])   

    p_Sun.append(Sun.Momentum)
    p_Mercury.append(Mercury.Momentum)
    p_Venus.append(Venus.Momentum)
    p_Earth.append(Earth.Momentum)
    p_Mars.append(Mars.Momentum)
    p_Jupiter.append(Jupiter.Momentum)
    p_Saturn.append(Saturn.Momentum)
    p_Uranus.append(Uranus.Momentum)
    p_Neptune.append(Neptune.Momentum)
    p_Pluto.append(Pluto.Momentum)
    p_Moon.append(Moon.Momentum)
    p_total.append(p_sys) 
    p_frac.append(p_sys_frac)

    k_Sun.append(Sun.KinE)
    k_Mercury.append(Mercury.KinE)
    k_Venus.append(Venus.KinE)
    k_Earth.append(Earth.KinE)
    k_Mars.append(Mars.KinE)
    k_Jupiter.append(Jupiter.KinE)
    k_Saturn.append(Saturn.KinE)
    k_Uranus.append(Uranus.KinE)
    k_Neptune.append(Neptune.KinE)
    k_Pluto.append(Pluto.KinE)
    k_Moon.append(Moon.KinE) 
    k_total.append(k_sys)
    k_frac.append(k_sys_frac)

    VE.append(VEn)
    VE_frac.append(VEn_frac)
     
plt.plot(x_Sun,y_Sun,'r.', label='Sun orbit')
plt.plot(x_Mercury,y_Mercury,'b--', label='Mercury orbit')
plt.plot(x_Venus,y_Venus,'m--', label='Venus orbit')
plt.plot(x_Earth,y_Earth,'g.', label='Earth orbit')
plt.plot(x_Moon,y_Moon,'k--', label='Moon orbit')
plt.plot(x_Mars,y_Mars,'r--', label='Mars orbit')
plt.plot(x_Jupiter,y_Jupiter,'y--', label='Jupiter orbit')
plt.plot(x_Saturn,y_Saturn,'c--', label='Saturn orbit')
plt.plot(x_Uranus,y_Uranus,'m-', label='Uranus orbit')
plt.plot(x_Neptune,y_Neptune,'g-', label='Neptune orbit')
plt.plot(x_Pluto,y_Pluto,'k-', label='Pluto orbit')
plt.xlabel('x-position (m)', fontsize=18)
plt.ylabel('y-position (m)', fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(bbox_to_anchor=(1.05, 1), fontsize=16, loc=2, borderaxespad=0.)
plt.show()

plt.plot(Time,p_Sun,'r-', label='Sun')
plt.plot(Time,p_Mercury,'b--', label='Mercury')
plt.plot(Time,p_Venus,'m--', label='Venus')
plt.plot(Time,p_Earth,'g--', label='Earth')
plt.plot(Time,p_Moon,'k--', label='Moon')
plt.plot(Time,p_Mars,'r--', label='Mars')
plt.plot(Time,p_Jupiter,'y--', label='Jupiter')
plt.plot(Time,p_Saturn,'c--', label='Saturn')
plt.plot(Time,p_Uranus,'m-', label='Uranus')
plt.plot(Time,p_Neptune,'g-', label='Neptune')
plt.plot(Time,p_Pluto,'b-', label='Pluto')
plt.xlabel('Time (s)', fontsize=18)
plt.ylabel('Magntiude of Momentum (kgm/s)', fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(bbox_to_anchor=(1.05, 1),fontsize=16, loc=2, borderaxespad=0.)
plt.show()

plt.plot(Time,p_total,'b-', label='system')
plt.xlabel('Time (s)', fontsize=18)
plt.ylabel('Magntiude of Momentum of the System (kgm/s)', fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(bbox_to_anchor=(1.05, 1),fontsize=16, loc=2, borderaxespad=0.)
plt.show()

plt.plot(Time,p_frac,'g-', label='system')
plt.xlabel('Time (s)', fontsize=18)
plt.ylabel('Fractional Change of Magntiude of Momentum of the System', fontsize=15)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(bbox_to_anchor=(1.05, 1),fontsize=16, loc=2, borderaxespad=0.)
plt.show()

plt.plot(Time,k_Sun,'r-', label='Sun')
plt.plot(Time,k_Mercury,'b--', label='Mercury')
plt.plot(Time,k_Venus,'m--', label='Venus')
plt.plot(Time,k_Earth,'g--', label='Earth')
plt.plot(Time,k_Moon,'k--', label='Moon')
plt.plot(Time,k_Mars,'r--', label='Mars')
plt.plot(Time,k_Jupiter,'y-', label='Jupiter')
plt.plot(Time,k_Saturn,'c--', label='Saturn')
plt.plot(Time,k_Uranus,'m-', label='Uranus')
plt.plot(Time,k_Neptune,'g-', label='Neptune')
plt.plot(Time,k_Pluto,'b-', label='Pluto')
plt.xlabel('Time (s)',fontsize=18)
plt.ylabel('Kinetic Energy (J)',fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(bbox_to_anchor=(1.05, 1),fontsize=16, loc=2, borderaxespad=0.)
plt.show()

plt.plot(Time,k_total,'b-', label='system')
plt.xlabel('Time (s)',fontsize=18)
plt.ylabel('Kinetic Energy of the System (J)',fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(bbox_to_anchor=(1.05, 1),fontsize=16, loc=2, borderaxespad=0.)
plt.show()

plt.plot(Time,k_frac,'g-', label='system')
plt.xlabel('Time (s)',fontsize=18)
plt.ylabel('Fractional Change of Kinetic Energy of the System ',fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(bbox_to_anchor=(1.05, 1),fontsize=16, loc=2, borderaxespad=0.)
plt.show()

plt.plot(Time, VE,'b-', label='System')
plt.xlabel('Time (s)',fontsize=18)
plt.ylabel('Virial Theorem Energy (J)',fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(bbox_to_anchor=(1.05, 1),fontsize=16, loc=2, borderaxespad=0.)
plt.show()

plt.plot(Time, VE_frac,'r-', label='System')
plt.xlabel('Time (s)',fontsize=18)
plt.ylabel('Fractional Virial Theorem Energy',fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(bbox_to_anchor=(1.05, 1),fontsize=16, loc=2, borderaxespad=0.)
plt.show()

""" this plots GRAPHS OF INNER PLANETS"""
data = np.load("Bodies_deltaT_10smaller.npy")
Time = []
x_Mercury = []
y_Mercury = []
x_Venus = []
y_Venus = []
x_Earth = []
y_Earth = []   
x_Mars = []
y_Mars = []
x_Moon = []
y_Moon = []
x_Sun = []
y_Sun = []
for line in data:
    Sun = line[1]
    Mercury = line[2]
    Venus = line[3]
    Earth = line[4]
    Mars = line[5]
    Moon = line[11]        
    x_Sun.append(Sun.position[0])
    y_Sun.append(Sun.position[1])
    x_Mercury.append(Mercury.position[0])
    y_Mercury.append(Mercury.position[1])
    x_Venus.append(Venus.position[0])
    y_Venus.append(Venus.position[1])
    x_Earth.append(Earth.position[0])
    y_Earth.append(Earth.position[1])
    x_Mars.append(Mars.position[0])
    y_Mars.append(Mars.position[1])
    x_Moon.append(Moon.position[0])
    y_Moon.append(Moon.position[1])         
plt.plot(x_Sun,y_Sun,'r.', label='Sun orbit')
plt.plot(x_Mercury,y_Mercury,'b--', label='Mercury orbit')
plt.plot(x_Venus,y_Venus,'m--', label='Venus orbit')
plt.plot(x_Earth,y_Earth,'g.', label='Earth orbit')
plt.plot(x_Moon,y_Moon,'k--', label='Moon orbit')
plt.plot(x_Mars,y_Mars,'c-', label='Mars orbit')
plt.xlabel('x-position (m)', fontsize=18)
plt.ylabel('y-position (m)', fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(bbox_to_anchor=(1.05, 1), fontsize=16, loc=2, borderaxespad=0.)
plt.show()

data = np.load("Bodies_deltaT_10larger.npy")
x_Mercury = []
y_Mercury = []
x_Venus = []
y_Venus = []
x_Earth = []
y_Earth = []   
x_Mars = []
y_Mars = []
x_Moon = []
y_Moon = []
x_Sun = []
y_Sun = []
for line in data:
    Sun = line[1]
    Mercury = line[2]
    Venus = line[3]
    Earth = line[4]
    Mars = line[5]
    Moon = line[11]        
    x_Sun.append(Sun.position[0])
    y_Sun.append(Sun.position[1])
    x_Mercury.append(Mercury.position[0])
    y_Mercury.append(Mercury.position[1])
    x_Venus.append(Venus.position[0])
    y_Venus.append(Venus.position[1])
    x_Earth.append(Earth.position[0])
    y_Earth.append(Earth.position[1])
    x_Mars.append(Mars.position[0])
    y_Mars.append(Mars.position[1])
    x_Moon.append(Moon.position[0])
    y_Moon.append(Moon.position[1])         
plt.plot(x_Sun,y_Sun,'r.', label='Sun orbit')
plt.plot(x_Mercury,y_Mercury,'b--', label='Mercury orbit')
plt.plot(x_Venus,y_Venus,'m--', label='Venus orbit')
plt.plot(x_Earth,y_Earth,'g.', label='Earth orbit')
plt.plot(x_Moon,y_Moon,'k--', label='Moon orbit')
plt.plot(x_Mars,y_Mars,'c-', label='Mars orbit')
plt.xlabel('x-position (m)', fontsize=18)
plt.ylabel('y-position (m)', fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(bbox_to_anchor=(1.05, 1), fontsize=16, loc=2, borderaxespad=0.)
plt.show()

"""" THis plots DATA FOR THE SUN, EARTH AND MOON"""
data = np.load("Sun_Earth_Moon.npy")
x_Sun= []
y_Sun = []
x_Earth = []
y_Earth = []
x_Moon = []
y_Moon = []   
for line in data:
    Sun = line[1]
    Earth = line[2]
    Moon = line[3]        
    x_Sun.append(Sun.position[0])
    y_Sun.append(Sun.position[1])
    x_Earth.append(Earth.position[0])
    y_Earth.append(Earth.position[1])
    x_Moon.append(Moon.position[0])
    y_Moon.append(Moon.position[1]) 
plt.plot(x_Sun,y_Sun,'r.', label='Sun orbit')
plt.plot(x_Earth,y_Earth, 'g.', label='Earth orbit')
plt.plot(x_Moon,y_Moon,'k--', label='Moon orbit')
plt.xlabel('x-position (m)', fontsize=18)
plt.ylabel('y-position (m)', fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2,  fontsize=16 ,borderaxespad=0.)
plt.show()