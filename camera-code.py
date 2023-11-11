import requests


def oneColorTest(goal, other1, other2, diffVal, thresh):
    sum = 0
    for i in range(len(goal)):
        for j in range(len(goal[0])):
            if goal[i][j] > diffVal and (other1[i][j] > diffVal or other2[i][j] > diffVal):
                goal[i][j] = 0
            elif goal[i][j] > thresh:
                goal[i][j] = 255
                sum += 1
    return goal, sum


cv2_image = cv2.cvtColor(np.array(cam.raw_image), cv2.COLOR_RGB2BGR)
b,g,r = cv2.split(cv2_image)
b2, g2, r2 = cv2.split(cv2_image)
b3, g3, r3 = cv2.split(cv2_image)
grey = cv2.cvtColor(cv2_image, cv2.COLOR_BGRA2GRAY)


diffVal = 80
thresh = 90
diffR, sumR = oneColorTest(r, g, b, diffVal, thresh)
diffG, sumG = oneColorTest(g2, r2, b2, diffVal, thresh)
diffB, sumB = oneColorTest(b3, g3, r3, diffVal, thresh)


print(sumR, sumG, sumB)
if sumR > sumG and sumR > sumB:
    itemColor = "Red"
elif sumG > sumR and sumG > sumB:
    itemColor = "Green"
elif sumB > sumR and sumB > sumG:
    itemColor = "Blue"
else:
    itemColor = "No clear color"


print("Color:", itemColor)                   
display(Image.fromarray(diffR))
display(Image.fromarray(diffG))
display(Image.fromarray(diffB))


if itemColor == "Red" or itemColor == "Green":
    base_url = "https://api.airtable.com/v0/app2LMuREL2bqnlFC/Tasks"
    api_key = "patBYc7DM1JgUiTuK.e3330a41c0fa783dae0dc3224aff7c169c4a3e8c34a838c383782a6d8cecadbc"
    
    # Specify the record ID you want to update
    record_id = "patBYc7DM1JgUiTuK"
    
    # Set the headers, including the API key
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",}
    
    # Define the data to be updated. For example, to update the 'color' field:
    data = {"fields": {"Value": itemColor}}
    
    try:
        update_url = f"{base_url}/{record_id}"
        response = requests.patch(update_url, headers=headers, json=data)
        response.raise_for_status()  # Check for HTTP status code errors
    
        updated_record = response.json()
        print("Updated Record:", updated_record)
    
    except Exception as e:
        print(f"An error occurred: {e}")
    

                
#oldthresh, diffThresh = cv2.threshold(diff,diffVal,255,cv2.THRESH_BINARY)

textBox.innerText=repr(np.sum(grey))