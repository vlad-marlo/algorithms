data = open('24_5641.txt').readline().strip()
print(len(max(data.replace('NP', 'N P').replace('PO', 'P O').split(), key=len)))
