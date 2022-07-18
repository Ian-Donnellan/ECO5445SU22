# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 10:50:46 2022

@author: Ian Ah
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

os.getcwd()

git_path = "C:\\Users\\Ian Ah\\Documents\\GitHub\\ECO5445"
os.chdir(git_path + '\\Project\\Data')

os.getcwd()

##################################################
# Question Number 3
##################################################

col_names = ["Sequence","Loan_Type","Loan_Purpose","Occupancy","Loan_Amount", 
             "Action_Taken","Location","County","Race", "Co_App_Race","Sex",
             "Co_App_Sex","App_Income","Loan_Purchaser","Reasons_For_Denial",
             "Reasons_Corr_1","Reasons_Corr_2","Reasons_Corr_3","Number_Units",
             "Marital_Status","Number_Dependents","Years_Employed",
             "Years_Employed_Job","Self_Employed","Base_Monthly_Income",
             "Base_Monthly_Income_Co_App","Total_Monthly_Income",
             "Total_Monthly_Income_Co_App","Prop_Monthly_Expense",
             "Purchase_Price","Other_Financing","Liquid_Assets",
             "Commercial_Credit_Report","Credit_History_Meets_Guidelines",
             "Consumer_Credit_Lines","Credit_History_Mortgage",
             "Credit_History_Consumer","Credit_History","Debt_to_Income_Housing",
             "Debt_to_Income_Total","Fixed_or_Adjustable_Loan","Term_of_Loan",
             "Special_Loan_Prog","Appraised_Value","Type_of_Property",
             "PMI_Sought?","PMI_Denied?","Gift_Grant_Downpayment?","Cosigner?",
             "Unverifiable_Info","Times_App_Reviewed","Net_Worth",
             "Prob_Unemployment","Minority_Population","Boarded_Up_Value",
             "Median_Income","Applicant_Age","Tract_Vacancy",
             "Years_of_Education","Change_in_Median_Value","Owner_Occupied_Dummy"
             ,"Type_of_Prop_Dummy"]



housing_data = pd.read_csv("hmda_sw.csv", names = col_names, header = 0, delimiter=",")

# The variables that I will be using in my calculations
variables = housing_data[["Debt_to_Income_Total", "Race", "Self_Employed","Marital_Status","Years_of_Education","Loan_Amount","Action_Taken","Sex","Total_Monthly_Income","Purchase_Price","Credit_History_Mortgage"]]

##################################################
# Question Number 4
##################################################

summary = variables.describe()

Pur_Price = variables["Purchase_Price"].tolist()
for average_p in Pur_Price:
    Pur_Price.remove(999999.4)
    
average_price = np.mean(Pur_Price)

plt.hist(variables["Race"], label = "Race")
plt.hist(variables["Sex"])
plt.hist(variables["Self_Employed"])
# Using the summary statistics and visualizations generated we can see that the
# average applicant seems to be white males that are not self employed.

plt.hist(variables["Total_Monthly_Income"])
plt.hist(Pur_Price)
# Using the summary statistics and visualizations generated we can see that the
# average applicant seems to be white males that are not self employed. They on
# average make ~$4,910 a month and are seeking loans for approximately $139,000.
# The average purchase price of homes in the sample is $190,000.

plt.hist(variables["Action_Taken"])
# Using the histogram we can see that the action taken are mainly approvals with 
# a small percentage being denials and an even smaller percentage being not 
# accepted by applicant. 


# The vast majority of applicants are married followed by separated individuals 
# and then unmarried individuals.

# The years of education data is skewed due to the entry of non answered 
# questions which are entered as 999999.4. Interpreting the data besides those
# entries the years seems to be approximately 15 years.


##################################################
# Question Number 5
##################################################

Approved_or_Denied = variables["Action_Taken"].tolist()
Approved = Approved_or_Denied.count(1)
Denied = Approved_or_Denied.count(3)

Prob_of_Approval = Approved / len(Approved_or_Denied)        
print(Prob_of_Approval)

##################################################
# Question Number 6
##################################################

Race = variables["Race"].tolist()
B = [Race,Approved_or_Denied]
a = np.array(B)

Black_Approved = a[1] + a[0] == 4
Black_Approved2 = a[1] + a[0] == 5
Black_Denied = a[1] - a[0] == 0
White_Approved = (a[1] - a[0] == -4)
White_Approved2 = a[1] + a[0] == 7
White_Denied = a[1] + a[0] == 8
Count_Black_App = np.count_nonzero(Black_Approved == True)
Count_Black_App2 = np.count_nonzero(Black_Approved2 == True)
Count_Black_Denied = np.count_nonzero(Black_Denied == True)
Count_White_App = np.count_nonzero(White_Approved == True)
Count_White_App2 = np.count_nonzero(White_Approved2 == True)
Count_White_Denied = np.count_nonzero(White_Denied == True)


Table = [["","Approved", "Denied", "Total"],["Black", Count_Black_App, Count_Black_Denied, (Count_Black_App + Count_Black_App2 + Count_Black_Denied)],["White", Count_White_App, Count_White_Denied, (Count_White_Denied+Count_White_App+Count_White_App2)]]
print(tabulate(Table, headers="firstrow", tablefmt="fancy_grid"))

##################################################
# Question Number 7
##################################################

#Probabilty Approved White
Prob_Approved_White = (Count_White_App/(Count_White_Denied+Count_White_App+Count_White_App2))
print(Prob_Approved_White)


#Probability Denied Black 
Prob_Denied_Black = (Count_Black_App/(Count_Black_Denied+Count_Black_App+Count_Black_App2))
print(Prob_Denied_Black)

