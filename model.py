import numpy as np
import pandas

input = np.matrix([4, 3, 2, 2, 2, 2, 0, 2, 2]).T
# Read category weights
weights = pandas.read_csv("data/ReducedCategoryWeights.csv", sep=",")#,skiprows=1)
weights = weights.drop(weights.columns[0],axis=1)


category =  pandas.read_csv("data/ReducedCategoryWeights.csv", sep=",",skiprows=1)
category = category.drop(category.columns[1:-1],axis=1).drop(category.columns[-1],axis=1)
weights = weights.values
category = category.values
category.tolist

labels = weights * input
out = zip(labels, category)
out = sorted(out, key = lambda x: x[0], reverse=True)
out = [out[i][1][0] for i in range(5)]
out = ','.join(out)
print out
# Calculate matrix multiplication

# Sort by largest

# Call Yelp with top 5 categories
