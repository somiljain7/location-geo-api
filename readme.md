#### Verloop FDE Assignment.

- Problem statement: You have to create an API endpoint, which returns data related to
geolocation. 

- 	POST URL:		http://127.0.0.1:5000/api/v1/getAddressDetails

- File Structure:
	1. 		flask-api.py --> MAIN FLASK FILE
	2. 		api_bp.py --> blueprint for routing and etc
	3. 		api_python.py --> script for dealing with request json 
	4.		get_address_details.py --> calling of api endpoints


# `Example`
```
Request:
{
"address" : "# 3582,13 G Main Road, 4th Cross Rd, Indiranagar,Bengaluru, Karnataka 560008" ,
"output_format" : "json"
}

Response:
{
    "Data": {
        "address": "# 3582,13 G Main Road, 4th Cross Rd, Indiranagar,Bengaluru, Karnataka 560008",
        "coordinates": {
            "lat": 12.9658286,
            "lng": 77.63948169999999
        }
    },
    "Message": "Successfull",
    "status": true
}
```
- By - SOMIL JAIN
