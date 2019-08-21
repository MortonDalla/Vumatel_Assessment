import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from datetime import date


INSTALATIONS = [
    {
        'id': uuid.uuid4().hex,
        'customer_name': 'Morton Tlemo',
        'Address': 'Newtown, Johhanesburg',
        'Appointment_date': '2017-08-28',
        'Created_date': '2017-08-28',
        'Modified_date': '2017-08-28',
        'Status': 'Inprogress',
         'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'customer_name': 'Dala Ntlemo',
        'Address': 'Gandhi quare, 22110',
        'Appointment_date': '2017-08-28',
        'Created_date': '2017-08-28',
        'Modified_date': '2017-08-28',
        'Status': 'Requested',
         'read': True
        
    },
    {
        'id': uuid.uuid4().hex,
        'customer_name': 'Paul Smith',
        'Address': 'Azadville, 7334 gert',
        'Appointment_date': '2017-08-28',
        'Created_date': '2017-08-28',
        'Modified_date': '2017-08-28',
        'Status': 'Complete',
         'read': True
    },
        {
        'id': uuid.uuid4().hex,
        'customer_name': 'Lucy Grey',
        'Address': 'Mulamula',
        'Appointment_date': '2017-08-28',
        'Created_date': '2017-08-28',
        'Modified_date': '2017-08-28',
        'Status': 'Rejected',
         'read': True
    }
]
# configuration
DEBUG = False

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128))

def remove_installation(installation_id):
    for installation in INSTALATIONS:
        if installation['id'] == installation_id:
            INSTALATIONS.remove(installation)
            return True
    return False


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/installations', methods=['GET', 'POST'])
def all_installations():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        INSTALATIONS.append({

            'id': uuid.uuid4().hex,
            'customer_name': post_data.get('customer_name'),
            'Address': post_data.get('Address'),
            'Appointment_date': post_data.get('Appointment_date'),
            'Created_date': post_data.get('Date_created'),
            'Modified_date': post_data.get('Date_modified'),
            'Status': post_data.get('Status'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'installation added!'
    else:
        response_object['installations'] = INSTALATIONS
    return jsonify(response_object)


@app.route('/installation/<installation_id>', methods=['PUT', 'DELETE'])
def single_installation(installation_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_installation(installation_id)
        INSTALATIONS.append({
            'id': uuid.uuid4().hex,
            'customer_name': post_data.get('customer_name'),
            'Address': post_data.get('Address'),
            'Appointment_date': post_data.get('Appointment_date'),
            'Created_date': post_data.get('Date_created'),
            'Modified_date': post_data.get('Date_modified'),
            'Status': post_data.get('Status'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'installation updated!'
    if request.method == 'DELETE':
        remove_installation(installation_id)
        response_object['message'] = 'installation removed!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()