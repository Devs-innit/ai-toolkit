# AI Toolkit - Python + OpenRouter API

## 1. Title and Objective
 **Technology chosen:** Python +OpenRouter API +OpenAI library + Mistral-small-3.1-24b model

 **Why I chose it:** I chose this as an absolute beginner developer as I wanted to apply what i had learnt to comprehend
  how GenAI tools work to my advantage in boosting productivity,learning and skills.This project helped me realize that
  AI isn't just magic...no,it's powered by structured API calls and well designed prompts.

 **What it does:**I built a simple command-line AI coding assistant that accepts user questions and sends it to the  (BRAIN)
  OpenRouter API. Using a securely loaded API key,the request is passed to the Mistral model, which processes it using my system 
  prompt to ensure beginner-friendly responses.The response is then returned to the program and displayed neatly in the terminal.

 **Key Features:**
-🔐 Secure API key storage using .env file for data security.
-🤖 Custom system prompt for a layer of personality
-🐍 Pure python - no framework needed.
-🌍 Free to run using OpenRouter free tier🎉


## 2. Quick Summary of the Technology
 **What is Python?:** I used Python as the programming language to build and control my application. It allowed me 
   to send requests to APIs, process the responses and manage the flow of data in a simple and efficient way.

**What is an API and which API did I use?** An API is the connection to a 'brain'- rather, it acts like a nervous system 
  between my code and an AI model. Using a securely loaded API key,my program sends a request(question) through the 
  API to the AI model(the 'brain'),and the API then returns the answer to the user(me). In my project, I used
  OpenRouter as the API service to connect to an AI model.

  For example,when I input a question like,'What is python?', my program sends it through the API to the AI model and displays
  the generated response in the terminal.

  **What is a system prompt?** A system prompt is an instruction that defines how it should behave before it receives user input. 
    It sets the tone, personality and rules for how responses should be generated.In my project, I used a custom system 
    prompt:'Keep answers simple, friendly and easy to understand,' which helped structure the AI as a helpful coding assistant to junior
    developers. Without the system prompt, the AI would respond more generally without a defined tone or behaviour.


## 3. System Requirements
 
  **This project runs in a simple environment and does not require any frameworks.**
   
   -Python (version 3.13 recommended)
   -Internet connection
   -A valid OpenRouter API key
   -OpenAI library
   -A code editor(eg.VS Code)
   -python-dotenv library (for API key security)


## 4. Installation and Setup Instructions
  
1. Make sure python version 3.13 is installed.

2. Install the required dependancies:
   ```
  py -m pip install openai python-dotenv
   ```

3.Create a file called hello_ai.py and paste the code from Section 5.
  
4. Create a .env file in the project folder and add your OpenRouter API key

5.Create a .gitignore file containing .env

6. Run the application using:py hello_ai.py

7. Enter a question in the terminal and a response will be given by the AI


## 5. Minimal Working Example
 ### What this example actually does:
 It takes a users question and returns a beginner-friendly response.

 ###The Code:
 
 ```python
 import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client = OpenAI(base_url="https://openrouter.ai/api/v1",api_key=os.getenv("OPENROUTER_API_KEY"))
question = input("Ask me anything: ")
response = client.chat.completions.create(model="mistralai/mistral-small-3.1-24b-instruct",messages=[{"role": "system", "content": "You are a helpful coding assistant for beginner developers.Keep answers simple, friendly and easy to understand."},{"role":"user","content": question}])
print(response.choices[0].message.content)
```

###Example Input:
What is python?

###Expected output:
Hello! I'm glad to help you understand Python.

Python is a popular programming language that's known for being easy to read and write.It's like a language that humans and computers can both understand!


## 6. AI Prompt Journal

### Entry 1
*Prompt:* "Help me set up Python and make 
my first AI API call"
*Tool:* Claude AI
*Helped with:* Full project setup and 
learning Python basics
*Learned:* input(), print(), variables, 
import, API keys, pip install
*Helpfulness:* 10/10

### Entry 2
*Error encountered:* NameError: name 
'genai' is not defined
*Cause:* Import alias mismatch - named it 
'generativeai' but code used 'genai'
*Fix:* import google.generativeai as genai
*Learned:* import alias must match exactly

### Entry 3
*Error encountered:* 404 model not found
*Cause:* Typo - wrote 'falsh' not 'flash'
*Fix:* Correct spelling to gemini-2.0-flash
*Learned:* Model names must be exact

### Entry 4
*Error encountered:* Quota exceeded, 
retry_delay 33 seconds
*Cause:* Free API rate limits
*Fix:* Wait and retry
*Learned:* Free APIs have rate limits

### Entry 5
*Error encountered:* Quota exceeded 
on gemini-2.0-flash
*Cause:* Daily free tier limit reached
*Fix:* Switch to gemini-1.5-flash
*Learned:* Check which models suit 
your API tier

### Entry 6
*Error encountered:* 404 models not found
*Cause:* Old library deprecated
*Fix:* Switch from google.generativeai 
to google-genai package
*Learned:* Libraries get updated - 
always check official docs

### Entry 7
*Error encountered:* SyntaxError: 
invalid syntax
*Cause:* Typed genai.com.configure 
instead of genai.configure
*Fix:* Remove the .com from the line
*Learned:* Every dot means "look inside 
this" - if it doesn't exist = error

### Entry 8
*Error encountered:* NameError: name 
'question' is not defined
*Cause:* Used variable before defining it
*Fix:* Move input() line before API call
*Learned:* Python reads top to bottom

### Entry 9
*Error encountered:* No endpoints found
*Cause:* Free model name changed 
on OpenRouter
*Fix:* Check openrouter.ai/models for 
current free models
*Learned:* Always verify model availability

### Entry 10
*Error encountered:* No endpoints found
*Cause:* Adding ":free" suffix to 
mistral model name
*Fix:* Remove ":free" suffix
*Learned:* Not all free models need suffix

### Entry 11
*Error encountered:* SyntaxError: 
invalid syntax
*Cause:* Old API key merged with 
os.getenv() code
*Fix:* Remove hardcoded key completely
*Learned:* Delete old code before 
adding new approach

### Entry 12
*Error encountered:* hello_ai.py 
not recognized
*Cause:* Missing 'py' prefix in PowerShell
*Fix:* Always use 'py hello_ai.py'
*Learned:* PowerShell needs 'py' to 
know it's Python

### Entry 13
*Observation:* Terminal cuts off responses
*Cause:* Terminal window width limitation
*Fix:* Added visual borders using "="*50
*Learned:* Always think about user 
experience not just functionality

## 7. Common Issues and Fixes

### Issue 1: pip not recognized
*Solution:* Use py -m pip install 
instead of pip install

### Issue 2: ModuleNotFoundError
*Solution:* Install missing library using
py -m pip install library-name

### Issue 3: API key exposed in screenshot
*Solution:* Immediately revoke key and 
create a new one. Never share API keys!

### Issue 4: Quota exceeded
*Solution:* Wait for rate limit reset or 
switch to different free model

### Issue 5: Model not found 404
*Solution:* Remove ":free" suffix from 
model name or check available models at 
openrouter.ai/models


## 8. References
- OpenRouter API: https://openrouter.ai
- Python docs: https://python.org
- python-dotenv: https://pypi.org/project/python-dotenv
- OpenAI library: https://pypi.org/project/openai
- Git: https://git-scm.com

This project demonstrates how beginner developers can integrate AI into simple applications using APIs,while following best practices 
for security and structure.
