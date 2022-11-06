# Predicting the stability of cobaltocenium derivatives 

Author: Shehani Wetthasinghe

Last modified: 11/05/2022

- According to the previous experimental work, cobaltocenium derivatives (CoCp<sub>2</sub>OH) are regarded as promising anion exchange membrane (AEM) components because of their excellent thermal and alkaline stability under operating conditions of fuel cells.
- In this project,  I provide a useful guidance for experimentalists to find out the stable cobaltocenium derivatives by introducing a machine learning model. 
- The stability of cobaltoceniums are studied based on the bond dissociation energy (BDE). 
- After an extensive analysis, I found that BDE can be predicted using few chemical properties of the fragments of cobaltocenium derivatives based on its substituents.

Here are the substituents used in this study:
![substituents](https://user-images.githubusercontent.com/50593017/187327244-749c48b3-b0bf-49ec-835e-14c6d2a8d145.png)

Check out following publications for more information about the theory model;
* https://pubs.acs.org/doi/10.1021/acs.jpca.1c10603
* https://pubs.acs.org/doi/10.1021/acs.jctc.1c01201


## Data Generation
I wanted to expand the data set with every possible di-substituted cobatocenium derivatives for 42 substituents. So here I share the python codes that I used for;
* generating input files for QChem calculations
* data extraction from QChem output files
* property calculation and data analysis

This is the procedure need to follow to add a new substituent;

**Guidlines to generate input files**

First, QChem input files for di-substituted CoCp<sub>2</sub>OH are required to generate with a given substituent set. To do that, xyz coordinates for di-substuted CoCp<sub>2</sub>OH are creating by;
* connecting one group directly to 15<sup>th </sup> atom (C) 
* connecting the second group to 4<sup>th </sup> atom (C) with a coordination rotation through z axis
![rotation](https://user-images.githubusercontent.com/50593017/187334600-a016c858-7223-49dd-b41f-6fc3c3c4e3d7.png)


Steps:
* Optimize the geometry of mono-substituted cobaltocenium with the new substituent group. (input file: Cobaltocenium_project/mono_sub_opt_sample.in) 
* Extract the xyz coordinates of optimized output files using "extract_subcor.py"
* Do any required changes in rem/pcm//basis set/charge/multiplicity in corresponding data files or di_input_generator.py (rem.dat, pcm.dat, basis.dat, "char" or "multi" variables in di_input_generator.py)
* Run "di_input_generator.py"

**Guidlines to submit mutiple QChem files**
*  Run "multi_cal.sh" file to submit the geometry optimization calculations in the serial manner. (It followes the list of di-substituted CoCp<sub>2</sub>OH in "der.dat" file which automatically generate by running the "di_input_generator.py" )

**Guidlines to data extraction, property calculation and data analysis**

* As the next task, the required data is needed to extract from the QChem output files and then calculate further chemical properties. For these calculations, previously calculated data for fragments is also needed. (ex: cp_homo.dat, cp_lumo.dat, cocp_homo.dat, cocp_lumo.dat, h_charge.dat) 

* Geometry optimaization calculations can be performed using "cocp_frag_opt.in" and "cp_frag_opt.in" for CoCpOH and Cp fragments respectively. Then required data can be extracted to following data files using "frag_extract.py"
  * Energy of substituted CoCpOH fragment:                                                cocp.dat
  * Energy of substituted Cp fragment:                                                    cp.dat
  * Energy of highest occupied molecular orbital (HOMO) for substituted CoCpOH fragment:  cocp_homo.dat
  * Energy of lowest unoccupied molecular orbital (LUMO) for substituted CoCpOH fragment: cocp_lumo.dat
  * Energy of HOMO for substituted Cp fragment:                                           cp_homo.dat
  * Energy of LUMO for substituted Cp fragment:                                           cp_lumo.dat
  
 * For the Hirshfeld charge calculation;
    * Create the input file for geometry optimization of substituted benzene using "h_charge_opt.in"
    * Perfom the Hirshfeld charge calculation by adding the optimized geometry to "h_charge_sub.in"
    * Use "h_charge_calculator.py" to calculate the sum of Hirshfeld charge on C<sub>6</sub>H<sub>5</sub> for each substituent and generate the "h_charge.dat" file
    
  * Once all required data files are created, "data.py" can be used to calculate BDE and other chemical properties for di-substituted complexes. (Note: Do the necessary changes in data.py file as in the comments)

The extracted data has published in Open Source Framework (OSF) and the link to the database is attached below;

https://osf.io/6za8c/

## Machine Learning Model

**NOTE:**
Before applying the machine learning techniquies, I removed derivatives below the DFT accuracy 3 kcal/mol of BDE.

The following heat map illustrates the correlation between the features of fragments based on the generated data.

![image](https://user-images.githubusercontent.com/50593017/200151745-c8868931-d0ca-43ce-9cb4-0f56d7663aa1.png)


First, I tried out few regressin machine learning models with the default parameters.
