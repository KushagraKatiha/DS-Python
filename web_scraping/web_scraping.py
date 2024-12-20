import requests

r = requests.get('https://www.w3schools.com/python/ref_requests_response.asp', allow_redirects=False)

print(r.text)

# output_file_path = "raw.txt"

# with open(output_file_path, 'w', encoding='utf-8') as file:
#     file.write(r.raw)

# output_file_path
