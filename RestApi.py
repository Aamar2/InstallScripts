import requests
import json


class RestApi:
    login_details = "{'user':'bg', 'password':'Infa@123', 'namespace':'Native'}"

    session = requests.Session()
    response = ""
    def __init__(self,ATUrl,TermName):
        self.ATUrl = ATUrl
        self.TermName = TermName

    def loginUrl(self):
        return self.ATUrl + "bg.auth/login"

    def term_query(self):
        return self.ATUrl + "glossary/api/v2/search?query=" + self.TermName

    def term_details_url(self,attributes):
        searchString = "&attributes="
        x=""
        for i in attributes:
            x = x + searchString + i
        return self.ATUrl + "glossary/api/v4/term?id=" + str(self.getTermID()) + "&attributes=" + x

    def getJson(self):
        response = self.session.post(self.loginUrl(), verify=False, data=RestApi.login_details)
        #print(response.cookies)

        response = self.session.get(self.term_query(), verify=False, cookies=response.cookies)
        #print(self.term_query())
        self.response = response
        #print(response)
        glossaries = response.json()['results']
        #print(glossaries)
        return glossaries

    def getTermID(self):
        glossaries = self.getJson()
        for term in glossaries:
            id = term['id']
        return str(id)

    def getTermAttribute(self,attributeName):
        glossaries = self.getJson()
        for term in glossaries:
            attributes = term['attributes']
        for attribute in attributes:
            if (attribute['id'] == attributeName):
                print(attribute['value'])

    def getTermDetails(self,attributeName):
        print(self.term_details_url(attributeName))
        response = self.session.get(self.term_details_url(attributeName), verify=False, cookies=self.response.cookies)
        attributes = response.json()['term']['attributes']
        for attribute in attributes:
            print(attribute['value'])




AtUrl = "http://invr74dsg939:8085/analyst/"
TermName = "Share"

rest = RestApi(AtUrl,TermName)
rest.getTermID()
#rest.getTermAttribute('phase')
name = ['name','phase','infa_description','Not Same As']
rest.getTermDetails(name)


#print(terms["results"])



