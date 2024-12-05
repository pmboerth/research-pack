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
