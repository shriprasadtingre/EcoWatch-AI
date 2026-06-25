# EcoWatch AI – Environmental Health Monitoring and Prediction System

## Problem Statement

Environmental conditions such as increasing pollution, rising temperatures, heatwaves, and environmental degradation affect human health and quality of life.

Although environmental information exists, users often face problems:

- Environmental data is difficult to interpret
- Information is distributed across multiple platforms
- Most systems react after environmental issues occur
- Limited predictive guidance is available
- Users receive data but not recommendations

There is a need for an AI-based solution that can monitor environmental conditions, analyze environmental health, predict possible hazards, and provide actionable insights.

---

# Proposed Solution

EcoWatch AI is an AI-powered environmental monitoring and prediction system.

The platform collects environmental data and transforms it into understandable outputs through environmental scoring, hazard prediction, forecasting, and AI-generated recommendations.

EcoWatch AI provides:

✓ Environmental monitoring  
✓ Environmental Health Index (EHI)  
✓ Heatwave prediction  
✓ Pollution prediction  
✓ Environmental trend forecasting  
✓ AI-based environmental assistant  

Installation & Setup
Step 1 — Clone Repository
git clone YOUR_REPOSITORY_LINK

Move into project:

cd EcoWatch_AI
Step 2 — Create Virtual Environment

Windows:

python -m venv venv

Activate:

PowerShell:

.\venv\Scripts\Activate

CMD:

venv\Scripts\activate
Step 3 — Install Requirements
pip install -r requirements.txt

Verify installation:

pip list
Step 4 — Configure AI (Optional)

Create:

.env

Add:

GEMINI_API_KEY=YOUR_API_KEY

Do not upload .env.

How To Run

Collect environmental data:

python scripts/collect_data.py

Start application:

streamlit run app.py

Open:

http://localhost:8501
How To Use
Step 1

Launch EcoWatch AI.

Step 2

Generate environmental data.

Step 3

Open dashboard.

Step 4

Observe:

Environmental Health Index
Hazard predictions
Forecast graph
Step 5

Use AI assistant to ask questions.

Examples:

Why is pollution increasing?

How dangerous is current AQI?

How can environmental conditions improve?
Technology Stack

Frontend:

Streamlit

Backend:

Python

Libraries:

Pandas
NumPy
Matplotlib
Scikit-learn
Prophet
Requests
Python-dotenv
Google Generative AI (Optional)

Version Control:

Git
GitHub
Project Structure
EcoWatch_AI/

├── app.py
├── chatbot/
├── dashboard/
├── prediction/
├── scripts/
├── data/
├── requirements.txt
├── README.md
├── .env
└── .gitignore
Example Output
Environmental Health Index: 76

Heatwave Risk: Medium

Pollution Risk: Low

Recommendation:
Reduce outdoor exposure.

# Key Features

### Environmental Data Monitoring
Tracks:

- Temperature
- Humidity
- Wind Speed
- Air Quality Index (AQI)
- PM2.5

---

### Environmental Health Index (EHI)

Generates an environmental score:

```text
0–100

Interpretation:

80–100 → Excellent
60–79 → Good
40–59 → Moderate
20–39 → Poor
0–19 → Critical
Hazard Prediction

Predicts:

Heatwave Risk
Pollution Risk

Outputs:

Low
Medium
High
Future Trend Forecast

Forecasts future environmental conditions using historical records.

AI Environmental Assistant

Provides:

Environmental explanations
Hazard interpretation
Preventive recommendations
Environmental awareness guidance

Future Scope
Live environmental APIs
Global environmental monitoring
Mobile support
Improved forecasting
Real-time alerts