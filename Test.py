def vertrektijdenUtrecht():
    import requests
    import xmltodict

    auth_details = ('Patrick.Dijkwel@student.hu.nl', '1zC8XifCQz0754NWzPeUumzDBpCRikAl9pMbJnymq815s710wN-YVA')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=Ut'

    response = requests.get(api_url, auth=auth_details)

    vertrekXML = xmltodict.parse(response.text)

    print('Dit zijn de vertrekkende treinen')
    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindbestemming=vertrek['EindBestemming']
        vertrekspoor = vertrek['VertrekSpoor']['#text']
        vertrektijd = vertrek['VertrekTijd']
        vertrektijd = vertrektijd[-13:-8]
        try:
            vertraging = vertrek['VertrekVertragingTekst']
            if vertraging is not None:
                print('Om {} vertrekt een trein naar {:22} vanaf spoor {}\n                                              '
                          '          met een vertraging van {}\n'.format(vertrektijd, eindbestemming, vertrekspoor, vertraging))
        except KeyError:
            print('Om {} vertrekt een trein naar {:22} vanaf spoor {}\n'.format(vertrektijd, eindbestemming, vertrekspoor))

def vertrektijdenOpvragen():
    import requests
    import xmltodict

    auth_details = ('Patrick.Dijkwel@student.hu.nl', '1zC8XifCQz0754NWzPeUumzDBpCRikAl9pMbJnymq815s710wN-YVA')

    while True:
        invoer = input("Wat is uw locatie? ")
        api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + invoer

        response = requests.get(api_url, auth=auth_details)

        vertrekXML = xmltodict.parse(response.text)

        print('Dit zijn de vertrekkende treinen')
        for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
            eindbestemming=vertrek['EindBestemming']
            vertrekspoor = vertrek['VertrekSpoor']['#text']
            vertrektijd = vertrek['VertrekTijd']
            vertrektijd = vertrektijd[-13:-8]
            try:
                vertraging = vertrek['VertrekVertragingTekst']
                if vertraging is not None:
                    print('Om {} vertrekt een trein naar {:22} vanaf spoor {}\n                                              '
                          '          met een vertraging van {}\n'.format(vertrektijd, eindbestemming, vertrekspoor, vertraging))
            except KeyError:
                print('Om {} vertrekt een trein naar {:22} vanaf spoor {}\n'.format(vertrektijd, eindbestemming, vertrekspoor))
