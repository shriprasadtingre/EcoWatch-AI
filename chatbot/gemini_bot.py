import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def ask_environment_ai(question, latest):

    prompt = f"""
You are EcoWatch AI.

Current Environment:

Temperature:
{latest['temperature']}

Humidity:
{latest['humidity']}

Wind:
{latest['wind_speed']}

AQI:
{latest['aqi']}

PM2.5:
{latest['pm25']}

User Question:

{question}

Explain:
1 Causes
2 Risks
3 Future concerns
4 Suggestions
"""

    response = model.generate_content(
        prompt
    )

    return response.text