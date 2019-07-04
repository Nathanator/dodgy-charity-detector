def get_enquiries():
    results = []
    with open("charity-enquiries.txt") as f:
        for l in f.read():
            results.append(l.strip())
    return results
