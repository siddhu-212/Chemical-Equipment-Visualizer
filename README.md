###### **Chemical Equipment Visualizer**



A full-stack data analysis and visualization system for chemical equipment datasets.

The project enables users to upload CSV files, perform automated statistical analysis, and visualize insights through a web dashboard and desktop application.



This system simulates a real-world industrial data pipeline used in chemical process monitoring and equipment analysis.



###### **Project Objective**



To design and develop a system that:



* Accepts CSV datasets of chemical equipment
* Analyzes key operational parameters
* Exposes results through REST APIs
* Provides a foundation for visualization and decision-support tools



The project simulates a real-world industrial data pipeline used in chemical process and equipment monitoring systems.



###### **Key Features**



* CSV file upload through REST API
* Automated data analysis using Pandas
* Computes:



 	Total equipment count

 	Average flow rate

 	Average pressure

 	Average temperature



* Equipment type distribution
* Stores historical analysis results
* History retrieval API
* Django admin panel for monitoring
* Modular architecture with separate data engine and backend API Layer



###### **Frontend (Web Dashboard)**



* Modern React-based dashboard
* CSV upload interface
* Displays computed metrics in cards
* Equipment type distribution chart
* Clean, professional UI suitable for presentations
* Communicates with backend via REST APIs
* Desktop Application
* Desktop interface built using PyQt
* CSV upload and analysis
* Displays results in a standalone GUI
* Uses the same backend API as the web app



###### **Desktop Application**



* Desktop interface built using PyQt
* CSV upload and analysis
* Displays results in a standalone GUI
* Uses the same backend API as the web app



###### **Project Architecture**



Chemical-Equipment-Visualizer/

│

├── data\_logic/                # Core data analysis engine (Pandas)

│   └── analyzer.py

│

├── backend/

│   └── server/                # Django backend

│       ├── equipment/         # API, models, serializers

│       ├── server/            # Project settings

│       └── manage.py

│

├── frontend/                  # React frontend

│   ├── src/

│   │   ├── components/

│   │   ├── pages/

│   │   └── App.js

│   └── package.json

│

├── desktop/                   # PyQt desktop application

│   └── app.py

│

└── README.md





###### Tech Stack



**Backend**

* Python 3
* Pandas
* Django
* Django REST Framework
* SQLite
* Git and GitHub



**Frontend**

* React.js
* HTML, CSS
* Chart.js



**Desktop**

* Python
* PyQt5



**Tools**

* Git \& GitHub



###### **CSV File Format**



The uploaded CSV file should contain columns similar to:

Equipment\_Name, Equipment\_Type, Flowrate, Pressure, Temperature



**Example Equipment Types:**



* Pump
* Compressor
* Valve
* Heat Exchanger
* Reactor
* Condenser



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





###### **How to Run the Project**



1. **Clone the Repository**



git clone https://github.com/siddhu-212/Chemical-Equipment-Visualizer.git

cd Chemical-Equipment-Visualizer



2\. **Backend Setup (Django)**



python -m venv env

env\\Scripts\\activate

pip install django djangorestframework pandas

cd backend/server

python manage.py migrate

python manage.py runserver



Backend runs at:

http://127.0.0.1:8000/





3\. **Frontend Setup (React)**



cd frontend

npm install

npm start



Frontend runs at:



http://localhost:3000/



4\. Desktop Application



cd desktop

pip install pyqt5 requests

python app.py





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

