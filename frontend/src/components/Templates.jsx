import { Briefcase, Code, Megaphone, PenTool, Database, Users } from 'lucide-react';
import './Pages.css';

const TEMPLATES = [
  {
    title: 'Software Engineer',
    industry: 'Technology',
    experience: '3-5 years',
    skills: 'React, Node.js, Python, AWS, SQL',
    department: 'Engineering',
    icon: Code
  },
  {
    title: 'Product Manager',
    industry: 'Technology',
    experience: '5+ years',
    skills: 'Agile, JIRA, Roadmap Planning, Stakeholder Management, Data Analysis',
    department: 'Product',
    icon: Briefcase
  },
  {
    title: 'Marketing Specialist',
    industry: 'Marketing',
    experience: '2-4 years',
    skills: 'SEO, Content Strategy, Google Analytics, Social Media Management',
    department: 'Marketing',
    icon: Megaphone
  },
  {
    title: 'UI/UX Designer',
    industry: 'Design',
    experience: '3+ years',
    skills: 'Figma, Adobe Creative Suite, Prototyping, User Research',
    department: 'Design',
    icon: PenTool
  },
  {
    title: 'Data Scientist',
    industry: 'Data',
    experience: '4+ years',
    skills: 'Python, R, Machine Learning, SQL, Data Visualization',
    department: 'Data Analytics',
    icon: Database
  },
  {
    title: 'HR Generalist',
    industry: 'Human Resources',
    experience: '2-5 years',
    skills: 'Employee Relations, Recruiting, Onboarding, HRIS',
    department: 'Human Resources',
    icon: Users
  }
];

function Templates({ onNavigate }) {
  const handleUseTemplate = (template) => {
    onNavigate('/', {
      job_title: template.title,
      industry: template.industry,
      experience: template.experience,
      skills: template.skills,
      department: template.department,
      tone: 'Professional'
    });
  };

  return (
    <div className="page-container">
      <div className="page-header-row">
        <h2>JD Templates</h2>
      </div>
      <p style={{ color: 'var(--text-secondary)', marginBottom: '24px', fontSize: '14px' }}>
        Start quickly with one of our pre-configured job description templates.
      </p>

      <div className="jds-grid">
        {TEMPLATES.map((tpl, idx) => {
          const Icon = tpl.icon;
          return (
            <div className="jd-list-card" key={idx} style={{ cursor: 'pointer', transition: 'all 0.2s' }} onClick={() => handleUseTemplate(tpl)}>
              <div className="jd-card-info">
                <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '8px' }}>
                  <div style={{ background: '#FFF0EA', padding: '8px', borderRadius: '8px', color: '#E8510A' }}>
                    <Icon size={20} />
                  </div>
                  <div className="jd-card-title" style={{ margin: 0 }}>{tpl.title}</div>
                </div>
                <div className="jd-card-meta" style={{ marginTop: '12px' }}>
                  <span className="industry-tag">{tpl.industry}</span>
                  <span style={{ fontSize: '12px', color: 'var(--text-secondary)' }}>{tpl.experience}</span>
                </div>
                <div style={{ marginTop: '12px', fontSize: '12px', color: 'var(--text-secondary)', lineHeight: '1.5' }}>
                  <strong>Skills:</strong> {tpl.skills}
                </div>
              </div>
              <div className="jd-card-actions" style={{ borderTop: '1px solid var(--border)', paddingTop: '12px', marginTop: '12px' }}>
                <button className="report-primary-btn" style={{ width: '100%', padding: '8px', fontSize: '13px' }} onClick={(e) => { e.stopPropagation(); handleUseTemplate(tpl); }}>
                  Use Template
                </button>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default Templates;
