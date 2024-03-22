Welcome to the Microservice Dashboard Application repository! This web application serves as a UI for monitoring and managing services within the DEP ecosystem. The dashboard provides real-time updates on service statuses, facilitates proactive issue resolution, and offers a user-friendly interface for seamless navigation.


Introduction

The Microservice Dashboard Application is designed to enhance operational efficiency by providing visibility into the health and status of various services within the DEP ecosystem. It enables teams to monitor service statuses in real-time, identify potential issues, and take proactive measures to ensure smooth operations.


## Setup Instructions

Follow these steps to set up the project locally:

1. Clone the repository: ```git clone https://github.com/menahil1901/MicroservicesDashboard.git```
2. Install dependencies: ```pip install -r requirements.txt```
3. Set up environment variables for configuration (e.g., database credentials, secret keys).
4. Run migrations: ```python manage.py migrate```
5. Start the development server: ```python manage.py runserver```

Testing

1. Run unit tests: ```python manage.py test```
2. Run security tests: bandit ```-r``` . (for static analysis), ```zap-full-scan.py```(for dynamic scanning with OWASP ZAP)
