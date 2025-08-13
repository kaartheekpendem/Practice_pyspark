from collections import defaultdict

data = [('A', 10), ('B', 20), ('A', 15)]

agg = defaultdict(list)
for key, value in data:
    agg[key].append(value)

# Sum per group
group_sums = {k: sum(v) for k, v in agg.items()}
print(group_sums)