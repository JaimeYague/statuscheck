import requests

def comprobar_estado():
    r = requests.get("http://api.ejemplo.com/estado", verify=False)
    if r.status_code == 200:
        print("OK!")
    else:
        print("ERROR")

    print(r)

comprobar_estado()



