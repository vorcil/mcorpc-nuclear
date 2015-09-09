"""
Author: vorcil
Repo: http://github.com/vorcil/mcorpc-nuclear
Note: Dimensional analysis of fundamental particles
"""
import math


#1.6*10^-19 couloumbs passed per singular volt
eV = 1.6 * (math.expm1(1e-19)) #insert basic atomic energy unit
unit_eV = "J" #assign the basic unit of joules

"""
Function which sets out the nuclear-zoo
mass, charge, spin angular momentum, composite particle and stability
"""

#global dictionary to handle nuclear-zoo
particle_attribute={};
def particle(name,mass,charge,spin,composite,stability):
    
    particle_attribute[name+'mass']=mass
    particle_attribute[name+'charge']=charge
    particle_attribute[name+'spin']=spin
    particle_attribute[name+'composite']=composite
    particle_attribute[name+'stability']=stability
       
#setup for reference
particle("Proton",'10^3MeV','+e','1/2hbar-fermion','uud','stable')
particle("Neutron",'10^3MeV','zero','1/2hbar-fermion','udd','unstable')
particle("Electron",'0.55MeV','e-','1/2hbar-fermion','null','stable')
particle("Positron", '0.55MeV','+e','1/2hbar-fermion','null','stable')
particle("Alpha",'4GeV','+2e','null','strong-bound','null')

#test access code:
#print particle_attribute["Neutroncharge"]

"""
Function setting a set of elements
name, p oribital, n oribital
"""

#global dictionary to handle list of test elements
element_attribute={};
def element(name,porb,norb):

    element_attribute[name+'porb']=porb
    element_attribute[name+'norb']=norb

#setup for reference
element("Hydrogen",'1','1')
element("Deuterium-iso",'2','1')
element("Helium-iso",'2','2')
element("Carbon-iso",'6','6')
element("Oxygen-iso",'8','8')

#test access code:
#print element_attribute["Hydrogennorb"]
#porb+norb=total number of nucleons
#norb=totalnumber of protons, neutrons is the diff as in A Z X format
#iso tag defines element isotope status






