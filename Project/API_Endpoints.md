Job Seeker

    Create Job Seeker Profile:
        Endpoint: POST /job_seekers
        Input: JSON payload containing job seeker information (name, status, skills, experience, bio, availability)
        Output: JSON response with message indicating success or failure

    Retrieve Job Seeker Profile:
        Endpoint: GET /job_seekers/{job_seeker_id}
        Input: Job seeker ID
        Output: JSON response with job seeker profile data

    Update Job Seeker Profile:
        Endpoint: PUT /job_seekers/{job_seeker_id}
        Input: Job seeker ID and JSON payload containing updated job seeker information
        Output: JSON response with message indicating success or failure

    Delete Job Seeker Profile:
        Endpoint: DELETE /job_seekers/{job_seeker_id}
        Input: Job seeker ID
        Output: JSON response with message indicating success or failure

Job Posting

    Create Job Posting:
        Endpoint: POST /job_postings
        Input: JSON payload containing job posting information (job title, status, start date, end date, hiring manager ID)
        Output: JSON response with message indicating success or failure

    Retrieve Job Posting:
        Endpoint: GET /job_postings/{job_posting_id}
        Input: Job posting ID
        Output: JSON response with job posting data

    Update Job Posting:
        Endpoint: PUT /job_postings/{job_posting_id}
        Input: Job posting ID and JSON payload containing updated job posting information
        Output: JSON response with message indicating success or failure

    Delete Job Posting:
        Endpoint: DELETE /job_postings/{job_posting_id}
        Input: Job posting ID
        Output: JSON response with message indicating success or failure

Application

    Submit Application:
        Endpoint: POST /applications
        Input: JSON payload containing application information (job seeker ID, job posting ID, application status)
        Output: JSON response with message indicating success or failure

    Retrieve Application:
        Endpoint: GET /applications/{application_id}
        Input: Application ID
        Output: JSON response with application data

    Update Application Status:
        Endpoint: PUT /applications/{application_id}/status
        Input: Application ID and JSON payload containing updated application status
        Output: JSON response with message indicating success or failure

    Retrieve All Applications for a Job Posting:
        Endpoint: GET /job_postings/{job_posting_id}/applications
        Input: Job posting ID
        Output: JSON response with a list of applications for the specified job posting