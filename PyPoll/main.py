import os
import csv

def main(csv_path):
    results = get_poll_data(csv_path)
    data_string = get_results_str(results)
    print_data(data_string)

def get_poll_data(csv_path):
    with open(csv_path) as csvfile:
        csvreader = csv.reader(csvfile)

        # Skip header
        next(csvreader)

        total_vote = 0
        candidates = {}
        for row in csvreader:
            candidate = row[2]
            if candidate in candidates:
                candidates[candidate] = candidates.get(candidate) + 1
            else:
                candidates[candidate] = 1
            
            total_vote = total_vote + 1

    return [
        candidates,
        total_vote
    ]

def get_results_str(results):
    candidates_dict = results[0]
    total_vote = results[1]

    # Gets highest key.value (vote count) and returns the key (candidate name)
    winner = max(candidates_dict, key=candidates_dict.get)

    output_str = "Election Results\n" \
        "-------------------------\n" \
        f"Total Votes: {total_vote}\n" \
        "-------------------------\n" \

    for candidate, votes in candidates_dict.items():
        output_str += f"{candidate}: {votes/total_vote: .3%} ({votes})\n"

    output_str += "-------------------------\n"
    output_str += f"Winner : {winner}"

    return output_str

def print_data(string):
    #open file
    filePath = os.path.join(os.path.dirname(__file__), "results.txt")
    file = open(filePath, "w")

    print(string)
    file.write(string)

if __name__ == "__main__":
    csv_path = os.path.join(os.path.dirname(__file__), 'Resources', 'election_data.csv')
    main(csv_path)