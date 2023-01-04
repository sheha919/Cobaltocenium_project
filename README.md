# Predicting the stability of cobaltocenium derivatives 

Author: Shehani Wetthasinghe

Last modified: 01/03/2023

![afm_aem](https://user-images.githubusercontent.com/50593017/200152591-233aee11-a424-46b4-9a55-d0cfa8bcac7f.png)

- According to the previous experimental work, cobaltocenium derivatives (CoCp<sub>2</sub>OH) are regarded as promising anion exchange membrane (AEM) components because of their excellent thermal and alkaline stability under operating conditions of fuel cells.
- In this project,  I provide a useful guidance for experimentalists to find out the stable cobaltocenium derivatives by introducing a machine learning model.
- The stability can be interpreted as measure of bond dissociation energy (BDE). 
- After an extensive analysis, I found that BDE can be predicted using few chemical properties of the fragments of cobaltocenium derivatives based on its substituents.

Here are the substituents used in this study:
![substituents](https://user-images.githubusercontent.com/50593017/187327244-749c48b3-b0bf-49ec-835e-14c6d2a8d145.png)

Check out following publications for more information about the theory model;
* https://pubs.acs.org/doi/10.1021/acs.jpca.1c10603
* https://pubs.acs.org/doi/10.1021/acs.jctc.1c01201


## Data Generation
I generated the data set with every possible di-substituted cobatocenium derivatives for 42 substituents. So here I share the python codes that I used for;
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

## Machine Learning Models

**NOTE:**
Before applying the machine learning techniquies, I removed derivatives below the DFT accuracy 3 kcal/mol of BDE.

The following heat map illustrates the correlation between the features of fragments based on the generated data.

![image](https://user-images.githubusercontent.com/50593017/200151745-c8868931-d0ca-43ce-9cb4-0f56d7663aa1.png)

First, I tried out few regression machine learning models with the default parameters. The following table shows their performence;
|Model|Train R2|Test R2|Train RMSE \(kcal/mol\)|Test RMSE \(kcal/mol\)|
|---|---|---|---|---|
|Linear Regression|0\.459858|0\.400263|4\.857049|5\.170292|
|Decision Tree|1|0\.500963|0|4\.716295|
|Bagged Tree|0\.968559|0\.758548|1\.171838|3\.280576|
|KNN|0\.699967|0\.428702|3\.619956|5\.046217|
|Random Forest|0\.982086|0\.795065|0\.884542|3\.022334|
|SVG|0\.479298|0\.378495|4\.768846|5\.263284|
|XG Boost|0\.905036|0\.844032|2\.036564|2\.636647|

![image](https://user-images.githubusercontent.com/50593017/200152014-b8e12650-6777-4b09-8cb1-fafc421f1c12.png)
![image](https://user-images.githubusercontent.com/50593017/200152026-eacfac2c-0493-47d7-b8c5-50ee0fc4ee8e.png)
![image](https://user-images.githubusercontent.com/50593017/200152031-68c122be-c68c-4947-a9b2-5fd3d0d87eb4.png)
![image](https://user-images.githubusercontent.com/50593017/200152035-5d050ae3-cc14-49eb-8f10-b21d6690384c.png)
![image](https://user-images.githubusercontent.com/50593017/200152043-e117e411-5c53-417d-a95e-c03f255b46c5.png)
![image](https://user-images.githubusercontent.com/50593017/210457193-87d61b1a-4213-4dc0-a284-682f8d3decbf.png)
![image](https://user-images.githubusercontent.com/50593017/210457210-532ce038-d598-4ad9-a041-d6a967bf9406.png)

- According to the train and test RMSE values for the models;
  - all models have overfilling issue and decision tree has the highest overfittin problem.
- Out of these 7 models, XG boost, random forest and bagged tree are selected based on the test R$^2$ score to do further optimizations.
 
 The following table illustrates the performence of the models after tunning the hyperparameters and carring out the cross validation (folds = 5);
 
|Model|Train R2|Test R2|Train RMSE \(kcal/mol\)|Test RMSE \(kcal/mol\)|
|---|---|---|---|---|
|XG Boost|0\.986399|0\.845785|0\.770731|2\.621787|
|Random Forest|0\.979996|0\.798638|0\.9347|2\.995871|
|Bagged Tree|0\.980953|0\.801947|0\.912076|2\.971157|

![image](https://user-images.githubusercontent.com/50593017/210457410-143e70a0-ce49-4846-ac13-142f5f54258e.png)
![image](https://user-images.githubusercontent.com/50593017/210457442-d0795964-28ed-4efe-9ac6-ee690ac29092.png)
![image](https://user-images.githubusercontent.com/50593017/210457461-2bfcc5df-81cd-4283-bd3e-3ff1ab2c5ec6.png)


- **Acording to the performence of optimized models, XG Boost regression model is selected as the best ML model since it gained the highest R<sup>2</sup> score and lowest train and test RMSE scores.**

- **But this model is suffering from overfitting, so here I tried few few deep learning models to overcome the overfitting problem.**

## Neural Network Models
Performence of the NN models

|Model|Train R2|Test R2|Train RMSE \(kcal/mol\)|Test RMSE \(kcal/mol\)|
|---|---|---|---|---|
|Model1|0\.513425|0\.418722|4\.609922|5\.090102|
|Model2|0\.77119|0\.771951|3\.161232|3\.18822|
|Model3|0\.607288|0\.508566|4\.141482|4\.680232|

### Model 1
- Model 1 is too simple or trained for too few epochs to predict a dataset well. As the next step, I increased the complexity of the model.
- According to the calculated scores, training scores are better than the testing scores which implies the overfitting.
- So I just gave a try by making the model much complicated by increasing the number of nodes and epoches.
- And also used the early stopping method to restrict over doing the epochs.

### Model 2
- In this model, the number of nodes increased from 10 to 20 and add early stopping method with the patience level of 10.
- According to R<sup>2</sup> scores, testing score is higher than the training score which is very good.
- But in MAE and RMSE scores, training score is slightly higher than the testing score.
- So far, model 2 is the best model to predict BDE with the minimum overfitting.

### Model 3
- I introduced model 3 by doing further modifications to model 2  to have better predictions.
- In model 3;
    - increase number of layers
    - increase number of nodes and applying "Dropout" to turn off some nodes during the training process to choose the correct number of nodes. This is a remedy for overfitting.
    - As another solution for overfitting, L1 and L2 regularization is used

![image](https://user-images.githubusercontent.com/50593017/210458680-3836ac4a-94a2-4e9a-b89d-84e064dbbca0.png)
![image](https://user-images.githubusercontent.com/50593017/210458820-9b661d32-ca62-418e-96ad-e2fcce419dbf.png)
![image](https://user-images.githubusercontent.com/50593017/210458850-37673526-37ff-493a-b69a-40cb538e1927.png)

## Recomendations
- Out of all ML models and NN models, model 2 is selected as best model because it showed the best performce (R<sup>2</sup> scores) with minimum overfitting.
- According to the predicted results of every model, you can observe that the predictions made for the derivatives with actual BDE values greater than 30 kcal/mol (derivatives with electron donating groups) produced the higher error and it caused to decrease the testing scores of the models.
- This is because, the number of highly stable derivatives (BDE > 30 kcal/mol) in the database is 32 out of 873 total data points and it is not sufficient
to train the models to provide accurate predictions for stable derivatives.
- Therefore, I recommend to add more derivatives with electron donating groups (BDE > 30 kcal/mol) to the database to enhance the accuracy of predictions.


