import mcu
mymcu = mcu.VASP()
mymcu.plot_band(spin=0, save=True, klabel='M-G-X-M', fontsize= 9, ylim=(-3,3), figsize=(3,3), dpi=300, format='png')
