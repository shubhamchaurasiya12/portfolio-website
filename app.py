import os
import smtplib
from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)
app.secret_key = "super_secret_key"  # Required for Flash messages

# =========================================
# DATA STORAGE
# =========================================
projects_data = [
    {
    "id": 1,
    "title": "Sensor-Fault-Detection",
    "description": "Transforming Sensor Data into Actionable Insights using a scalable ML pipeline.",
    "about": "An all-in-one developer toolkit for building scalable machine learning solutions in fault detection and predictive analytics with Flask and MongoDB.",
    "tags": ["machine-learning", "python", "flask", "mongodb", "predictive-analytics", "fault-detection"],
    "tech_stack": {
        "Python": 89.5,
        "CSS": 5.9,
        "HTML": 4.6
    },
    "readme_content": """
        <h3>Shubhamchaurasiya/sensorproject01</h3>
        <p><strong>Transforming Sensor Data into Actionable Insights</strong></p>
        
        <h3>Overview</h3>
        <p>sensorproject01 is an all-in-one developer toolkit for building scalable machine learning solutions in fault detection and predictive analytics. It integrates data ingestion, preprocessing, model training, and deployment within a cohesive architecture, all accessible through a user-friendly web interface.</p>

        <h3>Why sensorproject01?</h3>
        <ul>
            <li><strong>Web-based Interaction:</strong> Easily trigger training and generate predictions via Flask web endpoints.</li>
            <li><strong>Modular Data Pipelines:</strong> Seamlessly ingest, transform, and manage sensor data from CSV files to MongoDB.</li>
            <li><strong>Automated Model Training:</strong> Experiment with multiple algorithms, tune hyperparameters, and select the best model for deployment.</li>
            <li><strong>Robust Logging & Error Handling:</strong> Maintain high reliability with centralized logs and detailed exception management.</li>
            <li><strong>End-to-End Workflow:</strong> Orchestrate data processing, model evaluation, and inference in a scalable, maintainable manner.</li>
        </ul>

        <h3>Installation & Usage</h3>
        <pre><code># Clone the repository
    git clone https://github.com/shubhamchaurasiya12/sensorproject01

    # Install dependencies
    pip install -r requirements.txt

    # Run the project
    python app.py</code></pre>
        """,
        "images": ["/static/images/sensor_dashboard.png"],
        "github_link": "https://github.com/shubhamchaurasiya12/sensorproject01"
    },
    
    {
    "id": 2,
    "title": "Myntra-Review-Scraper",
    "description": "A Streamlit web application to scrape and analyze Myntra product reviews.",
    "about": "Real-time scraping engine for Myntra products that fetches reviews and stores them in MongoDB Atlas for analysis using Streamlit.",
    "tags": ["web-scraping", "streamlit", "mongodb", "python", "beautifulsoup", "pandas"],
    "tech_stack": {
        "Jupyter Notebook": 99.0,
        "Python": 1.0
    },
    "folder_structure": [
        {"name": "src", "type": "folder", "msg": "Core Python modules (MongoDB IO, constants)", "time": "7 months ago"},
        {"name": "pages", "type": "folder", "msg": "Streamlit multipage app components", "time": "7 months ago"},
        {"name": "templates", "type": "folder", "msg": "HTML templates", "time": "7 months ago"},
        {"name": "static/css", "type": "folder", "msg": "Custom CSS for Streamlit styling", "time": "7 months ago"},
        {"name": "app.py", "type": "file", "msg": "Main Streamlit app entry point", "time": "7 months ago"},
        {"name": "myntra.ipynb", "type": "file", "msg": "Jupyter notebook for development/testing", "time": "7 months ago"},
        {"name": "data.csv", "type": "file", "msg": "Sample scraped data", "time": "7 months ago"},
        {"name": "requirements.txt", "type": "file", "msg": "Python dependencies", "time": "7 months ago"},
        {"name": "setup.py", "type": "file", "msg": "Setup for packaging", "time": "7 months ago"},
        {"name": "README.md", "type": "file", "msg": "Project documentation", "time": "7 months ago"},
        {"name": ".gitignore", "type": "file", "msg": "Git ignore rules", "time": "7 months ago"}
    ],
    "readme_content": """
        <h3>Myntra Product Review Scraper</h3>
        <p><strong>Automated Insights from E-Commerce Data</strong></p>
        
        <h3>Overview</h3>
        <p>This is a Streamlit web application that allows users to scrape product reviews from Myntra and store them in a MongoDB Atlas database. The app fetches reviews using a scraping pipeline and provides an intuitive UI for input and display.</p>

        <h3>Project Structure</h3>
        <pre style="background: #1e1e1e; padding: 15px; border-radius: 6px; color: #d4d4d4; font-family: monospace; font-size: 0.85rem; overflow-x: auto;">
        Myntra_Scrapper_Project/
        │
        ├── src/                      # Core Python modules (MongoDB IO, constants)
        ├── pages/                    # Streamlit multipage app components
        ├── templates/                # HTML templates (if any)
        ├── static/css/               # Custom CSS for Streamlit styling
        │
        ├── app.py                    # Main Streamlit app entry point
        ├── myntra.ipynb              # Jupyter notebook for development/testing
        ├── data.csv                  # Sample scraped data
        ├── requirements.txt          # Python dependencies
        ├── setup.py                  # Setup for packaging (if needed)
        ├── README.md                 # Project documentation
        ├── .gitignore                # Git ignore rules</pre>

                <h3>Key Features</h3>
                <ul>
                    <li><strong>Search & Scrape:</strong> Input product names to automatically fetch reviews from Myntra.</li>
                    <li><strong>Database Integration:</strong> Securely stores scraped data in MongoDB Atlas.</li>
                    <li><strong>Data Visualization:</strong> View and analyze review data directly within the dashboard.</li>
                </ul>

                <h3>Installation & Usage</h3>
                <pre><code># Clone the repository
        git clone https://github.com/shubhamchaurasiya12/myntra_review_project

        # Create Environment
        conda create -n myntra_scrapper python=3.10
        conda activate myntra_scrapper

        # Install dependencies
        pip install -r requirements.txt

        # Run the App
        streamlit run app.py</code></pre>
            """,
            "images": ["/static/images/myntra_dashboard.png"],
            "github_link": "https://github.com/shubhamchaurasiya12/myntra_review_project"
   },
    {
        "id": 3,
        "title": "Google-Play-Store-Analytics",
        "description": "Exploratory Data Analysis on 10k+ apps.",
        "about": "Deep dive analysis into the Google Play Store dataset to identify trends in app ratings, sizing, and pricing.",
        "stars": 5,
        "forks": 0,
        "watching": 1,
        "tags": ["data-analysis", "pandas", "seaborn", "visualization"],
        "tech_stack": {"Jupyter Notebook": 60.0, "Python": 40.0},
        "folder_structure": [
            {"name": "data", "type": "folder", "msg": "Raw csv files", "time": "2 months ago"},
            {"name": "EDA_Notebook.ipynb", "type": "file", "msg": "Complete analysis", "time": "1 month ago"},
            {"name": "cleaning.py", "type": "file", "msg": "Data cleaning script", "time": "1 month ago"},
            {"name": "README.md", "type": "file", "msg": "Initial commit", "time": "2 months ago"}
        ],
        "readme_content": """
            <h3>Google Play Store Analysis</h3>
            <p>Analyzed 10,000+ apps to uncover market trends. Key findings include the dominance of free apps in install counts and the correlation between app size and ratings in the Game category.</p>
        """,
        "images": [],
        "github_link": "#"
    }
]

