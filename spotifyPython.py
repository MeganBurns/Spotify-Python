import requests
import json

uris = []

endpoint_url = "https://api.spotify.com/v1/recommendations?"
access_token = "BQDhfioHLza9hiNRfpCXDGxEw2c7Jhkhhupkt2eMRXGQHtk6VH_FRA6NBpBVDH8ZDKKzvtGESYGr3i4-R0mcb8UMvoofbnLBFgGcRi3OVO_uV4tTC2-IbXVoUnoslqrKvDQNV4UqP9JhW8CRR7_oDbLgpwvV0FCytk5n-ArNd9Ui"

#Filters:
limit = 10 #number of songs in playlist
market = "AU" #country
seed_genres = "pop" #genre
target_danceability = 0.7 #on a scale from 0-1
seed_artists = "06HL4z0CvFAxyc27GXpf02,0uq5PttqEjj3IH1bzwcrXF"



#QUERY FOR SONGS
query = f'{endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres}&target_danceability={target_danceability}&seed_artists={seed_artists}'


response = requests.get(query,
               headers={"Content-Type":"application/json",
                        "Authorization":f"Bearer {access_token}"})


print(response.json)

json_response = response.json()
for i,j in enumerate(json_response['tracks']):
            uris.append(j['uri'])
            print(f"{i+1}) \"{j['name']}\" by {j['artists'][0]['name']}")


