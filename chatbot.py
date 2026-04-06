from llama_cpp import Llama
import os

script_dir = os . path . dirname ( os . path . abspath ( __file__ ) ) # Get the directory of the current script
model_path = os . path . join ( script_dir , "slm.gguf" ) # Construct the full path to the model file
model = Llama ( model_path = os.path.join(script_dir , "slm.gguf" ) ,n_ctx =512 , verbose = False )


n_ctx =512 
verbose = False 
while True:
    question = input("Enter your question: ")
    if question . strip () . lower () == "q" :
        print ( " Goodbye ! " )   
        break

    response = model.create_chat_completion( # Call the create_chat_completion method of the model to generate a response
        messages =[
            { "role" : "system",
             "content" : " You are a helpful assistant ."} ,
             { "role" : "user", "content" : question } ,] , max_tokens =256 ,)
    print ( " AI : " , response[ "choices" ][0][ "message" ][ "content" ])
