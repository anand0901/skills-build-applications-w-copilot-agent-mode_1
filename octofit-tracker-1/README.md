# Octofit Tracker

The Octofit Tracker is a fitness application designed to help users track their activities, manage teams, and receive personalized workout suggestions. The application includes features for user authentication, activity logging, team management, and a competitive leaderboard.

## Project Structure

The project is organized into two main directories: `backend` and `frontend`.

### Backend

The backend is built using Django and includes the following components:

- **venv/**: Contains the Python virtual environment for isolating dependencies.
- **requirements.txt**: Lists the required Python packages for the project.
- **manage.py**: Command-line utility for managing the Django project.
- **.env**: Contains environment variables such as secret keys and database configurations.
- **octofit_tracker/**: The main Django application directory containing:
  - `__init__.py`: Marks the directory as a Python package.
  - `asgi.py`: ASGI configuration for asynchronous capabilities.
  - `settings.py`: Project settings and configurations.
  - `urls.py`: URL routing for the Django project.
  - `wsgi.py`: WSGI configuration for serving web applications.
- **apps/**: Contains individual apps for users, activities, teams, leaderboard, and workouts.

### Frontend

The frontend is built using React and includes the following components:

- **package.json**: Configuration file for npm, listing dependencies and scripts.
- **tsconfig.json**: TypeScript configuration file specifying compiler options.
- **public/**: Contains the main HTML file for the application.
- **src/**: Contains the source code for the React application, including:
  - `index.tsx`: Entry point for the application.
  - `App.tsx`: Main application component.
  - `components/`: Reusable React components.
  - `pages/`: Different pages of the application.
  - `services/`: Services for API calls and business logic.

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd octofit-tracker
   ```

2. **Set up the backend**:
   - Create a Python virtual environment:
     ```
     python3 -m venv backend/venv
     ```
   - Activate the virtual environment:
     ```
     source backend/venv/bin/activate
     ```
   - Install the required packages:
     ```
     pip install -r backend/requirements.txt
     ```

3. **Run the backend server**:
   ```
   python backend/manage.py runserver
   ```

4. **Set up the frontend**:
   - Navigate to the frontend directory and install dependencies:
     ```
     cd frontend
     npm install
     ```

5. **Run the frontend application**:
   ```
   npm start
   ```

## Features

- User authentication and profiles
- Activity logging and tracking
- Team creation and management
- Competitive leaderboard
- Personalized workout suggestions

## License

This project is licensed under the MIT License.