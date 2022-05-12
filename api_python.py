from flask import request
from flask import make_response,jsonify
from get_address_details import main_extract

def send_response(data,code):
	response=make_response(
		jsonify(
				data
				),
		code,
		)
	response.headers['Content-Type']="application/json"
	return response
def send_response_xml(data,code):
	response=make_response(data,code)
	response.headers['Content-Type']="application/xml"
	return response

def get_address_main_extract():
	try:
		if 'address' not in request.json or not request.json['address']:
			if 'output_format' not in request.json or not request.json['output_format']:
				return send_response({
					"status" :	False,
					"Message" :	"address and format not mentioned in request",
					"Data" : {}	
					},400)

		address=request.json['address']
		output_format=request.json['output_format']
		if(output_format=="xml"):
			data=main_extract(address,output_format)
			if data:
				return send_response_xml(data,400)
		else:
			data=main_extract(address,output_format)
			if data:
				return send_response({
					"status" :	True,
					"Message" :	"Successfull",
					"Data" :	data	
					},400)
	except Exception as e:
		print(e)
		return send_response({
					"status" :	False,
					"Message" :	"Failed",
					"Data" : {}	
					},500)			

