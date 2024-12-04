from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

# create the departments blueprint object
departments = Blueprint('departments', __name__)

#------------------------------------------------------------
# Get a department name from a specific ID
@departments.route('/departments/d<departmentID>', methods=['GET'])
def get_department_name_from_id(departmentID):
    current_app.logger.info('GET /departments/d<departmentID> route')
    cursor = db.get_db().cursor()
    cursor.execute('SELECT Name FROM Departments WHERE DepartmentID = %s', (departmentID,))
    
    theData = cursor.fetchall()
    cursor.close()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response