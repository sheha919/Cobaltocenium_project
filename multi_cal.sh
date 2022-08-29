#!/bin/sh
#SBATCH --job-name=multi_bde
#SBATCH -o tt%j.log
#SBATCH -e tt%j.err
#SBATCH -n 5
#SBATCH -N 1
#SBATCH -p all
 

#add or modify code below
ulimit -l unlimited
source /share/apps/qchem/5.4/qcenv.sh #provide the path to QChem
export QCMPI=mpich
 
cd .
 

for i in $(cat der.dat);
do
	export file=$i
	export QCSCRATCH=/home/username/qchemscr
	qchem -nt 5 $file.in $file.out  $file
	Out_file=$file.out
	if grep  "Maximum optimization cycles reached" $Out_file;
	then	
		echo "$i : Maximum optimization cycles reached" >> summary.dat  
	elif grep  "Invalid charge/multiplicity combination in MoleculeInput::getNElectrons!" $Out_file;
	then
		echo "$i : Invalid charge/multiplicity combination in MoleculeInput::getNElectrons" >> summary.dat
	elif grep  "SCF failed to converge" $Out_file;
	then
		echo "$i : SCF failed to converge" >> summary.dat 
	elif grep  "*  Thank you very much for using Q-Chem.  Have a nice day.  *" $Out_file;
    then
		echo "$i : The calculation completed successfully" >> summary.dat
    else
        echo "$i : Unknown error"
	fi
done
echo "sleeping"
sleep 15
hostname
date
echo "done"
