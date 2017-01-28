"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
from random import randint
import json

isItASwear = ["jerk", "bitch", "tool", "fuck", "shit", "whore", "ass", "cunt", "dick", "crap", "David"]
isItAQ = ["?"]
isItJC = ["JOHN", "CENA"]
isThereADog = ["dog", "dogs", "shiba", "inu", "greyhound", "corgi", "doge", "boxer", "retriever",]
isThereAFly = ["jump", "fly", "flight", "jump", "hops", "hop", "high", "airplane", "heights", "takeoff"]
isThereAJoke = ["tell me a joke", "make me laugh", "tell me a funny"]


@route('/', method='GET')
def index():
    return template("chatbot.html")

def checkSwear(l):
    swearLower = [item.lower() for item in isItASwear]
    listLower = [item.lower() for item in l]
    if any(x in listLower for x in swearLower):
        print(type(l))
        return True
    return False

def handleSwear():
    return json.dumps({"animation": "no", "msg": "Hold your tongue, curr!"})

def checkDog(l):
    smallDog = [item.lower() for item in isThereADog]
    listLower = [item.lower() for item in l]
    if any(x in listLower for x in smallDog):
        return True
    return False
def handleDog():
    return json.dumps({"animation": "dog", "msg": "HAVE YOU SEEN MY AWESOME DOG? HIS NAME IS SPOT!"})

def checkQ(m):
    # print("'"+m+"'")
    if m[-1] == "?":
        return True
    return False

def handleQ():
    return json.dumps({"animation": "confused", "msg": "Wait, what?"})

def checkJC(l):
    smallJohn = [item.lower() for item in isItJC]
    listLower = [item.lower() for item in l]
    if any(x in listLower for x in smallJohn):
        return True
    return False

def handleJC():
    return json.dumps({"animation": "excited", "msg": "JOHHHNNNNNNN CENNNNAAAAAA!!!!!!!! DOODOOODODODOOOOOOOOOO"})
def checkFly(l):
    smallFly = [item.lower() for item in isThereAFly]
    listLower = [item.lower() for item in l]
    if any(x in listLower for x in smallFly):
        return True
    return False
def handleFly():
    return json.dumps({"animation": "takeoff", "msg": "Yeah, I can fly. Check it out! 3, 2, 1, TAKE OFFF!!!!"})
def checkJoke(m):
    smallJoke = [item.lower() for item in isThereAJoke]
    # listLower = [item.lower() for item in l]
    messageLower = m.lower()
    if any(x in messageLower for x in smallJoke):
        return True
    return False
def handleJoke():
    jokeList = ["How do you get a tissue to dance? You put a little boogey in it!",
                "Why was Cinderella thrown off the basketball team? She ran away from the ball.",
                "I'd tell you a chemistry joke but I know I wouldn't get a reaction.",
                "I'm glad I know sign language, it's pretty handy.",
                "A friend of mine tried to annoy me with bird puns, but I soon realized that toucan play at that game.",
                "Thieves had broken into my house and stolen everything except my soap, shower gel, towels and deodorant. Dirty Bastards."]
    i = randint(0,5)
    return json.dumps({"animation": "giggling", "msg": jokeList[i]})
@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg')
    user_list = user_message.split(" ")
    if checkSwear(user_list):
        return handleSwear()
    elif checkQ(user_message):
        return handleQ()
    elif checkDog(user_list):
        return handleDog()
    elif checkJC(user_list):
        return handleJC()
    elif checkFly(user_list):
        return handleFly()
    elif checkJoke(user_message):
        return handleJoke()
    return json.dumps({"animation": "inlove", "msg": user_message})




@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()
