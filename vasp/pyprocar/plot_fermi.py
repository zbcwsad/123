import pyprocar
###########1.scf#############
###########2.conda activate pyprocar#########
###########3.run#############
pyprocar.fermi2D(code = 'vasp', 
               mode='plain',
               fermi=-2.8067,
               energy=-0.5,
               savefig='fermi.png',
               dirname='./')
