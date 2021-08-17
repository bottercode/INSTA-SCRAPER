try:
    from colorama import Fore as F
    import sys,os
    import requests
    import instaloader
    import pyfiglet
    from bs4 import BeautifulSoup

except:
    print("All the prerequisites are not fulfilled")
    sys.exit(1)


profile_search = instaloader.Instaloader()
profile_name = input("Enter the profile name to see the Details: ")

def Start():
    result = pyfiglet.figlet_format("\tINSTA-SCRAPER")
    print(F.BLUE + result)
    Bio()

def Bio():
    try:
        print(F.YELLOW+"\n\t\t\tProfile Bio: "+F.BLUE)
        profile = instaloader.Profile.from_username(profile_search.context, profile_name)
        print(profile.biography)
        Details()

    except:
        print(F.RED+"Profile seems to be invalid !"+F.WHITE)
        sys.exit(1)

URL = f"https://www.instagram.com/{profile_name}/"

def Details():
     print(F.YELLOW+"\n\t\t\tProfile Data: "+F.CYAN+"\n")
     html = requests.get(URL, headers={'User-agent': 'My User Agent 1.0'})
     soup = BeautifulSoup(html.text, 'lxml')

     data = soup.find_all('meta',property='og:description')
     text = data[0].get('content').split()

     user = '%s %s %s' % (text[-3], text[-2], text[-1])
     followers = text[0]
     following = text[2]

     print('User:', user)
     print('Followers:', followers)
     print('Following:', following) 


Start()