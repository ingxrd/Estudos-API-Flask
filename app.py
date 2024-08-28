from flask import Flask, render_template
import urllib.request, json


app = Flask(__name__)

@app.route("/")
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    
    return render_template("characters.html", characters=dict["results"])


@app.route("/profile/<id>")
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    
    return render_template("profile.html", profile=dict)



@app.route('/lista') 
def get_list_characters():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)

    characters = []

    for character in dict["results"]:
        character = {
            "name": character["name"],
            "status": character["status"],
        }
        
        characters.append(character)

    return {"characters": characters}
 


 #rota para os episódios
@app.route('/episodes')
def get_episodes():
    url = "https://rickandmortyapi.com/api/episode"
    responde = urllib.request.urlopen(url)
    episodes = responde.read()
    dict = json.loads(episodes)

    episodes = []

    for episode in dict["results"]:
        episode = {
            "name": episode["name"],
            "air_date": episode["air_date"],
            "episode": episode["episode"]
        }

        episodes.append(episode)
    return {"episodes": episodes}