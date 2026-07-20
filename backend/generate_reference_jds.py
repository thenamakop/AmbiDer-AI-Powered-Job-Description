import os
import time
from groq import Groq
from dotenv import load_dotenv
from db import get_db

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

roles = [
    ("Chief Technology Officer", "IT"),
    ("Machine Learning Engineer", "IT"),
    ("Product Designer", "IT"),
    ("Cybersecurity Analyst", "IT"),
    ("Cloud Architect", "IT"),
    ("Operations Research Analyst", "Manufacturing"),
    ("Supply Chain Manager", "Manufacturing"),
    ("Industrial Engineer", "Manufacturing"),
    ("Maintenance Manager", "Manufacturing"),
    ("EHS Manager", "Manufacturing"),
    ("Cardiology Nurse", "Healthcare"),
    ("Medical Coder", "Healthcare"),
    ("Healthcare Data Analyst", "Healthcare"),
    ("Physiotherapist", "Healthcare"),
    ("Hospital Finance Manager", "Healthcare"),
    ("Investment Banker", "BFSI"),
    ("Wealth Manager", "BFSI"),
    ("Insurance Underwriter", "BFSI"),
    ("Treasury Analyst", "BFSI"),
    ("Fintech Product Manager", "BFSI"),
    ("E-commerce Manager", "Retail"),
    ("Retail Operations Manager", "Retail"),
    ("Merchandising Manager", "Retail"),
    ("Loss Prevention Manager", "Retail"),
    ("Customer Experience Manager", "Retail"),
    ("EdTech Product Manager", "Education"),
    ("Learning Experience Designer", "Education"),
    ("University Placement Officer", "Education"),
    ("School Principal", "Education"),
    ("Corporate Trainer", "Education"),
    ("Startup Founder Associate", "Startups"),
    ("Business Development Manager", "Startups"),
    ("Community Manager", "Startups"),
    ("Technical Recruiter", "Startups"),
    ("Revenue Operations Manager", "Startups"),
    ("District Education Officer", "Government"),
    ("Urban Planner", "Government"),
    ("Public Health Officer", "Government"),
    ("Legal Advisor Government", "Government"),
    ("Smart City Project Manager", "Government"),
    ("Real Estate Sales Manager", "Real Estate"),
    ("Property Valuer", "Real Estate"),
    ("Facility Manager", "Facilities Management"),
    ("Legal Counsel", "Legal"),
    ("HR Business Partner", "Human Resources"),
    ("Talent Acquisition Lead", "Human Resources"),
    ("Logistics Manager", "Logistics"),
    ("International Trade Manager", "Trade"),
    ("ESG Analyst", "Sustainability"),
    ("Digital Marketing Manager", "Marketing"),
]

def generate_jd(job_title, industry):
    generate_prompt = f"""
You are a top-tier HR consultant. Write a world-class 
Job Description for a {job_title} in the {industry} industry.

This JD will be used as a reference example to train 
an AI to generate better JDs. It must be exceptionally 
well-written, specific and professional.

Format with these exact sections:
1. About the Role (3 lines — compelling and specific)
2. Key Responsibilities (10 bullet points — action verbs, specific)
3. Required Qualifications (education, years, certifications)
4. Skills and Tools (specific tools and technologies)
5. Good to Have (5 complementary skills)
6. What We Offer (culture, growth, benefits)

Write only the JD. No preamble. No explanation.
Make it the best possible JD for this role.
"""
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": generate_prompt}],
        model="llama-3.1-8b-instant",
        temperature=0.7,
        max_tokens=1500,
    )
    return chat_completion.choices[0].message.content

def main():
    db_client = get_db()
    for i, (job_title, industry) in enumerate(roles):
        try:
            generated_jd = generate_jd(job_title, industry)
            db_client.execute(
                "INSERT INTO reference_jds (job_title, industry, jd_text, source) VALUES (?, ?, ?, ?)",
                (job_title, industry, generated_jd, "AI-Generated-HighQuality")
            )
            print(f"Generated {i+1}/50: {job_title} - {industry}")
        except Exception as e:
            print(f"Error generating {job_title}: {e}")
        time.sleep(15)
    db_client.close()

if __name__ == "__main__":
    main()
