import requests

# COMPLETE URL
url = 'INSIRA A URL'

# REQUESTS (GET, POST, PUT, PATCH or DELETE)
op = 'GET'

# HEADERS
head = {
    'var1': 'value1',
    'var2': 'value2'
}

###################################################################
# CURL FUNCTION

# GET REQUEST
if op == 'GET':
  # USING HEADERS
  if headers_on == True:
    response = requests.get(url, headers=headers)
    output = response.text
    output = output.split('\n')
    for x in output:
      print(x)
  # NOT USING HEADERS
  else:
    if headers_on == False:
      response = requests.get(url, headers=headers)
      output = response.text
      output = output.split('\n')
      for x in output:
        print(x)

# POST REQUEST
if op == 'POST':
  # USING HEADERS
  if headers_on == True:
    response = requests.post(url, headers=headers)
    output = response.text
    output = output.split('\n')
    for x in output:
      print(x)
  # NOT USING HEADERS
  else:
    if headers_on == False:
      response = requests.post(url, headers=headers)
      output = response.text
      output = output.split('\n')
      for x in output:
        print(x)

# PUT REQUEST
if op == 'PUT':
  # USING HEADERS
  if headers_on == True:
    response = requests.put(url, headers=headers)
    output = response.text
    output = output.split('\n')
    for x in output:
      print(x)
  # NOT USING HEADERS
  else:
    if headers_on == False:
      response = requests.put(url, headers=headers)
      output = response.text
      output = output.split('\n')
      for x in output:
        print(x)

# PATCH REQUEST
if op == 'PATCH':
  # USING HEADERS
  if headers_on == True:
    response = requests.patch(url, headers=headers)
    output = response.text
    output = output.split('\n')
    for x in output:
      print(x)
  # NOT USING HEADERS
  else:
    if headers_on == False:
      response = requests.patch(url, headers=headers)
      output = response.text
      output = output.split('\n')
      for x in output:
        print(x)

# DELETE REQUEST
if op == 'DELETE':
  # USING HEADERS
  if headers_on == True:
    response = requests.delete(url, headers=headers)
    output = response.text
    output = output.split('\n')
    for x in output:
      print(x)
  # NOT USING HEADERS
  else:
    if headers_on == False:
      response = requests.delete(url, headers=headers)
      output = response.text
      output = output.split('\n')
      for x in output:
        print(x)
    
