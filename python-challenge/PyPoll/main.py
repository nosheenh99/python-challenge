# Importing the csv module for reading the csv file
import csv

# Importing the defaultdict from the collections module for creating a dictionary with default int values (0 - zero)
from collections import defaultdict

# Read the "election_data.csv" file using csv module and a context manager
with open("Resources/election_data.csv", "r") as file:
    # Using csv reader to read the file object
    reader = csv.reader(file)

    # Reading the header (first line of the file)
    header = next(reader)

    # Initilizing the 'votes' as a dictionary
    # Every new 'key' added to this dictionary would have a default '0' zero as its value
    votes = defaultdict(int)

    # Initializing the 'total_votes' as 0
    total_votes = 0

    for row in reader:
        candidate = row[2]
        votes[candidate] = votes[candidate] + 1
        total_votes = total_votes + 1


# Getting the entire list of candidates from the votes dictionary
candidates = list(votes.keys())

# Counting the total votes of all the candidates using list comprehension
vote_counts = [votes[candidate] for candidate in candidates]

# Calculating the votes percentage based on the vote count using list comprehension
vote_percentages = [vote_count / total_votes * 100 for vote_count in vote_counts]

# Finding the index of the candidate with maximum vote count
winner_index = vote_counts.index(max(vote_counts))

# Getting the winner's name based on the winner index
winner = candidates[winner_index]


# Printing or displaying the output to the terminal screen
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Iterating through candidate, vote percentage and vote count in a single for loop
# Using zip function we can iterate through more than one list
for candidate, percentage, count in zip(candidates, vote_percentages, vote_counts):
    result_line = f"{candidate}: {percentage:.3f}% ({count})"
    print(result_line)

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Writing the output to the .txt file
# Using csv module writer to write the text (ouptut) to the .txt file
with open("election_results.txt", "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")

    for candidate, percentage, count in zip(candidates, vote_percentages, vote_counts):
        result_line = f"{candidate}: {percentage:.3f}% ({count})"
        file.write(result_line + "\n")

    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
