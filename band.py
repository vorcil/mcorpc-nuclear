"""
Author: Vorcil
Repo: http://github.com/vorcil/mcorpc-nuclear
Note: Framework for band structure and energy derivations
"""
import math
#The fermi level is an existential bandgap for both semiconductors and insulators
#In short the semiconductor is an insulator, with a smaller bandgap;

#dictionary of energy level increases - direct proportionality to number of electrons
max_electrons={};
def energyCalc():
    #arbitrary range, but must make sure the quantized state exists
    #as a basic example with 5 levels, could potentially alter to include range as argument
    for i in range(1,5):
        max_electrons[i]=2*math.pow(i,2)
        print max_electrons[i]
        
#energy levels in an isolated atom has those same states
def config():
    #depending on which orbital they are in they share particular energies
    config1="1s^2"
    config2="2s^2"
    config3="2p^6"
    config4="3s^1"#as an example this continues

    #A more qualitative approach to the functionality of the object
    #increasing the number of atoms the allowed energy states in the atoms
    #will begin to broaden into bands as atoms are pushed together
    #as required by the Pauli principle
    #band splitting disallows the electrons to be at the same energy and place
    
