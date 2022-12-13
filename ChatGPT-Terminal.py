import openai
import os
import getpass

api_key = ""
temperature = 0.5 # 0 to 1
max_tokens = 2000 # max 4000
personality = ""

if os.name == 'nt':
    clear = 'cls'
else:
    clear = 'clear'

def clearScreen():
  os.system(clear)
  print("===== ChatGPT-Terminal =====")

clearScreen()

if api_key == "":
  openai.api_key = getpass.getpass(prompt="OpenAI API Key")
else:
  openai.api_key = api_key

while True:
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=personality + input('\n' + "> "),
    temperature=temperature,
    max_tokens=max_tokens,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )

  print(">> " + response["choices"][0]["text"].strip())
