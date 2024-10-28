import pyprocar
####获取K点信息####

data_dir='./band-pyprocar'
parser = pyprocar.io.Parser(code = 'vasp', dir=data_dir)
kpath = parser.kpath
ebs = parser.ebs
kpath = ebs.kpath

pyprocar.bandsplot(dirname = data_dir,mode = 'plain', code = 'vasp',fermi=-2.8228,elimit=[-2.0,1.5],savefig='band-pyprocar.png')

