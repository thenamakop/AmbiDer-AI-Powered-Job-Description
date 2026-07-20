import { useLocation } from 'react-router-dom';
import { Sparkles, FileText, Bookmark, BarChart2, Clock, FileBarChart, Settings, HelpCircle, LogOut } from 'lucide-react';
import './Sidebar.css';

function Sidebar({ onNavigate, user, onLogout }) {
  const location = useLocation();
  const currentPath = location.pathname;

  return (
    <aside className="sidebar">
      <div className="sidebar-top">
        <img src="/logo.png" alt="AmbiDer Logo" className="sidebar-logo" onError={(e) => {
          e.target.style.display = 'none';
          document.getElementById('sidebar-fallback-logo-text').style.display = 'block';
        }} />
        <h2 id="sidebar-fallback-logo-text" style={{display: 'none', color: 'var(--primary)', fontWeight: 'bold', margin: '0'}}>AmbiDer</h2>
        <div className="sidebar-subtitle">Job Description Generator</div>
      </div>

      <nav className="sidebar-nav">
        <button
          className={`sidebar-nav-item ${currentPath === '/' || currentPath === '/output' ? 'active' : ''}`}
          onClick={() => onNavigate('/')}
        >
          <Sparkles className="nav-icon" />
          <span>Generate JD</span>
        </button>

        <button
          className={`sidebar-nav-item ${currentPath === '/templates' ? 'active' : ''}`}
          onClick={() => onNavigate('/templates')}
        >
          <FileText className="nav-icon" />
          <span>Templates</span>
        </button>

        <button
          className={`sidebar-nav-item ${currentPath === '/saved' ? 'active' : ''}`}
          onClick={() => onNavigate('/saved')}
        >
          <Bookmark className="nav-icon" />
          <span>Saved JDs</span>
        </button>

        <button 
          className={`sidebar-nav-item ${currentPath === '/analytics' ? 'active' : ''}`}
          onClick={() => onNavigate('/analytics')}
        >
          <BarChart2 className="nav-icon" />
          <span>Analytics</span>
        </button>

        <button 
          className={`sidebar-nav-item ${currentPath === '/history' ? 'active' : ''}`}
          onClick={() => onNavigate('/history')}
        >
          <Clock className="nav-icon" />
          <span>History</span>
        </button>
        
        <button 
          className={`sidebar-nav-item ${currentPath === '/reports' ? 'active' : ''}`}
          onClick={() => onNavigate('/reports')}
        >
          <FileBarChart className="nav-icon" />
          <span>Reports</span>
        </button>

        <div className="sidebar-divider"></div>

        <button 
          className={`sidebar-nav-item ${currentPath === '/settings' ? 'active' : ''}`}
          onClick={() => onNavigate('/settings')}
        >
          <Settings className="nav-icon" />
          <span>Settings</span>
        </button>

        <button className="sidebar-nav-item">
          <HelpCircle className="nav-icon" />
          <span>Help & Support</span>
        </button>
      </nav>

      {user && (
        <div className="sidebar-bottom">
          <div className="sidebar-user">
            <div className="sidebar-user-name">{user.full_name}</div>
            <button className="sidebar-logout-btn" onClick={onLogout} title="Logout">
              <LogOut size={16} />
              <span>Logout</span>
            </button>
          </div>
        </div>
      )}
    </aside>
  );
}

export default Sidebar;
