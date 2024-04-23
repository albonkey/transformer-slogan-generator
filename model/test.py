import gzip
import pickle

# Open and decompress the .gz file
with gzip.open('modelOutput/model.pkl.gz', 'rb') as f:
    # Load the pickled data
    data = pickle.load(f)

# Inspect the data
print(data)