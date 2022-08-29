import numpy as np

d=np.empty(4)

#define the names of substituents
der=['x_name','y_name']


energy=np.empty(len(der))
dipole=np.empty(len(der))
homo=np.empty(len(der))
lumo=np.empty(len(der))


for i in range(len(der)):
        file=open(str('frag_output'+der[i]+'.out'), "r")    #open the fragment output file (change "'frag_output'+der[i]+'.out'" accordingly)
        data=file.readlines()
        for indx,line in enumerate(data):
                if 'Final energy is' in line:
                        energy[i]=(line.split()[3])
                if 'OPTIMIZATION CONVERGED' in line:
                        d[0]=indx
                if 'Z-matrix' in line:
                        d[1]=indx
                if '-- Virtual --' in line:
                        d[2]=indx
                if 'Archival summary' in line:
                        d[3]=indx
        file.close()

        file=open(str('frag_output'+der[i]+'.out'), "r")     #open the fragment output file (change "'frag_output'+der[i]+'.out'" accordingly)
        data=file.readlines()
        write_file=open(str(der[i]+'.xyz'), "w")
        for indx, line in enumerate(data):
                if indx>=d[0]+5:
                        if indx<d[1]:
                                write_file.write(line)
                if indx==d[2]-1:
                        homo[i]=(line.split()[-1])
                if indx==d[2]+1:
                        lumo[i]=line.split()[0]
                if indx>=d[3]-16:
                        if indx<d[3]:
                                if 'Tot' in line:
                                        dipole[i]=(line.split()[1])
        write_file.close()
        file.close()

energy_file=open('frag.dat', "w")
dipole_file=open('frag_dipole.dat',"w")
homo_file=open('frag_homo.dat',"w")
lumo_file=open('frag_lumo.dat',"w")
for i in range(len(der)):
	energy_file.write(der[i]+ '   ' +str(energy[i])+'\n')
	dipole_file.write(der[i]+ '   ' +str(dipole[i])+'\n')
	homo_file.write(der[i]+ '   ' +str(homo[i])+'\n')
	lumo_file.write(der[i]+ '   ' +str(lumo[i])+'\n')
energy_file.close()
dipole_file.close()
homo_file.close()
lumo_file.close()
