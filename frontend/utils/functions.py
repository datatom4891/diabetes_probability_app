import requests

base_url = "http://backend:8000"

def submit_prediction(input_request):
  diabetes_endpoint = f"{base_url}/diabetes/probability_ui"
  response_obj = requests.post(diabetes_endpoint, json=input_request)
  return response_obj