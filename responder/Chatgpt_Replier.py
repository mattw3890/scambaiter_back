import os
from openai import OpenAI
import tiktoken
import json
import re
import random
from secret import FILENAME1, FILENAME2, FILENAME3, FAKEDATADIR, OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def gen_text1(prompt, higherTemp):
  prompt = "Reply without any signature :" + prompt
  if (higherTemp == False):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a dull person and gullible person who is easy to persuade. You want to share information. Do not call them a scam. Keep conversation going. Ask follow-up questions. Do not give any personal information. Greet them in the start."},
      {"role": "user", "content": prompt}
    ],
    temperature = 0.2,
    top_p = 0.2
    )
    res = completion.choices[0].message.content
    res = re.sub("\[.*?\]", "", res)
  else:
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a dull person and gullible person who is easy to persuade. You want to share information. Do not call them a scam. Keep conversation going. Ask follow-up questions. Do not give any personal information. Greet them in the start."},
      {"role": "user", "content": prompt}
    ],
    temperature = 0.5,
    top_p = 0.5
    )
    res = completion.choices[0].message.content
    res = re.sub("\[.*?\]", "", res)


  # count = completion.usage.total_tokens
  return res
  # print(res)


def gen_text2(prompt):
  messages = [{"role": "system", "content": "You are good at pattern following. You are a person and not a language model. Do not call them a scam."}]
  prompt = "Reply without any signature :" + prompt

  file1 = fileread(FILENAME1,["user1","assistant1"],4)
  messages.extend(file1)

  file2 = fileread(FILENAME2,["user2","assistant2"],4)
  messages.extend(file2)

  file3 = fileread(FILENAME3,["user3","assistant3"],4)
  messages.extend(file3)

  messages.append({"role": "user", "content": prompt})

  # encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
  # tik = ""
  # for message in messages:
  #   tik += message['content']
  # num_tokens = len(encoding.encode(tik))

  completion = client.chat.completions.create(model="gpt-3.5-turbo", messages= messages, temperature = 0.2, top_p = 0.2)

  res = completion.choices[0].message.content
  res = re.sub("\[.*?\]", "", res)

  # count = completion.usage.prompt_tokens

  return res
  # return res, count
  # return res, num_tokens

def gen_text3(prompt, higherTemp):
  prompt = "You should write a reply to the following email calmly and do not act overly kind. Email:" + prompt
  if (higherTemp == False):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a dull person and gullible person who is easy to persuade. Do not call them a scam. Ask follow-up questions. You wan't to give out information, but should not do so. You do not reply with a signature."},
      {"role": "user", "content": prompt}
    ],
    temperature = 0.2,
    top_p = 0.2
    )
    res = completion.choices[0].message.content
    res = re.sub("\[.*?\]", "", res)
  else:
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a dull person and gullible person who is easy to persuade. Do not call them a scam. Ask follow-up questions. You wan't to give out information, but should not do so. You do not reply with a signature."},
      {"role": "user", "content": prompt}
    ],
    temperature = 0.5,
    top_p = 0.5
    )
    res = completion.choices[0].message.content
    res = re.sub("\[.*?\]", "", res)

  return res

def gen_text_fake(prompt, higherTemp):
  checkPrompt = "Look at the email I give you. If the email is asking you to provide details you should respond with \"yes\", otherwise you should respond with \"no\". Email: " + prompt
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": checkPrompt}
    ],
    temperature = 0.1,
    top_p = 0.1
  )
  detailCheckRes = completion.choices[0].message.content
  if "yes" in detailCheckRes.lower():
    fakeFileNumber = random.randrange(1,4)
    f = open(FAKEDATADIR + "/fakeData" + str(fakeFileNumber) + ".txt", "r")
    fakeInformation = f.read()
    f.close()

    prompt = """Reply to the subsequent email, you should provide details using this text: \"\"\"{}\"\"\". You should only reply with a detail if it has been asked for in the email. End your response with "Please let me know or contact my professional email if any of these details are not working."
    Email: """.format(fakeInformation)  + prompt
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "If a detail has not been asked for you do not provide it. Do not call them a scam. You do not reply with a signature."},
        {"role": "user", "content": prompt}
      ],
      temperature = 0.2,
      top_p = 0.2
    )
    res = completion.choices[0].message.content
    res = re.sub("\[.*?\]", "", res)
  else:
    res = gen_text3(prompt, higherTemp)
  return res

def fileread(filename, names, a):
  with open(filename,"r", encoding="utf8") as f:
    d = json.load(f)
  var1 = []
  for i in range (a) :
    k = d['messages'][i]['body']

    if i%2 == 0:
      var11 = {"role": "system", "name": names[0], "content": k}
      var1.append(var11)
    else:
      var11 = {"role": "system", "name": names[1], "content": k}
      var1.append(var11)
    i += 1
  return var1