import json

def generate_users(n=20):
    users = []
    for i in range(101, 101 + n):
        users.append({
            "userId": i,
            "username": f"user_{i}",
            "profile": {
                "name": { "first": f"User{i}", "last": "Test" },
                "contact": { "email": f"user{i}@example.com", "phone": f"+1-555-{i:04d}" },
                "preferences": {
                    "language": "en",
                    "notifications": { "email": True, "sms": False, "push": True }
                }
            },
            "activity": [
                { "timestamp": "2025-08-01T10:15:00Z", "action": "login", "device": "Windows" },
                { "timestamp": "2025-08-01T10:45:00Z", "action": "upload", "file": f"report_{i}.pdf" }
            ],
            "accountStatus": {
                "isActive": i % 2 == 0,
                "createdAt": "2023-05-15T08:30:00Z"
            }
        })
    return users

json_data = json.dumps(generate_users(), indent=2)
print(json_data)