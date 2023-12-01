import os


Direc = "./css"
print(f"Css files: {Direc}")

files = os.listdir(Direc)
files = [f for f in files if os.path.isfile(Direc+'/'+f)] #Filtering only the files.
print(*files, sep="\n")

def get_text(filename):
    with open(Direc+"/"+filename,"r") as f:
        text=f.read()
    return text

css=[get_text(file) for file in files]

css="\n".join(css)

print(css)

with open("./docs/main.css","w") as f:
    f.write(css)