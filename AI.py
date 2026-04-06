from llama_cpp import Llama
import os

script_dir = os . path . dirname ( os . path . abspath ( __file__ ) ) # Get the directory of the current script
model_path = os . path . join ( script_dir , "slm.gguf" ) # Construct the full path to the model file
model = Llama ( model_path = os.path.join(script_dir , "slm.gguf" ) ,n_ctx =1050 , verbose = False )

with open("article.txt", "r",encoding="utf-8") as f:
    text = f.read()

response = model.create_chat_completion(
    messages=[
        {
            "role": "system",
            "content": "İngilizceye çevir."
        },
        {
            "role": "user",
            "content": text
        }
    ],
    max_tokens=1050,
    
)

print(response) 