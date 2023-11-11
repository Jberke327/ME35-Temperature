import wifiLib
import secrets
import urequests as requests


baseId = secrets.AirtableBaseID
apiKey = secrets.AirtableAPIKey
colorID = secrets.AirtableColorID
tableName = "Tasks"

baseUrl = "https://api.airtable.com/v0/%s/%s" % (baseId, tableName)
headers = {"Authorization": f"Bearer {apiKey}",}

def getColor():
    try:
        response = requests.get(baseUrl, headers=headers)
        data = response.json()
        records = data.get('records', [])
        for record in records:
            if record["id"] == colorID:
                print(record["fields"])
                return record["fields"]["Value"]
        return None
            
    except Exception as e:
        print(f"An error occurred: {e}")