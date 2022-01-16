import os
import sys
import json
 
path = "files/"
dir_list = os.listdir(path)
clean = {"clean", "c", ""}
noisy = {"noisy", "n"}
quality = {};

def main():
    for i in dir_list:
        answer = False
    
        if ".mp3" in i:
            os.system("ffplay -autoexit " + path + i)
            while(answer == False):
                print("Was the '" + i + "' audio clean/c or noisy/n ?")
                choice = raw_input().lower()
                if choice in clean:
                    answer = True
                    choice = "Clean"
                elif choice in noisy:
                    answer = True
                    choice = "Noisy"
                else:
                    answer = False
        
            quality[i] = choice
            json_quality = json.dumps(quality)

    with open("audio.json", "w") as outfile:
        outfile.write(json_quality)

main()

