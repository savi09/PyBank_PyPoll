{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5e57b953-5f8d-42f1-9cf6-88c1e2aa89c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv\n",
    "\n",
    "#Creates file path\n",
    "budget_csv = os.path.join(\".\",  \"budget_data.csv\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "68c980c2-b53d-43bd-bed4-dc5a825d009d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<_csv.reader object at 0x000002C3367250A0>\n",
      "CSV Header: ['Date', 'Profit/Losses']\n"
     ]
    }
   ],
   "source": [
    "# Openning file\n",
    "with open(budget_csv) as csvfile:\n",
    "\n",
    "    # CSV reader specifies delimiter and variable that holds contents\n",
    "    csvreader = csv.reader(csvfile, delimiter=',')\n",
    "    print(csvreader)\n",
    "\n",
    "    # Read the header row first \n",
    "    csv_header = next(csvreader)\n",
    "    print(f\"CSV Header: {csv_header}\")\n",
    "\n",
    "    date_lst = []\n",
    "    lose_prof_lst = []\n",
    "    \n",
    "    # Read each row of data after the header\n",
    "    for row in csvreader:\n",
    "        date = row[0]\n",
    "        date_lst.append(date) # adding the element to the date list\n",
    "        \n",
    "        lose_prof = float(row[1]) \n",
    "        lose_prof_lst.append(lose_prof) # adding the element to the lose/profit list\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "07c3b897-dc72-401b-8f4b-ff2550b4b708",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Jan-2010', 'Feb-2010', 'Mar-2010', 'Apr-2010', 'May-2010', 'Jun-2010', 'Jul-2010', 'Aug-2010', 'Sep-2010', 'Oct-2010', 'Nov-2010', 'Dec-2010', 'Jan-2011', 'Feb-2011', 'Mar-2011', 'Apr-2011', 'May-2011', 'Jun-2011', 'Jul-2011', 'Aug-2011', 'Sep-2011', 'Oct-2011', 'Nov-2011', 'Dec-2011', 'Jan-2012', 'Feb-2012', 'Mar-2012', 'Apr-2012', 'May-2012', 'Jun-2012', 'Jul-2012', 'Aug-2012', 'Sep-2012', 'Oct-2012', 'Nov-2012', 'Dec-2012', 'Jan-2013', 'Feb-2013', 'Mar-2013', 'Apr-2013', 'May-2013', 'Jun-2013', 'Jul-2013', 'Aug-2013', 'Sep-2013', 'Oct-2013', 'Nov-2013', 'Dec-2013', 'Jan-2014', 'Feb-2014', 'Mar-2014', 'Apr-2014', 'May-2014', 'Jun-2014', 'Jul-2014', 'Aug-2014', 'Sep-2014', 'Oct-2014', 'Nov-2014', 'Dec-2014', 'Jan-2015', 'Feb-2015', 'Mar-2015', 'Apr-2015', 'May-2015', 'Jun-2015', 'Jul-2015', 'Aug-2015', 'Sep-2015', 'Oct-2015', 'Nov-2015', 'Dec-2015', 'Jan-2016', 'Feb-2016', 'Mar-2016', 'Apr-2016', 'May-2016', 'Jun-2016', 'Jul-2016', 'Aug-2016', 'Sep-2016', 'Oct-2016', 'Nov-2016', 'Dec-2016', 'Jan-2017', 'Feb-2017']\n",
      "[867884.0, 984655.0, 322013.0, -69417.0, 310503.0, 522857.0, 1033096.0, 604885.0, -216386.0, 477532.0, 893810.0, -80353.0, 779806.0, -335203.0, 697845.0, 793163.0, 485070.0, 584122.0, 62729.0, 668179.0, 899906.0, 834719.0, 132003.0, 309978.0, -755566.0, 1170593.0, 252788.0, 1151518.0, 817256.0, 570757.0, 506702.0, -1022534.0, 475062.0, 779976.0, 144175.0, 542494.0, 359333.0, 321469.0, 67780.0, 471435.0, 565603.0, 872480.0, 789480.0, 999942.0, -1196225.0, 268997.0, -687986.0, 1150461.0, 682458.0, 617856.0, 824098.0, 581943.0, 132864.0, 448062.0, 689161.0, 800701.0, 1166643.0, 947333.0, 578668.0, 988505.0, 1139715.0, 1029471.0, 687533.0, -524626.0, 158620.0, 87795.0, 423389.0, 840723.0, 568529.0, 332067.0, 989499.0, 778237.0, 650000.0, -1100387.0, -174946.0, 757143.0, 445709.0, 712961.0, -1163797.0, 569899.0, 768450.0, 102685.0, 795914.0, 60988.0, 138230.0, 671099.0]\n"
     ]
    }
   ],
   "source": [
    "# Check the lists        \n",
    "print(date_lst)\n",
    "print(lose_prof_lst)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0c3ae3a1-a958-4e6c-8467-ff1f77ac0ace",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[116771.0, -662642.0, -391430.0, 379920.0, 212354.0, 510239.0, -428211.0, -821271.0, 693918.0, 416278.0, -974163.0, 860159.0, -1115009.0, 1033048.0, 95318.0, -308093.0, 99052.0, -521393.0, 605450.0, 231727.0, -65187.0, -702716.0, 177975.0, -1065544.0, 1926159.0, -917805.0, 898730.0, -334262.0, -246499.0, -64055.0, -1529236.0, 1497596.0, 304914.0, -635801.0, 398319.0, -183161.0, -37864.0, -253689.0, 403655.0, 94168.0, 306877.0, -83000.0, 210462.0, -2196167.0, 1465222.0, -956983.0, 1838447.0, -468003.0, -64602.0, 206242.0, -242155.0, -449079.0, 315198.0, 241099.0, 111540.0, 365942.0, -219310.0, -368665.0, 409837.0, 151210.0, -110244.0, -341938.0, -1212159.0, 683246.0, -70825.0, 335594.0, 417334.0, -272194.0, -236462.0, 657432.0, -211262.0, -128237.0, -1750387.0, 925441.0, 932089.0, -311434.0, 267252.0, -1876758.0, 1733696.0, 198551.0, -665765.0, 693229.0, -734926.0, 77242.0, 532869.0]\n"
     ]
    }
   ],
   "source": [
    "# Calculate change\n",
    "# help from https://www.w3schools.com/python/python_lists_loop.asp\n",
    "difference = []\n",
    "i = 1\n",
    "while i < len(lose_prof_lst):\n",
    "    diff = lose_prof_lst[i]-lose_prof_lst[i-1]\n",
    "    difference.append(diff)\n",
    "    i = i + 1\n",
    "\n",
    "# Check the lists  \n",
    "print(difference)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "006847b7-e753-4c7e-83b5-e747d6ca3090",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Feb-2012 $1,926,159.00\n"
     ]
    }
   ],
   "source": [
    "# Calculate greatest increase\n",
    "great_increase_index = difference.index(max(difference))\n",
    "great_increase_month = date_lst[great_increase_index+1]\n",
    "\n",
    "# '${:,.2f}'.format(amount) formats value; source: https://stackoverflow.com/questions/21208376/converting-float-to-dollars-and-cents\n",
    "great_increase = '${:,.2f}'.format(max(difference))\n",
    "\n",
    "# Checking values\n",
    "print(great_increase_month, great_increase)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "246340e4-36b8-4f67-a931-2e5237da65ed",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sep-2013 $-2,196,167.00\n"
     ]
    }
   ],
   "source": [
    "# Calculate greatest decrease\n",
    "great_decrease_index = difference.index(min(difference))\n",
    "great_decrease_month = date_lst[great_decrease_index+1]\n",
    "\n",
    "# '${:,.2f}'.format(amount) formats value; source: https://stackoverflow.com/questions/21208376/converting-float-to-dollars-and-cents\n",
    "great_decrease = '${:,.2f}'.format(min(difference))\n",
    "\n",
    "# Checking values\n",
    "print(great_decrease_month, great_decrease)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "03ab3661-c08f-4b9b-82f4-d50d6294ba73",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "--------------------------------\n",
      "Total months: 86\n",
      "Total: $38,382,578.00\n",
      "Average Change: $-2,315.12\n",
      "Greatest Increase in Profits: Feb-2012, $1,926,159.00\n",
      "Greatest Decrease in Profits: Sep-2013, $-2,196,167.00\n"
     ]
    }
   ],
   "source": [
    "# Analysis\n",
    "# title \n",
    "print(\"Financial Analysis\")\n",
    "print(\"--------------------------------\")      \n",
    "\n",
    "# Total months\n",
    "total_mon = len(date_lst)\n",
    "print(f\"Total months: {total_mon}\")\n",
    "\n",
    "# Total net profit\n",
    "# '${:,.2f}'.format(amount) formats value; source: https://stackoverflow.com/questions/21208376/converting-float-to-dollars-and-cents\n",
    "total = '${:,.2f}'.format(sum(lose_prof_lst))  \n",
    "print(f\"Total: {total}\")\n",
    "\n",
    "# Average change\n",
    "avg_change = round(sum(difference)/len(difference), 2)\n",
    "format_avg = '${:,.2f}'.format(avg_change)\n",
    "print(f\"Average Change: {format_avg}\")\n",
    "\n",
    "# Greatest increase in profits\n",
    "print(f\"Greatest Increase in Profits: {great_increase_month}, {great_increase}\")\n",
    "\n",
    "# Greatest increase in profits\n",
    "print(f\"Greatest Decrease in Profits: {great_decrease_month}, {great_decrease}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "5ad2eea6-fbca-47fe-bc2b-ba8244b957c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Export Financial Analysis\n",
    "# Specify the file to write to\n",
    "output_path = os.path.join(\".\", \"financial_analysis.csv\")\n",
    "\n",
    "# Open the file using \"write\" mode. Specify the variable to hold the contents\n",
    "with open(output_path, 'w', newline='') as csvfile:\n",
    "\n",
    "    # Initialize csv.writer\n",
    "    csvwriter = csv.writer(csvfile, delimiter=',')\n",
    "    \n",
    "    # Write column headers\n",
    "    csvwriter.writerow(['Financial Analysis', ''])\n",
    "    \n",
    "    # Write the first row \n",
    "    csvwriter.writerow(['Total months: ', total_mon])\n",
    "\n",
    "    # Write the second row\n",
    "    csvwriter.writerow(['Total:', total])\n",
    "    \n",
    "    # Write the third row\n",
    "    csvwriter.writerow(['Average Change:', format_avg])\n",
    "    \n",
    "    # Write the fourth row\n",
    "    csvwriter.writerow(['Greatest Increase in Profits:', great_increase_month, great_increase])\n",
    "    \n",
    "    # Write the fifth row\n",
    "    csvwriter.writerow(['reatest Decrease in Profits:', great_decrease_month, great_decrease])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "55080fa9-c7dc-42d1-b751-b931f8c84e9e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
