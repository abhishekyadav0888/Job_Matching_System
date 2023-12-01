from flask import Flask, jsonify, request, make_response
import mysql.connector

app = Flask(__name__)

@app.route('/job_seekers', methods=['GET'])
def get_job_seekers():
    # Connect to the database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="job_matching_system"
    )
    cursor = db.cursor()

    # Execute query to retrieve all job seekers
    cursor.execute("SELECT * FROM job_seekers")
    results = cursor.fetchall()

    # Convert results to JSON format
    job_seekers = []
    for row in results:
        job_seeker = {
            "id": row[0],
            "name": row[1],
            "status": row[2],
            "skills": row[3],
            "experience": row[4],
            "bio": row[5],
            "availability": row[6]
        }
        job_seekers.append(job_seeker)

    # Close database connection
    db.close()

    # Return JSON response
    return jsonify({"job_seekers": job_seekers})

@app.route('/job_seekers', methods=['POST'])
def create_job_seeker():
    # Connect to the database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="job_matching_system"
    )
    cursor = db.cursor()

    # Extract data from the request body
    job_seeker_data = request.get_json()
    name = job_seeker_data["name"]
    status = job_seeker_data["status"]
    skills = job_seeker_data["skills"]
    experience = job_seeker_data["experience"]
    bio = job_seeker_data["bio"]
    availability = job_seeker_data["availability"]

    # Execute query to insert a new job seeker
    cursor.execute("INSERT INTO job_seekers (name, status, skills, experience, bio, availability) VALUES (%s, %s, %s, %s, %s, %s)", (name, status, skills, experience, bio, availability))
    db.commit()

    # Close database connection
    db.close()

    # Return success message
    return jsonify({"message": "Job seeker created successfully"})

@app.route('/job_seekers/<int:id>', methods=['GET'])
def get_job_seeker(id):
    # Connect to the database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="job_matching_system"
    )
    cursor = db.cursor()

    # Execute query to retrieve a specific job seeker
    cursor.execute("SELECT * FROM job_seekers WHERE id = %s", (id,))
    result = cursor.fetchone()

    if result:
        # Convert result to JSON format
        job_seeker = {
            "id": result[0],
            "name": result[1],
            "status": result[2],
            "skills": result[3],
            "experience": result[4],
            "bio": result[5],
            "availability": result[6]
        }

        # Return JSON response
        return jsonify({"job_seeker": job_seeker})
    else:
        # Return error message if job seeker not found
        return make_response("Job seeker with ID {} not found".format(id), 404)

@app.route('/job_seekers/<int:id>', methods=['PUT'])
def update_job_seeker(id):
    # Connect to the database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="job_matching_system"
    )
    cursor = db.cursor()

    # Extract data from the request body
    job_seeker_data = request.get_json()
    name = job_seeker_data["name"]
    status = job_seeker_data


@app.route('/job_postings', methods=['POST'])
def create_job_posting():
    # Extract data from the request body
    job_posting_data = request.get_json()
    title = job_posting_data["title"]
    status = job_posting_data["status"]
    start_date = job_posting_data["start_date"]
    end_date = job_posting_data["end_date"]
    hiring_manager_id = job_posting_data["hiring_manager_id"]

    # Execute query to insert a new job posting
    cursor.execute("INSERT INTO job_postings (title, status, start_date, end_date, hiring_manager_id) VALUES (%s, %s, %s, %s, %s)", (title, status, start_date, end_date, hiring_manager_id))
    db.commit()

    # Return success message
    return jsonify({"message": "Job posting created successfully"})


@app.route('/job_postings', methods=['GET'])
def get_job_postings():
    # Execute query to retrieve all job postings
    cursor.execute("SELECT * FROM job_postings")
    results = cursor.fetchall()

    # Convert results to JSON format
    job_postings = []
    for row in results:
        job_posting = {
            "id": row[0],
            "title": row[1],
            "status": row[2],
            "start_date": row[3],
            "end_date": row[4],
            "hiring_manager_id": row[5]
        }
        job_postings.append(job_posting)

    # Return JSON response
    return jsonify({"job_postings": job_postings})


@app.route('/job_postings/<int:id>', methods=['PUT'])
def update_job_posting(id):
    # Extract data from the request body
    job_posting_data = request.get_json()
    title = job_posting_data["title"]
    status = job_posting_data["status"]
    start_date = job_posting_data["start_date"]
    end_date = job_posting_data["end_date"]

    # Execute query to update the specific job posting
    cursor.execute("UPDATE job_postings SET title = %s, status = %s, start_date = %s, end_date = %s WHERE id = %s", (title, status, start_date, end_date, id))
    db.commit()

    # Return success message
    return jsonify({"message": "Job posting updated successfully"})


@app.route('/job_postings/<int:id>/applications', methods=['POST'])
def submit_application(id):
    # Extract data from the request body
    application_data = request.get_json()
    job_seeker_id = application_data["job_seeker_id"]
    status = application_data["status"]

    # Execute query to create a new application
    cursor.execute("INSERT INTO applications (job_posting_id, job_seeker_id, status) VALUES (%s, %s, %s)", (id, job_seeker_id, status))
    db.commit()

    # Return success message
    return jsonify({"message": "Application submitted successfully"})


@app.route('/applications/<int:id>', methods=['PUT'])
def review_application(id):
    # Extract data from the request body
    application_data = request.get_json()
    status = application_data["status"]

    # Execute query to update the application status
    cursor.execute("UPDATE applications SET status = %s WHERE id = %s", (status, id))
    db.commit()

    # Return success message
    return jsonify({"message": "Application status updated successfully"})


@app.route('/applications', methods=['GET'])
def get_applications():
    # Execute query to retrieve all applications
    cursor.execute("SELECT * FROM applications")
    results = cursor.fetchall()

    # Convert results to JSON format
    applications = []
    for row in results:
        application = {
            "id": row[0],
            "job_posting_id": row[1],
            "job_seeker_id": row[2],
            "status": row[3],
        }
        applications.append(application)

    # Return JSON response
    return jsonify({"applications": applications})


@app.route('/skill_sets', methods=['POST'])
def create_skill_set():
    # Extract data from the request body
    skill_set_data = request.get_json()
    name = skill_set_data["name"]
    descriptions = skill_set_data["descriptions"]

    # Execute query to create a new skill set
    cursor.execute("INSERT INTO skill_sets (name, descriptions) VALUES (%s, %s)", (name, descriptions))
    db.commit()

    # Return success message
    return jsonify({"message": "Skill set created successfully"})


@app.route('/skill_sets', methods=['GET'])
def get_skill_sets():
    # Execute query to retrieve all skill sets
    cursor.execute("SELECT * FROM skill_sets")
    results = cursor.fetchall()

    # Convert results to JSON format
    skill_sets = []
    for row in results:
        skill_set = {
            "id": row[0],
            "name": row[1],
            "descriptions": row[2]
        }
        skill_sets.append(skill_set)

    # Return JSON response
    return jsonify({"skill_sets": skill_sets})


@app.route('/job_postings/<int:id>/skills', methods=['POST'])
def assign_skill_to_job_posting(id):
    # Extract data from the request body
    skill_set_id = request.get_json()["skill_set_id"]

    # Execute query to add skill set to job posting
    cursor.execute("UPDATE job_postings SET skill_set_id = %s WHERE id = %s", (skill_set_id, id))
    db.commit()

    # Return success message
    return jsonify({"message": "Skill set assigned successfully"})


