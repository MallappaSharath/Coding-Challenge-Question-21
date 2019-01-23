"""
Coding Challenge Question 21 - Sachin's score assesment
"""

# Count the number of innings Sachin scored less than 25 runs in 2001

# Fill the missing pieces in the below line to get the list of runs scored by Sachin in 2001.
runs = [ num.strip() for num in open("sachin_runs.csv").read().split() ]


# Use the above "runs" list to find out the number of innings Sachin scored less than 25 runs
## YOUR CODE GOES HERE ##
less_than_25 = 0
for innigs_score in runs[9:]:
	if int(innigs_score) < 25:
		less_than_25 += 1

print("Number of innings in which Sachin scored less than 25 runs is:", less_than_25)


# A Journalist makes a claim that in 2001, Sachin scored less than 33 runs, in less than 33% of his innings

# Write Python code to check the claim made by this Journalist
## YOUR CODE GOES HERE ##

total_innings = len(runs[9:])
less_than_33 = 0
claim_by_jurno = (33*total_innings)/100

for innigs_score in runs[9:]:
	if int(innigs_score) < 33:
		less_than_33 += 1

print("Number of innings in which sachin scored less than 33 is:", less_than_33)

if claim_by_jurno < less_than_33:
	print("Yes. Journalist was right. Sachin scored less than 33 runs, in less than 33% of his innings")
else:
	print("No. Journalist was wrong. Sachin scored less than 33 runs, in more than 33% of his innings")

		
# A Commentator then claims that in 2001, Sachin's score on an average, crossed half a century in at least one of every 2 innings.


# Write Python code to check the claim made by this Commentator
## YOUR CODE GOES HERE ##
half_century = 0
for innigs_score in runs[9:]:
	if int(innigs_score) >= 50:
		half_century += 1

one_of_every_2_innings = total_innings / 2

if half_century >= one_of_every_2_innings:
	print("Yes. Commentator was right. Sachin's score on an average, crossed half a century in at least one of every 2 innings")
else:
	print("No. Commentator was wrong. Sachin's score on an average doesn't crossed half a century in at least one of every 2 innings")