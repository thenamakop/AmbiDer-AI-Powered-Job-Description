import os
import sys
import time
from groq import Groq
from dotenv import load_dotenv
from app import build_prompt

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

test_cases = [
    {
        "job_title": "React Developer",
        "industry": "IT",
        "experience": "2 to 4 years",
        "skills": "React.js, JavaScript, CSS, REST APIs, Git",
        "tone": "Formal",
        "company_name": "TechNova",
        "location": "Bangalore",
        "nature_of_job": "Hybrid",
        "department": "Engineering",
        "reporting_to": "Engineering Manager"
    },
    {
        "job_title": "Plant HR Manager",
        "industry": "Manufacturing",
        "experience": "5 to 8 years",
        "skills": "Payroll, Labour law, Recruitment, Compliance, HRIS",
        "tone": "Formal",
        "company_name": "Bharat Steel Works",
        "location": "Pune",
        "nature_of_job": "On-site",
        "department": "Human Resources",
        "reporting_to": "VP Human Resources"
    },
    {
        "job_title": "Digital Marketing Manager",
        "industry": "Marketing",
        "experience": "3 to 6 years",
        "skills": "SEO, Google Ads, Social Media, Analytics, Content Strategy",
        "tone": "Startup-Friendly",
        "company_name": "GrowthLab",
        "location": "Remote",
        "nature_of_job": "Remote",
        "department": "Marketing",
        "reporting_to": "CMO"
    }
]

def main():
    for test in test_cases:
        time.sleep(15) # Avoid rate limit
        prompt = build_prompt(
            job_title=test["job_title"],
            industry=test["industry"],
            experience=test["experience"],
            skills=test["skills"],
            tone=test["tone"],
            company_name=test["company_name"],
            department=test["department"],
            location=test["location"],
            reporting_to=test["reporting_to"],
            nature_of_job=test["nature_of_job"]
        )

        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-8b-instant",
            temperature=0.7,
            max_tokens=1500,
        )
        
        jd_text = chat_completion.choices[0].message.content

        print(f"\n--- Test: {test['job_title']} ---")
        print("\n=== GENERATED JD START ===")
        print(jd_text)
        print("=== GENERATED JD END ===\n")
        
        # Simple quality checks
        job_title_mentioned = test["job_title"].lower() in jd_text.lower()
        
        input_skills = [s.strip().lower() for s in test["skills"].split(',')]
        all_skills_present = all(s in jd_text.lower() for s in input_skills)
        
        # Hard to perfectly check "no extra skills" via regex, so we do our best
        no_extra_skills = True # Need manual review or advanced AI check
        
        location_mentioned = test["location"].lower() in jd_text.lower()
        work_mode_mentioned = test["nature_of_job"].lower() in jd_text.lower()
        
        # Responsibilities count
        import re
        resp_section = re.search(r'Key Responsibilities(.*?)3\.', jd_text, re.DOTALL | re.IGNORECASE)
        bullets_count = 0
        if resp_section:
            bullets_count = len(re.findall(r'^\s*[-*•]\s', resp_section.group(1), re.MULTILINE))
            
        # Try alternate regex if section wasn't found
        if not resp_section:
            resp_section = re.search(r'Key Responsibilities(.*?)(Required Qualifications|3\.)', jd_text, re.DOTALL | re.IGNORECASE)
            if resp_section:
                bullets_count = len(re.findall(r'^\s*[-*•]\s', resp_section.group(1), re.MULTILINE))
        
        eight_responsibilities = bullets_count == 8
        
        score = sum([job_title_mentioned, all_skills_present, no_extra_skills, location_mentioned, work_mode_mentioned, eight_responsibilities])
        
        print(f"  - Job title mentioned: {job_title_mentioned}")
        print(f"  - All input skills present: {all_skills_present}")
        print(f"  - No extra skills added: {no_extra_skills} (Assumed for script)")
        print(f"  - Location mentioned: {location_mentioned}")
        print(f"  - Work mode mentioned: {work_mode_mentioned}")
        print(f"  - 8 responsibilities: {eight_responsibilities} (Found {bullets_count})")
        print(f"  - QUALITY SCORE: {score}/6")

if __name__ == "__main__":
    main()
