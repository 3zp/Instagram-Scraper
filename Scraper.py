import requests
import json
user = str(input("Enter Username : "))
hd = {
    "Host": "www.instagram.com",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Cookie": "csrftoken=missing; sessionid=missing; mid=missing",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
    "Accept-Language": "en-us",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}
req = requests.get(f"https://www.instagram.com/{user}/?__a=1", headers=hd)
idd = json.loads(req.text)["graphql"]["user"]["id"]
bio = json.loads(req.text)["graphql"]["user"]['biography']
name = json.loads(req.text)["graphql"]["user"]['full_name']
pfp = json.loads(req.text)["graphql"]["user"]['profile_pic_url_hd']
private = json.loads(req.text)["graphql"]["user"]['is_private']
verified = json.loads(req.text)["graphql"]["user"]['is_verified']
business = json.loads(req.text)["graphql"]["user"]['is_business_account']
recent = json.loads(req.text)["graphql"]["user"]['is_joined_recently']
followers = json.loads(req.text)["graphql"]["user"]['edge_followed_by']['count']
following = json.loads(req.text)["graphql"]["user"]['edge_follow']['count']
print("User ID : "+idd)
print("Full name : "+name)
print("Biography : "+bio)
print("Followers :",followers)
print("Following :",following)
print("Private Account :",private)
print("Verified Account :",verified)
print("Business Account :",business)
print("Recently Joined :",business)
print("Profile Picture :",pfp)
input()
