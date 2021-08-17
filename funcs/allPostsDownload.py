try:
    import instaloader
    import sys, os
    from colorama import Fore as F
    import pyfiglet
except:
    print("Some Dependencies are not install properly. Make Sure You Run build.py")
    exec(open('build.py').read())

bot = instaloader.Instaloader()

def banner():
    result = pyfiglet.figlet_format("\t\tINSTA-SCRAPER")
    print(F.BLUE + result)
    login()

print("\n\n\t\t\t\t DMake sure that 2FA is disabled \n")

user_id = input("Enter your instagram username: ")
user_pass = input("Enter your instagram password: ")
print()

insta_profile = input("Enter the Profile name to download posts of: ")
print()

print("Hold on for a minute while we are connecting to the Server!!")

def login():
    try:
        you = bot.login(user=user_id, passwd=user_pass)
        print(F.WHITE+"Login Successful.\n")
        print("\tDownloading Posts.....................\n")
        main()
    except:
        print("Invalid Credentials or 2FA enabled on the ID!")
        sys.exit(1)

def main():
    try:
        bot.download_profile(profile_name=insta_profile)
        print("Downloaded Successfully.")
    except:
        print("Invalid Profile name or Private Profile!")

banner()