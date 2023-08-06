import json
import os
import jsonlines

iname = []
text = []
for file in os.listdir("./"):
    if file.endswith(".png"):
        iname.append(file)
    if file.endswith('.txt'):
        f = open(file, "r")
        text.append(f.read())
captions = []
for i,j in zip(iname,text):
    captions.append({"file_name": i, "text": j})

# json_obj = json.dumps(captions, indent= 4)
# print(json_obj)

# with open("metadata.json", "w") as f:
#     f.write(json_obj)
    
with open("metadata.jsonl", 'w') as f:
    for entry in captions:
        f.write(json.dumps(entry)+ "\n")
