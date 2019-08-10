import os
import csv

data = os.path.join('..','CSVFILES','election_data.csv')

total_votes = 0
candidates_list = []
votes_list = []
khan_votes=0
correy_votes = 0
li_votes=0
otooley_votes = 0

with open(data, newline = '') as csvfile:
    csvdata = csv.reader(csvfile, delimiter = ',')
    next(csvdata,None)

    for row in csvdata:
         if row[2] not in candidates_list:
            candidates_list.append(row[2]) # this will make our list of all candidates 

         total_votes += 1
         if row[2]=="Khan":
            khan_votes +=1
         elif row[2]=="Correy":
            correy_votes +=1
         elif row[2]=="Li":
            li_votes += 1
         else:
            otooley_votes += 1


kp = (khan_votes/total_votes)*100
kpr = round(kp,4)
cp = (correy_votes/total_votes)*100
cpr = round(cp,4)
lp = (li_votes/total_votes)*100
lpr = round(lp,4)
op = (otooley_votes/total_votes)*100
opr = round(op,4)
votes_list = [khan_votes,correy_votes,li_votes,otooley_votes]
winner_votes = max(votes_list)
winner_index = votes_list.index(winner_votes)
winner = candidates_list[winner_index]

#print(candidates_list)
print("Election Results")
print("--------------------")      
print("Total Votes: "+ str(total_votes))
print("--------------------")   
print("Khan: "+ str(kpr) + "% "+ "(" +str(khan_votes)+")")
print("Correy: "+ str(cpr) + "% "+ "(" +str(correy_votes)+")")
print("Li: "+ str(lpr) + "% "+ "(" +str(li_votes)+")")
print("O'Tooley: "+ str(opr) + "% "+ "(" +str(otooley_votes)+")")
print("--------------------")
print("Winner: "+ str(winner))
print("--------------------")

text_file = open("election_output.txt","w")
text_file.write("Election Results")
text_file.write("\n""--------------------")      
text_file.write("\n""Total Votes: "+ str(total_votes))
text_file.write("\n""--------------------")   
text_file.write("\n""Khan: "+ str(kpr) + "% "+ "(" +str(khan_votes)+")")
text_file.write("\n""Correy: "+ str(cpr) + "% "+ "(" +str(correy_votes)+")")
text_file.write("\n""Li: "+ str(lpr) + "% "+ "(" +str(li_votes)+")")
text_file.write("\n""O'Tooley: "+ str(opr) + "% "+ "(" +str(otooley_votes)+")")
text_file.write("\n""--------------------")
text_file.write("\n""Winner: "+ str(winner))
text_file.write("\n""--------------------")
text_file.close()