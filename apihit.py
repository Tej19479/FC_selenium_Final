import requests

# List of invest_ids
invest_ids = [
    1142276,1145581,1148755,1149774,1150392,1150614,1151316,1153620,1153870,1154660,1155197,1156403,1156990,1158345,1158827,1159038,1159789,1160488,1161332,1162527,1163499,1163699,1164353,1164635,1166587,1166870,1167540,1169418,1170027,1170876,1172819,1173769,1174083,1175566,1175701,1176634,1178980,1180803,1183890,1188564,1189768,1192478,1194908,1197313,1197728,1198559

]

# API endpoint
url = 'https://www.faircent.com/p1/poolapi/fsigp_react_api.json'

# Headers for the request
headers = {
    'x-application-id': 'fe95241d3fd717dd5377d5b0649e2bf7',
    'x-application-name': 'FSIGP',
    'Content-Type': 'application/json'
}

# Common data for the POST request
data_template = {
    "uid": "1619371",
    "source": "REACT",
    "api_type": "fsigp_liquidity_move_funds",
    "sid": "6lCfIb0S9NwxlNoexeHyWZ3de5U8xn3ZyWlE2QsJ7qw",
    "fip_plan_id": "90158361"
}

# Loop through each invest_id and make the POST request
for invest_id in invest_ids:
    # Update the invest_id in the data
    data = data_template.copy()
    data["invest_id"] = invest_id

    # Make the POST request
    response = requests.post(url, headers=headers, json=data)

    # Print the response (you can modify this as per your need)
    print(f"Response for invest_id {invest_id}: {response.status_code}, {response.text}")
