import os
import csv

pyPoll_csv = os.path.join('election_data.csv')

with open(pyPoll_csv, 'r') as pyPollData:
    electionData = csv.reader(pyPollData, delimiter=",")

    next(electionData, None)
    totalVotes = 0
    election = {}
    candidates = []

    for vote in electionData:

        totalVotes += 1

        candidate = vote[2]

        if not candidate in election:
            election[candidate] = 1
        else:
            election[candidate] += 1
        if not candidate in candidates:
            candidates.append(candidate)

votePerc = []
candidateData = []

for i in range(len(candidates)):
    votePerc.append(election[candidates[i]] / totalVotes)
    votePerc[i] = format(votePerc[i], ".3%")
    candidateData.append(f"{candidates[i]}: {votePerc[i]} ({election[candidates[i]]}) \n")

mostVotes = 0
winningCandidate = 0

for i in candidates:
    if election[i] > mostVotes:
        mostVotes = election[i]
        winningCandidate = i

print("Election Results")       
print("----------------")
print(f"Total Votes: {totalVotes}")
print("---------------- \n")
for i in range(len(candidates)):
    print(f"{candidateData[i]}")
print("----------------")
print(f"Winner: {winningCandidate}")


electionDocument = open('election_results.txt','w')
electionDocument.write(f"""Election Results 
---------------- 
Total Votes: {totalVotes} 
---------------- \n""") 
electionDocument.writelines(candidateData)
electionDocument.write(f"""---------------- 
Winner: {winningCandidate}""")
electionDocument.close()