import openai
openai.api_key='---------------'
response=openai.Completion.create(
    model = "text-davinci-003",
    prompt = "I like chocolate because",
    temperature = 0.7, #controls determinism, 0.1=almost same, 0.9=most creative
    max_tokens = 256,
    top_p = 1.0,
    frequency_penalty = 0.0,
    presence_penalty = 0.0,
)
print(response)
