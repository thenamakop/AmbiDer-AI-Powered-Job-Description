AmbiDer — AI-Pow ered Job Description Generator
A web app that generates, edits, scores, and stores professional job descriptions using an AI backend. Designed for recruiters and hiring managers who want high-quality, structured JDs quickly. The repo contains a Flask-based API (backend) and a React + Vite frontend; both are configured to deploy together on Vercel.

Key features
Generate job descriptions using an LLM (via Groq client).
Edit generated JDs with instruction-based rewriting.
Save, list, delete and view history of JDs per user.
ATS scoring endpoint to evaluate JD quality.
JWT-based authentication (register, login, me).
Simple local DB storage (SQLite) with optional Turso/libsql integration for production.
Stack
Language(s): Python (backend), JavaScript/React (frontend)
Framework / runtime:
Backend: Flask
Frontend: React + Vite
Notable libraries:
Backend: flask, flask-jwt-extended, flask-cors, groq (Groq client), libsql-client (optional), bcrypt (optional)
Frontend: react, react-router-dom, react-markdown, recharts
Repository layout
Code
api/                   # Vercel serverless entry that imports backend.app
backend/               # Flask application + DB helper
  app.py               # Main Flask app — endpoints, AI prompt builder, auth
  db.py                # DB initialization and transport (SQLite wrapper / libsql)
  requirements.txt     # backend Python deps
frontend/              # React + Vite frontend
  package.json         # frontend deps & scripts
  src/                 # React source (entry: src/main.jsx)
requirements.txt       # top-level Python deps (for Vercel function bundling)
vercel.json            # Vercel build & route configuration (serves API + frontend/dist)
.gitignore
How it fits together:

Vercel runs api/index.py as the serverless function entry (it inserts backend/ into sys.path and imports the Flask app from backend/app.py).
The frontend is a Vite app built into dist and served as static files. API routes under /api/* are routed to the Python function by vercel.json.
The Flask app uses a small wrapper in backend/db.py to connect to either a libsql/Turso DB (when configured) or a local SQLite file (fallback). JWT tokens secure most endpoints.
API (major endpoints)
Authentication

POST /auth/register or /api/auth/register
Body: { full_name, email, password }
Returns: token and user
POST /auth/login or /api/auth/login
Body: { email, password }
Returns: token and user
GET /auth/me or /api/auth/me
JWT required. Returns current user info.
Job description operations

POST /generate or /api/generate
JWT optional. Body contains fields used to build the AI prompt (job_title, industry, skills, tone, etc.). Requires Groq API configured; otherwise responds with "AI service not configured".
POST /edit or /api/edit
JWT optional. Provide current_jd and instruction to get an edited version from the AI.
POST /save or /api/save
JWT required. Save a JD to saved_jds table.
GET /saved or /api/saved
JWT required. List saved JDs (supports ?search=).
DELETE /saved/<id> or /api/saved/<id>
JWT required. Delete a saved JD owned by user.
GET /history or /api/history
JWT required. Returns saved JDs plus edit history.
GET /analytics or /api/analytics
JWT required. Returns stats for the user.
POST /ats-score or /api/ats-score
JWT optional. Returns a JSON ATS score (0–100) plus a breakdown and tips.
Health

GET /, /health, or /api/health
Notes:

Many endpoints are mirrored under /api/* and root paths.
Some endpoints return a descriptive error when the Groq client is not configured (GROQ_API_KEY missing).
Database
On startup, backend/db.py::init_db() creates these tables if missing:
users
saved_jds
reference_jds
jd_edits
Database transport:
If TURSO_DATABASE_URL and TURSO_AUTH_TOKEN are set and libsql_client is available, the app tries to use Turso.
Otherwise it falls back to a local SQLite file: backend/app.db, or a temp file when deployed where the repository path is not writable (Vercel).
Password hashing:
Uses bcrypt if available; otherwise falls back to SHA-256 (less secure — bcrypt recommended).
Environment variables
Create a .env file (not included). Key vars used by the app:

JWT_SECRET_KEY — secret used by flask-jwt-extended (defaults to "ambider-jd-secret-2025" if unset).
GROQ_API_KEY — required to enable the AI features (generation, edit, ATS scoring).
TURSO_DATABASE_URL — optional, Turso connection URL for libsql.
TURSO_AUTH_TOKEN — optional, auth token for Turso.
VERCEL — (set by platform); db path selection uses presence of VERCEL to switch to temp DB file.
Additionally, the backend sets SSL_CERT_FILE using certifi internally.

Local development
Prerequisites

Python 3.10+ (or supported by the dependencies)
Node.js (recommended LTS) and npm/yarn
(Optional) A Groq API key if you want to test AI endpoints.
Backend (run locally)

Create and activate a virtual environment:
python -m venv .venv
source .venv/bin/activate (Windows: .venv\Scripts\activate)
Install Python dependencies:
pip install -r backend/requirements.txt (Top-level requirements.txt contains similar entries used for the Vercel function.)
Create a .env file in repo root or backend/ with the environment variables above (GROQ_API_KEY if available).
Initialize DB (app will auto-initialize on first request; you can also run):
python backend/db.py
Run the Flask app:
python backend/app.py
By default app.run(debug=False) starts a server on 127.0.0.1:5000
Frontend

Move to frontend directory:
cd frontend
Install deps:
npm install
Run dev server:
npm run dev
Build for production:
npm run build
After build, dist/ is produced and served in Vercel configuration.
Example: Generate a JD (curl)

Register/login to get a JWT (token).
Example generate call: curl -X POST http://localhost:5000/generate
-H "Content-Type: application/json"
-H "Authorization: Bearer <JWT_TOKEN>"
-d '{ "job_title":"Senior Backend Engineer", "industry":"IT", "experience":"5+ years", "skills":"Python,Flask,SQL", "tone":"Professional", "company_name":"Acme Corp", "location":"Remote", "nature_of_job":"Remote" }'
If GROQ_API_KEY is not set, /generate will return an error: {"error":"AI service not configured"}.

Deployment
The repository includes a top-level vercel.json that:
Builds api/index.py as a Python serverless function (includes backend/** in the function bundle).
Builds the React frontend with frontend/package.json using the static-build adapter and serves frontend/dist.
On Vercel, the system environment should include GROQ_API_KEY and any DB credentials (TURSO vars) you want to use. If you do not provide a writable filesystem, the app will use a temp file for SQLite.
Troubleshooting & notes
If bcrypt isn't available, the code falls back to SHA-256 hashing — install bcrypt for secure hashing: pip install bcrypt
If libsql_client and Turso vars are present but the connection fails, the app falls back to local SQLite and logs a warning.
To allow the AI endpoints to work, set GROQ_API_KEY in environment. The code expects the Groq client to expose chat completions with model "llama-3.1-8b-instant".
The API expects the DB to be initialized automatically, but you can run backend/db.py directly to pre-create tables.
Contributing
Open issues for bugs or feature requests.
Suggested improvements: add CI tests, add E2E tests for frontend/backend, add migration scripts and stronger secrets handling, add proper license.
License
No license file is present. Add a LICENSE if you plan to open-source this project.

