# coding: utf-8

from flask import Blueprint
from flask import request, render_template, render_template_string, Flask
from flask import jsonify
import json
import random
from ..decorators.crossdomain import crossdomain

__all__ = ['bp']

bp = Blueprint('demo_handler', __name__)

@bp.route('/', methods=['GET'])
def login():
    return render_template('security/login-user.html')

@bp.route('/forgot-password')
def forgot_password():
    return render_template('security/forgot-password.html')

@bp.route('/reset-password')
def reset_password():
    return render_template('security/reset-password.html')

@bp.route('/dashboard')
def dashboard():
    return render_template('dashboard/dashboard-container.html')

@bp.route('/product-search')
def product_search():
    return render_template('product/product-search.html')

@bp.route('/user-mgmt')
def user_mgmt():
    return render_template('user/user-container.html')

@bp.route('/user-group-mgmt')
def user_group_mgmt():
    return render_template('user-group/user-group-container.html')

@bp.route('/role-mgmt')
def role_mgmt():
    return render_template('role/role-container.html')

@bp.route('/privilege-mgmt')
def privilege_mgmt():
    return render_template('privilege/privilege-container.html')

@bp.route('/criteria-mgmt')
def criteria_mgmt():
    return render_template('criteria/criteria-container.html')

@bp.route('/role-details')
def role_details():
    return render_template('role/role-details.html')

@bp.route('/privilege-details')
def privilege_details():
    return render_template('privilege/privilege-details.html')

@bp.route('/criteria-details')
def criteria_details():
    return render_template('criteria/criteria-details.html')

@bp.route('/vehicle-mgmt')
def vehicle_mgmt():
    response = render_template('vehicle/vehicle-container.html')
    return response

@bp.app_errorhandler(404)
def not_found(error):
    return render_template('security/404.html'), 404

@bp.app_errorhandler(500)
def internal_error(error):
    return render_template('security/500.html'), 500


###############################################################
#
# Mock Data Requests Handling
#
###############################################################
@bp.route('/user-mgmt-data')
def user_mgmt_data():
    return jsonify(retrieve_mock_data('mock-user-mgmt.json'))

@bp.route('/userGroup-mgmt-data')
def userGroup_mgmt_data():
    return jsonify(retrieve_mock_data('mock-userGroup-mgmt.json'))

@bp.route('/vehicle-mgmt-data')
def vehicle_mgmt_data():
    return jsonify(retrieve_mock_data('mock-vehicle-mgmt.json'))

@bp.route('/role-mgmt-data')
def role_mgmt_data():
    return jsonify(retrieve_mock_data('mock-role-mgmt.json'))

@bp.route('/privilege-mgmt-data')
def privilege_mgmt_data():
    return jsonify(retrieve_mock_data('mock-privilege-mgmt.json'))

@bp.route('/criteria-mgmt-data')
def criteria_mgmt_data():
    return jsonify(retrieve_mock_data('mock-criteria-mgmt.json'))

@bp.route('/role-history-data')
def role_history_data():
    return jsonify(retrieve_mock_data('mock-role-history.json'))

@bp.route('/privilege-history-data')
def privilege_history_data():
    return jsonify(retrieve_mock_data('mock-privilege-history.json'))

@bp.route('/criteria-history-data')
def criteria_history_data():
    return jsonify(retrieve_mock_data('mock-criteria-history.json'))


###############################################################
#
# Mock Data With BACKBONE.JS
#
###############################################################

### Vehicle Mock Data
@bp.route('/vehicles', methods=['GET'])
@crossdomain(origin='*', headers='Content-Type')
def fetch_vehicles():
    mock_vehicles = retrieve_mock_data('mock-vehicle-record.json', 'mock-data-backbone')
    return json.dumps(mock_vehicles);

