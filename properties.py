"""
Author: vorcil
Repo: http://github.com/vorcil/mcorpc-nuclear
Note: Conglamatory of semiconductor property methods
"""
import math

#console message for user 
intro_message="The existance of the band gap for a semiconductor means that the absorption of light by a slab of the semiconductor depends very much on the frequency or wavelength of the light: Photons with an energy less than the band gap will not be absorbed as there are no electronic energy levels available in the gap, as indicated schematically in /bin.

 For photons with an energy h.v greater than the gap, absorption is possible through the excitation of an electron in the valence band to an empty level in the conduction band at an energy h.v above the filled level."

#We measure the absorption through the absorption coefficent alpha defined by the following relationship
def absorption(l0,l,x):
    # l0 is the incident light intensity
    # l is the transmitted light intensity
    # x is the thickness of the material
    #Note that this ignores the small loss of intensity due to reflections at the two air-material interface.
    #the absorption coefficent 
    alpha=math.log1p(l0/l)/x
    
"""
theory shows that the absorption coefficient varies with energy in the following way;

alpha = alpha_d sqrt(hbar omega - E_g) for direct gap materials
alpha = alpha_i (hbar omega - E_g)^2 for indirect gap materials
Where E_g is the band gap energy and hbar omega is the photon energy.

The proportional test is to utilize an optical spectrometer system;

The jobin-Yvon monochromator disperses incident white light into it's component wavelengths with a diffraction grating. The grating is rotated to select the wavelength which is trasmitted and the counter attached to the rotation knob mechanism indicating the wavelength.

With the 300 lines/mm grating currently installed, the counter reading should be multiplied by 4 to give the wavelength. The range of wavelengths which is trasmitted  ("the bandpass") is given by the slit-width x 16nm/mm for this grating. The detector is a sandwich composite of two detectors, the front one is a silicon pin diode, whereas the rear one is lead sulphide.

The silicon detector generates a photo current prportional to the light intensity falling on it for incident light above the band gap energy of silicon of around 1.1eV for light below this energy, the light falls on the lead sulphide detector.
"""

#operation installation
"""
Spectrometer Calibration:
The counter reading is close to 1/4 the wavelength for first order diffraction, but the relationship is not exact.
------------------------------------------------------------------------------"""
#Calibrate the monochromator counter reading in terms of wavelength with a helium neon laser.
"""
The monochromator will pass He-Ne laser light (wavelength 632.8nm) in zeroth, 1st, second, third, fourth order etc."""

#Check that the entrance and exit slits are the 0.5mm width ones, and use the maximum slit height possible.

#Gently remove the monochromator from its location on the wooden base and put it flat on a surface.

#Organize the laser to be straddling the height-correction, pointing directly into the slit entrance of the monochromator and along the axis

#Put a piece of paper at the exit slit and rotate the grating until you see the 1st order diffraction at ~ 633/4nm.

#Repeat for the other orders, including the zeroth. (The second order response is equivalent to incident light of wavelength 2*(632.8nm) ect)




