import requests

def client():
  # data = {
  #   "username": "resttest",
  #   "email": "test@rest.com", 
  #   "password1": "changeme123",
  #   "password2": "changeme123",
  #   }

  # response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/",
    # data=data)
  token_h = "Token 413248f9dd4c6a4e17a60bed4b1ca4f9d166c355"
  headers = {"Authorization": token_h}

  response = requests.get("http://127.0.0.1:8000/api/profiles/",
    headers=headers)

  print("Status code: ", response.status_code)
  response_data = response.json()
  print(response_data)

if __name__ == "__main__":
  client()