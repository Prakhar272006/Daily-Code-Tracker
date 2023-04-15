import requests
from datetime import datetime
TOKEN = "asd5f4a2sdd2fbdf4b"
USER_NAME = "prakhar27"
pixela_endpoint = "https://pixe.la/v1/users"
user_parameter = {
    "token" : TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# response = requests.post(url=pixela_endpoint,json=user_parameter)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id" : "graph1",
    "name" : "My Programming Graph ",
    "unit": "hrs",
    "type": "float",
    "color" : "kuro"
}
headers = {
    "X-USER-TOKEN":TOKEN,
}

# response = requests.post(url=graph_endpoint,headers=headers,json=graph_config)
# print(response.text)

user_entry_input = input("Did You Code Today?(yes/no)\n")
if user_entry_input=="yes":

    today = datetime.now()
    value_endpoint = f"https://pixe.la/v1/users/{USER_NAME}/graphs/graph1"
    value_config = {
        "date" : today.strftime("%Y%m%d"),
        "quantity":input("How many Hrs did you code today"),
    }
    
    response = requests.post(url=value_endpoint,headers=headers,json=value_config)
    print(response.text)

user_update_input = input("What do you want to perform?(update/delete/nothing)\n")
if user_update_input == "update":
    date_update = input("which date you want to update?(please give input in yyymmdd formate)\n")
    update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/graph1/{date_update}"
    update_value = input("what is the updated value?\n")
    new_pixel_data ={
        "quantity":f"{update_value}"
    }
    response = requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
    print(response.text)

elif user_update_input =="delete":
    date_delete = input("which date you want to delete?(please give input in yyymmdd formate)")
    delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/graph1/{date_delete}"
    response = requests.delete(url=delete_endpoint,headers=headers)
else:
    pass

print(f"please go and check on : https://pixe.la/v1/users/prakhar27/graphs/graph1.html")
