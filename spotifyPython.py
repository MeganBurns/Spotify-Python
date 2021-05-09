import requests
import json
uris = []


endpoint_url = "https://api.spotify.com/v1/recommendations?"
access_token = ""

#Filters:
limit = 15
market = "AU"
#seed_tracks = "4PvbbMYL4fkToni5BLaYRb,2drtd6SptpMJ1KylMQ7mrE,43E0f1S0rOGCo6YYRYHjHP,3dNjUFt6EFU4Gq6Q5vfJqf,6Qjk6ZEltFhFqCIU2cp4Yd"
seed_tracks = "6VCeywT4JeawuZOUkQ1okx,1kqc6U8hVYZhY0gFGQclCz"
seed_artists ="5DGJC3n9DS0Y9eY5ul9y0O,3l0CmX0FuQjFxr8SK7Vqag,6beUvFUlKliUYJdLOXNj9C"

#QUERY FOR SONGS
#query = f'{endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres}&target_danceability={target_danceability}&seed_artists={seed_artists}'
query = f'{endpoint_url}limit={limit}&market={market}&seed_tracks={seed_tracks}&seed_artists={seed_artists}'

response = requests.get(query,
               headers={"Content-Type":"application/json",
                        "Authorization":f"Bearer {access_token}"})


print(response.json)

json_response = response.json()
for i,j in enumerate(json_response['tracks']):
            uris.append(j['uri'])
            print(f"{i+1}) \"{j['name']}\" by {j['artists'][0]['name']}")



user_id = "megan272727"
playlist_url = f"https://api.spotify.com/v1/users/{user_id}/playlists"

request_body = json.dumps({
          "name": "I coded this Playlist",
          "description": "I'm going to create an environment so gay",
          "public": False # let's keep it between us - for now
        })

response = requests.post(url = playlist_url, data = request_body, headers={"Content-Type":"application/json", "Authorization":"Bearer " + access_token})
print(response.status_code)

playlist_id = response.json()['id']


fill_playlist = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

request_body = json.dumps({
          "uris" : uris
        })
response = requests.post(url = fill_playlist, data = request_body, headers={"Content-Type":"application/json", "Authorization":f"Bearer {access_token}"})
print(response.status_code)
