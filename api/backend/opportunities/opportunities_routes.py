from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

# create the opportunities blueprint object
opportunities = Blueprint('opportunities', __name__)

#------------------------------------------------------------
# Get all opportunities from the system
@opportunities.route('/opportunities', methods=['GET'])
def get_all_opportunities():
    cursor = db.get_db().cursor()
    cursor.execute('''
                   SELECT *
                   FROM ResearchOpportunities
    ''')
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Get all opportunities with the particular DepartmentID
@opportunities.route('/opportunities/<departmentID>', methods=['GET'])
def get_opportunities(departmentID):
    current_app.logger.info('GET /opportunities/<departmentID> route')
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM ResearchOpportunities WHERE DepartmentId = {0}'.format(departmentID))
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Get all opportunities posted by the particular OwnerID
@opportunities.route('/opportunities/<ownerID>', methods=['GET'])
def get_opportunities_by_owner(ownerID):
    current_app.logger.info('GET /opportunities/<ownerID> route')
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM ResearchOpportunities WHERE ownerID = {0}'.format(ownerID))
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response
