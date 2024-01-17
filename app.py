import requests

API_URL = "https://api-inference.huggingface.co/models/ingen51/DialoGPT-medium-GPT4"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": {
		"past_user_inputs": ["Which movie is the best ?"],
		"generated_responses": ["It is Die Hard for sure."],
		"text": "Can you explain why ?"
	},
})
