import os
import numpy as np


der=['dme','meth','eth','pr2','thl','c6h5','c2h3','c2h','ch3','tch3','c3h7','h','cl','br','f','conhr',
     'conh2','cooch3','coch3','coh','cof','cocl','cf3','ccl3','cbr3','cn','soor','no2','soocf3','ph_p_cl',
     'ph_o_cl','ph_m_cl','ph_o_cf3','ph_m_cf3','ph_p_cf3','ph_p_ch3','ph_p_och3','ph_op_ch3','ph_op_och3',
     'piperidine','paryl2','naryl2']

#der=['pr2','thl','c6h5','c2h3','c2h','ch3','tch3'] 
#der=['dme','meth','eth'] 

wrk_dir='../../subs/'

der_list = open(os.path.join('der.dat'),"w")

for i in range(len(der)):
    for j in range(i,len(der)):
        save_as_file=os.path.join(str('di_cocp2_'+der[i]+'_'+der[j]+'.in'))
        cocp2oh=open(os.path.join(wrk_dir,'cocp2oh.xyz'), "r").read()
        rem=open(os.path.join(wrk_dir,'rem.dat'), "r").read()
        pcm=open(os.path.join(wrk_dir,'pcm.dat'), "r").read()
        basis=open(os.path.join(wrk_dir,'basis.dat'), "r").read()
        der_list.write('di_cocp2_'+der[i]+'_'+der[j]+'\n')

        write_file = open(save_as_file,"w")
        write_file.write('$molecule'+'\n')
        write_file.write('0'+' ' +'1'+'\n')
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
                write_file.write(str(sub[0])+'   '+str(float(sub[1])*-1)+'   '+str(float(sub[2])*-1)+'   '+str(float(sub[3])*1)+ '\n')
                file.close()
        write_file.write('$end'+'\n')
        write_file.write('\n'+rem+'\n\n'+pcm+'\n\n'+basis)
        write_file.close()
der_list.close()
