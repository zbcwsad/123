import pyprocar
####获取K点信息####
####普通的能带图####
###fermi能级需要手动修改，data_dir是能带计算目录，需计算完######
###elimit是能量范围，即Y轴范围###
data_dir='./band-pyprocar'
parser = pyprocar.io.Parser(code = 'vasp', dir=data_dir)
kpath = parser.kpath
ebs = parser.ebs
kpath = ebs.kpath

pyprocar.bandsplot(dirname = data_dir,mode = 'plain', code = 'vasp',fermi=-2.8228,elimit=[-2.0,1.5],savefig='band-pyprocar.png')

