import sys
import pandas as pd

# read in worksheet from file into a data frame
scores_frame = pd.read_excel("performance.xlsx","Sheet1")

# show information about this dataframe
scores_frame.info()
print()

# sort by score
print("Top 10 Scores: ")

top_ten_scores = scores_frame.sort_values(
    by=["GOALS", "MATCHES PLAYED"],
    ascending=False
).head(10)

# print the top 10 scorers
print(top_ten_scores)
print()

# rename some columns and print
print("Columns Renamed: ")

some_dict = {'PLAYER NUMBER': 'Player', 'YEARS': 'Age',
             'GOALS': 'Score', 'MATCHES PLAYED': 'Played'}

top_ten_scores.rename(columns=some_dict, inplace=True)

print(top_ten_scores)
print()

# obtain performance stats and print
print("Performance Stats: ")

performance_stats = top_ten_scores.agg({'Score':  ['min', 'max', 'median', 'mean'],
                                        'Played':  ['min', 'max', 'median', 'mean']})

print(performance_stats)