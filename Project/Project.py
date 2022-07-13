# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 10:50:46 2022

@author: Ian Ah
"""

import os
import numpy as np
import pandas as pd

os.getcwd()

git_path = "C:\\Users\\Ian Ah\\Documents\\GitHub\\ECO5445"
os.chdir(git_path + '\\Project\\Data')

os.getcwd()

col_names = ["Sequence","Loan_Type","Loan_Purpose","Occupancy","Loan_Amount","Action_Taken","Location","County","Race", "Co_App_Race","Sex","Co_App_Sex","App_Income","Loan_Purchaser","Reasons_For_Denial","Reasons_Corr_1","Reasons_Corr_2","Reasons_Corr_3","Number_Units","Marital_Status","Number_Dependents","Years_Employed","Years_Employed_Job","Self_Employed","Base_Monthly_Income","Base_Monthly_Income_Co_App","Total_Monthly_Income","Total_Monthly_Income_Co_App","Prop_Monthly_Expense","Purchase_Price","Other_Financing","Liquid_Assets","Commercial_Credit_Report","Credit_History_Meets_Guidelines","Consumer_Credit_Lines","Credit_History_Mortgage","Credit_History_Consumer","Credit_History","Debt_to_Income_Housing","Debt_to_Income_Total","Fixed_or_Adjustable_Loan","Term_of_Loan","Special_Loan_Prog","Appraised_Value","Type_of_Property","PMI_Sought?","PMI_Denied?","Gift_Grant_Downpayment?","Cosigner?","Unverifiable_Info","Times_App_Reviewed","Net_Worth","Prob_Unemployment","Minority_Population","Boarded_Up_Value","Median_Income","Applicant_Age","Tract_Vacancy","Years_of_Education","Change_in_Median_Value","Owner_Occupied_Dummy","Type_of_Prop_Dummy"]

housing_data = pd.read_csv("hmda_sw.csv", names = col_names, header = 0, delimiter=",")

summary = housing_data["Debt_to_Income_Total"].describe()
