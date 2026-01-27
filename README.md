###### **Chemical Equipment Visualizer**



A backend-driven data analysis system to upload, analyze, and track chemical equipment datasets using Python, Pandas, and Django REST Framework.

This project processes CSV files containing chemical equipment parameters and generates statistical summaries through REST APIs.

###### 

###### **Project Objective**



To design and develop a system that:



* Accepts CSV datasets of chemical equipment
* Analyzes key operational parameters
* Stores analysis history in a database
* Exposes results through REST APIs
* Provides a foundation for visualization and decision-support tools



The project simulates a real-world industrial data pipeline used in chemical process and equipment monitoring systems.



###### **Key Features**



* CSV file upload through REST API
* Automated data analysis using Pandas
* Computes:



&nbsp;	Total equipment count

&nbsp;	Average flow rate

&nbsp;	Average pressure

&nbsp;	Average temperature



* Equipment type distribution
* Stores historical analysis results
* History retrieval API
* Django admin panel for monitoring
* Modular architecture with separate data engine and backend



###### **Project Architecture**



Chemical-Equipment-Visualizer/

│

├── data\_logic/          # Core data analysis engine (Pandas)

│   └── analyzer.py

│

├── backend/server/      # Django backend

│   ├── equipment/       # API and models

│   ├── server/          # Project settings

│   └── manage.py

│

└── .gitignore





###### Tech Stack



* Python 3
* Pandas
* Django
* Django REST Framework
* SQLite
* Git and GitHub



###### **API Endpoints**



Upload and Analyze CSV



POST /api/upload/



Uploads a CSV file, analyzes it using the Pandas data engine, stores the summary in the database, and returns the computed results.



Example:



curl -X POST -F "file=@sample\_equipment\_data.csv" http://127.0.0.1:8000/api/upload/



* Response includes:
* total equipment count
* average flow rate
* average pressure
* average temperature
* equipment type distribution



###### **Analysis History**



GET /api/history/





Returns previously analyzed dataset summaries stored in the database.



This API is used to maintain upload history and enable future dashboard features.



###### **How to Run the Project**



1. Clone the repository



git clone https://github.com/your-username/Chemical-Equipment-Visualizer.git

cd Chemical-Equipment-Visualizer



2\. Create virtual environment



python -m venv env

env\\Scripts\\activate



3\. Install dependencies



pip install django djangorestframework pandas



4\. Run migrations



cd backend/server

python manage.py migrate



5\. Start the server



python manage.py runserver





Server will run at:



http://127.0.0.1:8000/





###### **Internship Relevance**



This project demonstrates:



* Backend system design and implementation
* REST API development
* Real-world dataset handling
* Modular software architecture
* Integration of analytics with web systems
* Industry-oriented problem solving



It reflects how industrial data processing and monitoring platforms are developed in real environments.



###### **Future Scope**



* Interactive web-based dashboard
* Data visualization and charts
* Desktop application integration
* Authentication and role-based access
* Advanced statistical and ML-based insights
* Downloadable analytical reports



###### **Author**



Siddhant Kumar

B.Tech CSE (AIML)

Aspiring Machine Learning and Backend Engineer

