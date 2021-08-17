try:
    from instaloader import instaloader
    import sys, os
    from colorama import Fore as F
    from instaloader.structures import Profile
    import pyfiglet
    from getpass import getpass
except:
    print("Some Dependencies are not install properly. Make Sure You Run build.py\nRunning build.py")
    exec(open('build.py').read())

bot = instaloader.Instaloader()

def banner():
    result = pyfiglet.figlet_format("\t\tINSTA-SCRAPER")
    print(F.BLUE + result + F.WHITE)
    login()

print("\n\n\t\t\t\t Make sure that 2FA is disabled \n")

user_id = input("Enter your instagram username: ")
user_pass = getpass("Enter your instagram password: ")
print()

insta_profile = input("Enter the Profile name to download Stories of: ")
print()
print("Hold on for a minute while we are connecting to the Server!!")

def login():
    try:
        you = bot.login(user=user_id, passwd=user_pass)
        print("Login Successful.\n")
        print(F.CYAN+"\tDownloading Stories.....................\n"+F.WHITE)
        main()
    except:
        print("Invalid Credentials or 2FA enabled on the ID!")
        sys.exit(1)

def main():
    try:
        profile = Profile.from_username(bot.context, username=insta_profile)
        bot.download_stories(userids=[profile.userid],filename_target='{}/stories'.format(profile.username))
        print("Downloaded Successfully.")
    except:
        print("Invalid Profile name or Private Profile!")

banner()