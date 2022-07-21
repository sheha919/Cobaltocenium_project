import os
import numpy as np
import pandas as pd
import math

value=np.empty(2)
def der_energy(i,j,file_name):
        file_x  = open(os.path.join(str(file_name+'.dat')),"r")
        data_x  = file_x.readlines()
        for indx_i,line_i in enumerate(data_x):
               x=line_i.split()[0]
               y=line_i.split()[1]
               if line_i== '\n':
                       indx_i=indx_i+1
               elif x== i:
                       der=x
                       print('function1: '+i+' '+der)
                       value[0]=y
                       print('function2 '+str(value[0])) 
               elif x== j:
                       der=x
                       print('function1: '+j+' '+der)
                       value[1]=y
                       print('function2 '+str(value[1]))
       
        file_x.close()
        return float(value[0]),float(value[1])


d=np.empty(4)
der_data = pd.DataFrame(columns=['Name', 'CoCp2 energy', 'CoCp name','CoCp energy', 'Cp name','Cp energy','BDE', 'Dipole moment', 'CoCp2 HOMO energy', 'CoCp2 LUMO energy', 'CoCp HOMO energy', 'CoCp LUMO energy', 'Cp HOMO energy', 'Cp LUMO energy','CoCp H charge','Cp H charge','CoCp polarizability','Cp polarizability','Hardness','dCOM','rCo-O'])

cocp2_der = np.loadtxt("der.dat", dtype='str')

energy=np.empty(len(cocp2_der))
dipole=np.empty(len(cocp2_der))
homo=np.empty(len(cocp2_der))
lumo=np.empty(len(cocp2_der))
r_com=np.empty(len(cocp2_der))
r=np.empty(len(cocp2_der))

out_path='../out_files/'
xyz_path='../xyz_files'

for i in range(len(cocp2_der)):
	file=open(os.path.join(out_path,cocp2_der[i]+'.out'),"r")
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
		if 'Dipole Moment (Debye)' in line:
			d[3]=indx
	file.close()

	file=open(os.path.join(out_path,cocp2_der[i]+'.out'),"r")
	data=file.readlines()
	write_file=open(os.path.join(xyz_path,cocp2_der[i]+'.xyz'), "w")
	for indx, line in enumerate(data):
		if indx>=d[0]+5:
			if indx<d[1]:
				write_file.write(line)
		if indx==d[2]-1:
			homo[i]=(line.split()[-1])
		if indx==d[2]+1:
			lumo[i]=line.split()[0]
		if indx==d[3]+2:
			dipole[i]=(line.split()[1])
	write_file.close()
	file.close()

der_data['CoCp2 energy'] = energy[:]
der_data['Dipole moment'] = dipole[:]
der_data['CoCp2 HOMO energy'] = homo[:]
der_data['CoCp2 LUMO energy']= lumo[:]
der_data['Hardness']=0.5*(der_data['CoCp2 HOMO energy'] - der_data['CoCp2 LUMO energy'])*627.5

energy_file=open('cocp2.dat', "w")
dipole_file=open('dipole.dat',"w")
homo_file=open('homo.dat',"w")
lumo_file=open('lumo.dat',"w")

for i in range(len(cocp2_der)):
	energy_file.write(cocp2_der[i]+ '   ' +str(energy[i])+'\n')
	dipole_file.write(str(dipole[i])+'\n')
	homo_file.write(str(homo[i])+'\n')
	lumo_file.write(str(lumo[i])+'\n')
energy_file.close()
dipole_file.close()
homo_file.close()
lumo_file.close()


der=['dme','meth','eth','pr2','thl','c6h5','c2h3','c2h','ch3','tch3','c3h7','h','cl','br','f','conhr',
     'conh2','cooch3','coch3','coh','cof','cocl','cf3','ccl3','cbr3','cn','soor','no2','soocf3','ph_p_cl',
     'ph_o_cl','ph_m_cl','ph_o_cf3','ph_m_cf3','ph_p_cf3','ph_p_ch3','ph_p_och3','ph_op_ch3','ph_op_och3',
     'piperidine','paryl2','naryl2']

bde_summary=open(os.path.join('bde_summary.dat'),'w')

num=len(der)

