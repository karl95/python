import requests

url = "https://metshein.com/kordamine/json/tooted.json"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    tooted = data.get("tooted")    

    odavaim = min(tooted, key=lambda x: x['hind'])
    kalleim = max(tooted, key=lambda x: x['hind'])
    kat = []
    toidukaubad = [toode for toode in tooted if toode['kategooria'] == 'Toidukaubad']
    
         
    for toode in data['tooted']:
        if toode["kategooria"] not in kat: 
            kat.append(toode["kategooria"])
    size = len(kat)
    print(f"Erinevaid tootekategooriaid on: {size} ja  nendeks on: {kat}")

    print(f"Kõige odavam toode on: {odavaim['nimi']} - {odavaim['hind']}€")
    print(f"Kõige kalleim toode on: {kalleim['nimi']} - {kalleim['hind']}€")
    print(f"Kategoorias Toidukaubad on {len(toidukaubad)} toodet.")




             
else:
    print(f"Jama. Staatus: {response.status_code}")
