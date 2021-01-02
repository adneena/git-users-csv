# git-users-csv
TASK 1
Get the users and their followers in the CSV format
1. To get the list of users https://api.github.com/users 
2. Get the list of user Ids divisible by 10 - 
3. Iterate the result and get the user details https://api.github.com/users/{login}
4. Get the followers list for that user https://api.github.com/users/{login}/followers

created 3 functions;
#one for returning all the user_data after converting them to json.
#one for returning particular user details and returning them in json format
#other function for returning the followers list from the login passed from the users and return them in json.

then using a for loop filtered the users with userid divisible by 10.
Atlast using csvwriter converted the filtered data to csv file.
