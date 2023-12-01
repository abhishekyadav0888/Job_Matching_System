import unittest
from app import app


class TestJobPostings(unittest.TestCase):

    def test_create_job_posting(self):
        # Prepare test data for creating a job posting
        job_posting_data = {
            "title": "Software Engineer",
            "status": "Open",
            "start_date": "2023-11-30",
            "end_date": "2024-06-30",
            "hiring_manager_id": 1
        }

        # Send a POST request to the create job posting endpoint
        response = app.test_client().post("/job_postings", json=job_posting_data)

        # Validate the response status code and data
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.json, {"message": "Job posting created successfully"})

    def test_retrieve_job_postings(self):
        # Send a GET request to the retrieve job postings endpoint
        response = app.test_client().get("/job_postings")

        # Validate the response status code and data structure
        self.assertEqual(response.status_code, 200)
        self.assertIn("job_postings", response.json)

        # Assert that the retrieved job postings are not empty
        self.assertGreater(len(response.json["job_postings"]), 0)

    def test_update_job_posting(self):
        # Create a job posting first
        response = app.test_client().post("/job_postings", json={
            "title": "Data Scientist",
            "status": "Open",
            "start_date": "2023-12-01",
            "end_date": "2024-12-31",
            "hiring_manager_id": 2
        })
        job_posting_id = response.json["id"]

        # Prepare updated job posting data
        updated_job_posting_data = {
            "title": "Senior Data Scientist",
            "status": "In Review",
            "start_date": "2024-01-01",
            "end_date": "2025-01-01"
        }

        # Send a PUT request to the update job posting endpoint
        response = app.test_client().put(f"/job_postings/{job_posting_id}", json=updated_job_posting_data)

        # Validate the response status code and message
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.json, {"message": "Job posting updated successfully"})


class TestApplications(unittest.TestCase):

    def test_submit_application(self):
        # Prepare test data for submitting an application
        application_data = {
            "job_seeker_id": 1,
            "status": "Pending"
        }

        # Send a POST request to the submit application endpoint for a specific job posting
        job_posting_id = 1  # Replace with the actual job posting ID
        response = app.test_client().post(f"/job_postings/{job_posting_id}/applications", json=application_data)

        # Validate the response status code and message
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.json, {"message": "Application submitted successfully"})

    def test_review_application(self):
        # Submit an application first
        job_posting_id = 1  # Replace with the actual job posting ID
        response = app.test_client().post(f"/job_postings/{job_posting_id}/applications", json={"job_seeker_id": 1, "status": "Pending"})

        # Prepare updated application data
        updated_application_data = {"status": "Reviewed"}

        # Send a PUT request to the review application endpoint
        application_id = response.json["id"]
        response = app.test_client().put(f"/applications/{application_id}", json=updated_application_data)

        # Validate the response status code and message
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.json, {"message": "Application status updated successfully"})


class TestSkillSets(unittest.TestCase):

    def test_create_skill_set(self):
        # Prepare test data for creating a skill set
        skill_set_data = {
            "title": "Python",
            "description": "A high-level, general-purpose programming language"
        }

        # Send a POST request to the create skill set endpoint
        response = app.test_client().post("/skill_sets", json=skill_set_data)

        # Validate the response status code and data
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.json, {"message": "Skill set created successfully"})

    def test_retrieve_skill_sets(self):
        # Send a GET request to the retrieve skill sets endpoint
        response = app.test_client().get("/skill_sets")

        # Validate the response status code and data structure
        self.assertEqual(response.status_code, 200)
        self.assertIn("skill_sets", response.json)

        # Assert that the retrieved skill sets are not empty
        self.assertGreater(len(response.json["skill_sets"]), 0)

    def test_update_skill_set(self):
        # Create a skill set first
        response = app.test_client().post("/skill_sets", json={
            "title": "Java",
            "description": "An object-oriented, class-based programming language"
        })
        skill_set_id = response.json["id"]

        # Prepare updated skill set data
        updated_skill_set_data = {
            "title": "JavaEE",
            "description": "A set of specifications for building enterprise applications"
        }

        # Send a PUT request to the update skill set endpoint
        response = app.test_client().put(f"/skill_sets/{skill_set_id}", json=updated_skill_set_data)

        # Validate the response status code and message
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.json, {"message": "Skill set updated successfully"})

    def test_delete_skill_set(self):
        # Create a skill set first
        response = app.test_client().post("/skill_sets", json={
            "title": "JavaScript",
            "description": "A scripting language for web development"
        })
        skill_set_id = response.json["id"]

        # Send a DELETE request to the delete skill set endpoint
        response = app.test_client().delete(f"/skill_sets/{skill_set_id}")

        # Validate the response status code and message
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.json, {"message": "Skill set deleted successfully"})

def test_skill_set_association_with_job_postings(self):
    # Create a job posting and associate it with a skill set
    skill_set_data = {
        "title": "Python",
        "description": "A high-level, general-purpose programming language"
    }
    response = app.test_client().post("/skill_sets", json=skill_set_data)
    skill_set_id = response.json["id"]

    job_posting_data = {
        "title": "Python Developer",
        "status": "Open",
        "start_date": "2023-11-30",
        "end_date": "2024-06-30",
        "hiring_manager_id": 1,
        "required_skill_set_ids": [skill_set_id]  # Associate the job posting with the created skill set
    }
    response = app.test_client().post("/job_postings", json=job_posting_data)

    # Retrieve the job posting and verify that the skill set is associated
    retrieved_job_posting = app.test_client().get(f"/job_postings/{response.json['id']}")
    job_posting_data = retrieved_job_posting.json

    for skill_set in job_posting_data["required_skill_sets"]:
        self.assertEqual(skill_set["id"], skill_set_id)
