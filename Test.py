import requests
import xmltodict

auth_details = ('Patrick.Dijkwel@student.hu.nl', '1zC8XifCQz0754NWzPeUumzDBpCRikAl9pMbJnymq815s710wN-YVA')

invoer = input("Wat is uw locatie? ")
api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + invoer

response = requests.get(api_url, auth=auth_details)

vertrekXML = xmltodict.parse(response.text)

print('Dit zijn de vertrekkende treinen')
for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
    eindbestemming=vertrek['EindBestemming']
    vertrektijd = vertrek['VertrekTijd']
    vertrektijd = vertrektijd[-13:-8]
    try:
        vertraging = vertrek['VertrekVertragingTekst']
        if vertraging is not None:
            print('Om '+vertrektijd+' vertrekt een trein naar '+ eindbestemming + ' met een vertraging van ' + vertraging)
    except KeyError:
        print('Om '+vertrektijd+' vertrekt een trein naar '+ eindbestemming)


