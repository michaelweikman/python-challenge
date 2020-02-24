import os
import csv

def main(csvpath):
    results = get_analysis_data(csvpath)
    data_string = get_output_str(results)
    print_data(data_string)

def get_analysis_data(csvpath):
    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile)

        #Skip header
        next(csvreader)

        #Grabbing first row (month) to initiate variables
        csv_first_row = next(csvreader)        
        prev_val = int(csv_first_row[1])
        change_list = {}
        count = 1
        total = prev_val
        sum_change = 0

        for row in csvreader:
            cur_val = int(row[1])
            change = cur_val - prev_val

            change_list[row[0]] = change
            sum_change = sum_change + change
            total = total + cur_val

            prev_val = cur_val
            count = count + 1

    avg_change = sum_change / (count - 1)

    return [
        change_list,
        count,
        total,
        avg_change
    ]

def get_output_str(results):
    change_list = results[0]
    count = results[1]
    total = results[2]
    avg_change = results[3]

    #max and min on dictionary return dict key. In order to get value I have to use .get(key)
    max_change_date = max(change_list, key=change_list.get)
    min_change_date = min(change_list, key=change_list.get)
    max_change_value = change_list.get(max_change_date)
    min_change_value = change_list.get(min_change_date)

    ouput_str = "Financial Analysis \n" \
        "----------------------------\n" \
        f"Total Months: {count}\n" \
        f"Total: ${total}\n" \
        f"Average Change: ${avg_change:.2f}\n" \
        f"Greatest Increase in Profits: {max_change_date} (${max_change_value})\n" \
        f"Greatest Decrease in Profits: {min_change_date} (${min_change_value})\n" \

    return ouput_str

def print_data(string):
    #open file
    filePath = os.path.join(os.path.dirname(__file__), "results.txt")
    file = open(filePath, "w")

    print(string)
    file.write(string)

if __name__ == "__main__":
    #Using __file__ variable to get .py path
    csvpath = os.path.join(os.path.dirname(__file__), 'Resources', 'budget_data.csv')
    main(csvpath)