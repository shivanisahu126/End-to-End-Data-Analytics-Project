# End-to-End-Data-Analytics-Project
Adavance Data Analytics Project using GenAI, SQL, Python and PowerBI
Play Store Apps Data Engineering & Analytics Project

This project demonstrates a full data pipeline, starting from raw data cleaning in Python, migrating data to a PostgreSQL database, performing advanced SQL analysis, and finally creating an interactive dashboard in Power BI.

🏗️ Project Architecture

Data Cleaning: Used Python (Pandas/NumPy) to handle null values and format data.
Database Migration: Utilized SQLAlchemy to transfer cleaned data into a PostgreSQL database.
Data Analysis: Executed complex SQL queries to extract business insights.
Data Visualization: Built an interactive Power BI Dashboard to visualize key performance indicators (KPIs).

🛠️ Tech Stack
Language: Python (Pandas, NumPy, SQLAlchemy)

Database: PostgreSQL
Tool: pgAdmin 4
Visualization: Power BI
Dataset: Play Store Apps CSV

🚀 Step-by-Step Implementation

1. Data Cleaning & Preprocessing (Python)

The raw dataset contained several null values and inconsistent column names.
Handling Nulls: Replaced missing Rating values with the Mean and Content Rating/Versions with the Mode.
Standardization: Converted column names to lowercase and replaced spaces with underscores for SQL compatibility.
Engine Creation: Established a connection to PostgreSQL using create_engine.

--------python code---------
<img width="872" height="704" alt="py1" src="https://github.com/user-attachments/assets/e6083d9c-eaa2-46f6-8edc-e8b979c1c25d" />
<img width="948" height="844" alt="py2" src="https://github.com/user-attachments/assets/4a9035e2-b611-477e-8379-80cd1116ce3f" />

2. SQL Analysis (PostgreSQL)

Once the data was loaded into the application table, I performed deep-dive analysis using SQL queries, including:
App Distribution: Categorizing total apps by Genre and Type (Free vs. Paid).
Popularity Metrics: Finding the top 10 most reviewed apps in the 'GAME' category.
Content Strategy: Identifying high-installation apps specifically with a 'Teen' content rating.
Filtering: Querying apps based on specific size (>50MB) and rating (>=4.5) constraints.

-------sql code--------
<img width="1287" height="1000" alt="sql" src="https://github.com/user-attachments/assets/5825d2d4-5c39-46ef-89ce-914c0c3d3d0e" />
<img width="960" height="812" alt="sql2" src="https://github.com/user-attachments/assets/2e6572cb-3f46-403e-857f-70f9c0a4809f" />

3. Data Visualization (Power BI)
   
The final step involved creating a high-level dashboard to present findings visually:
Key KPIs: Total Apps (10K), Total Genres (120), and Total Installs (168bn).
Visual Insights: * App Count by Category: Dominance of Family and Game categories.
Free vs Paid: A massive 92.6% of apps on the store are Free.
Installation Trends: Subway Surfers leading as one of the most installed apps.


------dashboard--------
<img width="1452" height="818" alt="adv1" src="https://github.com/user-attachments/assets/dd7a32a6-33d6-4cfb-b254-0df43297a1ed" />

📊 Key Insights from the Project

Market Dominance: The "Family" and "Game" categories represent the largest volume of apps.
User Preference: Users heavily favor free apps, though paid apps still maintain a niche market.
Rating Correlation: High-rated apps tend to have a higher volume of installs, particularly in the Communication and Social categories.

📂 Project Structure

├── data/               # Raw and Cleaned CSV files
├── scripts/            # Python cleaning and migration script
├── sql_queries/        # PostgreSQL scripts for insights
├── dashboard/          # Power BI .pbix file and screenshots
└── README.md


