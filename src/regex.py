import re

date_list = [
    "2025-01-10",
    "2025-02-18",
    "20-12-2025",
    "2024-12-07",
    "2024-12-10",
    "2025-01-02",
    "2025-01-03",
    "2025-01-01",
    "2026-01-01",
    "2025-02-01"
]

k=[]
for i in date_list:
    if bool(re.match(r'\d{4}-\d{2}-\d{2}',i)):
        k.append(i)


print(k)

print([re.findall(r'\d{4}-\d{2}-\d{2}',i)[0] for i in date_list if re.findall(r'\d{4}-\d{2}-\d{2}', i)
])