from llama_cpp import Llama
import os

script_dir = os . path . dirname ( os . path . abspath ( __file__ ) ) # Get the directory of the current script
model_path = os . path . join ( script_dir , "slm.gguf" ) # Construct the full path to the model file
model = Llama ( model_path = os.path.join(script_dir , "slm.gguf" ) ,n_ctx =256 , verbose = False )


n_ctx =256 
verbose = False 
while True:
    question = input("Enter your question: ")
    if question . strip () . lower () == "q" :
        print ( " Goodbye ! " )   
        break
response = model.create_chat_completion( 
        messages =[
            { "role" : "user","content" : " Explain gravity ."} ],
            max_tokens =200 ,
            )
reason = response["choices" ][ 0 ]["message"]["content"]
print(reason)