# =========================================
# ROUTES
# =========================================
@app.route("/")
def home():
    return render_template("index.html", projects=projects_data)

# NEW: Dynamic Project Page Route
@app.route("/project/<int:id>")
def project_detail(id):
    # Find the project with the matching ID
    project = next((p for p in projects_data if p["id"] == id), None)
    
    # Define the colors here (Backend Logic)
    gh_colors = ['#3572A5', '#e34c26', '#563d7c', '#f1e05a', '#00E5FF']
    
    if project:
        # Pass 'gh_colors' to the template
        return render_template("project.html", project=project, gh_colors=gh_colors)
    else:
        return "Project not found", 404

# NEW: Contact Logic
@app.route("/contact", methods=["POST"])
def contact():
    # 1. Get data from form
    name = request.form.get("name")
    message = request.form.get("message")
    
    # 2. Email Configuration
    # REPLACE THESE WITH YOUR REAL DETAILS
    my_email = "xshubhamchaurasiya@gmail.com" 
    my_app_password = "ctpk ocgs zmgi egsd" 
    
    # 3. Construct the Email Content
    subject = f"Neural Nexus Portfolio: New Message from {name}"
    email_body = f"Subject: {subject}\n\nName: {name}\n\nMessage:\n{message}"
    
    # 4. Send Email via Gmail SMTP
    try:
        # Connect to Gmail Server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls() # Secure the connection
        
        # Login and Send
        server.login(my_email, my_app_password)
        server.sendmail(my_email, my_email, email_body) # Sending to yourself
        server.quit()
        
        # Success Feedback
        flash("Transmission Received. I will respond shortly.", "success")
        print("Email sent successfully!")
        
    except Exception as e:
        # Error Feedback
        print(f"Error sending email: {e}")
        flash("Transmission Failed. Please contact me directly via LinkedIn.", "error")
    
    return redirect(url_for("home") + "#contact")

if __name__ == "__main__":
    app.run(debug=True)