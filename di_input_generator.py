import os
import numpy as np

#define the substituent group names
der=['dme','meth','eth','pr2','thl','c6h5','c2h3','c2h','ch3','tch3','c3h7','h','cl','br','f','conhr',
     'conh2','cooch3','coch3','coh','cof','cocl','cf3','ccl3','cbr3','cn','soor','no2','soocf3','ph_p_cl',
     'ph_o_cl','ph_m_cl','ph_o_cf3','ph_m_cf3','ph_p_cf3','ph_p_ch3','ph_p_och3','ph_op_ch3','ph_op_och3',
     'piperidine','paryl2','naryl2']


wrk_dir='x_path' # define the path to files

der_list = open(os.path.join('der.dat'),"w")

for i in range(len(der)):
    for j in range(i,len(der)):
        save_as_file=os.path.join(str('di_cocp2_'+der[i]+'_'+der[j]+'.in'))
        cocp2oh=open(os.path.join(wrk_dir,'cocp2oh.xyz'), "r").read() #call the coordinates structure for cocp2oh
        rem=open(os.path.join(wrk_dir,'rem.dat'), "r").read()         #call the rem variable file
        pcm=open(os.path.join(wrk_dir,'pcm.dat'), "r").read()         #call the pcm variable file
        basis=open(os.path.join(wrk_dir,'basis.dat'), "r").read()     #call the basis sets
        der_list.write('di_cocp2_'+der[i]+'_'+der[j]+'\n')
         
        multi=1, char=0                                               #Define the multiplicity and the charge of the molecule  
        write_file = open(save_as_file,"w")
        write_file.write('$molecule'+'\n')
        write_file.write(str(char)+' ' +str(multi)+'\n')
        write_file.write(cocp2oh)

        file=open(os.path.join(wrk_dir,str(der[i]+'.xyz')), "r")
        data=file.readlines()

        for indx,line in enumerate(data):
            if line == "\n":
                file.close()
            else:
                sub=line.split()
                write_file.write(str(sub[0])+'   '+str(float(sub[1])*1)+'   '+str(float(sub[2])*1)+'   '+str(float(sub[3])*1)+ '\n')
                file.close()

        file=open(os.path.join(wrk_dir,str(der[j]+'.xyz')), "r")
        data=file.readlines()
        
        for indx,line in enumerate(data):
            if line == "\n":
                file.close()
            else:
                sub=line.split()
                #rotating the coodinates of substituent group through Z axis    
                write_file.write(str(sub[0])+'   '+str(float(sub[1])*-1)+'   '+str(float(sub[2])*-1)+'   '+str(float(sub[3])*1)+ '\n')
                file.close()
        write_file.write('$end'+'\n')
        write_file.write('\n'+rem+'\n\n'+pcm+'\n\n'+basis)
        write_file.close()
der_list.close()
