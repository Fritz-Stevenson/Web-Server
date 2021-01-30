from flask import Flask, render_template, send_from_directory, request
import os, wtforms
import csv
app = Flask(__name__)
    
@app.route('/')
def html():
    return render_template('new_index.html')
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico')
@app.route('/images/banner.jpg')
def send_banner():
    return send_from_directory(os.path.join(app.root_path, 'static'),'background.png')
@app.route('/message_received', methods=['POST', 'GET'])
def submit_info():
    error = None
    if request.method == 'POST':
        data = request.form.to_dict()
        with open('database.csv','a', newline = '') as new_data:
            writer = csv.DictWriter(new_data, fieldnames=['name', 'email', 'message'])
            writer.writerow(data)
    return render_template('received_page_index.html')