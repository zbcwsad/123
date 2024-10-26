import mcu
mymcu = mcu.VASP()
label = 'M-G-X-M'
mymcu.plot_pband(lm=['V:d','W:d'], color=['#00ccff','#ff0000'], alpha=0.3, klabel=label, fontsize= 9, ylim=(-1.5,1.5),figsize=(4,3),legend=['V:d','W:d'],legend_size=1, save=True, figname='pband', dpi=300)
