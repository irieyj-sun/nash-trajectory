# DeepNash
## Description of the model 

Adapation of the DeepHit model to forecast the trajectories of Non-alcoholic Steatohepatitis(NASH) patients on the liver transplant waitlist trained using the Scientific Registry of Transplant Recipients(SRTR). The model makes discrete monthly prediction of the probability of death and transplant using static data. 

## Using the model
The SRTR format data can be processed using the data_processing.py file located in the data folder. Once the data has been processed, run load_model_predict.py file located in the DeepNash folder. The output would be the monthly competing risk predictions for patients in the csv.format. Each two rows correspond to the patients trajectory forecast where the first row is the probability of death and the second row is the probability of transplant. 

## Dashboard 
The model can be used in the dashboard linked below. The model requires .csv or .xlsx file of patient covariates in the SRTR format. 


