# Stability of cobaltocenium derivatives 
In this project, I investigate the stability of cobaltocenium derivatives used in anion exchange membrane of alkaline fuel cells based on the bond dissociation energy (BDE). After an extensive analysis, I found that BDE can be predicted using few chemical properties of the fragments of cobaltocenium derivatives based on their substituents. Check out below publications for more information about the theory model and machine learning models that I introduced with my colleagues;
* https://pubs.acs.org/doi/10.1021/acs.jpca.1c10603
* https://pubs.acs.org/doi/10.1021/acs.jctc.1c01201

As the next step, I wanted to expand the data set with every possible di-substituted cobatocenium derivatives for 42 substituents. So here I share the python codes that I used for;
* generating input files for QChem calculations
* data extraction from QChem output files
* property calculation and data analysis

This is the procedure need to follow to add a new substituent;

**Guidlines to generate input files**

Here the QChem input files for di-substuted CoCp<sub>2</sub>OH are generating with a given substituent set. The xyz coordinates for di-substuted CoCp<sub>2</sub>OH are creating by;
* one group is directly attaching to C15
* second group is attaching to C4 with a coordination rotation through z axis

Steps:
* Optimize the geometry of mono-substituted cobaltocenium with the new substituent group. (input file: Cobaltocenium_project/mono_sub_opt_sample.in) 
* Extract the xyz coordinates of optimized output files using "extract_subcor.py"
* Do any required changes in rem/pcm//basis set/charge/multiplicity in corresponding data files or di_input_generator.py (rem.dat, pcm.dat, basis.dat, char or multi variables in di_input_generator.py)
* Run di_input_generator.py

