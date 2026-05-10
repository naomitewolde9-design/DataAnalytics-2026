contact_info = {"name": "Naomi Tewolde", "address": "222 silver ln", "city": "Charlotte", "state": "North Carolina", "zip": "22222"}

print(contact_info["name"])
print(contact_info["address"])
print(contact_info["city"])
print(contact_info["state"])
print(contact_info["zip"])

print(f"""{contact_info["name"]}
{contact_info["address"]} 
{contact_info["city"]}, {contact_info["state"]}
{contact_info["zip"]}""")

#Naomi Tewolde
#222 silver ln 
#Charlotte, North Carolina
#22222

contact_info.pop("name")
print(contact_info)
#{'address': '222 silver ln', 'city': 'Charlotte', 'state': 'North Carolina', 'zip': '22222'}

full_name_info = {"first name": "Naomi", "last name": "Tewolde"}
print(full_name_info)
#{'first name': 'Naomi', 'last name': 'Tewolde'}

full_name_info.update({"honorific": "Ms."})
print(full_name_info)
#{'first name': 'Naomi', 'last name': 'Tewolde', 'honorific': 'Ms.'}

contact_info.update({"full_name": full_name_info})
print(contact_info)
#{'address': '222 silver ln', 'city': 'Charlotte', 'state': 'North Carolina', 'zip': '22222', 'full_name': {'first name': 'Naomi', 'last name': 'Tewolde', 'honorific': 'Ms.'}}

#formating with updated information
#adding the ms. and first and last name together 1st, then separating address line, with city state and zip for the correct format 
print(f"""
{contact_info["full_name"]["honorific"]} {contact_info["full_name"]["first name"]} {contact_info["full_name"]["last name"]} 
{contact_info["address"]}
{contact_info["city"]},{contact_info["state"]} {contact_info["zip"]}
""")
#Ms. Naomi Tewolde 
#222 silver ln
#Charlotte,North Carolina 22222