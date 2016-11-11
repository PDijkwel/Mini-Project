#test
def stationsnamen(stat):
    import requests
    import xmltodict

    auth_details = ('Patrick.Dijkwel@student.hu.nl', '1zC8XifCQz0754NWzPeUumzDBpCRikAl9pMbJnymq815s710wN-YVA')
    api_url = 'http://webservices.ns.nl/ns-api-stations-v2'
    response1 = requests.get(api_url, auth=auth_details)
    stationXML = xmltodict.parse(response1.text)
    langeNaam = ""
    lijstStations = []
    lijstCodeNamen = []
    for station in stationXML['Stations']['Station']:
        stationNaamKort = station['Namen']['Kort']
        stationNaamMiddel = station['Namen']['Middel']
        stationNaamLang = station['Namen']['Lang']
        codeNaam = station['Code']

        if stat == codeNaam:
            lijstCodeNamen.append(codeNaam)
            langeNaam += stationNaamLang

        elif stat in stationNaamKort:
            lijstStations.append(stationNaamKort)
        elif stat in stationNaamMiddel:
            lijstStations.append(stationNaamMiddel)
        elif stat in stationNaamLang:
            lijstStations.append(stationNaamLang)

    if stat in lijstCodeNamen:
        return('Dit zijn de vertrekkende treinen van station ' + stat + "(" + langeNaam + ")" '\n' + vertrektijdenOpvragen(stat))
    elif stat in lijstStations:
        return('Dit zijn de vertrekkende treinen van station ' + stat + '\n' + vertrektijdenOpvragen(stat))
    else:
        return("Het ingevoerde station bestaat niet")

def vertrektijdenUtrecht():
    import requests
    import xmltodict

    auth_details = ('Patrick.Dijkwel@student.hu.nl', '1zC8XifCQz0754NWzPeUumzDBpCRikAl9pMbJnymq815s710wN-YVA')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=Ut'

    response = requests.get(api_url, auth=auth_details)

    vertrekXML = xmltodict.parse(response.text)
    Tijden = ""
    Tijden += ('Dit zijn de vertrekkende treinen van station: Utrecht Centraal\n'+ '\n')
    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindbestemming=vertrek['EindBestemming']
        vertrektijd = vertrek['VertrekTijd']
        vertrekspoor = vertrek['VertrekSpoor']['#text']
        vertrektijd = vertrektijd[-13:-8]
        treinsoort = vertrek['TreinSoort']
        try:
            vertraging = vertrek['VertrekVertragingTekst']
            if vertraging is not None:
                Tijden += ('Om {} vertrekt een trein naar {:40} vanaf spoor {:20} met een vertraging van {}\n'.format(vertrektijd, eindbestemming, vertrekspoor, vertraging))
        except KeyError:
            Tijden += ('Om {} vertrekt een trein naar {:40} vanaf spoor {}\n'.format(vertrektijd, eindbestemming, vertrekspoor))
    return Tijden

def vertrektijdenOpvragen(invoer):
    import requests
    import xmltodict
    Tijden = ""

    auth_details = ('Patrick.Dijkwel@student.hu.nl', '1zC8XifCQz0754NWzPeUumzDBpCRikAl9pMbJnymq815s710wN-YVA')


    api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + invoer

    response = requests.get(api_url, auth=auth_details)

    vertrekXML = xmltodict.parse(response.text)

    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindbestemming=vertrek['EindBestemming']
        vertrekspoor = vertrek['VertrekSpoor']['#text']
        vertrektijd = vertrek['VertrekTijd']
        vertrektijd = vertrektijd[-13:-8]
        try:
            vertraging = vertrek['VertrekVertragingTekst']
            if vertraging is not None:
                Tijden += ('Om {} vertrekt een trein naar {:22} vanaf spoor {}\nmet een vertraging van {}\n\n'.format(vertrektijd, eindbestemming, vertrekspoor, vertraging))
        except KeyError:
            Tijden += ('Om {} vertrekt een trein naar {:22} vanaf spoor {}\n'.format(vertrektijd, eindbestemming, vertrekspoor))
    return Tijden
