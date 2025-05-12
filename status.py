import requests

def comprobar_estado():
    r = requests.get("http://api.ejemplo.com/estado")

    print(r)

comprobar_estado()



