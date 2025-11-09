import requests

base_url = "http://127.0.0.1:8000"

def submit_prediction(input_request):
  diabetes_endpoint = f"{base_url}/diabetes/probability"
  response_obj = requests.post(diabetes_endpoint, json=input_request)
  return response_obj