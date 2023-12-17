import openai
import config

def gpt(message) -> str:
    #secret key to connect backend to API
    openai.api_key = config.gpt_api_key

    #function to send request to the turbo model
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        #input for the model
        #content is user input
        messages=[
        {"role": "system", "content": "You are a professional writer drafting a cover letter for a student trying to get a job"},
        {"role": "user", "content": message}
        ]
        
    )
    #extract response from complete function
    response = completion.choices[0].message
    #return the actual message you see from
    print(response["content"])
    return response["content"]
    