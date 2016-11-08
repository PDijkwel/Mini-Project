tekst = 'wat=wat'
for i in tekst:
    regelsplit = tekst.split('=')
    regelsplit[1] = 'Graftak'
    print(regelsplit+regelsplit[1])
