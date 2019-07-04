import charity
import pickle

results = []

for i in range(800000, 800500):
    c = charity.get_charity(i)
    if c and c['Status'] != "Removed":
        print(c)
        results.append(c)

f = open("data.pickle", "wb")
pickle.dump(results, f)
