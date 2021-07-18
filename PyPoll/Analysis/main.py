{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c6d6a9c3-78a0-42a4-818f-1d64990d2fb9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv\n",
    "\n",
    "#Creates file path\n",
    "election_csv = os.path.join(\".\", \"election_data.csv\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "43841608-9969-4aed-8203-5091a6b05d8e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<_csv.reader object at 0x00000221875FE100>\n",
      "CSV Header: ['Voter ID', 'County', 'Candidate']\n"
     ]
    }
   ],
   "source": [
    "with open(election_csv) as csvfile:\n",
    "\n",
    "    # CSV reader specifies delimiter and variable that holds contents\n",
    "    csvreader = csv.reader(csvfile, delimiter=',')\n",
    "    print(csvreader)\n",
    "\n",
    "    # Read the header row first \n",
    "    csv_header = next(csvreader)\n",
    "    print(f\"CSV Header: {csv_header}\")\n",
    "    \n",
    "    voter_id_lst = []\n",
    "    canidate_lst = []\n",
    "    \n",
    "    # Read each row of data after the header\n",
    "    for row in csvreader:\n",
    "        voter = row[0]\n",
    "        voter_id_lst.append(voter) # adding the element to the date list\n",
    "        \n",
    "        canidate = row[2]\n",
    "        canidate_lst.append(canidate)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "50b68dcb-7a91-4e32-a279-0c46cdbbe692",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Total votes\n",
    "total_votes = len(voter_id_lst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b99a0965-500b-42a7-8036-cc08e91c0ac8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Khan', 'Correy', 'Li', \"O'Tooley\"]\n"
     ]
    }
   ],
   "source": [
    "# Get canidate list\n",
    "# help from https://www.w3schools.com/python/python_lists_loop.asp\n",
    "canidate_lst_2 = []\n",
    "i = 0\n",
    "while i < len(canidate_lst):\n",
    "    if  canidate_lst[i] not in canidate_lst_2:\n",
    "        new = canidate_lst[i]\n",
    "        canidate_lst_2.append(new)\n",
    "    i = i + 1\n",
    "\n",
    "# Check the lists  \n",
    "print(canidate_lst_2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e1d09927-d485-44d3-bb2c-01f3dd0ceae5",
   "metadata": {},
   "outputs": [],
   "source": [
    "def count(canidate2):\n",
    "    count_canidate_lst = []\n",
    "    i = 0\n",
    "    while i < len(canidate_lst):\n",
    "        if  canidate_lst[i] == canidate2:\n",
    "            new = canidate_lst[i]\n",
    "            count_canidate_lst.append(new)\n",
    "        i = i + 1\n",
    "    return len(count_canidate_lst)\n",
    "\n",
    "# def square(number):\n",
    "#     return number * number"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a71062c5-c53a-45e6-b058-98c57137802f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2218231"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Khan votes\n",
    "khan = count('Khan')\n",
    "khan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "cfe2d1ec-4cd9-4cbb-a189-6e9595993a7c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "704200"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Correy votes\n",
    "correy = count('Correy')\n",
    "correy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "c2f4d72f-c151-48bd-ab95-8529da2c1353",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "492940"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Li votes\n",
    "li = count('Li')\n",
    "li"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "612ba226-f5e2-405c-bf71-6730ac57a755",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "105630"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# O'Tooley votes\n",
    "tooley = count(\"O'Tooley\")\n",
    "tooley"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "05977dd6-1b70-4c89-8854-202b584fa2b6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# #check calc\n",
    "# total_votes_check = khan + correy + li + tooley\n",
    "# total_votes_check"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "9172efbf-16a0-4ded-9d47-b1b9be4e21e1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Calculate percentages\n",
    "khan_per = khan/total_votes\n",
    "correy_per = correy/total_votes\n",
    "li_per = li/total_votes\n",
    "tooley_per = tooley/total_votes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "fe4bc2fa-c88e-4f0c-8226-df2776af44aa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Khan'"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Dictionary to find winner\n",
    "canidate_dict = {\n",
    "    \"name\" : [\n",
    "        canidate_lst_2[0],\n",
    "        canidate_lst_2[1],\n",
    "        canidate_lst_2[2],\n",
    "        canidate_lst_2[3]\n",
    "    ],\n",
    "    \"Vote Percentage\":\n",
    "        [khan_per,\n",
    "        correy_per,\n",
    "        li_per,\n",
    "        tooley_per]\n",
    "}\n",
    "# locate winner vote counts\n",
    "x = max(canidate_dict[\"Vote Percentage\"])\n",
    "\n",
    "# Check value\n",
    "# x\n",
    "\n",
    "# Determine index of winner and extract name\n",
    "winner = canidate_dict[\"name\"][canidate_dict[\"Vote Percentage\"].index(x)]\n",
    "winner"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "3a196949-31a4-4589-bc0b-acc09193538f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "------------------------------------------\n",
      "Total Votes: 3,521,001\n",
      "------------------------------------------\n",
      "Khan: 63.00%, 2,218,231.00\n",
      "Correy: 20.00%, 704,200.00\n",
      "Li: 14.00%, 492,940.00\n",
      "O'Tooley: 3.00%, 105,630.00\n",
      "------------------------------------------\n",
      "Winner: Khan\n",
      "------------------------------------------\n"
     ]
    }
   ],
   "source": [
    "# Analysis Results\n",
    "print(\"Election Results\")\n",
    "\n",
    "print(\"------------------------------------------\")\n",
    "\n",
    "print(f\"Total Votes: {'{:,}'.format(total_votes)}\")\n",
    "\n",
    "print(\"------------------------------------------\")\n",
    "\n",
    "# Format values\n",
    "a = '{:,.2%}'.format(khan_per)\n",
    "b = '{:,.2%}'.format(correy_per)\n",
    "c = '{:,.2%}'.format(li_per)\n",
    "d = '{:,.2%}'.format(tooley_per)\n",
    "e = '{:,.2f}'.format(khan)\n",
    "f = '{:,.2f}'.format(correy)\n",
    "g = '{:,.2f}'.format(li)\n",
    "h = '{:,.2f}'.format(tooley)\n",
    "\n",
    "print(f\"{canidate_lst_2[0]}: {a}, {e}\")\n",
    "print(f\"{canidate_lst_2[1]}: {b}, {f}\")\n",
    "print(f\"{canidate_lst_2[2]}: {c}, {g}\")\n",
    "print(f\"{canidate_lst_2[3]}: {d}, {h}\")\n",
    "\n",
    "print(\"------------------------------------------\")\n",
    "\n",
    "print(f\"Winner: {winner}\")\n",
    "\n",
    "print(\"------------------------------------------\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "5d6d6831-1e00-40f2-b990-c36956284376",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Export Financial Analysis\n",
    "# Specify the file to write to\n",
    "output_path = os.path.join(\".\", \"election_results.csv\")\n",
    "\n",
    "# Open the file using \"write\" mode. Specify the variable to hold the contents\n",
    "with open(output_path, 'w', newline='') as csvfile:\n",
    "\n",
    "    # Initialize csv.writer\n",
    "    csvwriter = csv.writer(csvfile, delimiter=',')\n",
    "    \n",
    "    # Write column headers\n",
    "    csvwriter.writerow(['Election Results', 'Percentage of Votes', 'Count of Votes'])\n",
    "    \n",
    "    # Write the first row \n",
    "    csvwriter.writerow(['Total Votes: ','', '{:,}'.format(total_votes)])\n",
    "\n",
    "    # Write the second row\n",
    "    csvwriter.writerow([canidate_lst_2[0], a, e])\n",
    "    \n",
    "    # Write the third row\n",
    "    csvwriter.writerow([canidate_lst_2[1], b, f])\n",
    "    \n",
    "    # Write the fourth row\n",
    "    csvwriter.writerow([canidate_lst_2[2], c, g])\n",
    "    \n",
    "    # Write the fifth row\n",
    "    csvwriter.writerow([canidate_lst_2[3], d, h])\n",
    "\n",
    "    # Write the sixth row\n",
    "    csvwriter.writerow(['Winner: ', winner, ''])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "02a3ce32-d9ff-4afa-a28d-718a597ddb22",
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
