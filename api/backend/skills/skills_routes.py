from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

# create the skills blueprint object
skills = Blueprint('skills', __name__)

#------------------------------------------------------------
# Get a skill name from a specific ID
@skills.route('/skills/s<skillID>', methods=['GET'])
def get_skill_name_from_id(skillID):
    current_app.logger.info('GET /skills/s<skillID> route')
    cursor = db.get_db().cursor()
    cursor.execute('SELECT Name FROM Skills WHERE SkillId = %s', (skillID,))
    
    theData = cursor.fetchall()
    cursor.close()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Check if a skill name exists in the database. If not, add it.
@skills.route('skills/s<skill_name>', methods=['POST'])
def check_or_add_skill(skill_name):
    current_app.logger.info('POST /skills/s<skill_name> route')
    cursor = db.get_db().cursor()
    
    #check if skill name exists
    cursor.execute('SELECT SkillId FROM Skills WHERE Name = %s', (skill_name,))

    theData = cursor.fetchone()

    #if the skill name exists
    if theData:
        skill_id = theData[0]
        cursor.close()
        the_response = make_response(jsonify(skill_id))
        the_response.status_code = 200
        return the_response
    else:
        cursor.execute('INSERT INTO Skills (Name) VALUES (%s)', (skill_name,))
        db.get_db().commit()

        #Get the new skill id
        cursor.execute('SELECT SkillId FROM Skills WHERE Name = %s', (skill_name,))
        theData = cursor.fetchone()
        new_skill_id = theData[0]
        cursor.close()
        
        the_response = make_response(jsonify(new_skill_id))
        the_response.status_code = 200
        return the_response
    

    