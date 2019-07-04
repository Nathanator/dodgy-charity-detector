import charity
import pickle

results = []

for i in range(800000, 800500):
    c = charity.get_charity(i)
    if c and c['Status'] != "Removed":
        print(c)
        results.append(c)

pickle.dump(results, "data.pickle")