@bp.route('/vehicles', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type')
def create_vehicle():
    return jsonify(id=random.randint(8, 1000))

@bp.route('/vehicles/<int:id>', methods=['DELETE', 'OPTIONS'])
@crossdomain(origin='*')
def destory_vehicle(id):
    print 'In DELETE METHOD..'
    return jsonify(id=id)

@bp.route('/vehicles/<int:id>', methods=['PUT', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type')
def update_vehicle(id):
    print 'In PUT METHOD..'
    return jsonify(id=id)

@bp.route('/vehicle-criteriable-attrs', methods=['GET'])
@crossdomain(origin='*')
def fetch_vehicle_criteriable_attrs():
    mock_vehicle_criteriable_attrs = retrieve_mock_data('mock-vehicle-header.json', 'mock-data-backbone')
    print mock_vehicle_criteriable_attrs
    return json.dumps(mock_vehicle_criteriable_attrs)

### User Mock Data
@bp.route('/users', methods=['GET'])
@crossdomain(origin='*', headers='Content-Type')
def fetch_users():
    mock_users = retrieve_mock_data('mock-user-record.json', 'mock-data-backbone')
    return json.dumps(mock_users);

@bp.route('/users', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type')
def create_user():
    return jsonify(id=random.randint(8, 1000));

@bp.route('/users/<int:id>', methods=['DELETE', 'OPTIONS'])
@crossdomain(origin='*')
def destory_user(id):
    print 'In DELETE METHOD..'
    return jsonify(id=id);

@bp.route('/users/<int:id>', methods=['PUT', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type')
def update_user(id):
    print 'In PUT METHOD..'
    return jsonify(id=id);

@bp.route('/user-attrs', methods=['GET'])
@crossdomain(origin='*', headers='Content-Type')
def fetch_user_atts():
    mock_user_group_attrs = retrieve_mock_data('mock-user-attrs.json', 'mock-data-backbone')
    return json.dumps(mock_user_attrs);

### User Group Mock Data
@bp.route('/user-groups', methods=['GET'])
@crossdomain(origin='*', headers='Content-Type')
def fetch_user_groups():
    mock_user_groups = retrieve_mock_data('mock-user-group-record.json', 'mock-data-backbone')
    return json.dumps(mock_user_groups);

@bp.route('/user-groups', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type')
def create_user_group():
    return jsonify(id=random.randint(8, 1000));

@bp.route('/user-groups/<int:id>', methods=['DELETE', 'OPTIONS'])
@crossdomain(origin='*')
def destory_user_group(id):
    print 'In DELETE METHOD..'
    return jsonify(id=id);

@bp.route('/user-groups/<int:id>', methods=['PUT', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type')
def update_user_group(id):
    print 'In PUT METHOD..'
    return jsonify(id=id);

@bp.route('/user-group-attrs', methods=['GET'])
@crossdomain(origin='*', headers='Content-Type')
def fetch_user_group_atts():
    mock_user_group_attrs = retrieve_mock_data('mock-user-group-attrs.json', 'mock-data-backbone')
    return json.dumps(mock_user_group_attrs);

### Role Mock Data
@bp.route('/roles', methods=['GET'])
@crossdomain(origin='*', headers='Content-Type')
def fetch_roles():
    mock_roles = retrieve_mock_data('mock-role-record.json', 'mock-data-backbone')
    return json.dumps(mock_roles);

@bp.route('/roles', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type')
def create_role():
    return jsonify(id=random.randint(8, 1000));

@bp.route('/roles/<int:id>', methods=['DELETE', 'OPTIONS'])
@crossdomain(origin='*')
def destory_role(id):
    print 'In DELETE METHOD..'
    return jsonify(id=id);

@bp.route('/roles/<int:id>', methods=['PUT', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type')
def update_role(id):
    print 'In PUT METHOD..'
    return jsonify(id=id);

@bp.route('/role-history', methods=['GET'])
@crossdomain(origin='*', headers='Content-Type')
def fetch_role_history():
    mock_role_hisroty = retrieve_mock_data('mock-role-history-record.json', 'mock-data-backbone')
    return json.dumps(mock_role_hisroty);

### Privilege Mock Data
@bp.route('/privileges', methods=['GET'])
@crossdomain(origin='*', headers='Content-Type')
def fetch_priveilges():
    mock_privileges= retrieve_mock_data('mock-privilege-record.json', 'mock-data-backbone')
    return json.dumps(mock_privileges);

@bp.route('/privileges', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type')
def create_privilege():
    return jsonify(id=random.randint(8, 1000));

@bp.route('/privileges/<int:id>', methods=['DELETE', 'OPTIONS'])
@crossdomain(origin='*')
def destory_privilege(id):
    print 'In DELETE METHOD..'
    return jsonify(id=id);

@bp.route('/privileges/<int:id>', methods=['PUT', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type')
def update_privilege(id):
    print 'In PUT METHOD..'
    return jsonify(id=id);

@bp.route('/privilege-history', methods=['GET'])
@crossdomain(origin='*', headers='Content-Type')
def fetch_privilege_history():
    mock_privilege_hisroty = retrieve_mock_data('mock-privilege-history-record.json', 'mock-data-backbone')
    return json.dumps(mock_privilege_hisroty);

### Criteria Mock Data
@bp.route('/criterias', methods=['GET'])
@crossdomain(origin='*', headers='Content-Type')
def fetch_criterias():
    fetch_criterias = retrieve_mock_data('mock-criteria-record.json', 'mock-data-backbone')
    return json.dumps(fetch_criterias);

@bp.route('/criterias', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type')
def create_criteria():
    return jsonify(id=random.randint(8, 1000));

@bp.route('/criterias/<int:id>', methods=['DELETE', 'OPTIONS'])
@crossdomain(origin='*')
def destory_criteria(id):
    print 'In DELETE METHOD..'
    return jsonify(id=id);

@bp.route('/criterias/<int:id>', methods=['PUT', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type')
def update_criteria(id):
    print 'In PUT METHOD..'
    return jsonify(id=id)

@bp.route('/criteria-history', methods=['GET'])
@crossdomain(origin='*', headers='Content-Type')
def fetch_criteria_history():
    mock_criteria_hisroty = retrieve_mock_data('mock-criteria-history-record.json', 'mock-data-backbone')
    return json.dumps(mock_criteria_hisroty)

### Generic Filter Mock Data
@bp.route('/generic-filter', methods=['GET'])
@crossdomain(origin='*', headers='Content-Type')
def fetch_generic_filter():
    mock_filter_settings = retrieve_mock_data('mock-filter-settings.json', 'mock-data-backbone')
    return json.dumps(mock_filter_settings)

@bp.route('/generic-records/filter', methods=['GET'])
@crossdomain(origin='*', headers='Content-Type')
def filter_generic_records():
    print 'Generic Filter Params >> '+request.args.get('q');
    mock_filter_records = retrieve_mock_data('mock-filter-records.json', 'mock-data-backbone')
    return json.dumps(mock_filter_records)

### Method for Mock data

def is_ajax(request):
    return "X-Requested-With" in request.headers and request.headers['X-Requested-With'] == "XMLHttpRequest"

def retrieve_mock_data(file_name, folder='mock-data'):
    import os
    DEMO_DATA_FOLDER = os.path.join(os.getcwd(), folder)
    with open(os.path.join(DEMO_DATA_FOLDER, file_name)) as mock_json: 
        mock_data = json.load(mock_json)
        return mock_data



