import os
import csv

data = os.path.join('..','CSVFILES','budget_data.csv')
total_months = 0
total_money = 0
change_in_money =[]
dates=[]
last_amount = 0


with open(data, newline = '') as csvfile:
    csvdata = csv.reader(csvfile, delimiter = ',')
    next(csvdata,None)
    header = next(csvdata)
    total_months += 1
    total_money += int(header[1])
    last_amount = int(header[1])
    
    for row in csvdata:
        dates.append(row[0])
        total_months += 1
        total_money +=  int(row[1])
        sub = (int(row[1]))- last_amount
        change_in_money.append(sub)
        last_amount = int(row[1])

         
average = round((sum(change_in_money)/len(change_in_money)),2)
max_list = max(change_in_money)
min_list = min(change_in_money)

index_max = change_in_money.index(max_list)       
index_min = change_in_money.index(min_list) 


print("Financial Analysis")
print("------------------------")
print("Total Months: "+str(total_months))
print("Total: "+"$"+ str(total_money))
print("Average Change: " + "$" + str(average))
print("Greatest Increase in Profits: " +(str(dates[index_max])) + " (" +"$"+ str(max_list)+")")
print("Greatest Decrease in Profits: " + (str(dates[index_min]))+" (" +"$"+ str(min_list)+")")

text_file = open("budget_output.txt","w")
text_file.write("Financial Analysis")
text_file.write("\n""------------------------")
text_file.write("\n""Total Months: "+str(total_months))
text_file.write("\n""Total: "+"$"+ str(total_money))
text_file.write("\n""Average Change: " + "$" + str(average))
text_file.write("\n""Greatest Increase in Profits: " +(str(dates[index_max])) + " (" +"$"+ str(max_list)+")")
text_file.write("\n""Greatest Decrease in Profits: " + (str(dates[index_min]))+" (" +"$"+ str(min_list)+")")
text_file.close()