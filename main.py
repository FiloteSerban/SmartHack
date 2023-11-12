import json
import pprint
import openai

api_key = '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'
openai.api_key = api_key

def generateChatResponse(prompt):
    messages = [{"role": "system",
                 "content": "Your are a data analyst. You are very good at understanding how companies function,"
                            "their activity and how markets work, and you are able to score them based on specific criteria."
                 # "content": "Your are a data analyst. You need to understand the business activity of a company, "
                 #            "what sort of services and products they offer, how big is the market they operate into,"
                 #            "geographical risk factors and other types of risks."
                 }]

    question = {'role': 'user', 'content': prompt}
    messages.append(question)

    response = openai.ChatCompletion.create(model="gpt-4-1106-preview", messages=messages)

    try:
        answer = response['choices'][0]['message']['content']
    except:
        answer = 'Unable to find an answer for your question :('

    return answer

with open('search.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

with open('clienti.json', 'r', encoding='utf-8') as file:
    data2 = json.load(file)

with open('mycompany.json', 'r', encoding='utf-8') as file:
    myself = json.load(file)

ranking = generateChatResponse(f"I am a company trying to find new clients. Here you have information about my company {myself}."
                           f" In the past I have worked with clients such as"
                           f"these found here {data2}. "
                           f"I am looking to expand my business and identify similar clients. I have available"
                           f"multiple data points on companies such as location, business industry and activities,"
                           f"revenue , employee counts and others, some examples"
                           f"can be found here {data}."
                           f"You need to help me decide"
                           f"my ideal customer profile or persona. Please calculate a score for each company based"
                           f"on the most relevant criteria and give me the final list of recommended clients (except those from the first json)."
                           f"Output only a json, the keys are companies name and the value is the score, without any other explanation.")

print(json.loads(ranking[7:-3]))
