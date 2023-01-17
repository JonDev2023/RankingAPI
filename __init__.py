import requests

def get(database):
  rqst = requests.get(database)
  if rqst.status_code == 200:
    return rqst, rqst.json()
  if rqst.status_code == 404:
    error = rqst
    print('Error: Client Error while tring to make a request')
    return error
