# create a Python script that analyzes the votes and calculates each of the following:

# * The total number of votes cast

# * A complete list of candidates who received votes

# * The percentage of votes each candidate won

# * The total number of votes each candidate won

# * The winner of the election based on popular vote.

#Import modules CSV and OS
import csv
import os
from re import U
PyPoll_csv =os.path.join("Resources","election_data.csv")


#creating the list
count = 0
candidate_list = []
unique_candidate = []
vote_count = []
vote_percent = []

#opening the csv by setting up the path
with open(PyPoll_csv, newline ="") as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")
    csv_header =next(csvreader)



#creating set from the candidate_list to get the unique_candidate names

    for row in csvreader:
        count = count +1
        candidate_list.append(row[2])


        
    for a in set(candidate_list):
        unique_candidate.append(a)
        #b is total number of votes per candidate
        b =candidate_list.count(a)
        vote_count.append(b)

        #c is the % of total votes 
        c=(b/count)*100
        vote_percent.append(c)


    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Election Results")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("total votes : "+ str(count))
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    for i in range(len(unique_candidate)):
        print(unique_candidate[i]+":" +str(vote_percent[i]) +"%"+(str(vote_count[i])))
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("The winner is :"+ winner)

#now printing the election results
with open("election_results.txt","w") as text:
    text.write("Election Results\n")
    text.write(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
    text.write("total vote:" +str(count)+"\n")
    text.write(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
    for i in range(len(set(unique_candidate))):
        text.write(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
        text.write(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        text.write("The winner is: " +winner+"\n")
        












