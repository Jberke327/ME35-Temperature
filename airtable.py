import wifiLib
import secrets
import urequests as requests


ID = secrets.AirtableBaseID
apiKey = secrets.AirtableAPIKey
color = secrets.AirtableColorID
table = "Tasks"

baseUrl = "https://api.airtable.com/v0/%s/%s" % (ID, table)
headers = {"Authorization": f"Bearer {apiKey}",}

#Connect to Airtable API and get data, Code taken from API example code
def getColor():
    try:
        response = requests.get(baseUrl, headers=headers)
        data = response.json()
        records = data.get('records', [])
        for record in records:
            if record["id"] == color:
                print(record["fields"])
                return record["fields"]["Value"]
        return None
            
    except Exception as e:
        print(f"An error occurred: {e}")
