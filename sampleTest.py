import requests


#response_data = ""

bg_url = "http://10.65.157.192:8084/analyst/"
bg_rest_url = bg_url + "glossary/api/v2/"

login_url = bg_url + "bg.auth/login"

get_term_api = bg_url + "glossary/api/v2/search?query="

termName = "MMBGDataLinks"

get_term_details = get_term_api + termName


login_details = "{'user':'bg', 'password':'Infa@123', 'namespace':'Native'}"

#
#	Actual code starts here!
#
def getJson():

    session = requests.Session()
    response = session.post(login_url, verify=False, data=login_details)
    response = session.get(get_term_details, verify=False, cookies=response.cookies)
    print(response)
    glossaries = response.json()['results']

    for term in glossaries:
      id = term['id']
      print(id)
      attributes = term['attributes']

    for attribute in attributes:
        if (attribute['id'] == 'name'):
            print(attribute['value'])
        if (attribute['id'] == 'infa_description'):
            print(attribute['value'])

    session.close()

getJson()
