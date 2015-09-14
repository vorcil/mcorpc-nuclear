"""
Author: vorcil
Repo: http://github.com/vorcil/mcorpc-nuclear
Desc: Phenomenology of superconduits
Location: Robinson Research Institute
"""

"""
Vision parameters

Check state arision:
Check material range:
Check technological super conductors:
Check origin: T_c, H_c, J_D -> counterparts H_irr, J_c
Check parameters: Eta, Lambda,
Check type: Differences type I, type II
Check applications:
Check cooling:
Check losses:
Check limitations:
Check Stabilisation:
"""

#build user query
def query():
    message1="Impurities dominate resistance constant"
    message2="Thermal vibration cease when resistance drops to zero"
    message3="Electron gas freezes when there's zero conductivity"
    message4="liquefaction of helium allows attainment of low temperatures"
    
#properties to intialize super conductor resonance
def conductivity(default):
    #default resistivity - set in console - default is 10^-26 ohm
    resistivity=default
    #n.b strange that the default is approximately 18 orders of magnitude lower than the resistivity of copper

    #a hypothetical perfect conductor would exclude flux

def diamagnetism(water,bismuth,pyrolytic):
    reminder="A diamagnet opposes an applied magnetic field. Has negative magnetic susceptibility, (chi) x = M/H"

    #Want to set super parameter la levitation magnetique
    #cancel with the entire body - parameter list
    chi_water=water; #usually -9.1*10^-6
    chi_bismuth=-1.7*10^-4
    chi_pyrolytic=-4.1*10^-4
    chi_superconductor=-1 #at least theoretically
    
    #pulled from spotaneous circulating supercurrent Bapp
    m_0="null" #super reference to application default
    #applied field around the super current
    B=m_0*(H+M)
    
def diamag_outside(Happ,M,M_0):
    #outside the super conductor
    M=0
    Bapp=M_0*Happ
    
def diamag_inside(M,H):
    #inside the super conductor
    chi=M/H#=1
    M=-1*H
    B=0;

