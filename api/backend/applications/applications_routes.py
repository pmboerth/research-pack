from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

applications = Blueprint('applications', __name__)

#------------------------------------------------------------
# Get all applications from the system
@applications.route('/applications', methods=['GET'])
def get_all_applications():
    cursor = db.get_db().cursor()
    cursor.execute('''
                   SELECT *
                   FROM Applications
    ''')
    
    theData = cursor.fetchall()
    cursor.close()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Get all applications for a specific opportunity
@applications.route('/applications/o<opportunityID>', methods=['GET'])
def get_applications_for_opportunity(opportunityID):
    current_app.logger.info('GET /applications/o<opportuntiyID> route')
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Applications WHERE PositionId = {0}'.format(opportunityID))
    
    theData = cursor.fetchall()
    cursor.close()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Get all applications from a specific student
@applications.route('/applications/s<studentID>', methods=['GET'])
def get_applications_from_student(studentID):
    current_app.logger.info('GET /applications/o<opportuntiyID> route')
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Applications WHERE ApplicantId = {0}'.format(studentID))
    
    theData = cursor.fetchall()
    cursor.close()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Add a new application to the system
@applications.route('/applications/o<opportunityID>', methods=['POST'])
def add_new_application(opportunityID):
    the_data = request.json
    current_app.logger.info(the_data)
    
    query = '''
            INSERT INTO Applications (
                ApplicantId,
                ApplicationStatus,
                PositionId
            ) VALUES (%s, 'Pending', %s)
        '''
        
    params = (
        the_data['applicant_id'],
        opportunityID        
    )

    cursor = db.get_db().cursor()
    cursor.execute(query, params)
    db.get_db().commit()
    cursor.close()
    
    return make_response({"message": "Successfully added application"}, 200)

