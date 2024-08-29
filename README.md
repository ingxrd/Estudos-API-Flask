# Aprendendo Flask com a API Rick and Morty

Este repositório contém um projeto de aplicação web desenvolvida com Flask, que utiliza a API Rick and Morty para exibir informações sobre personagens e episódios. O projeto faz parte do Bootcamp da WoMakersCode, e usa Bootstrap para a estilização das páginas.

## Estrutura do Projeto

### Arquivos e Funções

- **`app.py`**: Arquivo principal da aplicação Flask. Define as rotas e a lógica para interagir com a API Rick and Morty. 
  - `/`: Exibe uma lista de personagens.
  - `/profile/<id>`: Mostra os detalhes de um personagem específico.
  - `/lista`: Retorna uma lista simplificada de personagens em formato JSON.
  - `/episodes`: Retorna uma lista de episódios em formato JSON.

- **`templates/`**: Diretório que contém os templates HTML utilizados pela aplicação.
  - **`layout.html`**: O layout base que inclui a estrutura principal da página e a barra de navegação. Todos os outros templates estendem este layout.
  - **`characters.html`**: Exibe a lista de personagens, com opções para visualizar detalhes de cada personagem.
  - **`profile.html`**: Mostra informações detalhadas sobre um personagem específico, como status, espécie, gênero e localização.


## Renderização 
- **Listagem de um personagem:**
![Listagem de um personagem](https://i.postimg.cc/zD7KsZsF/1.png)

- **Listagem de vários personagens:**

![Listagem de vários personagens](https://i.postimg.cc/W3wnhDhd/2.png)

- **Listagem de um episódio:**
![Episode List](https://i.postimg.cc/VL9WXnf5/episode-list.png)

- **Listagem de vários episódio**
![Episodes](https://i.postimg.cc/HkB0hm7g/episodes.png)

- **Listagem de um local e seus residentes**
![Location Lists](https://i.postimg.cc/MGH0kLyj/location-lists.png)

- **Listagem de vários locais**
![Locations](https://i.postimg.cc/CK2Gw4Nr/locations.png)
