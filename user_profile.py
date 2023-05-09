import openai
import re

# Function to standardize gender values
def standardize_gender(value):
    if isinstance(value, str):
        value = value.lower()
        return 'woman' if 'woman' in value else 'man' if 'man' in value else value
    return value

# Function to extract numbers from a string
def extract_number(s):
    match = re.search(r'\d+', s)
    return int(match.group()) if match else 0

# Function to clean a string by removing non-alphanumeric characters and converting to lowercase
def clean_string(s):
    return re.sub(r'[^a-zA-Z0-9]+', '', s).lower()

# Function to import user profile using GPT-3
def import_user_profile(user_text):
    # Set OpenAI API key
    openai.api_key = "ENTER OPENAI KEY HERE"

    # Function to get GPT-3 response for a given command
    def gpt_response(cmd):
        with open(f'{cmd}.txt', 'r') as f:
            contents = f.read()
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user",
                "content": f"{contents} Here is the client response: {user_text}"
            }]
        )
        return completion["choices"][0]["message"]["content"]

    # Get GPT-3 responses for each command and store them in a dictionary
    res = {cmd: gpt_response(cmd) for cmd in ['age', 'gender', 'weight', 'target_weight', 'medical']}

    # Standardize and clean the gender response
    gender_resp = standardize_gender(clean_string(res['gender']))
    # Calculate weight loss by subtracting target weight from current weight
    weight_loss_resp = extract_number(res['weight']) - extract_number(res['target_weight'])

    # Return a dictionary containing the user profile data
    return {
        "gender": gender_resp,
        "weight_loss": weight_loss_resp,
        "health": res['medical'],
        "age": extract_number(clean_string(res['age']))
    }
