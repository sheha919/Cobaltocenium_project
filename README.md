# Stability of cobaltocenium derivatives 
In this project, I investigate the stability of cobaltocenium derivatives used in anion exchange membrane of alkaline fuel cells based on the bond dissociation energy (BDE). After an extensive analysis, I found that BDE can be predicted using few chemical properties of the fragments of cobaltocenium derivatives based on their substituents. Check out below publications for more information about the theory model and machine learning techniques that I introduced with my colleagues;
* https://pubs.acs.org/doi/10.1021/acs.jpca.1c10603
* https://pubs.acs.org/doi/10.1021/acs.jctc.1c01201

As the next step, I wanted to expand the data set with every possible di-substituted cobatocenium derivatives for 42 substituents. So here I share the python codes that I used for;
* generating input files for QChem calculations
* data extraction from QChem output files
* property calculation and data analysis

This is the procedure need to follow to add a new substituent

Guidlines to generate input files
*Optimize the geometry of mono-substituted cobaltocenium with new substituent group. (The input) 

