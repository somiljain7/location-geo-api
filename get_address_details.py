from IPython import embed
import requests
import re
import xml.etree.ElementTree as ET
def value_from_response_json(result):
    lat=None
    lng=None
    for i in range(len(result["results"])):
        if(lat==None and lng==None):
            for j in result["results"][i]:
                if(j=="geometry"):
                    lat=result["results"][i][j]["location"]['lat']
                    lng=result["results"][i][j]["location"]['lng']
                    break
    return lat,lng

def extract_lat_long_via_address(address_or_zipcode):
    try:
        lat, lng = None, None
        GOOGLE_API_KEY = 'ADD-HERE' 
        api_key = GOOGLE_API_KEY
        address_or_zipcode = re.sub('[^.,a-zA-Z0-9 \n\.]', '', address_or_zipcode)
        base_url = "https://maps.googleapis.com/maps/api/geocode/json"
        endpoint = f"{base_url}?address={address_or_zipcode}&key={api_key}"
        r = requests.get(endpoint)
        if r.status_code not in range(200, 299):
                return None, None
        try:
                result = r.json()
                lat,lng=value_from_response_json(result)
                return lat, lng
        except:
                pass
                return lat, lng
    except Exception as e:
        print(e)
def main_extract(address,json_xml):
    try:
        lat,lng=extract_lat_long_via_address(address)
        if(lat!=None and lng!=None):
            if(json_xml=="json"):
                output={}
                output["coordinates"]={}
                output["coordinates"]["lat"]=lat
                output["coordinates"]["lng"]=lng
                output["address"]=address
                return output
            elif(json_xml=="xml"):
                data=ET.Element('root')
                s_elem1 = ET.SubElement(data, 'address')
                s_elem2 = ET.SubElement(data, 'coordinates')
                s_elem1.text = address
                element1 = ET.SubElement(s_elem2, 'lat')
                element2 = ET.SubElement(s_elem2, 'lng')
                element1.text = str(lat)
                element2.text = str(lng)
                b_xml=ET.tostring(data)
                return b_xml
    except Exception as e:
        print(e)
        



