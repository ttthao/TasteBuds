import numpy as np

input = [0, 2, 2, 1, 1, 1, 1, 1, 1, 1]
# Read category weights
weights = np.loadtxt(open("data/ReducedCategoryWeights.csv", "rb"), delimiter=",", skiprows=1)

print weights

# Calculate matrix multiplication

# Sort by largest

# Call Yelp with top 5 categories