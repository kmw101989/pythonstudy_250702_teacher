import json

data = """
{
    "id":"01", "language":"python", "edition":"third", "author":"David",
    "history":
        [
            {
                "date":"2025-07-16",
                "item":"iPhone"
            },
            {
                "date":"2025-03-11",
                "item":"Android"
            }
        ]
}
"""

json_data = json.loads(data)
# print(json_data)
print(json_data["history"][0]["date"])