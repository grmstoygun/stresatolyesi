import openai

openai.api_key = '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'

def communicate(user_message):
    instructions = []
    instructions.append({"role": "system", "content": "Kullanıcı bir teknoloji şirketinde çalışandır. Şu an mesai saatleri içerisinde ve ofistedir."})
    instructions.append({"role": "user", "content" : user_message})
    reply = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=instructions) 
    return reply

print(communicate("Senin adın nedir?").choices[0].message)