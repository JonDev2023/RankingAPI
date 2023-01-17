import requests

def get(database):
  rqst = requests.get(database)
  if rqst:
    return rqst, rqst.json()
  else:
    print('Error: The Server Creator make a error or you make a error')

