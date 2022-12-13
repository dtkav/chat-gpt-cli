# Import the necessary modules
import openai
import os
import getpass

# Set the API key and some initial parameter values
api_key = ""
temperature = 0.5 # 0 to 1
max_tokens = 2000 # max 4000
personality = ""

# Check the operating system and set the appropriate command to clear the terminal screen
if os.name == 'nt':
    clear = 'cls'
else:
    clear = 'clear'

# Define a function to clear the terminal screen
def clearScreen():
  os.system(clear)
  print("===== ChatGPT-Terminal =====")

# Call the function to clear the terminal screen
clearScreen()

# Prompt the user for their API key if it hasn't been provided in the code already
if api_key == "":
  openai.api_key = getpass.getpass(prompt="OpenAI API Key")
else:
  openai.api_key = api_key

# Enter a while loop to continually prompt the user for input and generate responses from the OpenAI API
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

  # Print the generated response
  print(">> " + response["choices"][0]["text"].strip())
