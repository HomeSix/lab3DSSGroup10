import csv
import os

base = os.path.dirname(os.path.abspath(__file__))
header = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]

files = ["iris.data", "bezdekIris.data"]
for name in files:
    src = os.path.join(base, name)
    dst = os.path.join(base, name.replace(".data", ".csv"))
    with open(src, "r", newline="") as fin, open(dst, "w", newline="") as fout:
        writer = csv.writer(fout)
        writer.writerow(header)
        for line in fin:
            line = line.strip()
            if not line:
                continue
            writer.writerow(line.split(","))
    print("Wrote", dst)
