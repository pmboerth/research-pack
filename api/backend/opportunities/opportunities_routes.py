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
# Enter a new opportunity into the system
@opportunities.route('/opportunities', methods=['POST'])
def add_new_opportunities():
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    name = the_data['name']
    owner_id = the_data['owner_id']
    reserach_area = the_data['research_area']
    description = the_data['description']
    department_id = the_data['department_id']
    skill_id = the_data['skill_id']
    
    query = '''
            INSERT INTO ResearchOpportunities (
                Name,
                OwnerId,
                ResearchArea,
                Description,
                DepartmentId,
                SkillId
            ) VALUES (%s, %s, %s, %s, %s, %s)
        '''
        
    params = (
        the_data['name'],
        the_data['owner_id'],
        the_data['research_area'],
        the_data['description'],
        the_data['department_id'],
        the_data['skill_id']
    )

    cursor = db.get_db().cursor()
    cursor.execute(query, params)
    db.get_db().commit()
    
    response = make_response("Successfully added opportunity")
    response.status_code = 200
    return response


#------------------------------------------------------------
# Get all opportunities with the particular DepartmentID
@opportunities.route('/opportunities/d<departmentID>', methods=['GET'])
def get_opportunities(departmentID):
    current_app.logger.info('GET /opportunities/d<departmentID> route')
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM ResearchOpportunities WHERE DepartmentId = {0}'.format(departmentID))
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Get all opportunities posted by the particular OwnerID
@opportunities.route('/opportunities/o<ownerID>', methods=['GET'])
def get_opportunities_by_owner(ownerID):
    current_app.logger.info('GET /opportunities/o<ownerID> route')
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM ResearchOpportunities WHERE OwnerId = {0}'.format(ownerID))
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response
