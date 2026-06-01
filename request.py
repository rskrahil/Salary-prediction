# import requests

# url = 'http://localhost:5000/predict_api'
# r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

# print(r.json())

#-----------------updated----------------------
import requests

url = 'http://localhost:5000/predict_api'

# Test case 1: Valid input
r = requests.post(url, json={'experience': 2, 'test_score': 9, 'interview_score': 6})
print(f"Valid input:        {r.json()}")

# Test case 2: Missing field
r = requests.post(url, json={'experience': 2, 'test_score': 9})
print(f"Missing field:     {r.json()}")

# Test case 3: Out of range score
r = requests.post(url, json={'experience': 2, 'test_score': 15, 'interview_score': 6})
print(f"Out of range:      {r.json()}")

# Test case 4: High experience
r = requests.post(url, json={'experience': 11, 'test_score': 7, 'interview_score': 8})
print(f"High experience:   {r.json()}")