from flask import send_file, Flask, request, make_response, jsonify
from flask_compress import Compress
from driver_helper import main_scanner_driver, clear_crap
from zipfile import ZipFile
from os.path import basename
import os
from flask_cors import CORS
import time
import jpg_compress_mechanisms
import oracle_apis
from flask_restful import Api, Resource
from flask_httpauth import HTTPBasicAuth

compress = Compress()
app = Flask(__name__)
compress.init_app(app)
CORS(app)
api = Api(app)
auth = HTTPBasicAuth()
USER_DATA = {
    "Username": "password"
}


@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password


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


class Route_Function_Ipd(Resource):
    @auth.login_required
    def get(self):
        mr = str(request.args.get('mr'))
        route_object = oracle_apis.ipd_patient_details(mr)
        return route_object


class Route_Function_Ipd_With_Date(Resource):
    @auth.login_required
    def get(self):
        mr = str(request.args.get('mr'))
        date = str(request.args.get('date'))
        route_object = oracle_apis.ipd_patient_details_with_date(date, mr)
        return route_object


class Route_Function_Ipd_Dates(Resource):
    @auth.login_required
    def get(self):
        mr = request.args.get('mr')
        route_object = oracle_apis.ipd_patient_details_dates_only(mr)
        return route_object


class Route_Function_Opd(Resource):
    @auth.login_required
    def get(self):
        mr = request.args.get('mr')
        route_object = oracle_apis.opd_patient_details(mr)
        return route_object


class Route_Function_Opd_Dates(Resource):
    @auth.login_required
    def get(self):
        mr = request.args.get('mr')
        route_object = oracle_apis.opd_patient_details_dates_only(mr)
        return route_object


class Route_Function_Opd_With_Date(Resource):
    @auth.login_required
    def get(self):
        mr = str(request.args.get('mr'))
        date = str(request.args.get('date'))
        route_object = oracle_apis.opd_patient_details_with_date(date, mr)
        return route_object


@app.route("/save")
def route_function_save():
    scanner_images = request.args.get("scanned_image")
    patient_info = request.args.get("patient_info")
    print(len(patient_info))
    print(len(scanner_images))
    return "GGWP"


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


api.add_resource(Route_Function_Ipd, "/ipd/all_details")
api.add_resource(Route_Function_Ipd_Dates, "/ipd/all_dates")
api.add_resource(Route_Function_Ipd_With_Date, "/ipd/with_date")
api.add_resource(Route_Function_Opd, "/opd/all_details")
api.add_resource(Route_Function_Opd_Dates, "/opd/all_dates")
api.add_resource(Route_Function_Opd_With_Date, "/opd/with_date")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', ssl_context='adhoc', threaded=True)
    # waitress.serve(app, host='0.0.0.0', port=5000)

# added this to push without ssl
