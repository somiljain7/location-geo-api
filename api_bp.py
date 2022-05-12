from flask import Blueprint
from api_python import get_address_main_extract
api_bp =Blueprint('api_bp',"forms")
api_bp.route('/getAddressDetails',methods=['POST'])(get_address_main_extract)