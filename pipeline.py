from flask import send_file, Flask, Response, jsonify
from flask_compress import Compress
import waitress
from driver_helper import main_scanner_driver, clear_crap
from zipfile import ZipFile
from os.path import basename
import os
from flask_cors import CORS
import time
import jpg_compress_mechanisms

compress = Compress()
app = Flask(__name__)
compress.init_app(app)
CORS(app)


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


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    # waitress.serve(app, host='0.0.0.0', port=5000)
