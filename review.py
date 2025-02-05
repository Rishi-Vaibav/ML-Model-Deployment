import pickle

# Sample data
data = {"movie": "Inception", "verdict": "Excellent"}

# Save to pickle file
with open("movieverdict.pkl", "wb") as f:
    pickle.dump(data, f)

print("Pickle file created successfully!")
