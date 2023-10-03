import requests

r = requests.get('https://corona.askbhunte.com/api/v1/data/nepal')
print(r.text)
print(r.status_code)
# # post request
# url ="www.something.com"
# data = {
#     "p1":2,
#     "p2":4
# }
# r2 =requests.post(url=url,data=data)
