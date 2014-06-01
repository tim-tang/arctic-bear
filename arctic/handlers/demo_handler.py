# coding: utf-8

from flask import Blueprint
from flask import request, render_template, render_template_string, Flask
from flask import jsonify
import json
import random
from ..decorators.crossdomain import crossdomain

__all__ = ['bp']

bp = Blueprint('demo_handler', __name__)


###############################################################
#
# Mock Data With BACKBONE.JS
#
###############################################################


##################### Security Mock Start #####################
@bp.route('/security/authenticate', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type')
def authenticate():
    print 'Auth User name :>>' + request.form.get('username')
    return jsonify(security_user={'auth_token': 'mocked-hmac-authorization-token'})

@bp.route('/security/signout', methods=['DELETE', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def signout():
    return jsonify(result='success')
##################### Security Mock End #######################

##################### Vehicle Mock Data #######################
@bp.route('/vehicles', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_vehicles():
    mock_vehicles = retrieve_mock_data('mock-vehicle-record.json', 'mock-data-backbone')
    return json.dumps(mock_vehicles);

@bp.route('/vehicles', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def create_vehicle():
    return jsonify(id=random.randint(8, 1000))

@bp.route('/vehicles/<int:id>', methods=['DELETE', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def destory_vehicle(id):
    print 'In DELETE METHOD..'
    return jsonify(id=id)

@bp.route('/vehicles/<int:id>', methods=['PUT', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def update_vehicle(id):
    print 'In PUT METHOD..'
    return jsonify(id=id)

@bp.route('/vehicle-criteriable-attrs', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_vehicle_criteriable_attrs():
    mock_vehicle_criteriable_attrs = retrieve_mock_data('mock-vehicle-header.json', 'mock-data-backbone')
    print mock_vehicle_criteriable_attrs
    return json.dumps(mock_vehicle_criteriable_attrs)

@bp.route('/vehicle-history/<int:id>', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_vehicle_history(id):
    mock_vehicle_hisroty = retrieve_mock_data('mock-vehicle-history-record.json', 'mock-data-backbone')
    return json.dumps(mock_vehicle_hisroty)

@bp.route('/vehicle-general-info/<int:id>', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_vehicle_general_info(id):
    mock_vehicle_general_info = retrieve_mock_data('mock-vehicle-details.json', 'mock-data-backbone')
    return json.dumps(mock_vehicle_general_info);
##################### Vehicle Mock Data #######################

####################### User Mock Data ########################
@bp.route('/users', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_users():
    mock_users = retrieve_mock_data('mock-user-record.json', 'mock-data-backbone')
    return json.dumps(mock_users);

@bp.route('/users', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def create_user():
    return jsonify(id=random.randint(8, 1000));

@bp.route('/users/<int:id>', methods=['DELETE', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def destory_user(id):
    print 'In DELETE METHOD..'
    return jsonify(id=id);

@bp.route('/users/<int:id>', methods=['PUT', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def update_user(id):
    print 'In PUT METHOD..'
    return jsonify(id=id);

@bp.route('/user-attrs', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_user_atts():
    mock_user_group_attrs = retrieve_mock_data('mock-user-attrs.json', 'mock-data-backbone')
    return json.dumps(mock_user_attrs);

@bp.route('/user-general-info/<int:id>', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_user_general_info(id):
    mock_user_general_info = retrieve_mock_data('mock-user-details.json', 'mock-data-backbone')
    return json.dumps(mock_user_general_info);

@bp.route('/user-user-groups/<int:id>', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_user_user_groups(id):
    mock_user_user_groups = retrieve_mock_data('mock-user-user-groups.json', 'mock-data-backbone')
    return json.dumps(mock_user_user_groups);

@bp.route('/user-history/<int:id>', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_user_history(id):
    mock_user_hisroty = retrieve_mock_data('mock-user-history-record.json', 'mock-data-backbone')
    return json.dumps(mock_user_hisroty);
####################### User Mock Data ########################

################### User Group Mock Data ######################
@bp.route('/user-groups', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_user_groups():
    mock_user_groups = retrieve_mock_data('mock-user-group-record.json', 'mock-data-backbone')
    return json.dumps(mock_user_groups);

@bp.route('/user-groups', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def create_user_group():
    return jsonify(id=random.randint(8, 1000));

@bp.route('/user-groups/<int:id>', methods=['DELETE', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def destory_user_group(id):
    print 'In DELETE METHOD..'
    return jsonify(id=id);

@bp.route('/user-groups/<int:id>', methods=['PUT', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def update_user_group(id):
    print 'In PUT METHOD..'
    return jsonify(id=id);

@bp.route('/user-group-attrs', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_user_group_atts():
    mock_user_group_attrs = retrieve_mock_data('mock-user-group-attrs.json', 'mock-data-backbone')
    return json.dumps(mock_user_group_attrs);

@bp.route('/user-group-general-info/<int:id>', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_user_group_general_info(id):
    mock_user_group_general_info = retrieve_mock_data('mock-user-group-details.json', 'mock-data-backbone')
    return json.dumps(mock_user_group_general_info);

@bp.route('/user-group-users/<int:id>', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_user_group_users(id):
    mock_user_user_groups = retrieve_mock_data('mock-user-group-users.json', 'mock-data-backbone')
    return json.dumps(mock_user_user_groups);

@bp.route('/user-group-history/<int:id>', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_user_group_history(id):
    mock_user_group_hisroty = retrieve_mock_data('mock-user-group-history-record.json', 'mock-data-backbone')
    return json.dumps(mock_user_group_hisroty);
################### User Group Mock Data ######################

####################### Role Mock Data ########################
@bp.route('/roles', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_roles():
    mock_roles = retrieve_mock_data('mock-role-record.json', 'mock-data-backbone')
    return json.dumps(mock_roles);

@bp.route('/roles/<int:id>', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_role_details(id):
    print id
    mock_role_details = retrieve_mock_data('mock-role-details.json', 'mock-data-backbone')
    return json.dumps(mock_role_details);

@bp.route('/roles', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def create_role():
    return jsonify(id=random.randint(8, 1000));

@bp.route('/roles/<int:id>', methods=['DELETE', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def destory_role(id):
    print 'In DELETE METHOD..'
    return jsonify(id=id);

@bp.route('/roles/<int:id>', methods=['PUT', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def update_role(id):
    print 'In PUT METHOD..'
    return jsonify(id=id);

@bp.route('/role-general-info/<int:id>', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_role_general_info(id):
    mock_role_general_info = retrieve_mock_data('mock-role-details.json', 'mock-data-backbone')
    return json.dumps(mock_role_general_info);

@bp.route('/role-history/<int:id>', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_role_history(id):
    mock_role_hisroty = retrieve_mock_data('mock-role-history-record.json', 'mock-data-backbone')
    return json.dumps(mock_role_hisroty);

@bp.route('/role-privileges/<int:id>', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_role_privileges(id):
    mock_role_privileges = retrieve_mock_data('mock-role-privileges.json', 'mock-data-backbone')
    return json.dumps(mock_role_privileges);

@bp.route('/role-user-groups/<int:id>', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_role_user_groups(id):
    mock_role_user_groups = retrieve_mock_data('mock-role-user-groups.json', 'mock-data-backbone')
    return json.dumps(mock_role_user_groups);

@bp.route('/role-users/<int:id>', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_role_users(id):
    mock_role_users = retrieve_mock_data('mock-role-users.json', 'mock-data-backbone')
    return json.dumps(mock_role_users);
####################### Role Mock Data ########################

##################### Privilege Mock Data #####################
@bp.route('/privileges', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_priveilges():
    mock_privileges= retrieve_mock_data('mock-privilege-record.json', 'mock-data-backbone')
    return json.dumps(mock_privileges);

@bp.route('/privileges', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def create_privilege():
    return jsonify(id=random.randint(8, 1000));

@bp.route('/privileges/<int:id>', methods=['DELETE', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def destory_privilege(id):
    print 'In DELETE METHOD..'
    return jsonify(id=id);

@bp.route('/privileges/<int:id>', methods=['PUT', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type')
def update_privilege(id):
    print 'In PUT METHOD..'
    return jsonify(id=id);

@bp.route('/privilege-history/<int:id>', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_privilege_history(id):
    mock_privilege_hisroty = retrieve_mock_data('mock-privilege-history-record.json', 'mock-data-backbone')
    return json.dumps(mock_privilege_hisroty);

@bp.route('/privilege-general-info/<int:id>', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_privilege_general_info(id):
    mock_privilege_general_info = retrieve_mock_data('mock-privilege-details.json', 'mock-data-backbone')
    return json.dumps(mock_privilege_general_info);

@bp.route('/privilege-roles/<int:id>', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_privilege_roles(id):
    mock_privilege_roles = retrieve_mock_data('mock-privilege-roles.json', 'mock-data-backbone')
    return json.dumps(mock_privilege_roles);
##################### Privilege Mock Data #####################

##################### Criteria Mock Data ######################
@bp.route('/criterias', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_criterias():
    fetch_criterias = retrieve_mock_data('mock-criteria-record.json', 'mock-data-backbone')
    return json.dumps(fetch_criterias);

@bp.route('/criterias', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def create_criteria():
    return jsonify(id=random.randint(8, 1000));

@bp.route('/criterias/<int:id>', methods=['DELETE', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def destory_criteria(id):
    print 'In DELETE METHOD..'
    return jsonify(id=id);

@bp.route('/criterias/<int:id>', methods=['PUT', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def update_criteria(id):
    print 'In PUT METHOD..'
    return jsonify(id=id)

@bp.route('/criteria-history/<int:id>', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_criteria_history(id):
    mock_criteria_hisroty = retrieve_mock_data('mock-criteria-history-record.json', 'mock-data-backbone')
    return json.dumps(mock_criteria_hisroty)

@bp.route('/criteria-general-info/<int:id>', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_criteria_general_info(id):
    mock_criteria_general_info = retrieve_mock_data('mock-criteria-details.json', 'mock-data-backbone')
    return json.dumps(mock_criteria_general_info);

@bp.route('/criteria-privileges/<int:id>', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_criteria_privileges(id):
    mock_criteria_privileges = retrieve_mock_data('mock-criteria-privileges.json', 'mock-data-backbone')
    return json.dumps(mock_criteria_privileges);
##################### Criteria Mock Data ######################

################# Generic Filter  Mock Data ###################
@bp.route('/generic-filter', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def fetch_generic_filter():
    print  request.headers.get('Authorization')
    mock_filter_settings = retrieve_mock_data('mock-filter-settings.json', 'mock-data-backbone')
    return json.dumps(mock_filter_settings)

@bp.route('/generic-records/filter', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type, Authorization')
def filter_generic_records():
    print  request.headers.get('Authorization')
    print 'Generic Filter Params >> '+request.args.get('q');
    mock_filter_records = retrieve_mock_data('mock-filter-records.json', 'mock-data-backbone')
    return json.dumps(mock_filter_records)
################# Generic Filter  Mock Data ###################


#################### Method for Mock data #####################
def is_ajax(request):
    return "X-Requested-With" in request.headers and request.headers['X-Requested-With'] == "XMLHttpRequest"

def retrieve_mock_data(file_name, folder='mock-data'):
    import os
    DEMO_DATA_FOLDER = os.path.join(os.getcwd(), folder)
    with open(os.path.join(DEMO_DATA_FOLDER, file_name)) as mock_json: 
        mock_data = json.load(mock_json)
        return mock_data
