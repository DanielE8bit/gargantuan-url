from bottle import route, run, template, redirect, request, post, response
import random

def get_urls():
    file = open("urls.csv", "r")
    data = file.read().split("\n")
    dict = {}
    for url in data:
        temp = url.split(",")
        dict.update({temp[0]:temp[1]})
    file.close()
    return dict

@route('/') 
def index(): 
    return template('index.html', long_url = "") 

def lengthen_url(url):
    file = open("long_urls.csv", "r")
    data = file.read()
    data = data.split("\n")
    long_url = random.choice(data)
    return long_url

@post('/')
def login():
    input_url = request.forms.get('text')
    file = open("urls.csv", "a")
    longurl = lengthen_url(input_url)
    file.write("\n"+longurl+","+input_url)
    file.close()
    return template('index.html', long_url = "Your lengthened url is: " + longurl)   

@route('/<short_url>') 
def index(short_url): 
    dict = get_urls()
    long_url = dict.get(short_url)
    if long_url:
        redirect(long_url, 302)
    else:
        response.status = 400
        return 'Invalid url' 

run(host='localhost', port=8080,debug=True)