import json

def main():
    news = open("assets/news.txt", "r").read().lower()
    sub_fptr = open("subs.json","r")
    sub = json.load()
    print(sub,type(sub))

    for k, v in sub.items(sub_fptr):
        text=text.replace(k,v)

    
    fptr = open("betternews.txt", "w")
    fptr.write(news)
    fptr.close()

main()