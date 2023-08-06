import requests

API_URL = "http://localhost:3050/api/v1/prediction/1272fc8f-e29f-4130-b139-e4efba77bea9"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()
    
output = query({
    "question": "Hey, how are you?",
})


output = query(
    {
        "question": "Who is Dave Ebbelaar? And how many subscribers does he have?",
        "memory_key": "chat_history",
        "input_key": "input",
    }
)

output = query(
    {
        "question": "What is that subscriber count multiplied by 4?",
        "memory_key": "chat_history",
        "input_key": "input",
    }
)

output = query(
    {
        "question": "What was my last question?",
        "memory_key": "chat_history",
        "input_key": "input",
    }
)
