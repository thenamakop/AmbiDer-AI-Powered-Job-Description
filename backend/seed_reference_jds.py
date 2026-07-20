import libsql_experimental as libsql
import os
from dotenv import load_dotenv

load_dotenv()

conn = libsql.connect(
    database=os.getenv("TURSO_DATABASE_URL"),
    auth_token=os.getenv("TURSO_AUTH_TOKEN")
)

jds = [

# ── IT ────────────────────────────────────────────────────────────────────

(
"Software Engineer", "IT", "LinkedIn",
"""About the Role
We are looking for a skilled Software Engineer to design, develop and maintain scalable web applications. You will work closely with cross-functional teams to deliver high quality software solutions that meet business requirements.

Key Responsibilities
- Design and develop scalable backend services and REST APIs using Node.js and Python
- Build responsive and performant frontend interfaces using React.js
- Collaborate with product managers to translate requirements into technical solutions
- Write clean, well-documented and testable code following best practices
- Participate in code reviews and contribute to improving team standards
- Troubleshoot and debug production issues in a timely manner
- Optimize application performance and ensure high availability
- Stay updated with emerging technologies and propose improvements

Required Qualifications
- Bachelor's degree in Computer Science or related field
- 2 to 4 years of experience in software development
- Strong proficiency in JavaScript, Node.js and React.js
- Experience with relational and non-relational databases

Skills and Tools
JavaScript, React.js, Node.js, REST APIs, Git, MongoDB, PostgreSQL, Docker

Good to Have
- Experience with cloud platforms like AWS or GCP
- Knowledge of CI/CD pipelines
- Familiarity with microservices architecture

What We Offer
Competitive salary, flexible work hours, remote work options, continuous learning budget and a collaborative team environment focused on growth."""
),

(
"Frontend Developer", "IT", "Naukri",
"""About the Role
We are seeking a talented Frontend Developer to build exceptional user interfaces for our web applications. You will be responsible for translating UI/UX designs into high quality code and ensuring the best visual and technical experience for our users.

Key Responsibilities
- Develop new user-facing features using React.js and modern JavaScript
- Build reusable components and front-end libraries for future use
- Translate designs and wireframes into high quality code
- Optimize components for maximum performance across devices and browsers
- Collaborate with backend developers to integrate APIs
- Ensure the technical feasibility of UI/UX designs
- Maintain and improve existing codebase
- Participate in agile ceremonies including sprint planning and retrospectives

Required Qualifications
- Bachelor's degree in Computer Science or related field
- 1 to 3 years of experience in frontend development
- Strong proficiency in HTML5, CSS3 and JavaScript ES6+
- Experience with React.js and component-based architecture

Skills and Tools
HTML5, CSS3, JavaScript, React.js, TypeScript, Tailwind CSS, Git, Figma, REST APIs

Good to Have
- Experience with Next.js or similar frameworks
- Knowledge of web performance optimization
- Familiarity with testing frameworks like Jest

What We Offer
Flexible work schedule, remote-friendly environment, quarterly performance bonuses and opportunity to work on cutting-edge products."""
),

(
"Backend Developer", "IT", "Indeed",
"""About the Role
We are looking for an experienced Backend Developer to build and maintain robust server-side applications. You will design APIs, manage databases and ensure our backend systems are scalable, secure and performant.

Key Responsibilities
- Design, build and maintain efficient and reliable backend services
- Develop and document RESTful APIs consumed by frontend and mobile teams
- Manage and optimize database schemas and queries
- Implement security best practices including authentication and authorization
- Monitor system performance and resolve bottlenecks
- Collaborate with frontend developers on API design and integration
- Write unit and integration tests to ensure code quality
- Participate in architecture discussions and technical planning

Required Qualifications
- Bachelor's degree in Computer Science, Engineering or related field
- 3 to 5 years of backend development experience
- Strong proficiency in Python or Java
- Experience with SQL and NoSQL databases

Skills and Tools
Python, Flask or Django, PostgreSQL, MongoDB, Redis, Docker, AWS, Git, Postman

Good to Have
- Experience with message queues like RabbitMQ or Kafka
- Knowledge of containerization and orchestration tools
- Familiarity with GraphQL

What We Offer
Competitive compensation, health benefits, remote work flexibility, learning and development allowance and a culture that values technical excellence."""
),

(
"Data Analyst", "IT", "LinkedIn",
"""About the Role
We are looking for a detail-oriented Data Analyst to interpret data and turn it into actionable insights. You will work with business stakeholders to understand data needs and deliver reports, dashboards and analyses that drive decisions.

Key Responsibilities
- Collect, clean and analyse large datasets from multiple sources
- Build and maintain dashboards and reports using BI tools
- Identify trends, patterns and anomalies in data
- Collaborate with business teams to understand reporting requirements
- Present findings to stakeholders in a clear and concise manner
- Support A/B testing and experiment design
- Ensure data accuracy and integrity across systems
- Document data models, definitions and processes

Required Qualifications
- Bachelor's degree in Statistics, Mathematics, Computer Science or related field
- 2 to 4 years of experience in data analysis
- Strong proficiency in SQL and Excel
- Experience with Python or R for data manipulation

Skills and Tools
SQL, Python, Excel, Tableau or Power BI, Google Analytics, Pandas, NumPy, Git

Good to Have
- Experience with cloud data warehouses like BigQuery or Redshift
- Knowledge of machine learning basics
- Familiarity with ETL pipelines

What We Offer
Competitive salary, data-driven culture, exposure to large-scale datasets, flexible work arrangements and strong learning opportunities."""
),

(
"DevOps Engineer", "IT", "Glassdoor",
"""About the Role
We are seeking a skilled DevOps Engineer to build and manage our infrastructure and deployment pipelines. You will work closely with development teams to enable fast, reliable and secure software delivery.

Key Responsibilities
- Design and maintain CI/CD pipelines for automated testing and deployment
- Manage and provision cloud infrastructure using Infrastructure as Code tools
- Monitor system health, performance and availability using observability tools
- Implement and maintain containerization and orchestration solutions
- Collaborate with development teams to improve deployment practices
- Ensure security and compliance across all infrastructure components
- Automate repetitive operational tasks to improve efficiency
- Respond to incidents and conduct post-mortems

Required Qualifications
- Bachelor's degree in Computer Science, IT or related field
- 3 to 5 years of DevOps or SRE experience
- Strong experience with AWS, Azure or GCP
- Proficiency in scripting languages like Bash or Python

Skills and Tools
AWS, Docker, Kubernetes, Terraform, Jenkins, GitHub Actions, Linux, Prometheus, Grafana

Good to Have
- Experience with service mesh technologies
- Knowledge of security scanning and compliance tools
- Certifications in AWS or Kubernetes

What We Offer
Remote-first culture, top-tier infrastructure stack, incident response training, generous learning budget and performance-based bonuses."""
),

# ── MANUFACTURING ─────────────────────────────────────────────────────────

(
"Plant HR Manager", "Manufacturing", "Naukri",
"""About the Role
We are looking for an experienced Plant HR Manager to lead all human resources functions at our manufacturing facility. You will be responsible for managing the complete employee lifecycle, ensuring statutory compliance and fostering a positive workplace culture on the shop floor.

Key Responsibilities
- Manage end-to-end recruitment for plant-level positions including operators and technicians
- Oversee payroll processing, attendance management and leave administration
- Ensure compliance with labour laws including Factories Act, PF, ESI and Gratuity
- Handle employee grievances and disciplinary proceedings at the plant level
- Coordinate with plant managers on manpower planning and deployment
- Conduct employee engagement initiatives and welfare activities
- Manage contract labour and liaise with labour contractors
- Prepare and submit statutory returns and reports to government authorities

Required Qualifications
- MBA or PGDM in Human Resources Management
- 5 to 8 years of HR experience in a manufacturing or industrial setup
- Thorough knowledge of Indian labour laws and statutory compliance
- Experience handling a workforce of 500 or more employees

Skills and Tools
Payroll software, HRIS, MS Excel, Labour law compliance, Contract labour management, Industrial relations

Good to Have
- Experience with ISO or SA8000 certification audits
- Knowledge of safety management systems
- Proficiency in local regional language

What We Offer
Stable work environment, quarterly performance bonus, on-site accommodation option, provident fund benefits and long-term growth within a reputed manufacturing group."""
),

(
"Production Engineer", "Manufacturing", "Indeed",
"""About the Role
We are seeking a Production Engineer to oversee and optimize manufacturing processes at our plant. You will ensure that production targets are met while maintaining quality standards, safety protocols and cost efficiency.

Key Responsibilities
- Plan and schedule daily production activities to meet output targets
- Monitor production processes and identify areas for efficiency improvement
- Coordinate with maintenance teams to minimize downtime and equipment failures
- Implement lean manufacturing and Six Sigma methodologies on the shop floor
- Prepare daily, weekly and monthly production reports for management review
- Ensure adherence to safety norms and quality standards during production
- Train and guide junior production staff and machine operators
- Collaborate with procurement for timely availability of raw materials

Required Qualifications
- Bachelor's degree in Mechanical, Industrial or Production Engineering
- 3 to 6 years of experience in a manufacturing environment
- Knowledge of lean manufacturing and process improvement techniques
- Familiarity with ERP systems for production planning

Skills and Tools
AutoCAD, SAP or Oracle ERP, MS Excel, Lean manufacturing, Six Sigma, Quality control tools

Good to Have
- Six Sigma Green Belt or Black Belt certification
- Experience with ISO 9001 quality management systems
- Knowledge of TPM methodology

What We Offer
Competitive CTC, annual performance appraisal, subsidized meals at plant canteen, safety training programmes and career growth in a large manufacturing conglomerate."""
),

(
"Quality Analyst", "Manufacturing", "LinkedIn",
"""About the Role
We are looking for a Quality Analyst to ensure our products meet the highest quality standards before reaching customers. You will be responsible for inspection, testing and documentation of quality processes across our manufacturing operations.

Key Responsibilities
- Conduct incoming, in-process and final product inspections as per quality plans
- Perform dimensional, functional and visual inspection of manufactured parts
- Investigate quality failures and initiate corrective and preventive actions
- Maintain and calibrate measuring instruments and testing equipment
- Prepare quality reports, NCRs and inspection records
- Collaborate with production and engineering teams on quality improvements
- Ensure compliance with customer specifications and industry standards
- Participate in internal and external quality audits

Required Qualifications
- Diploma or Bachelor's degree in Mechanical or Production Engineering
- 2 to 5 years of quality inspection experience in manufacturing
- Knowledge of quality tools like SPC, FMEA, Control Charts, 8D
- Experience reading engineering drawings and GD&T

Skills and Tools
Vernier caliper, CMM, SPC software, MS Excel, AutoCAD, ISO 9001, APQP, PPAP

Good to Have
- Experience with IATF 16949 automotive quality standards
- Knowledge of Six Sigma methodology
- Familiarity with ERP quality modules

What We Offer
Technical skill development, exposure to world-class quality systems, quarterly incentives, health insurance and stable long-term career in a growing manufacturing company."""
),

(
"Safety Officer", "Manufacturing", "Naukri",
"""About the Role
We are hiring a Safety Officer to implement, monitor and enforce health, safety and environment standards at our manufacturing plant. You will play a critical role in creating a zero-accident workplace culture.

Key Responsibilities
- Develop and implement safety policies, procedures and training programmes
- Conduct regular safety inspections and audits across plant areas
- Investigate workplace accidents and near-miss incidents and recommend preventive measures
- Ensure compliance with Factories Act, OSHA and other statutory safety requirements
- Organize safety drills including fire evacuation and first aid exercises
- Maintain all safety records, permits to work and accident registers
- Liaise with government safety inspectors and statutory authorities
- Train employees on safe operating procedures and personal protective equipment

Required Qualifications
- Diploma in Industrial Safety or B.E. with ADIS certification
- 3 to 6 years of safety experience in a manufacturing or industrial facility
- Knowledge of legal and regulatory requirements under Factories Act
- Certified first aider

Skills and Tools
Safety audit tools, Incident investigation methodology, Fire safety systems, MS Excel, PPE standards, HIRA

Good to Have
- NEBOSH certification
- Experience with ISO 45001 occupational health and safety management
- Knowledge of chemical or hazardous material handling

What We Offer
Career growth in HSE function, uniform and PPE provided, statutory benefits, annual safety bonus for achieving zero-incident milestones and government-recognized safety certifications."""
),

(
"Plant Manager", "Manufacturing", "Glassdoor",
"""About the Role
We are looking for an experienced Plant Manager to lead all operations at our manufacturing facility. You will be responsible for production, quality, safety, maintenance and people management to ensure the plant operates at peak efficiency and profitability.

Key Responsibilities
- Lead and manage all plant operations including production, quality, maintenance and logistics
- Develop and execute production plans to meet customer delivery schedules
- Drive continuous improvement initiatives to reduce costs and increase productivity
- Ensure compliance with safety, environmental and quality standards
- Manage plant budgets, capital expenditure and cost control initiatives
- Build and develop a high-performing team of engineers, supervisors and operators
- Liaise with customers, suppliers and corporate management on plant performance
- Analyse KPIs and prepare monthly MIS reports for senior management

Required Qualifications
- Bachelor's or Master's degree in Mechanical, Production or Industrial Engineering
- 12 to 18 years of experience in manufacturing with at least 5 years in a leadership role
- Proven track record of managing a plant with 500 or more employees
- Strong knowledge of lean manufacturing, Six Sigma and ERP systems

Skills and Tools
SAP or Oracle ERP, Lean manufacturing, Six Sigma, MS Excel, Power BI, P&L management

Good to Have
- MBA in Operations Management
- Experience in setting up greenfield manufacturing facilities
- Knowledge of export compliance and international quality standards

What We Offer
Senior leadership role, executive compensation package, performance-linked annual bonus, company accommodation and car, comprehensive health benefits for family and long-term career progression."""
),

# ── HEALTHCARE ────────────────────────────────────────────────────────────

(
"ICU Nurse", "Healthcare", "Indeed",
"""About the Role
We are looking for a dedicated and experienced ICU Nurse to provide critical care to patients in our intensive care unit. You will work as part of a multidisciplinary team to deliver high-quality, patient-centred care in a fast-paced clinical environment.

Key Responsibilities
- Monitor and assess patients' vital signs and clinical condition continuously
- Administer medications, IV fluids and treatments as prescribed by physicians
- Operate and troubleshoot critical care equipment including ventilators and cardiac monitors
- Respond promptly to changes in patient condition and initiate emergency protocols
- Maintain accurate and detailed patient records and nursing notes
- Educate patients and families on treatment plans and post-discharge care
- Collaborate with doctors, specialists and allied health professionals
- Maintain strict infection control and hygiene standards in the ICU

Required Qualifications
- B.Sc. Nursing or GNM from a recognised institution
- Valid nursing registration with the State Nursing Council
- 2 to 5 years of ICU or critical care nursing experience
- BLS and ACLS certification

Skills and Tools
Ventilator management, Cardiac monitoring, IV administration, Patient assessment, Electronic medical records, BLS, ACLS

Good to Have
- CCRN or similar critical care nursing certification
- Experience with ECMO or CRRT procedures
- Ability to mentor junior nursing staff

What We Offer
Competitive salary as per healthcare industry standards, shift allowances, annual appraisal, health insurance for self and family, CPD training and a respectful and supportive work environment."""
),

(
"Hospital Administrator", "Healthcare", "LinkedIn",
"""About the Role
We are seeking a capable Hospital Administrator to manage the overall non-clinical operations of our hospital. You will ensure smooth day-to-day functioning across departments while maintaining quality standards and patient satisfaction.

Key Responsibilities
- Oversee daily hospital operations including housekeeping, security, billing and patient services
- Manage hospital budgets, procurement and vendor contracts
- Coordinate between clinical departments and administrative functions
- Ensure compliance with NABH, JCI or other accreditation standards
- Monitor patient satisfaction scores and implement improvement initiatives
- Manage staff scheduling, attendance and administrative HR functions
- Handle patient complaints and escalations professionally and promptly
- Prepare operational reports and present to hospital management and trustees

Required Qualifications
- MBA in Hospital Administration or MHA from a recognised institution
- 5 to 8 years of hospital administration experience
- Knowledge of NABH accreditation standards and healthcare regulations
- Experience managing a hospital with 200 or more beds

Skills and Tools
Hospital Management Systems, MS Office Suite, Budget management, Quality management systems, Patient feedback tools

Good to Have
- Six Sigma certification in healthcare quality
- Experience with hospital ERP systems
- Knowledge of CGHS and insurance billing processes

What We Offer
Senior management role, competitive salary, health insurance, annual performance bonus, professional development support and opportunity to lead a growing healthcare institution."""
),

(
"Clinical Research Associate", "Healthcare", "Naukri",
"""About the Role
We are hiring a Clinical Research Associate to monitor and coordinate clinical trials at our research sites. You will ensure that clinical studies are conducted in compliance with ICH-GCP guidelines, protocol requirements and regulatory standards.

Key Responsibilities
- Conduct site initiation, monitoring and close-out visits for clinical trials
- Verify informed consent process and patient eligibility at research sites
- Review source documents and case report forms for accuracy and completeness
- Ensure compliance with GCP, ICH guidelines and local regulatory requirements
- Communicate protocol deviations and adverse events to the sponsor and IRB
- Maintain trial master file and site documentation
- Train site staff on protocol procedures and data collection requirements
- Coordinate with investigators and site coordinators on trial progress

Required Qualifications
- Bachelor's or Master's degree in Life Sciences, Pharmacy or Medicine
- 1 to 3 years of CRA or clinical research experience
- Good understanding of ICH-GCP and clinical trial regulations in India
- Willingness to travel to clinical sites across India

Skills and Tools
EDC systems like Medidata Rave, ICH-GCP, CTMS, MS Excel, Medical terminology, Site monitoring tools

Good to Have
- ACRP or SOCRA CRA certification
- Experience with Phase II or Phase III oncology trials
- Knowledge of CDSCO regulatory requirements

What We Offer
Competitive salary, travel reimbursement, annual bonus, professional certification support, exposure to multi-country clinical programmes and career growth in the CRO industry."""
),

(
"Pharmacist", "Healthcare", "Indeed",
"""About the Role
We are looking for a qualified Pharmacist to manage the dispensing of medications and provide pharmaceutical care to patients at our hospital pharmacy. You will ensure safe, accurate and efficient medication management across all departments.

Key Responsibilities
- Dispense prescription medications accurately and counsel patients on proper use
- Verify prescriptions for completeness, appropriateness and potential drug interactions
- Maintain adequate inventory levels and manage procurement of drugs and consumables
- Ensure storage of medications as per cold chain and pharmaceutical standards
- Coordinate with clinical teams on medication management and pharmacovigilance
- Maintain records as per pharmacy and drug control regulations
- Conduct medication reconciliation for admitted patients
- Train pharmacy assistants and interns

Required Qualifications
- B.Pharma or M.Pharma from a recognised institution
- Registered pharmacist with the State Pharmacy Council
- 2 to 4 years of hospital pharmacy experience
- Knowledge of drug regulations and pharmacy laws in India

Skills and Tools
Pharmacy Management Software, Drug interaction databases, Inventory management, Cold chain management, MS Excel

Good to Have
- Experience with oncology or parenteral nutrition pharmacy
- Knowledge of NABH pharmacy standards
- Familiarity with insurance and CGHS billing for medications

What We Offer
Stable employment, health insurance, uniform allowance, shift-based duty structure, annual appraisal and professional development through CME programmes."""
),

(
"Lab Technician", "Healthcare", "Glassdoor",
"""About the Role
We are seeking a skilled Lab Technician to perform diagnostic tests and assist in laboratory procedures at our pathology department. You will ensure accurate, timely and quality test results that support clinical decision-making.

Key Responsibilities
- Collect blood, urine and other biological specimens from patients
- Perform haematology, biochemistry, microbiology and serology tests
- Operate and maintain laboratory equipment including analyzers and centrifuges
- Ensure quality control of test procedures and report results accurately
- Follow biosafety guidelines and infection control protocols at all times
- Maintain laboratory records, specimen logs and test registers
- Assist pathologist in histopathology and cytology specimen processing
- Coordinate with clinical wards for urgent sample collection and reporting

Required Qualifications
- Diploma or B.Sc. in Medical Laboratory Technology from a recognised institution
- Registration with the Allied Health Council or equivalent
- 1 to 3 years of clinical laboratory experience
- Knowledge of standard laboratory procedures and quality control

Skills and Tools
Laboratory analysers, Microscopy, LIS software, Biosafety protocols, Phlebotomy, Quality control tools

Good to Have
- Experience with molecular diagnostics or PCR techniques
- Knowledge of NABL accreditation requirements
- Familiarity with histopathology staining techniques

What We Offer
Fixed working shifts, health benefits, uniform provided, annual increment, safe and well-equipped laboratory environment and career growth within a multi-specialty hospital group."""
),

# ── BFSI ─────────────────────────────────────────────────────────────────

(
"Credit Risk Analyst", "BFSI", "LinkedIn",
"""About the Role
We are looking for a Credit Risk Analyst to assess, monitor and manage credit risk across our lending portfolio. You will analyse borrower financials, prepare credit proposals and support the credit team in making sound lending decisions.

Key Responsibilities
- Analyse financial statements and creditworthiness of individual and corporate borrowers
- Prepare detailed credit appraisal notes and risk assessment reports
- Monitor existing loan accounts for early warning signals and portfolio health
- Conduct industry and sector analysis to assess macro-level credit risks
- Support relationship managers in structuring credit facilities
- Ensure compliance with RBI guidelines and internal credit policies
- Assist in preparation of credit committee presentations
- Maintain and update credit risk databases and MIS reports

Required Qualifications
- Bachelor's or Master's degree in Finance, Economics or CA
- 2 to 5 years of credit risk or credit analysis experience in a bank or NBFC
- Strong knowledge of financial statement analysis and credit appraisal
- Understanding of RBI lending norms and banking regulations

Skills and Tools
MS Excel, Financial modelling, Credit rating tools, Bloomberg or Reuters, RBI guidelines, Power BI

Good to Have
- CFA Level 1 or FRM certification
- Experience with retail or SME credit assessment
- Knowledge of Basel III credit risk framework

What We Offer
Competitive compensation, exposure to diverse credit portfolios, professional certification support, annual performance bonus, health insurance and fast-track career growth in risk management."""
),

(
"Branch Manager", "BFSI", "Naukri",
"""About the Role
We are seeking a high-performing Branch Manager to lead and manage all operations at our bank branch. You will be responsible for business development, customer service, team management and ensuring compliance with regulatory requirements.

Key Responsibilities
- Lead branch operations and ensure achievement of business targets including CASA, loans and fee income
- Build and manage relationships with high-value customers and corporate clients
- Supervise branch staff and conduct regular performance reviews
- Ensure branch compliance with RBI guidelines, KYC norms and internal audit requirements
- Handle customer escalations and ensure high levels of service quality
- Manage branch cash, vault operations and daily reconciliation
- Develop new business through networking, referrals and community engagement
- Prepare and submit branch MIS reports to the regional office

Required Qualifications
- Bachelor's or Master's degree in Finance, Commerce or Business Administration
- 8 to 12 years of banking experience with at least 3 years in branch management
- Strong knowledge of retail banking products and RBI regulations
- Proven track record of achieving business targets

Skills and Tools
Core Banking Software, MS Excel, CRM systems, KYC and AML tools, Financial planning tools

Good to Have
- MBA in Finance or Banking
- JAIIB or CAIIB certification
- Experience in a high-footfall urban branch

What We Offer
Leadership role with P&L responsibility, attractive performance-linked incentive, company car allowance, health insurance, provident fund and structured career path to regional level."""
),

(
"Compliance Officer", "BFSI", "Indeed",
"""About the Role
We are looking for a diligent Compliance Officer to ensure that our financial institution operates within all applicable legal and regulatory frameworks. You will be responsible for developing and implementing compliance programmes and monitoring adherence across the organisation.

Key Responsibilities
- Monitor and ensure compliance with RBI, SEBI, AMFI and other regulatory requirements
- Develop, update and implement compliance policies and procedures
- Conduct internal compliance audits and identify areas of regulatory risk
- Report compliance findings to senior management and the board
- Liaise with regulators during inspections and examinations
- Train employees on compliance requirements, AML and KYC norms
- Review and clear new products, processes and marketing materials for compliance
- Maintain compliance registers, breach logs and regulatory correspondence

Required Qualifications
- Bachelor's degree in Law, Finance or Commerce with a compliance qualification
- 4 to 8 years of compliance experience in a bank, NBFC or financial institution
- In-depth knowledge of RBI regulations, PMLA, FEMA and banking laws
- Experience dealing with regulatory authorities

Skills and Tools
Compliance management software, AML monitoring tools, MS Office, Regulatory reporting systems, Legal research databases

Good to Have
- CAMS certification for AML compliance
- Experience with GDPR or international data privacy regulations
- Legal qualification or LLB degree

What We Offer
Senior role with direct board-level exposure, competitive salary, professional certification reimbursement, stable employment in a regulated environment and health and retirement benefits."""
),

(
"Relationship Manager", "BFSI", "Glassdoor",
"""About the Role
We are hiring a Relationship Manager to manage and grow our portfolio of retail and HNI customers. You will be responsible for understanding customer financial needs, offering appropriate products and building long-term profitable relationships.

Key Responsibilities
- Manage and grow a book of retail, HNI or SME clients as assigned
- Identify and cross-sell banking products including investments, insurance, loans and trade finance
- Conduct regular client meetings and portfolio reviews
- Achieve revenue targets through new client acquisition and existing client deepening
- Ensure KYC compliance and accurate documentation for all clients
- Resolve customer queries and escalate complex issues appropriately
- Stay updated on market trends, products and competitor offerings
- Prepare client presentations and periodic portfolio performance reports

Required Qualifications
- Bachelor's or Master's degree in Finance, Commerce or Business Administration
- 3 to 6 years of relationship management experience in banking or wealth management
- AMFI or IRDA certification as applicable
- Strong sales and communication skills

Skills and Tools
CRM software, Bloomberg or Reuters, MS Excel, Wealth management platforms, Financial planning tools

Good to Have
- CFP or CWM certification
- Experience managing an AUM of Rs.50 crore or more
- Knowledge of derivatives and structured products

What We Offer
High earning potential with performance-linked incentives, access to premium client segment, fast-track career growth, travel allowance and comprehensive benefits package."""
),

(
"Audit Manager", "BFSI", "LinkedIn",
"""About the Role
We are looking for an experienced Audit Manager to lead internal audit functions for our financial institution. You will plan and execute risk-based audits, report findings to senior management and support the organisation in strengthening internal controls.

Key Responsibilities
- Plan, execute and report on risk-based internal audits across business units and functions
- Evaluate the adequacy and effectiveness of internal controls, risk management and governance
- Lead a team of auditors and review audit working papers and reports
- Present audit findings and recommendations to senior management and audit committee
- Follow up on management action plans and track resolution of audit findings
- Assess compliance with RBI guidelines, SOX requirements and internal policies
- Conduct special investigations and forensic audit assignments as required
- Keep current with regulatory changes and evolving audit standards

Required Qualifications
- Chartered Accountant or MBA in Finance with internal audit background
- 8 to 12 years of internal audit experience in banking or financial services
- Knowledge of risk-based auditing methodology and internal control frameworks
- Experience managing a team of 5 or more auditors

Skills and Tools
ACL or IDEA audit software, MS Excel, Power BI, COSO framework, Risk assessment matrices, Banking CBS

Good to Have
- CIA or CISA certification
- Experience with big four or internal audit consulting background
- Knowledge of Basel III and ICAAP frameworks

What We Offer
Senior leadership role with audit committee access, competitive salary, annual performance bonus, professional certification support, health insurance and long-term career growth in a systemically important financial institution."""
),

# ── RETAIL ───────────────────────────────────────────────────────────────

(
"Store Manager", "Retail", "Naukri",
"""About the Role
We are looking for a dynamic Store Manager to lead the operations of our retail store. You will be responsible for driving sales, managing staff, maintaining store standards and delivering an exceptional customer experience.

Key Responsibilities
- Manage all day-to-day store operations including opening and closing procedures
- Drive achievement of daily, weekly and monthly sales targets
- Lead, motivate and develop a team of sales associates and department heads
- Monitor inventory levels, conduct stock audits and manage shrinkage
- Ensure visual merchandising standards are maintained as per brand guidelines
- Handle customer escalations and ensure high levels of service satisfaction
- Review store KPIs including conversion rate, average basket value and footfall
- Coordinate with area manager and corporate on store initiatives and campaigns

Required Qualifications
- Bachelor's degree in Business, Retail Management or related field
- 5 to 8 years of retail experience with at least 2 years in store management
- Proven ability to manage a team of 20 or more people
- Strong understanding of retail operations and sales driving techniques

Skills and Tools
POS systems, Inventory management software, MS Excel, Visual merchandising, Customer service tools

Good to Have
- Experience in fashion, lifestyle or FMCG retail
- Knowledge of loyalty programme management
- Multilingual communication skills

What We Offer
Attractive base salary plus sales incentive, staff discounts, health insurance, annual increment, structured training programmes and career growth across our growing retail network."""
),

(
"Category Manager", "Retail", "Indeed",
"""About the Role
We are seeking an analytical Category Manager to own and drive the performance of specific product categories. You will be responsible for range selection, pricing strategy, supplier management and sales growth for your assigned categories.

Key Responsibilities
- Develop and implement category strategy to drive revenue and profitability growth
- Manage supplier relationships, negotiate terms, pricing and promotional support
- Analyse category performance data and identify trends and opportunities
- Build and manage product assortments and planograms for stores
- Collaborate with marketing on promotional campaigns and trade activations
- Monitor competitor activity and market trends within the category
- Work with supply chain on inventory planning and stock availability
- Prepare category business reviews and present to senior management

Required Qualifications
- Bachelor's or Master's degree in Business, Marketing or related field
- 4 to 7 years of category management or buying experience in retail
- Strong analytical skills with experience in data-driven decision making
- Experience managing P&L for a category with a turnover of Rs.50 crore or more

Skills and Tools
MS Excel, Power BI, ERP systems, Nielsen or IRI data, Planogram software, Supplier management tools

Good to Have
- Experience in FMCG, electronics or apparel categories
- Knowledge of e-commerce category management
- MBA from a premier institution

What We Offer
Competitive salary, exposure to end-to-end category ownership, annual performance bonus, travel allowance for supplier meetings, health benefits and fast-track career growth."""
),

(
"Visual Merchandiser", "Retail", "LinkedIn",
"""About the Role
We are looking for a creative and detail-oriented Visual Merchandiser to create compelling in-store displays that drive customer engagement and sales. You will be responsible for bringing the brand to life in our stores through thoughtful and strategic merchandising.

Key Responsibilities
- Plan and implement visual merchandising displays as per brand guidelines and seasonal themes
- Conduct window dressing and key focal point displays across all store locations
- Train store teams on VM standards and ensure consistent execution
- Analyse sales data to optimise product placement and display effectiveness
- Coordinate with buying and marketing teams on new product launches
- Manage VM props, signage and display materials inventory
- Conduct regular store audits and provide feedback to store teams
- Stay updated on retail design trends and competitor VM practices

Required Qualifications
- Diploma or Bachelor's degree in Fashion Design, Interior Design or Visual Merchandising
- 2 to 4 years of visual merchandising experience in a retail brand
- Strong creative skills with a keen eye for colour, layout and aesthetics
- Willingness to travel to multiple store locations

Skills and Tools
Adobe Photoshop, Illustrator, AutoCAD, Planogram software, MS Office, Photography tools

Good to Have
- Experience in fashion or luxury retail VM
- Knowledge of retail space planning principles
- Photography and styling skills

What We Offer
Creative work environment, travel to multiple store locations, annual performance bonus, staff discounts, professional development workshops and exposure to national retail campaigns."""
),

(
"Supply Chain Analyst", "Retail", "Glassdoor",
"""About the Role
We are looking for a Supply Chain Analyst to support our retail supply chain operations. You will analyse supply chain data, identify inefficiencies and recommend improvements to ensure optimal inventory levels and on-time product availability.

Key Responsibilities
- Analyse supply chain performance data including fill rates, lead times and stock availability
- Support demand forecasting and replenishment planning processes
- Monitor inventory levels across stores and distribution centres
- Identify and resolve supply chain disruptions in collaboration with suppliers and logistics partners
- Prepare supply chain KPI dashboards and reports for management
- Support implementation of supply chain improvement projects
- Coordinate with buying, logistics and store operations teams on supply chain matters
- Assist in vendor evaluation and performance tracking

Required Qualifications
- Bachelor's degree in Supply Chain Management, Logistics, Operations or related field
- 2 to 4 years of supply chain or logistics analysis experience
- Strong analytical skills and proficiency in Excel and data tools
- Understanding of retail replenishment and inventory management

Skills and Tools
MS Excel, Power BI, SAP or Oracle SCM, Demand planning tools, Warehouse management systems

Good to Have
- APICS CSCP or CPIM certification
- Experience with e-commerce fulfillment operations
- Knowledge of import and customs processes

What We Offer
Analytical and fast-paced work environment, competitive salary, annual bonus, health insurance, flexible work arrangements and career development in a leading retail organisation."""
),

(
"Retail Buyer", "Retail", "Naukri",
"""About the Role
We are seeking an experienced Retail Buyer to select and procure products that meet customer demand and support our commercial strategy. You will manage supplier relationships, negotiate terms and build winning product ranges for our stores.

Key Responsibilities
- Develop seasonal buying strategies aligned with category plans and customer insights
- Select and curate product ranges across assigned categories or brands
- Negotiate pricing, payment terms and exclusivity with suppliers
- Monitor sell-through rates and make markdown or replenishment decisions
- Collaborate with visual merchandising and marketing on product launches
- Analyse competitor ranges and market trends to stay ahead of the curve
- Manage open-to-buy budgets and ensure margin targets are achieved
- Build strong, long-term relationships with key suppliers and brand partners

Required Qualifications
- Bachelor's or Master's degree in Fashion Management, Business or Retail
- 4 to 7 years of buying or merchandising experience in a retail organisation
- Strong commercial acumen with experience managing a buying budget
- Good negotiation and supplier management skills

Skills and Tools
MS Excel, ERP buying modules, Planogram tools, Sales analytics platforms, Supplier portals

Good to Have
- Experience in international sourcing or private label development
- Knowledge of sustainable and ethical sourcing practices
- Language skills for dealing with international suppliers

What We Offer
Commercial leadership role, competitive salary, product travel to trade shows and supplier markets, annual buying bonus, staff discounts and career growth in a dynamic retail business."""
),

# ── EDUCATION ────────────────────────────────────────────────────────────

(
"Curriculum Designer", "Education", "LinkedIn",
"""About the Role
We are looking for an innovative Curriculum Designer to develop engaging, effective and learner-centred educational content. You will work with subject matter experts and instructional designers to create curricula that meet learning objectives and standards.

Key Responsibilities
- Design and develop curriculum frameworks, lesson plans and learning objectives
- Collaborate with subject matter experts to ensure content accuracy and relevance
- Create engaging learning materials including modules, assessments and multimedia content
- Apply instructional design principles including Bloom's taxonomy and backward design
- Review and evaluate existing curricula and recommend improvements
- Develop assessment tools to measure learner outcomes effectively
- Align curriculum to regulatory standards and accreditation requirements
- Stay updated on educational research and emerging pedagogical practices

Required Qualifications
- Master's degree in Education, Instructional Design, Curriculum Development or related field
- 3 to 6 years of curriculum design experience in K-12, higher education or corporate learning
- Strong understanding of instructional design models like ADDIE and SAM
- Experience using LMS platforms and e-learning authoring tools

Skills and Tools
Articulate Storyline, Adobe Captivate, Moodle or Canvas LMS, MS Office, SCORM, Bloom's taxonomy

Good to Have
- Experience with gamification or adaptive learning design
- Knowledge of accessibility standards for educational content
- Proficiency in graphic design or video production for e-learning

What We Offer
Creative and purpose-driven work environment, competitive salary, professional development through educational conferences, flexible work arrangements and opportunity to impact thousands of learners."""
),

(
"Admission Counsellor", "Education", "Naukri",
"""About the Role
We are hiring an Admission Counsellor to guide prospective students through the admissions process and help them make informed decisions about their educational journey. You will be the first point of contact for students and parents enquiring about our programmes.

Key Responsibilities
- Counsel prospective students and parents on programme offerings, eligibility and career pathways
- Handle inbound enquiries via phone, email, WhatsApp and walk-ins
- Conduct campus tours and information sessions for prospective students
- Follow up with leads and convert enquiries into confirmed admissions
- Achieve monthly and annual admission targets set by the management
- Maintain accurate records of student interactions in the CRM system
- Participate in school visits, education fairs and outreach events
- Coordinate with academic departments on admission requirements and documentation

Required Qualifications
- Bachelor's degree in any discipline with strong communication skills
- 1 to 3 years of admissions, sales or counselling experience
- Empathetic and student-centric approach
- Ability to handle high volumes of enquiries and work under targets

Skills and Tools
CRM software like Salesforce or LeadSquared, MS Excel, WhatsApp Business, Zoom or Teams for virtual counselling

Good to Have
- Experience in higher education admissions
- Knowledge of career counselling tools and psychometric assessments
- Multilingual communication skills

What We Offer
Performance-linked incentive on top of fixed salary, conveyance allowance, health insurance, training on counselling techniques and career growth within a growing educational institution."""
),

(
"Academic Coordinator", "Education", "Indeed",
"""About the Role
We are looking for an organised and proactive Academic Coordinator to manage academic schedules, faculty coordination and student academic support. You will ensure the smooth delivery of academic programmes and serve as a bridge between faculty, students and administration.

Key Responsibilities
- Coordinate academic calendars, examination schedules and timetables
- Liaise with faculty to ensure timely completion of syllabi and academic plans
- Monitor student attendance, academic progress and flag at-risk students for support
- Organise academic events including guest lectures, seminars and workshops
- Maintain student academic records and generate required reports
- Handle student grievances related to academics and escalate where necessary
- Coordinate with the examination department for internal and external assessments
- Support accreditation processes by maintaining required documentation

Required Qualifications
- Master's degree in Education, Management or a related field
- 2 to 5 years of academic administration or coordination experience
- Strong organisational and multitasking skills
- Proficiency in academic management systems

Skills and Tools
ERP academic modules, MS Excel, Google Workspace, LMS platforms, Student information systems

Good to Have
- Experience with NAAC or NIRF accreditation processes
- Knowledge of NEP 2020 framework
- Familiarity with student counselling and support systems

What We Offer
Stable academic work environment, leaves aligned with academic calendar, health benefits, professional development support and opportunity to make a meaningful impact on student success."""
),

(
"Training Manager", "Education", "Glassdoor",
"""About the Role
We are seeking an experienced Training Manager to design, deliver and manage learning and development programmes for our institution's staff and faculty. You will build a culture of continuous learning and professional excellence.

Key Responsibilities
- Conduct training needs analysis across departments and identify learning gaps
- Design and develop training programmes for faculty, administrative staff and leadership
- Facilitate training sessions including workshops, e-learning and blended learning programmes
- Manage the training calendar, logistics and post-training evaluation
- Evaluate training effectiveness using Kirkpatrick model and ROI measures
- Partner with external trainers and vendors for specialised training content
- Maintain training records and prepare L&D reports for management
- Build and manage the institution's learning management system

Skills and Tools
LMS platforms, Articulate Storyline, MS Office, Training evaluation tools, Facilitation skills, Instructional design

Required Qualifications
- MBA or PGDM in HRM or Master's degree in Education
- 5 to 8 years of training and development experience
- Strong facilitation and presentation skills
- Experience managing a training function in an educational or corporate environment

Good to Have
- CPTD or ATD certification
- Experience with leadership development programmes
- Knowledge of competency framework design

What We Offer
Intellectually stimulating environment, opportunity to shape institutional learning culture, competitive salary, leaves aligned to academic calendar, health benefits and long-term career in the education sector."""
),

(
"Content Writer Education", "Education", "Naukri",
"""About the Role
We are looking for a skilled Content Writer to develop high-quality academic and marketing content for our educational institution. You will write across multiple formats and platforms to support student engagement, brand building and academic publishing.

Key Responsibilities
- Write and edit academic content including study materials, assignments and case studies
- Create engaging digital content for website, blog, social media and email campaigns
- Collaborate with subject matter experts to develop accurate and relevant educational articles
- Produce marketing content including brochures, emailers and programme descriptions
- Ensure content is aligned with brand guidelines and institutional tone of voice
- Conduct research on educational trends, industry developments and academic topics
- Proofread and edit content from other team members before publication
- Manage content calendar and ensure timely delivery of all content pieces

Required Qualifications
- Bachelor's or Master's degree in English, Journalism, Communications or Education
- 2 to 4 years of content writing experience preferably in the education sector
- Excellent written communication skills in English
- Experience writing for both academic and general audiences

Skills and Tools
MS Word, Google Docs, WordPress or CMS platforms, SEO tools like SEMrush, Canva, Grammarly

Good to Have
- Experience with video script writing or podcast content
- Knowledge of academic writing styles like APA or MLA
- SEO content writing experience

What We Offer
Creative and purposeful writing environment, flexible work arrangements, byline opportunities on published content, annual appraisal, health benefits and exposure to a wide variety of content formats."""
),

# ── STARTUPS ─────────────────────────────────────────────────────────────

(
"Growth Marketing Manager", "Startups", "LinkedIn",
"""About the Role
We are looking for a data-driven and creative Growth Marketing Manager to own and drive our customer acquisition and retention strategy. You will experiment rapidly, scale what works and build a growth engine that drives sustainable business growth.

Key Responsibilities
- Develop and execute multi-channel growth marketing campaigns across SEO, SEM, social media, email and partnerships
- Build and optimise acquisition funnels from awareness to conversion
- Run rapid A/B tests and growth experiments to identify high-ROI channels
- Analyse marketing data and KPIs to drive informed decisions and optimise spend
- Collaborate with product and engineering teams on growth features and optimisations
- Manage performance marketing budgets and ensure positive CAC/LTV ratios
- Build referral, retention and loyalty programmes to reduce churn
- Lead a team of marketing specialists and agency partners

Required Qualifications
- Bachelor's or Master's degree in Marketing, Business or related field
- 3 to 6 years of growth marketing experience preferably in a B2C startup
- Proven track record of driving measurable growth through digital channels
- Strong analytical skills with experience using marketing analytics tools

Skills and Tools
Google Analytics, Google Ads, Meta Ads Manager, HubSpot or Klaviyo, SEMrush, SQL basics, Power BI

Good to Have
- Experience scaling a startup from Series A to Series B or beyond
- Knowledge of product-led growth strategies
- Familiarity with attribution modelling and incrementality testing

What We Offer
Fast-paced and high-ownership environment, ESOPs, flexible work hours, competitive salary, remote-friendly culture and opportunity to build a marketing function from the ground up."""
),

(
"Product Manager", "Startups", "Naukri",
"""About the Role
We are hiring a Product Manager to define, build and ship products that customers love. You will own the product roadmap, work closely with engineering and design and be the voice of the customer within the organisation.

Key Responsibilities
- Define and prioritise the product roadmap based on customer insights, data and business strategy
- Write clear and detailed product requirement documents and user stories
- Collaborate with engineering, design and data teams to ship high-quality features
- Conduct user research, interviews and usability testing to validate product decisions
- Define and track product KPIs and use data to iterate and improve
- Manage the product backlog and facilitate agile ceremonies
- Communicate product vision and progress to stakeholders and leadership
- Identify market opportunities and competitive differentiators

Required Qualifications
- Bachelor's or Master's degree in Engineering, Business or Computer Science
- 3 to 5 years of product management experience in a technology product company
- Strong understanding of product development methodologies including agile and scrum
- Experience with user research and data-driven product decisions

Skills and Tools
Jira or Linear, Figma, Mixpanel or Amplitude, SQL basics, Notion, UserTesting platforms

Good to Have
- Experience building consumer mobile or SaaS products
- Technical background in software development
- MBA from a premier institution

What We Offer
High-autonomy product ownership, ESOPs, competitive salary, flexible work arrangements, learning budget and opportunity to shape the product of a fast-growing startup."""
),

(
"Full Stack Developer Startup", "Startups", "Indeed",
"""About the Role
We are looking for a talented Full Stack Developer to help us build and scale our product. You will work across the entire stack, own features end-to-end and contribute to building a product used by thousands of customers.

Key Responsibilities
- Design and build new product features across the full stack from frontend to backend
- Write clean, scalable and well-tested code across React and Node.js or Python
- Collaborate with product managers and designers to translate requirements into great user experiences
- Participate in architecture decisions and technical planning sessions
- Conduct code reviews and mentor junior developers on the team
- Optimise application performance, scalability and reliability
- Contribute to CI/CD pipeline and DevOps practices
- Stay current with emerging technologies and propose improvements

Required Qualifications
- Bachelor's degree in Computer Science or equivalent practical experience
- 2 to 5 years of full stack development experience
- Proficiency in React.js and a backend framework like Node.js, Django or Flask
- Experience with SQL and NoSQL databases and cloud deployment

Skills and Tools
React.js, Node.js or Python, PostgreSQL, MongoDB, AWS or GCP, Docker, Git, REST APIs, TypeScript

Good to Have
- Experience with real-time applications using WebSockets
- Knowledge of mobile development with React Native
- Contributions to open source projects

What We Offer
Competitive salary with ESOPs, flexible and remote-friendly work culture, ownership of meaningful features, learning and conference budget, and the excitement of building something from early stage."""
),

(
"Operations Manager Startup", "Startups", "Glassdoor",
"""About the Role
We are looking for a hands-on Operations Manager to build and optimise the operational backbone of our startup. You will work across functions to streamline processes, manage vendors and ensure the business runs efficiently as we scale.

Key Responsibilities
- Design and implement operational processes and SOPs across the organisation
- Manage vendors, service providers and third-party partnerships
- Monitor operational KPIs and identify bottlenecks and areas for improvement
- Coordinate cross-functional projects and ensure timely delivery
- Support the finance team on budgeting, forecasting and cost optimisation
- Build and manage the operations team as the company scales
- Handle logistics, supply chain or fulfilment operations as applicable to the business
- Prepare weekly and monthly operational reports for the leadership team

Required Qualifications
- Bachelor's or Master's degree in Business, Operations or Engineering
- 4 to 7 years of operations experience preferably in a startup or high-growth company
- Strong problem-solving and process improvement skills
- Experience managing teams and external partners

Skills and Tools
MS Excel, ERP or operations management software, Project management tools like Asana or Notion, Data analysis tools

Good to Have
- Experience in logistics, supply chain or marketplace operations
- Knowledge of lean or agile operations principles
- Familiarity with financial modelling and budgeting

What We Offer
High ownership and visibility role, competitive salary, ESOPs, flexible work culture, opportunity to build operational systems from scratch and direct impact on the company's growth trajectory."""
),

(
"Customer Success Manager", "Startups", "LinkedIn",
"""About the Role
We are hiring a Customer Success Manager to ensure our customers achieve their desired outcomes using our product. You will build deep relationships with customers, drive adoption and reduce churn through proactive engagement and support.

Key Responsibilities
- Onboard new customers and ensure a smooth and successful product adoption journey
- Build and maintain strong relationships with key customer stakeholders
- Conduct regular business reviews and share product usage insights with customers
- Identify upsell and cross-sell opportunities within the existing customer base
- Monitor customer health scores and proactively address at-risk accounts
- Collaborate with product teams to relay customer feedback and feature requests
- Manage renewals and work with the sales team on account expansion
- Develop playbooks and best practices for the CS team

Required Qualifications
- Bachelor's degree in Business, Communications or related field
- 2 to 5 years of customer success or account management experience in a SaaS company
- Strong empathy for customers and a solutions-oriented mindset
- Experience using CS tools and CRM platforms

Skills and Tools
Gainsight or ChurnZero, Salesforce, Intercom, MS Excel, Zoom, Jira for escalation management

Good to Have
- Experience working with enterprise or mid-market SaaS customers
- Knowledge of SaaS metrics including NRR, NPS and CSAT
- Technical background to understand and explain product capabilities

What We Offer
Competitive salary with performance bonus, ESOPs, flexible and remote-first work culture, strong learning environment and the opportunity to be a key part of a customer-centric high-growth startup."""
),

# ── GOVERNMENT ───────────────────────────────────────────────────────────

(
"Project Officer", "Government", "Indeed",
"""About the Role
We are looking for a Project Officer to support the planning, implementation and monitoring of government development projects. You will coordinate with multiple stakeholders, track project milestones and ensure effective utilisation of public resources.

Key Responsibilities
- Assist in the planning, designing and implementation of government schemes and projects
- Coordinate with district authorities, NGOs, community organisations and beneficiaries
- Monitor project progress against targets and prepare periodic status reports
- Facilitate community meetings, beneficiary consultations and stakeholder engagements
- Maintain project documentation including reports, proposals and correspondence
- Support procurement processes in compliance with government financial rules
- Analyse field data and prepare MIS reports for senior officials and funding agencies
- Identify implementation challenges and recommend corrective actions

Required Qualifications
- Bachelor's or Master's degree in Public Policy, Development Studies, Social Work or related field
- 2 to 5 years of experience in government projects or development sector programmes
- Knowledge of government schemes, implementation frameworks and financial management rules
- Willingness to travel extensively to field locations

Skills and Tools
MS Office, GIS basics, MIS reporting tools, Government portal systems, Data analysis tools

Good to Have
- Experience with World Bank, UNDP or other multilateral funded projects
- Knowledge of government procurement rules like GFR or GeM
- Proficiency in regional language of the state

What We Offer
Stable government-linked employment, travel allowance, accommodation support for field postings, PF and gratuity benefits and opportunity to contribute to meaningful development outcomes at the grassroots level."""
),

(
"Policy Analyst", "Government", "LinkedIn",
"""About the Role
We are looking for an analytical and insightful Policy Analyst to support evidence-based policymaking for government programmes. You will research, analyse and provide recommendations on complex policy issues across social, economic and governance domains.

Key Responsibilities
- Conduct in-depth research and analysis on policy issues, legislation and regulatory frameworks
- Review and evaluate existing government policies and programmes for effectiveness and impact
- Prepare policy briefs, cabinet notes, discussion papers and background reports
- Analyse quantitative and qualitative data to draw insights for policy recommendations
- Engage with stakeholders including ministries, industry bodies, civil society and academia
- Monitor implementation of policy decisions and assess outcomes
- Track national and international policy trends and best practices
- Present research findings to senior government officials and policymakers

Required Qualifications
- Master's degree or PhD in Public Policy, Economics, Political Science or related field
- 3 to 7 years of policy research or analysis experience
- Strong analytical, writing and communication skills
- Ability to work in a complex multi-stakeholder government environment

Skills and Tools
STATA or R for data analysis, MS Office, Policy research databases, NITI Aayog frameworks, Parliament and legislative databases

Good to Have
- Experience with international development organisations or think tanks
- Knowledge of SDG framework and India's voluntary national reviews
- Proficiency in Hindi or other regional languages

What We Offer
High-impact policy work at the national level, competitive compensation for government advisory roles, exposure to senior policymakers, research publication opportunities and a career at the intersection of data and governance."""
),

(
"Programme Coordinator", "Government", "Naukri",
"""About the Role
We are hiring a Programme Coordinator to manage the day-to-day coordination of government-sponsored programmes and schemes. You will work with implementation partners, field teams and government officials to ensure effective programme delivery.

Key Responsibilities
- Coordinate programme implementation activities across districts and states
- Liaise with government departments, NGO partners and community organisations
- Organise capacity building workshops and training sessions for field staff
- Collect, verify and compile programme data from field reports and partner submissions
- Prepare monthly and quarterly progress reports for programme management and funding agencies
- Support procurement and logistics for programme materials and activities
- Facilitate stakeholder meetings, reviews and convergence activities
- Maintain programme documentation and financial records

Required Qualifications
- Bachelor's or Master's degree in Social Work, Public Administration or Development Studies
- 3 to 5 years of programme coordination experience in government or NGO sector
- Strong coordination and communication skills
- Experience with MIS, data management and report writing

Skills and Tools
MS Excel, MIS portals, Government scheme management systems, Google Workspace, Video conferencing tools

Good to Have
- Experience with centrally sponsored schemes like MGNREGS, PMGSY or NRHM
- Knowledge of social audits and community monitoring mechanisms
- Proficiency in regional language

What We Offer
Stable employment in the development sector, opportunity to work on nationally significant programmes, travel allowance and accommodation for field visits, PF benefits and a career contributing directly to social change."""
),

(
"District Manager Government", "Government", "Glassdoor",
"""About the Role
We are looking for an experienced District Manager to oversee the implementation of government programmes and schemes across an assigned district. You will coordinate between state headquarters, local administration and field teams to ensure effective service delivery.

Key Responsibilities
- Oversee implementation of all assigned government schemes across the district
- Manage a team of field officers, coordinators and support staff
- Liaise with district collector, block development officers and other government officials
- Monitor programme targets, expenditure and outcomes on a regular basis
- Facilitate community outreach and beneficiary enrolment for government schemes
- Conduct field visits to verify programme implementation and beneficiary satisfaction
- Prepare district-level reports and present to state programme management unit
- Handle grievances from beneficiaries and local officials promptly

Required Qualifications
- Bachelor's or Master's degree in Public Administration, Rural Development or related field
- 6 to 10 years of experience in government programme implementation
- Experience in a district or block-level leadership role
- Strong people management and stakeholder coordination skills

Skills and Tools
MS Excel, Government MIS portals, GeM portal, Field data collection apps, Reporting tools

Good to Have
- Experience with district administration, collector office or DRDA
- Knowledge of public financial management and government accounting
- Regional language proficiency

What We Offer
Leadership role in government programme delivery, competitive salary for development sector, field travel support, PF and gratuity, job security and a meaningful career serving communities at the grassroots."""
),

(
"Data Officer Government", "Government", "Indeed",
"""About the Role
We are looking for a Data Officer to manage, analyse and report on data for government programmes and digital initiatives. You will ensure data quality, build dashboards and support evidence-based decision-making for senior government officials.

Key Responsibilities
- Collect, clean, validate and maintain programme data from multiple sources and field teams
- Build and maintain MIS dashboards and reporting systems for programme monitoring
- Analyse data to identify trends, gaps and implementation issues at district and state level
- Prepare data-driven reports, infographics and presentations for senior officials
- Train field staff and partner organisations on data collection tools and processes
- Ensure data security and confidentiality in compliance with government data policies
- Support development and maintenance of government databases and portals
- Coordinate with technology teams on digital data systems and integrations

Required Qualifications
- Bachelor's or Master's degree in Statistics, Computer Science, IT or Economics
- 2 to 5 years of data management or analytics experience
- Proficiency in MS Excel, SQL and basic data visualisation tools
- Experience working with government MIS or programme data systems

Skills and Tools
MS Excel, SQL, Power BI or Tableau, Government MIS portals, Python basics, QGIS or ArcGIS for spatial data

Good to Have
- Experience with national programme data systems like HMIS, PFMS or NIC portals
- Knowledge of open government data standards
- Familiarity with GIS and spatial data analysis

What We Offer
Stable government-linked employment, exposure to national data systems and digital governance, competitive salary for public sector advisory roles, annual increment, PF benefits and opportunity to drive data literacy in government programmes."""
),

]

print(f"Inserting {len(jds)} reference JDs...")

for i, (job_title, industry, source, jd_text) in enumerate(jds):
    conn.execute(
        "INSERT INTO reference_jds (job_title, industry, jd_text, source) VALUES (?, ?, ?, ?)",
        [job_title, industry, jd_text, source]
    )
    print(f"Inserted {i+1}/{len(jds)}: {job_title} - {industry}")

conn.commit()
conn.close()
print("All 80 JDs inserted successfully.")