from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db


# Blueprint object for all applications routes
applications = Blueprint('applications', __name__)


#------------------------------------------------------------
# Get all applications from the system
@applications.route('/applications', methods=['GET'])
def get_all_applications():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Applications')
    
    theData = cursor.fetchall()
    cursor.close()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response


#------------------------------------------------------------
# Get all applications for a specific opportunity based on the OpportunityId
@applications.route('/applications/o<opportunityID>', methods=['GET'])
def get_applications_for_opportunity(opportunityID):
    current_app.logger.info('GET /applications/o<opportuntiyID> route')
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Applications WHERE PositionId = %s', (opportunityID))
    
    theData = cursor.fetchall()
    cursor.close()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response


#------------------------------------------------------------
# Get all applications from a specific student based on the StudentId
@applications.route('/applications/s<studentID>', methods=['GET'])
def get_applications_by_student(studentID):
    current_app.logger.info('GET /applications/s<studentID> route')
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Applications WHERE ApplicantId = %s', (studentID))
    
    theData = cursor.fetchall()
    cursor.close()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response


#------------------------------------------------------------
# Add a new application to the system for a specific opportunity given the OpportunityId
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


#------------------------------------------------------------
# Update a specific application based on its ApplicationId
@applications.route('/applications/a<applicationID>', methods=['PUT'])
def update_application(applicationID):
    the_data = request.get_json()
    
    valid_fields = {
            'applicant_id': 'ApplicantId',
            'app_status': 'ApplicationStatus',
            'position_id': 'PositionId',
        }

    # build the set dynamically based on which fields were provided
    update_fields = []
    params = []
        
    for json_key, db_column in valid_fields.items():
        if json_key in the_data:
            update_fields.append(f"{db_column} = %s")
            params.append(the_data[json_key])

    if not update_fields:
        return make_response({"error": "No valid fields to update"}, 400)

    query = f'''
        UPDATE Applications 
        SET {', '.join(update_fields)}
        WHERE ApplicationId = %s
    '''
        
    params.append(applicationID)

    cursor = db.get_db().cursor()
    cursor.execute(query, params)            
    db.get_db().commit()
    cursor.close()

    return make_response({"message": f"Successfully updated application {applicationID}"}, 200)


#------------------------------------------------------------
# Delete a specific application based on the ApplicationId
@applications.route('/applications/a<applicationID>', methods=['DELETE'])
def del_application(applicationID):
    cursor = db.get_db().cursor()    
    query = 'DELETE FROM Applications WHERE ApplicationId = %s'
    cursor.execute(query, (applicationID))
        
    db.get_db().commit()
    cursor.close()
        
    return make_response({"message": f"Successfully deleted application {applicationID}"}, 200)