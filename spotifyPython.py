import requests
import json
uris = []


endpoint_url = "https://api.spotify.com/v1/recommendations?"
access_token = "BQAvhhVNQnBVVOjMZea9yGgNNH18_VwUwMFefb-Sf7Fq5X3lyVpFo6al-GaEWqztCq9kQqyDsb6-R0cHeE3GppTVRnb0fr2b1yEFpBDoOSHN57ZIlwz7pyq45NeuScJHcZ1xpx_6tmvZ8QqNjZHNYsuXhSjVPvowG9m3wFzpPvmG"

#Filters:
limit = 10 #number of songs in playlist
market = "AU" #country
#seed_genres = "indie-pop,pop" #genre
#target_danceability = 0.7 #on a scale from 0-1
#seed_artists = "06HL4z0CvFAxyc27GXpf02,3l0CmX0FuQjFxr8SK7Vqag,4QkSD9TRUnMtI8Fq1jXJJe"
seed_tracks = "4PvbbMYL4fkToni5BLaYRb,2drtd6SptpMJ1KylMQ7mrE,43E0f1S0rOGCo6YYRYHjHP,3dNjUFt6EFU4Gq6Q5vfJqf,6Qjk6ZEltFhFqCIU2cp4Yd"


#QUERY FOR SONGS
#query = f'{endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres}&target_danceability={target_danceability}&seed_artists={seed_artists}'
query = f'{endpoint_url}limit={limit}&market={market}&seed_tracks={seed_tracks}'

response = requests.get(query,
               headers={"Content-Type":"application/json",
                        "Authorization":f"Bearer {access_token}"})


print(response.json)

json_response = response.json()
for i,j in enumerate(json_response['tracks']):
            uris.append(j['uri'])
            print(f"{i+1}) \"{j['name']}\" by {j['artists'][0]['name']}")


