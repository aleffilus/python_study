import urllib.request

def check_profanity(text_to_check):
    resp = urllib.request.urlopen(("http://www.wdylike.appspot.com/?q="+text_to_check)
    resp.read()
    resp.close()
    
def read_text():
    quotes = open("C:\Projetos\Pessoal\python\git\python_study\movie_texts.txt")
    content_file = quotes.read()
    quotes.close()
    check_profanity(content_file)

read_text()

print(dir())
