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
    character = json.loads(data)

    #todas as minhas urls da origem  serão guardadas
    # Criação do dicionário de perfil
    profile = {
        "image": character["image"],
        "name": character["name"],
        "status": character["status"],
        "species": character["species"],
        "gender": character["gender"],
        "origin": {
            "name": character["origin"]["name"],
            "url": "/locations/" + str(character["origin"]["url"].split('/')[-1])  # Assume que a URL termina com o ID
        },
        "location": {
            "name": character["location"]["name"],
            "url": "/locations/" + str(character["location"]["url"].split('/')[-1])  # Assume que a URL termina com o ID
        }
    }    
    
    return render_template("profile.html", profile=profile)



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
    url = "https://rickandmortyapi.com/api/episode/"
    response = urllib.request.urlopen(url)
    episodes = response.read()
    data = json.loads(episodes)

    episodes = []

    for episode in data["results"]:
        episode_info = {
            "name": episode["name"],
            "air_date": episode["air_date"],
            "episode": episode["episode"],
            "id": episode["id"] 
        }
        episodes.append(episode_info)

    return render_template("episodes.html", episodes=episodes)


#rota para episode by id

@app.route("/episodes/<id>")
def get_episode(id):
    url = "https://rickandmortyapi.com/api/episode/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    episode = json.loads(data)

    characters = []

    for characters_url in episode['characters']:
        characters_response = urllib.request.urlopen(characters_url)
        characters_data = characters_response.read()
        character = json.loads(characters_data)
        characters.append({
            "id": character["id"],
            "url": "/profile/" + str(character["id"])
        })

        episode['characters'] = characters 

    
    return render_template("episode.html", episode=episode)





#rota para locations
@app.route('/locations')
def get_locations():
    url = "https://rickandmortyapi.com/api/location"
    response = urllib.request.urlopen(url)
    locations = response.read() 
    data = json.loads(locations)

    locations = []

    for location in data["results"]:
        location_info = {
            "name": location["name"],
            "dimension": location["dimension"],
            "type": location["type"],
            "id": location["id"]      
        }
        locations.append(location_info)

    return render_template("locations.html", locations=locations)

#location by id

@app.route("/locations/<id>")
def get_location(id):
    url = "https://rickandmortyapi.com/api/location/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    location = json.loads(data)

    #Aplicando a lógica para renderizar as informações de residents 

    #Primeiro passo: criação de array vazio para guardar infos dos residents
    residents = []

    #segundo passo: criação de um laço for para iterar sobre os residents 

    for resident_url in location['residents']:
        resident_response = urllib.request.urlopen(resident_url)
        resident_data = resident_response.read()
        resident = json.loads(resident_data)
        residents.append({
            "id": resident["id"],
            "name": resident["name"],
            "url": "/profile/" + str(resident["id"])
        })

        location['residents'] = residents 
    
    return render_template("location.html", locations=location)
