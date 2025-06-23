import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

# Настройка страницы
st.set_page_config(
    page_title="LibreChat Clone",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Кастомный CSS для стилизации
st.markdown("""
<style>
    /* Основные цвета и фон */
    .main {
        background-color: #f8fafc;
    }
    
    /* Стилизация сайдбара */
    .css-1d391kg {
        background-color: #ffffff;
        border-right: 1px solid #e2e8f0;
    }
    
    /* Карточки с градиентами */
    .gradient-card {
        padding: 2rem;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s;
        cursor: pointer;
        min-height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    .gradient-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
    }
    
    .green-gradient {
        background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
    }
    
    .blue-gradient {
        background: linear-gradient(135deg, #3b82f6 0%, #1e40af 100%);
    }
    
    .purple-gradient {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%, #dc2626 100%);
    }
    
    .red-gradient {
        background: linear-gradient(135deg, #dc2626 0%, #991b1b 50%, #4c1d95 100%);
    }
    
    .teal-gradient {
        background: linear-gradient(135deg, #14b8a6 0%, #0f766e 100%);
    }
    
    .orange-gradient {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
    }
    
    .card-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .card-title {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .card-subtitle {
        font-size: 1rem;
        opacity: 0.9;
    }
    
    /* Quick Start секция */
    .quick-start-card {
        background: #f1f5f9;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
        text-align: center;
    }
    
    .quick-start-icon {
        font-size: 2rem;
        margin-bottom: 1rem;
    }
    
    /* Заголовки */
    .section-title {
        font-size: 2rem;
        font-weight: bold;
        color: #1e293b;
        margin-bottom: 1rem;
    }
    
    .subsection-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #334155;
        margin: 2rem 0 1rem 0;
    }
    
    /* Навигация */
    .nav-item {
        padding: 0.5rem 1rem;
        margin: 0.25rem 0;
        border-radius: 6px;
        cursor: pointer;
        transition: background-color 0.2s;
    }
    
    .nav-item:hover {
        background-color: #f1f5f9;
    }
    
    .nav-item.active {
        background-color: #dbeafe;
        color: #2563eb;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# Сайдбар навигация
with st.sidebar:
    st.markdown("### 🤖 LibreChat")
    
    # Основное меню
    selected = option_menu(
        menu_title=None,
        options=["Get Started", "Features", "Local Installation", "Remote Hosting", "Configuration", "User Guides", "Translation"],
        icons=["play-circle", "star", "laptop", "cloud", "gear", "book", "translate"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#64748b", "font-size": "18px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#f1f5f9"},
            "nav-link-selected": {"background-color": "#dbeafe", "color": "#2563eb"},
        }
    )
    
    # Дополнительные разделы
    st.markdown("---")
    st.markdown("**Development**")
    st.markdown("**Documentation**")
    st.markdown("---")
    st.markdown("⚙️ System")

# Основной контент
if selected == "Get Started":
    # Заголовок страницы
    st.markdown('<h1 class="section-title">Get Started</h1>', unsafe_allow_html=True)
    
    # Quick Start Guides
    st.markdown('<h2 class="subsection-title">Quick Start Guides</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="quick-start-card">
            <div class="quick-start-icon">⚡</div>
            <h3>Quick Local Setup</h3>
            <p>Get started quickly with local installation</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="quick-start-card">
            <div class="quick-start-icon">🔗</div>
            <h3>Custom Endpoints</h3>
            <p>Configure custom API endpoints</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Explore Documentation
    st.markdown('<h2 class="subsection-title">Explore our Documentation</h2>', unsafe_allow_html=True)
    
    # Первый ряд карточек
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("", key="local_install"):
            st.success("Local Installation selected!")
        st.markdown("""
        <div class="gradient-card green-gradient" style="margin-top: -3rem;">
            <div class="card-icon">💻</div>
            <div class="card-title">Local Installation</div>
            <div class="card-subtitle">Set up on your machine</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        if st.button("", key="remote_hosting"):
            st.success("Remote Hosting selected!")
        st.markdown("""
        <div class="gradient-card blue-gradient" style="margin-top: -3rem;">
            <div class="card-icon">🌐</div>
            <div class="card-title">Remote Hosting</div>
            <div class="card-subtitle">Deploy to the cloud</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        if st.button("", key="configuration"):
            st.success("Configuration selected!")
        st.markdown("""
        <div class="gradient-card purple-gradient" style="margin-top: -3rem;">
            <div class="card-icon">⚙️</div>
            <div class="card-title">Configuration</div>
            <div class="card-subtitle">Customize your setup</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Второй ряд карточек
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("", key="features"):
            st.success("Features selected!")
        st.markdown("""
        <div class="gradient-card red-gradient">
            <div class="card-icon">⭐</div>
            <div class="card-title">Features</div>
            <div class="card-subtitle">Discover capabilities</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        if st.button("", key="user_guides"):
            st.success("User Guides selected!")
        st.markdown("""
        <div class="gradient-card teal-gradient">
            <div class="card-icon">📚</div>
            <div class="card-title">User Guides</div>
            <div class="card-subtitle">Step-by-step tutorials</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        if st.button("", key="api_docs"):
            st.success("API Documentation selected!")
        st.markdown("""
        <div class="gradient-card orange-gradient">
            <div class="card-icon">📖</div>
            <div class="card-title">API Documentation</div>
            <div class="card-subtitle">Technical reference</div>
        </div>
        """, unsafe_allow_html=True)

elif selected == "Features":
    st.markdown('<h1 class="section-title">Features</h1>', unsafe_allow_html=True)
    st.markdown("### 🚀 Powerful AI Chat Interface")
    st.markdown("- Multiple AI model support")
    st.markdown("- Real-time conversations")
    st.markdown("- Custom configurations")

elif selected == "Local Installation":
    st.markdown('<h1 class="section-title">Local Installation</h1>', unsafe_allow_html=True)
    st.markdown("### 💻 Setup Instructions")
    st.code("""
# Clone the repository
git clone https://github.com/danny-avila/LibreChat.git
cd LibreChat

# Install dependencies
npm install

# Start the application
npm start
    """)

elif selected == "Remote Hosting":
    st.markdown('<h1 class="section-title">Remote Hosting</h1>', unsafe_allow_html=True)
    st.markdown("### ☁️ Cloud Deployment Options")
    st.markdown("- Docker deployment")
    st.markdown("- Railway hosting")
    st.markdown("- Heroku deployment")

elif selected == "Configuration":
    st.markdown('<h1 class="section-title">Configuration</h1>', unsafe_allow_html=True)
    st.markdown("### ⚙️ Customize Your Setup")
    st.markdown("Configure your LibreChat instance with custom settings.")

elif selected == "User Guides":
    st.markdown('<h1 class="section-title">User Guides</h1>', unsafe_allow_html=True)
    st.markdown("### 📚 Step-by-Step Tutorials")
    st.markdown("Comprehensive guides to help you get the most out of LibreChat.")

elif selected == "Translation":
    st.markdown('<h1 class="section-title">Translation</h1>', unsafe_allow_html=True)
    st.markdown("### 🌍 Internationalization")
    st.markdown("Help translate LibreChat into your language.")

# Правая панель "On This Page"
with st.sidebar:
    st.markdown("---")
    st.markdown("**On This Page**")
    st.markdown("📋 Quick Start Guides")
    st.markdown("📖 Explore our Documentation")
    st.markdown("---")
    st.markdown("❓ Question? Give us feedback →")
    st.markdown("📝 Edit this page on GitHub")
