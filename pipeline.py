from flask import send_file, Flask, request, make_response, jsonify
from flask_compress import Compress
from driver_helper import main_scanner_driver, clear_crap
from zipfile import ZipFile
from os.path import basename
import os
from flask_cors import CORS, cross_origin
import time
import jpg_compress_mechanisms
import oracle_apis
from flask_restful import Api, Resource
import datetime
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from pymongo import MongoClient
import bcrypt
import clone_server

compress = Compress()
app = Flask(__name__)
cors = CORS(app)
compress.init_app(app)

api = Api(app)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'zb$@ic^Jg#aywFO1u9%shY7E66Z1cZnO&EK@9e$nwqTrLF#ph1'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)

my_client = MongoClient()
my_client = MongoClient('localhost', 27017)
collection = my_client["DOC_SCAN"]
doc_id = collection['AUTH']


@app.route("/docscan/login", methods=["POST"])
def login():
    clone_server.clone_mongo()
    # login_username = request.form.get('username')
    # login_password = request.form.get('password')
    # print(login_username)
    # print(login_password)
    login_details = request.get_json()
    print(login_details)
    user_from_db = doc_id.find_one({'USERNAME': str(login_details['USERNAME']).upper()})  # search for user in database
    print(user_from_db)
    if user_from_db:
        print("in if")
        encrpted_password = login_details['PASSWORD'].encode("utf-8")
        print(user_from_db['PASSWORD'])
        if bcrypt.checkpw(encrpted_password, user_from_db['PASSWORD'].encode("utf-8")):
            access_token = create_access_token(identity=user_from_db['USERNAME'])  # create jwt token
            return jsonify({"access_token": access_token,
                            "status": True
                            }), 200, {"Access-Control-Allow-Origin": "http://localhost:3000"}

    return jsonify({'msg': 'The username or password is incorrect',
                    "status": False
                    }), 401


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,Access-Control-Allow-Origin')
    #     response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


@app.route("/scan_zip_file")
def route_function_zip():
    os.system("CmdTwain -q C:\\DocScan\\Doc_Scan_Test_Document.jpg")
    time.sleep(0.5)
    jpg_compress_mechanisms.resize_without_loosing_quality()
    with ZipFile('scan_result.zip', 'w') as zipObj:
        # Iterate over all the files in directory
        for folderName, subfolders, filenames in os.walk("C:\\DocScan"):
            for filename in filenames:
                # create complete filepath of file in directory
                filePath = os.path.join(folderName, filename)
                print(filePath)
                # Add file to zip
                zipObj.write(filePath, basename(filePath))
    clear_crap('C:\\DocScan')
    return send_file("scan_result.zip", as_attachment=True, download_name="scan_result.zip")


@app.route("/scan_base64")
def route_function_base():
    route_object = main_scanner_driver()
    return route_object


@app.route("/ipd/all_details")
@jwt_required()
def Route_Function_Ipd():
    mr = str(request.args.get('mr'))
    route_object = oracle_apis.ipd_patient_details(mr)
    return route_object


@app.route("/ipd/with_date")
@jwt_required()
def Route_Function_Ipd_with_date():
    mr = str(request.args.get('mr'))
    date = str(request.args.get('date'))
    route_object = oracle_apis.ipd_patient_details_with_date(date, mr)
    return route_object


@app.route("/ipd/all_dates")
@jwt_required()
def Route_Function_Ipd_all_dates():
    mr = request.args.get('mr')
    route_object = oracle_apis.ipd_patient_details_dates_only(mr)
    return route_object


@app.route("/opd/all_details")
@jwt_required()
def Route_Function_Opd():
    mr = request.args.get('mr')
    route_object = oracle_apis.opd_patient_details(mr)
    return route_object


@app.route("/opd/all_dates")
@jwt_required()
def Route_Function_Opd_all_dates():
    mr = request.args.get('mr')
    route_object = oracle_apis.opd_patient_details_dates_only(mr)
    return route_object


@app.route("/opd/with_date")
@jwt_required()
def Route_Function_Opd_with_date():
    mr = str(request.args.get('mr'))
    date = str(request.args.get('date'))
    route_object = oracle_apis.opd_patient_details_with_date(date, mr)
    return route_object


@app.route("/docscan/patient_demographics")
@jwt_required()
def Route_Function_Patient_Demographics():
    mr = str(request.args.get('mrno'))
    route_object = oracle_apis.demo(mr)
    return route_object


@app.route("/save")
def route_function_save():
    scanner_images = request.args.get("scanned_image")
    patient_info = request.args.get("patient_info")
    print(scanner_images)
    print(patient_info)
    return "GGWP"


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', threaded=True)
    # waitress.serve(app, host='0.0.0.0', port=5000)

# added this to push without ssl
