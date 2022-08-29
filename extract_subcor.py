import numpy as np

d=np.empty(4)

#define new derivatives
der=['x_name','y_name']


energy=np.empty(len(der))
dipole=np.empty(len(der))
homo=np.empty(len(der))
lumo=np.empty(len(der))


for i in range(len(der)):
	file=open(str('insert_path'+der[i]+'.xyz'), "r") #path to outputfile of mono-substituted cocp2oh deraivative
	write_file=open(str(der[i]+'.xyz'),'w')
	data=file.readlines()
	for indx,line in enumerate(data):
		if indx>21:
			write_file.write(line)
	write_file.close()
	file.close()

