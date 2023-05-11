import json

def main():
    text = open("news.txt", "r").readlines()
    sub_fptr = open("subs.json","r")
    subs = json.load(sub_fptr)
    print(subs,type(subs))

    for x, y in subs.json(sub_fptr):
        text=text.replace(x,y)

    
    fptr = open("betternews.txt", "w")
    fptr.write(text)
    fptr.close()