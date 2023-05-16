import os
import openai
import tiktoken
import json
import re
from secret import FILENAME1, FILENAME2, FILENAME3, OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY # os.getenv("OPENAI_API_KEY")

def gen_text1(prompt):
  prompt = "Reply without any signature :" + prompt
  completion = openai.ChatCompletion.create(
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

  completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages= messages, temperature = 0.2, top_p = 0.2)

  res = completion.choices[0].message.content
  res = re.sub("\[.*?\]", "", res)

  # count = completion.usage.prompt_tokens

  return res
  # return res, count
  # return res, num_tokens

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

# print(gen_text1(CONTENT))
# print(gen_text2(" "))
# list = fileread("../../../scambaiting_dataset-master/eliza_dane_green_days.json",["kg","pb"],4)
# for i in list:
#   print(i)