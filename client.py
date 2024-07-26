from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="sk-proj-j9gFicErROvwFaF14MnJT3BlbkFJq2zi2JJ0Hw58BJhTJyrK",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named Abdul Subhan , skilled in python , and knows English and Urdu , you analyze chat history and talk like Abdul Subhan"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)