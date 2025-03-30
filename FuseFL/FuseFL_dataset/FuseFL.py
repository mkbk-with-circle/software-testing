from revChatGPT.V3 import Chatbot
import os
api_key_gpt = "OpenAI_key"


folders = ['question_1', 'question_2', 'question_3', 'question_4', 'question_5']


prompt_loc = "Prompts/FuseFL/" 
for folder in folders:
    result_loc = "Prompts_Results/fusefl_prompt/"
    if not os.path.exists(result_loc):
       os.makedirs(result_loc)
    result_loc += folder
    if not os.path.exists(result_loc):
       os.makedirs(result_loc)

    prompt = prompt_loc+folder 
    list_files = [f for f in os.listdir(prompt) if os.path.isfile(os.path.join(prompt, f))]   
    for file in list_files:
       print(prompt+" "+file)
       if os.path.exists(prompt+"/"+file) and not os.path.exists(result_loc+"/json/"+file):
            f = open(prompt+"/"+file, "r")
            prompt_test = f.read()
            f.close()
            chatbot = Chatbot(api_key=api_key_gpt)
            result = chatbot.ask(prompt_test, model="gpt-3.5-turbo")
        
            f = open(result_loc+"/json/"+file, "w")
            f.write(result)
            f.close()
