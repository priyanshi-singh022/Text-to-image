from monsterapi import client
import requests
import webbrowser

api_key ="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IjhjZWNhOGEwOWYzZmIyZmNlMWM1ZTNjODBiZjkyMzJlIiwiY3JlYXRlZF9hdCI6IjIwMjUtMDctMDhUMDY6MjI6MTguNTA0NjIzIn0.TfYdtxlKu11wUMqJCwM-V5u7_4KY7fByLck-A6UGe-U"

monster_client = client(api_key)   # Initialize client

prompt = input("Prompt: ")

model = "txt2img"

input_data = {
    'prompt': prompt,
    'negprompt': 'bad anatomy',
    'samples': 1,
    'steps': 50,
    'aspect_ratio': 'square',
    'guidance_scale': 7.5,  # <-- fixed typo here
    'seed': 2414,
}

result = monster_client.generate(model, input_data)

img_url = result['output'][0]

file_name = "generated.jpg"

#download the image
response = requests.get(img_url)

if response.status_code == 200:
    with open(file_name, 'wb') as file:
        file.write(response.content)
    print("Image downloaded")

    #opent the file
    webbrowser.open(file_name)
else:
    print("Failed to download")


