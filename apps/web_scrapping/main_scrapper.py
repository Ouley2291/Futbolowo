import requests
import json


def download_data(group_id):
    url=f"https://competition-api-pro.laczynaspilka.pl/api/bus/competition/v1/plays/{group_id}/tables"
    response=requests.get(url) #udajemy przeglądarke
    if response.status_code ==200:
        api_data=response.json()
        print("Pobrałem dane")
        return api_data
    else:
        print(f"Wystąpił błąd w pobieraniu: {response.status_code}")
        return None
        
        
        
bomba=download_data("e63d66b8-ca92-4f75-bf34-fb412fb52dd0")