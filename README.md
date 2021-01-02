# git-users-csv
# TASK 1
###### Get the users and their followers in the CSV format
* To get the list of users https://api.github.com/users 
* Get the list of user Ids divisible by 10 - 
* Iterate the result and get the user details https://api.github.com/users/{login}
* Get the followers list for that user https://api.github.com/users/{login}/followers

###### created 3 functions
* one for returning all the user_data after converting them to json.
* one for returning particular user details and returning them in json format
* other function for returning the followers list from the login passed from the users and return them in json.
* then using a for loop filtered the users with userid divisible by 10.
* Atlast using csvwriter converted the filtered data to csv file.


# TASK 2
###### Upload the constructed CSV file into Google Drive.
* created credentials for google drive api.
    * open google cloud platform
    * create a project
    * Choose API and credentials option and enable API services
    * click create credentials options
    * select Oauth client ID
    * select application type and save
    * get the credentials from the dashboard. (copy or download the file)
    * create client_secrets.json file in the same project directory and paste the credentials
* Run the program, this will take you to upload csv file to drive. we will get as The authentication flow has completed.
* created upload_file_to_drive function to upload csv file to drive
