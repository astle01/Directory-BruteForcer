import requests

domain = input("Enter domain to bruteforce :")

file_name = input("Enter wordlist file :")
f = open(file_name,"r")

for i in f.readlines():

    url = domain + i[0:len(i)-1] #to remove blankspaces after words
    response = requests.get(url)
    if response.status_code==200:
        print(url)

f.close()
