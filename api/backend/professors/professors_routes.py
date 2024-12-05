from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

# Blueprint object for all professors routes
professors = Blueprint('professors', __name__)

#------------------------------------------------------------
# Get a professors name based on the given ProfessorId
@professors.route('/professors/p<professorID>', methods=['GET'])
def get_professor_name_from_id(professorID):
    current_app.logger.info('GET /professors/p<professorID> route')
    cursor = db.get_db().cursor()
    cursor.execute('SELECT FirstName, LastName FROM Professors WHERE ProfessorId = %s', (professorID,))
    
    theData = cursor.fetchall()
    cursor.close()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response