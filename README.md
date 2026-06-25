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

# Installation & Setup

Follow the steps below to install and run **EcoWatch AI** on your local system.

## Step 1 — Clone the Repository

Clone the project repository to your local machine:

```bash
git clone github.com/shriprasadtingre/EcoWatch-AI
```

Move into the project directory:

```bash
cd EcoWatch_AI
```

---

## Step 2 — Create a Virtual Environment

It is recommended to use a virtual environment to isolate project dependencies.

Create the environment:

```bash
python -m venv venv
```

Activate the environment:

### Windows PowerShell

```powershell
.\venv\Scripts\Activate
```

### Windows Command Prompt (CMD)

```cmd
venv\Scripts\activate
```

Once activated, your terminal should display:

```text
(venv)
```

---

## Step 3 — Install Project Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

Verify successful installation:

```bash
pip list
```

---

## Step 4 — Configure AI Integration (Optional)

EcoWatch AI supports Generative AI integration using Gemini API.

Create a file named:

```text
.env
```

Add your API key:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Example:

```env
GEMINI_API_KEY=AIza...
```

Important:

* Keep API keys private.
* Do not upload `.env` files to GitHub.
* Ensure `.env` is included in `.gitignore`.

---

# Running the Application

## Step 1 — Generate Environmental Data

Run the data collection module to create environmental records:

```bash
python scripts/collect_data.py
```

Running this command multiple times generates additional environmental samples used for analysis and forecasting.

---

## Step 2 — Launch the Dashboard

Start the Streamlit application:

```bash
streamlit run app.py
```

After execution, open:

```text
http://localhost:8501
```

Your browser will launch the EcoWatch AI dashboard.

---

# How to Use EcoWatch AI

## 1. Start the Application

Launch the Streamlit dashboard.

---

## 2. Generate Environmental Records

Execute:

```bash
python scripts/collect_data.py
```

to generate environmental observations.

---

## 3. Explore Dashboard Insights

The dashboard provides:

* Environmental Health Index (EHI)
* Heatwave Risk Prediction
* Pollution Risk Prediction
* Environmental Trend Forecasts

---

## 4. Use the AI Environmental Assistant

Navigate to the assistant section and ask environment-related questions.

Example queries:

```text
Why is pollution increasing?

How dangerous is the current AQI?

How can environmental conditions improve?

What environmental risks may occur in the coming days?
```

The assistant will generate contextual analysis and recommendations.

---

# Technology Stack

## Frontend

Responsible for application interface and visualization.

* Streamlit

---

## Backend

Responsible for application logic and data processing.

* Python

---

## Core Libraries

### Data Processing

* Pandas
* NumPy

### Data Visualization

* Matplotlib

### Machine Learning & Prediction

* Scikit-learn
* Prophet

### API & Environment Management

* Requests
* Python-dotenv

### Artificial Intelligence

* Google Generative AI (Gemini API) *(Optional Integration)*

---

## Version Control

Used for source code management and collaboration.

* Git
* GitHub

---

# Project Structure

```plaintext
EcoWatch_AI/

├── app.py                      # Main application entry point

├── chatbot/                    # AI assistant modules
│   ├── assistant.py
│   └── gemini_bot.py

├── dashboard/                  # Streamlit dashboard components
│   ├── home.py
│   ├── forecast.py
│   └── assistant.py

├── prediction/                 # Prediction modules
│   ├── health_index.py
│   ├── hazard_predictor.py
│   └── forecast.py

├── scripts/                    # Data collection scripts
│   └── collect_data.py

├── data/
│   ├── raw/                    # Generated environmental records
│   └── processed/

├── requirements.txt            # Dependency list
├── README.md                   # Project documentation
├── .env                        # Environment variables
└── .gitignore                  # Ignored files
```

---

# Example Output

```text
Environmental Health Index (EHI): 76

Environmental Status:
Good

Heatwave Risk:
Medium

Pollution Risk:
Low

AI Recommendation:
Reduce prolonged outdoor exposure and monitor AQI changes regularly.
```


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
