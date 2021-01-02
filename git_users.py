import requests
import json
import csv
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def list_of_complete_users(): #returns complete git users details
    user_data=requests.get(f'https://api.github.com/users').json()
    return user_data

def particular_users(login): #returns particular user details
    particular_user_data = requests.get(f'https://api.github.com/users/{login}').json()
    return particular_user_data

def followers_list(login): #returns particular users followers
    followers_data = requests.get(f'https://api.github.com/users/{login}/followers').json()
    return followers_data

def upload_file_to_drive(): #function to upload csv to drive
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth() #client_secrets.json need to be in the same directory as the script
    drive = GoogleDrive(gauth)
    file = drive.CreateFile({"mimeType": "text/csv"})
    file.SetContentFile(r"C:\Users\Aradh\Desktop\users_report_task\users_list.csv")
    file.Upload()
    
all_user_data = list_of_complete_users()
rows = []
for user in all_user_data:
    if user["id"]%10==0:
        single_user_data = particular_users(user["login"])
        followers_details = followers_list(single_user_data["login"])

        for followers in followers_details:
            rows.append([user["id"],user["login"],single_user_data["name"],followers["id"],followers['login']])


with open("users_list.csv", 'w') as csvfile: #conversion to csv file
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['UserId', 'UserLogin', 'UserName', 'FollowerId', 'FollowerLogin'])
    csvwriter.writerows(rows)
    
upload_file_to_drive()
