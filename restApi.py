import requests

import smtplib
import time

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

response_data = ""


bg_url = "http://hostname:8085/analyst/"
bg_rest_url = bg_url + "glossary/api/v2/"

login_url = bg_url + "bg.auth/login"

get_term_details = bg_url + "glossary/api/v4/search?query=notification"

get_all_glossaries_url = bg_rest_url + "glossaries"
delete_glossary_url = bg_rest_url + "glossary/" #glossary_name
delete_custom_relationship_url = bg_rest_url + "relType/" #relationship_name
delete_custom_attribute_url = bg_rest_url + "attribute/" #attribute_name

login_details = "{'user':'bg', 'password':'admin', 'namespace':'Native'}"

#
#	Actual code starts here!
#

session = requests.Session()
response = session.post(login_url, verify = False, data = login_details)
response_data += str(response) + "<br />"

response = session.get(get_term_details, verify = False, cookies = response.cookies)
print(response)
response_data += str(response) + "<br />"
glossaries = response.json()['results']


for term in glossaries:
	id = term['id']
	print(id)
	attributes = term['attributes']
	
	for attribute in attributes:
		if(attribute['id'] == 'name'):
			print (attribute['value'])

	
	
	
	
	
	
	
	
# me == my email address
# you == recipient's email address
me = "avallapre@informatica.com"
you = "avallapre@informatica.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "BG 10.1 - Rest API Calls."
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = "BG 10.1 - Rest Api calls."
html = response_data
print (html)

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.
s = smtplib.SMTP('mail.informatica.com')
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.sendmail(me, you, msg.as_string())
s.quit()
