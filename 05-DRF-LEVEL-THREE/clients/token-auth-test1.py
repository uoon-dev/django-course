import requests

def client():
  token_h = "Token b6f3005353d00ab065e89962d944f6cb9dc81bbd"
  # credentials = {"username": "admin", "password": "1234"}

  # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/",
  #   data=credentials)

  headers = {"Authorization": token_h}

  response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)

  print("Status code: ", response.status_code)
  response_data = response.json()
  print(response_data)

if __name__ == "__main__":
  client()