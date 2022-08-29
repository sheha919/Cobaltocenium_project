import numpy as np

#define the names of substitient groups
der=['x_name','y_name']

h_charge=np.empty(len(der))

for i in range(len(der)):
        file=open(str(der[i]+'.out'), "r") #open output file from the Hirshfeld charge calculation
        data=file.readlines()
        for indx,line in enumerate(data):
                if 'Hirshfeld Atomic Charges' in line:
                        d=indx
        file.close()
        h=0.0
        file=open(str(der[i]+'.out'), "r") #open output file from the Hirshfeld charge calculation
        data=file.readlines()
        for indx, line in enumerate(data):
                if indx>=d+4:
                        if indx<d+15:
                                h=h+float(line.split()[2]) #calculating sum of H charge on C6H5 ring
        file.close()
        h_charge[i]=h

hcharge_file=open('hcharge.dat',"w")
for i in range(len(der)):
        hcharge_file.write(der[i]+ '   ' +str(h_charge[i])+'\n')
hcharge_file.close()