import requests

def fetch(url):
    response = requests.get(url)
    return response

url = "https://api.freeapi.app/api/v1/public/randomusers"

def main():
    response = fetch(url)
    print(response.json())

if __name__ == "__main__":
    main()    