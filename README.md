# Student Website using Python and Flask

This project is a full-fledged student website that allows users to perform CRUD (Create, Read, Update, Delete) operations on student records. The website is built using Python and the Flask framework, providing a seamless and interactive user experience.

## Features

- **Create**: Users can add new student records by entering their details such as name, age, and grade.
- **Read**: Users can view a list of all existing student records, including their information.
- **Update**: Users have the ability to edit and update the details of any specific student.
- **Delete**: Users can delete student records from the database if no longer needed.

## Technologies Used

- Python
- Flask (Web framework)
- SQLite (Database)

## Installation and Setup

1. Clone the repository: `git clone https://github.com/yourusername/student-website.git`
2. Navigate to the project directory: `cd student-website`
3. Create a virtual environment: `python -m venv env`
4. Activate the virtual environment:
   - On Windows: `.\env\Scripts\activate`
   - On macOS/Linux: `source env/bin/activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Start the Flask development server: `python app.py`
7. Open your web browser and access the website at `http://localhost:5000`

## Usage

Once the server is running and the website is accessible, you can perform the following actions:

- **Create a new student record**:
  - Fill in the required details in the provided form and click the "Add Student" button.
- **View all student records**:
  - Click the "View Students" link in the navigation menu to see a list of all existing student records.
- **Update a student record**:
  - Click the "Edit" button next to the student record you want to update.
  - Modify the student details in the edit form and click the "Update" button.
- **Delete a student record**:
  - Click the "Delete" button next to the student record you want to remove.

## Folder Structure

- `app.py`: Main Flask application file containing the routes and logic for handling CRUD operations.
- `templates/`: Directory containing HTML templates for the website's pages.
- `static/`: Directory for static assets such as CSS stylesheets or JavaScript files.

## Acknowledgments

Special thanks to the Flask developers and the Python community for providing the necessary tools and resources for building web applications.