for i in range(num):
    for j in range(i,num):
        k= (num*(num-1)/2)-((num-i)*(num-i-1)/2)+j
        cocp2 = open(os.path.join('cocp2.dat'),"r").readlines()
        for indx,line in enumerate(cocp2):
            if (str('di_cocp2_'+der[i]+'_'+der[j])) in line:
                        cocp2_name=line.split()[0]
                        cocp2_energy=float(line.split()[1])

                        cocp_i,cocp_j=der_energy(der[i],der[j],"cocp")
                        cp_j, cp_i=der_energy(der[j],der[i],"cp")
                        cocp_i_homo,cocp_j_homo=der_energy(der[i],der[j],'cocp_homo')
                        cocp_i_lumo,cocp_j_lumo=der_energy(der[i],der[j],'cocp_lumo')
                        cp_j_homo,cp_i_homo=der_energy(der[j],der[i],'cp_homo')
                        cp_j_lumo,cp_i_lumo=der_energy(der[j],der[i],'cp_lumo')
                        cocp_i_hcharge,cocp_j_hcharge=der_energy(der[i],der[j],'h_charge')
                        cp_j_hcharge,cp_i_hcharge=der_energy(der[j],der[i],'h_charge')
                        cocp_i_pol,cocp_j_pol=der_energy(der[i],der[j],'pol')
                        cp_j_pol,cp_i_pol=der_energy(der[j],der[i],'pol')
                        
                        tot_ij = cocp_i + cp_j
                        tot_ji = cocp_j + cp_i
        
                        if tot_ij <= tot_ji:
                                bde= (tot_ij - cocp2_energy)*627.5
                                bde_summary.write( cocp2_name +'>> cocp : '+der[i]+' '+'>> cp : '+der[j]+' '+ '>> BDE : '+str(bde)+'\n')
                                
                                der_data.at[k,'Name']=cocp2_name
                                der_data.at[k,'CoCp name']=der[i]
                                der_data.at[k,'CoCp energy']=cocp_i
                                der_data.at[k,'Cp name']=der[j]
                                der_data.at[k,'Cp energy']=cp_j
                                der_data.at[k,'BDE']=bde
                                der_data.at[k,'CoCp HOMO energy']=cocp_i_homo
                                der_data.at[k,'CoCp LUMO energy']=cocp_i_lumo
                                der_data.at[k,'Cp HOMO energy']=cp_j_homo
                                der_data.at[k,'Cp LUMO energy']=cp_j_lumo
                                der_data.at[k,'CoCp H charge']=cocp_i_hcharge
                                der_data.at[k,'Cp H charge']=cp_j_hcharge
                                der_data.at[k,'CoCp polarizability']=cocp_i_pol
                                der_data.at[k,'Cp polarizability']=cp_j_pol
                                
                        else:
                                bde=(tot_ji-cocp2_energy)*627.5
                                bde_summary.write(cocp2_name +'>> cocp : '+der[j]+' '+'>> cp : '+der[i]+' '+ '>> BDE : '+str(bde)+'\n')


                                der_data.at[k,'Name']=cocp2_name
                                der_data.at[k,'CoCp name']=der[j]
                                der_data.at[k,'CoCp energy']=cocp_j
                                der_data.at[k,'Cp name']=der[i]
                                der_data.at[k,'Cp energy']=cp_i
                                der_data.at[k,'BDE']=bde                        
                                der_data.at[k,'CoCp HOMO energy']=cocp_j_homo
                                der_data.at[k,'CoCp LUMO energy']=cocp_j_lumo
                                der_data.at[k,'Cp HOMO energy']=cp_i_homo
                                der_data.at[k,'Cp LUMO energy']=cp_i_lumo
                                der_data.at[k,'CoCp H charge']=cocp_j_hcharge
                                der_data.at[k,'Cp H charge']=cp_i_hcharge
                                der_data.at[k,'CoCp polarizability']=cocp_j_pol
                                der_data.at[k,'Cp polarizability']=cp_i_pol

            opt_xyz = open(os.path.join(xyz_path,str('di_cocp2_'+der[i]+'_'+der[j]+'.xyz')),"r").readlines()
            corx1=0.0
            cory1=0.0
            corz1=0.0
            corx2=0.0
            cory2=0.0
            corz2=0.0
            x_co=0.0
            y_co=0.0
            z_co=0.0
            x_o=0.0
            y_o=0.0
            z_o=0.0
            for n,line_n in enumerate(opt_xyz):
                if n>=0:
                   if n<5:
                      corx1= corx1 + float(line_n.split()[2])
                      cory1= cory1 + float(line_n.split()[3])
                      corz1= corz1 + float(line_n.split()[4])

                if n>=10:
                   if n<15:
                      corx2= corx2 + float(line_n.split()[2])
                      cory2= cory2 + float(line_n.split()[3])
                      corz2= corz2 + float(line_n.split()[4])
      
                if n==9:
                   x_co= x_co + float(line_n.split()[2])
                   y_co= y_co + float(line_n.split()[3])
                   z_co= z_co + float(line_n.split()[4])

                if n==19:
                   x_o= x_o + float(line_n.split()[2])
                   y_o= y_o + float(line_n.split()[3])
                   z_o= z_o + float(line_n.split()[4])

            r_com= math.sqrt(((corx1-corx2)/5)**2 + ((cory1-cory2)/5)**2 + ((corz1-corz2)/5)**2)
            r= math.sqrt((x_co-x_o)**2 + (y_co-y_o)**2 + (z_co-z_o)**2)
            print(str(r_com))

            der_data.at[k,'dCOM']=r_com
            der_data.at[k,'rCo-O']=r


bde_summary.close()
der_data.to_excel("output.xlsx") 
