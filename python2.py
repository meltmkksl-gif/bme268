from llama_cpp import Llama
import os

script_dir = os . path . dirname ( os . path . abspath ( __file__ ) ) # Get the directory of the current script
model_path = os . path . join ( script_dir , "slm.gguf" ) # Construct the full path to the model file
model = Llama ( model_path = os.path.join(script_dir , "slm.gguf" ) ,n_ctx =256 , verbose = False )


question = "Tell me a fun fact about the human brain"  
for temp in [0.1,0.7,1.5]:
    response = model.create_chat_completion (
        messages = [
             { "role" : "system" , "content" : "You are helpful." }, 
             { "role" : "user" , "content" : question } ,
             ] ,
         
        max_tokens = 128 ,
        temperature= temp,
    )
    answer=response["choices" ][ 0 ]["message"]["content"]
    print(f" Temperature : { temp } \n Answer : { answer } \n " )