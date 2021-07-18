# PyBank_PyPoll
Using Python script for analyzing the financial records of a company and votes from a small, rural town.

## Repository Description

This repository includes two projects. The first project, PyBank, analyzes a bank's financial profit/losses by month. The original file can be found in PyBank -> Resources --> budget_data.csv. In PyBank's Analysis folder includes:

    1. main.py: this is the python script used that led to the results. In this script you can find two 
    sources I used:

        1. Help formatting values:
        https://stackoverflow.com/questions/21208376/converting-float-to-dollars-and-cents
            '${:,.2f}'.format(amount)
                 This line formats the variable, amount to include a $, commas in the right place, 
                 and a decimal to the hundreth value.

        2. Help understanding While loops
        https://www.w3schools.com/python/python_while_loops.asp
    
    2. There is a PNG file labeled PyBank_Analysis_Results. This is a picture of the results in the terminal

    3. financial_analysis.csv is a CSV with the PyBank project results. This file was exported using the 
    last section of code.

The second project, PyPoll, analyzes voter data of a small, rural town to determine Election results.The original file can be found in PyPoll -> Resources --> election_data.csv