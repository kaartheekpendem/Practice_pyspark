import pandas as pd

data = [
    (1, "Alice", 25, "NY", 5000),
    (2, "Bob", None, "CA", 6000),
    (2, "Bob", None, "CA", 6000),
    (3, "Charlie", 30, "NY", None),
    (4, "David", 45, "TX", 8000),
    (5, "Eve", 35, "CA", 6000),
    (6, "Frank", None, "TX", 7000),
    (7, "Grace", 30, "NY", 5000),
    (8, "Heidi", 28, "CA", None),
    (9, "Ivan", 35, "TX", 8000),
    (9, "Ivan", 35, "TX", 8000),
    (10, "Judy", 25, "NY", 5000),
    (11, "Kyle", 40, "TX", 9000),
    (12, "Laura", 32, "CA", 6500),
    (13, "Mallory", 29, "NY", 5200),
    (14, "Niaj", None, "TX", None),
    (15, "Olivia", 38, "CA", 7000),
    (16, "Peggy", 30, "NY", 5000),
    (17, "Quentin", 45, "TX", 8000),
    (18, "Rupert", 35, "CA", 6000),
    (19, "Sybil", 28, "NY", 5200),
    (20, "Trent", 25, "TX", 7500)
]

columns = ["id", "name", "age", "state", "salary"]
schema={
    'id': int,
    'name': str,
    'age': int,
    'state': str,
    'salary': int
}
df = pd.DataFrame(data,columns=schema.keys())
df.head(5)