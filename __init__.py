import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from flask import Flask,jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from .handler import WorklogHandler, ReportProcessedHandler
from .service import ReportService
from .service import ParserService

@app.route('/')
def main():
    return "Application is up"

@app.route('/reports', methods=['GET'])
def get_reports():
    reportservice = ReportService(WorklogHandler())
    return jsonify(reportservice.get_payroll_report())

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            return "No file selected"

        parserservice = ParserService(WorklogHandler(), ReportProcessedHandler())
        filename = secure_filename(file.filename)
        reportid = int(filename.split("-")[2].split(".")[0])
        if parserservice.is_report_uploaded(reportid):
            return "This report is already uploaded"

        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])

        filefullpath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filefullpath)
        if parserservice.parse_csv(filefullpath):
            parserservice.add_report_id(reportid)
            return filename + " uploaded and parsed successfully"
        else:
            return "Failed to parse " + filename
