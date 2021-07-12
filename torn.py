import requests, pprint

def test(apikey):
    print('Use the comma to look for multiple fields\n')
    while True:
        fields=input('Available fields: \nammo, attacks, attacksfull, bars, basic, battlestats, \nbazaar, cooldowns, crimes, discord, display, education, \nevents, gym, hof, honors, icons, inventory, \njobpoints, log, medals, merits, messages, money, \nnetworth, notifications, perks, personalstats, profile, properties, \nreceivedevents, refills, reports, revives, revivesfull, skills, \nstocks, timestamp, travel, weaponexp, workstats: \n\n')
        if ' ' in fields:
            fields=fields.replace(' ','')
        url='https://api.torn.com/user/?selections='+fields+'&key='+apikey
        r=requests.get(url)
        if 'error' in r.json():
            print('Wrong API key or fields!')
            with open('apikey.txt', mode='w') as f:
                f.write('')

        pprint.pprint(r.json())


try:
    with open('apikey.txt', mode='r') as f:
        apikey = f.read()
        if len(apikey)!=16:
            raise ValueError('The saved API key lenght is wrong')
        test(apikey)
except:
    apikey=input('Enter your API key: ')
    while len(apikey)!=16:
        apikey=input('Your API key lenght is wrong! Try again: ')
    with open('apikey.txt', mode='w') as f:
        f.write(apikey)
    test(apikey)
