import requests

API_KEY = input("enter the api")

 
history = []

def ask_groq(question):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    
    history.append({"role": "user", "content": question})

    data = {"model": "llama-3.1-8b-instant","messages": history}

    try:
        response = requests.post(url, headers=headers, json=data,timeout=10)
        result = response.json()
    except Exception as e:
        print(e)
    if "choices" not in result:
        return f"error：{result}"

    answer = result["choices"][0]["message"]["content"]

   
    history.append({"role": "assistant", "content": answer})

    return answer
MAX_HISTORY = 10  

def trim_history():
    global history
    if len(history) > MAX_HISTORY:
        history = history[-MAX_HISTORY:]


print("lets start（press E to exit）")

try:
    while True:
        user_input = input("you： ")
        if user_input.lower() == "e":
            break


        try:
            reply = ask_groq(user_input)
            print("AI：", reply)
            trim_history()
        except Exception as e:
            print(e)
except Exception as e:
    print(e)
