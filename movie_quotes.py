import urllib.request

def check_profanity(text_to_check):
    resp = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+"beach")
    html = resp.read()
    resp.close()
    is_profanity(html.decode("utf-8"))
    
def read_text():
    quotes = open("C:\Projetos\Pessoal\python\git\python_study\movie_texts.txt")
    content_file = quotes.read()
    quotes.close()
    check_profanity(content_file)

def is_profanity(response):
    if "true" in response:
        print("Profanity Alert!")
    elif "false" in response:
        print("This Document has no curse words!")
    else:
        print("Could not scan the document!")
        
read_text()
