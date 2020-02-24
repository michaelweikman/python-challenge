import os
import csv

def main(csv_path):
    results = get_poll_data(csv_path)
    print_data(results)

def get_poll_data(csv_path):
    with open(csv_path) as csvfile:
        csvreader = csv.reader(csvfile)
        csvheader = next(csvreader)

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

def print_data(results):
    candidates_dict = results[0]
    total_vote = results[1]

    winner = max(candidates_dict, key=candidates_dict.get)

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_vote}")
    print("-------------------------")

    for candidate, votes in candidates_dict.items():
        # percent = candidate
        print(f"{candidate}: {votes/total_vote: .3%} ({votes})")

    print("-------------------------")
    print(f"Winnder : {winner}")

if __name__ == "__main__":
    csv_path = os.path.join(os.path.dirname(__file__), 'Resources', 'election_data.csv')
    main(csv_path)