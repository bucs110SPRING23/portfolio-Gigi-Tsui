import json

def main():
    text = open("news.txt", "r").readlines()
    sub_fptr = open("subs.json","r")
    subs = json.load(sub_fptr)
    print(subs,type(subs))

    for k, v in subs.items(sub_fptr):
        text=text.replace(k,v)

    
    fptr = open("betternews.txt", "w")
    fptr.write(text)
    fptr.close()

main()