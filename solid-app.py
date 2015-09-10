"""
Author: vorcil
Repo: http://github.com/vorcil/mcorpc-nuclear
Note: Framework for solidstate app

Purpose: Provide a banal framework to explore the exotic properties of solids,
to delve into the microscopic properties of mostly crystalline solids in raybanal crossectional analysis
"""
import math
#Crystalline solids are materials with an atomic structure based on a repeated pattern (i.e. a regular and dense assembly of atoms very close together) something easily exploited with computational methods in computer science

#opposing to the particle physics modules included within the mcorpc repository, i.e. unfocusing on computational analysis of singularities and focus on general summation of "blocks" or "collections" of particles, can average quantities and utilize smaller sized variables (in terms of memory e.g not 10^-30 ~ 100-500)

def motivation():
    #user interface message
    technological_motivation="Solid State Physics is right at the heart of the majority of modern society and technology. The entire computer and electronics industry relies on the semiconductor. Solid State Physics is traditionally linked to materials science, chemistry & engineering but also recently overlaps with ibology, biochemistry, biotechnology & medicine."

    #user interface message2
    fundamental_motivation="The original motivation to study Solid State Physics is that the fundamental physics needed ot understand the microscopic properties of solids is very stimulating. To understand these properties, the ideas and methods of quantum mechanics had to be developed. The physics of solids is very deeply quantum mechanical."

#define the tri circular arrangement
def bound_SS():
    #link all three arrangements
    SS1="Experimental observations and theoretical development"
    SS2="Fundamental Properties"
    SS3="Devices, Nano-technology and fabrication"

#define eye sensitivity function
def eye_sensitivity():
    #user response
    m1="Photopic curve, eye sensitivity function, shows the eye's response to different wavelengths of light"
    m2="The eye's sensitivity is maximum at 555nm (Yellowish-green) and by definition is 683 lm/W"
    m3="Luminous power (or luminous flux) in lumen represents the pwoer of al imuniuos source (in watt) weighted to match the eye response of the standard observer"

def lumen():
    #at 555nm
    w555="683.0 LUMENS"
    #at 480nm
    w480="63.0 LUMENS"
    #colour rendering index
    #On a scale of 1-100 that measures a light source's ability to render/reproduce
    #the colours of various objects faithfully in comparison with an
    #ideal or natural light source (often the sunlight)
    CRI={};
    for i in range(1,100):
        CRI[i]=i;
        print CRI[i];
        
def temperature():
    #a way to think of the oclour temperature is how warm or cool/cold the light is
    #another way is the blackbody radiator; wavelength of the emitted radiation decreases when the temperature increases
    
    #human perception in kelvin, decending order of "yellowish" warmth
    light_warm1=2700
    light_warm2=3200
    light_cold2=4500
    light_cold1=6000 

#calculating the merit of LED properties
def LEDmerit(emit,inject,active):
    #number of photons that come out of LED per second - set in console
    n_emission=emit
    #number of electrons injected to LED per second - set in console
    n_injection=inject
    #external quantum efficency
    n_external=n_emission/n_injection
    #number of photons emitted from active region per second - set in console
    n_active=active
    #ninternal defines the structural quality of materials and interfaces
    n_internal=n_active/n_injection
    #nextraction defines the packaging architecture
    n_extraction=n_emission/n_active

#energy efficent lighting function - set in console
 def EEL(emit,inject,power_optical,current,voltage):
    #same as above but for non-diodal sources
    n_emission=emit
    n_injection=inject
    n_external=n_emission/n_injection

    #power efficency of source
    n_power=power_optical.(current*voltage)
    
#trasmission photons from light escape cone
#console is able to rearange/switch n1/n2theta1/theta2 via the switch argument
#switch(photon_extraction(...);
def photon_extraction(n1,n2,theta1,theta2,n_sc):
    #snell-descarteslaw n1*math.sin(theta1)=n2*math.sin(theta2)
    theta1=(n2/n1)*math.sin(theta2)
    #critical angle of extraction
    thetac=math.arcsin(1/n_sc)*n_sc # should be approx 25degrees for LED
    n_extraction=(1-math.sin(thetac))/(2) #should be approx 5% for LED

#set properties under console->semi-conductor->properties
def properties(conductivity,resistivity,dq,dt,vd,A):
    #electrical conductivity
    conduct=conductivity
    #electrical resistivity
    resist=resistivity
    #current, delta Q being the change in charge per change in time delta T
    I=dq/dt
    #in average time delta T charge carriers move an average distance
    avex=vd*dt
    #current density per unit area - incoincidentally = nAeVd/A = neVd = sigmaE
    J=I/A

#exploration function for relation between electrical and thermal conductivity
def wiedemannFranzLaw(K,sigma,T,Na,Kb):
    #derivation of the charge resistance per K^2 per second
    charge_resistance=K/(sigma*T);
    #basic heat capacity - per mol
    Cmol=3*Na*Kb;
    #kb the boltzman constant, Na avagadros number
    #material heat capacity
    C=3*Na*Kb#===(dU/dT)
    #experimental behaviour predicts the dulong-petit observation
    
    
    

        
    

    
