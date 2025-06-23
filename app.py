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
    
    # Инициализация состояния для раскрывающихся меню
    if 'expanded_sections' not in st.session_state:
        st.session_state.expanded_sections = {
            'get_started': False,
            'features': False,
            'local_installation': False,
            'remote_hosting': False,
            'configuration': False,
            'user_guides': False,
            'development': False,
            'documentation': False
        }
    
    if 'selected_page' not in st.session_state:
        st.session_state.selected_page = 'Get Started'
    
    # Функция для переключения секций
    def toggle_section(section_name):
        st.session_state.expanded_sections[section_name] = not st.session_state.expanded_sections[section_name]
    
    # Функция для выбора страницы
    def select_page(page_name):
        st.session_state.selected_page = page_name
    
    # Get Started секция
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        if st.button("📚 Get Started", key="get_started_btn", use_container_width=True):
            toggle_section('get_started')
            select_page('Get Started')
    with col2:
        st.markdown("▼" if st.session_state.expanded_sections['get_started'] else "▶")
    
    if st.session_state.expanded_sections['get_started']:
        if st.button("  📋 Quick Start", key="quick_start", use_container_width=True):
            select_page('Quick Start')
        if st.button("  🔧 Setup Guide", key="setup_guide", use_container_width=True):
            select_page('Setup Guide')
        if st.button("  📖 Documentation", key="docs", use_container_width=True):
            select_page('Documentation')
    
    # Features секция
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        if st.button("⭐ Features", key="features_btn", use_container_width=True):
            toggle_section('features')
            select_page('Features')
    with col2:
        st.markdown("▼" if st.session_state.expanded_sections['features'] else "▶")
    
    if st.session_state.expanded_sections['features']:
        if st.button("  🤖 AI Models", key="ai_models", use_container_width=True):
            select_page('AI Models')
        if st.button("  💬 Chat Features", key="chat_features", use_container_width=True):
            select_page('Chat Features')
        if st.button("  🔌 Plugins", key="plugins", use_container_width=True):
            select_page('Plugins')
    
    # Local Installation секция
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        if st.button("💻 Local Installation", key="local_btn", use_container_width=True):
            toggle_section('local_installation')
            select_page('Local Installation')
    with col2:
        st.markdown("▼" if st.session_state.expanded_sections['local_installation'] else "▶")
    
    if st.session_state.expanded_sections['local_installation']:
        if st.button("  🐳 Docker", key="docker", use_container_width=True):
            select_page('Docker')
        if st.button("  📦 NPM", key="npm", use_container_width=True):
            select_page('NPM')
        if st.button("  🔧 Helm Chart", key="helm", use_container_width=True):
            select_page('Helm Chart')
    
    # Remote Hosting секция
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        if st.button("☁️ Remote Hosting", key="remote_btn", use_container_width=True):
            toggle_section('remote_hosting')
            select_page('Remote Hosting')
    with col2:
        st.markdown("▼" if st.session_state.expanded_sections['remote_hosting'] else "▶")
    
    if st.session_state.expanded_sections['remote_hosting']:
        if st.button("  🚂 Railway", key="railway", use_container_width=True):
            select_page('Railway')
        if st.button("  🔺 Heroku", key="heroku", use_container_width=True):
            select_page('Heroku')
        if st.button("  ☁️ Azure", key="azure", use_container_width=True):
            select_page('Azure')
    
    # Configuration секция
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        if st.button("⚙️ Configuration", key="config_btn", use_container_width=True):
            toggle_section('configuration')
            select_page('Configuration')
    with col2:
        st.markdown("▼" if st.session_state.expanded_sections['configuration'] else "▶")
    
    if st.session_state.expanded_sections['configuration']:
        if st.button("  🔑 API Keys", key="api_keys", use_container_width=True):
            select_page('API Keys')
        if st.button("  🎨 Custom Endpoints", key="endpoints", use_container_width=True):
            select_page('Custom Endpoints')
        if st.button("  👤 User Management", key="users", use_container_width=True):
            select_page('User Management')
    
    st.markdown("---")
    
    # Development секция
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        if st.button("🛠️ Development", key="dev_btn", use_container_width=True):
            toggle_section('development')
            select_page('Development')
    with col2:
        st.markdown("▼" if st.session_state.expanded_sections['development'] else "▶")
    
    if st.session_state.expanded_sections['development']:
        if st.button("  🔧 Contributing", key="contributing", use_container_width=True):
            select_page('Contributing')
        if st.button("  🧪 Testing", key="testing", use_container_width=True):
            select_page('Testing')
        if st.button("  📊 Debugging", key="debugging", use_container_width=True):
            select_page('Debugging')
    
    # Documentation секция
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        if st.button("📚 Documentation", key="doc_btn", use_container_width=True):
            toggle_section('documentation')
            select_page('Documentation')
    with col2:
        st.markdown("▼" if st.session_state.expanded_sections['documentation'] else "▶")
    
    if st.session_state.expanded_sections['documentation']:
        if st.button("  📖 API Reference", key="api_ref", use_container_width=True):
            select_page('API Reference')
        if st.button("  🌍 Translation", key="translation", use_container_width=True):
            select_page('Translation')
        if st.button("  ❓ FAQ", key="faq", use_container_width=True):
            select_page('FAQ')
    
    st.markdown("---")
    st.markdown("⚙️ System")
    
    # Получаем выбранную страницу
    selected = st.session_state.selected_page

# Основной контент - теперь с поддержкой всех страниц
if selected == "Get Started":
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

elif selected == "Quick Start":
    st.markdown('<h1 class="section-title">📋 Quick Start</h1>', unsafe_allow_html=True)
    st.markdown("### Get up and running in minutes")
    st.markdown("1. Clone the repository")
    st.markdown("2. Install dependencies")
    st.markdown("3. Configure your environment")
    st.markdown("4. Start the application")

elif selected == "Setup Guide":
    st.markdown('<h1 class="section-title">🔧 Setup Guide</h1>', unsafe_allow_html=True)
    st.markdown("### Detailed setup instructions")
    st.markdown("Complete walkthrough for setting up LibreChat")

elif selected == "Documentation":
    st.markdown('<h1 class="section-title">📖 Documentation</h1>', unsafe_allow_html=True)
    st.markdown("### Complete documentation")
    st.markdown("All the information you need to use LibreChat effectively")

elif selected == "Features":
    st.markdown('<h1 class="section-title">⭐ Features</h1>', unsafe_allow_html=True)
    st.markdown("### 🚀 Powerful AI Chat Interface")
    st.markdown("- Multiple AI model support")
    st.markdown("- Real-time conversations")
    st.markdown("- Custom configurations")

elif selected == "AI Models":
    st.markdown('<h1 class="section-title">🤖 AI Models</h1>', unsafe_allow_html=True)
    st.markdown("### Supported AI Models")
    st.markdown("- OpenAI GPT models")
    st.markdown("- Anthropic Claude")
    st.markdown("- Google Bard")
    st.markdown("- Custom models")

elif selected == "Chat Features":
    st.markdown('<h1 class="section-title">💬 Chat Features</h1>', unsafe_allow_html=True)
    st.markdown("### Advanced Chat Capabilities")
    st.markdown("- Message history")
    st.markdown("- File uploads")
    st.markdown("- Code syntax highlighting")

elif selected == "Plugins":
    st.markdown('<h1 class="section-title">🔌 Plugins</h1>', unsafe_allow_html=True)
    st.markdown("### Extend Functionality")
    st.markdown("- Web search plugin")
    st.markdown("- Calculator plugin")
    st.markdown("- Custom plugins")

elif selected == "Local Installation":
    st.markdown('<h1 class="section-title">💻 Local Installation</h1>', unsafe_allow_html=True)
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

elif selected == "Docker":
    st.markdown('<h1 class="section-title">🐳 Docker Installation</h1>', unsafe_allow_html=True)
    st.markdown("### Using Docker")
    st.code("""
# Pull the image
docker pull librechat/librechat

# Run the container
docker run -p 3080:3080 librechat/librechat
    """)

elif selected == "NPM":
    st.markdown('<h1 class="section-title">📦 NPM Installation</h1>', unsafe_allow_html=True)
    st.markdown("### Using NPM")
    st.code("""
npm install -g librechat
librechat start
    """)

elif selected == "Helm Chart":
    st.markdown('<h1 class="section-title">🔧 Helm Chart</h1>', unsafe_allow_html=True)
    st.markdown("### Kubernetes Deployment")
    st.code("""
helm repo add librechat https://librechat.ai/helm
helm install librechat librechat/librechat
    """)

elif selected == "Remote Hosting":
    st.markdown('<h1 class="section-title">☁️ Remote Hosting</h1>', unsafe_allow_html=True)
    st.markdown("### ☁️ Cloud Deployment Options")
    st.markdown("- Docker deployment")
    st.markdown("- Railway hosting")
    st.markdown("- Heroku deployment")

elif selected == "Railway":
    st.markdown('<h1 class="section-title">🚂 Railway Deployment</h1>', unsafe_allow_html=True)
    st.markdown("### Deploy to Railway")
    st.markdown("1. Fork the repository")
    st.markdown("2. Connect to Railway")
    st.markdown("3. Deploy with one click")

elif selected == "Heroku":
    st.markdown('<h1 class="section-title">🔺 Heroku Deployment</h1>', unsafe_allow_html=True)
    st.markdown("### Deploy to Heroku")
    st.markdown("Step-by-step Heroku deployment guide")

elif selected == "Azure":
    st.markdown('<h1 class="section-title">☁️ Azure Deployment</h1>', unsafe_allow_html=True)
    st.markdown("### Deploy to Microsoft Azure")
    st.markdown("Azure Container Instances deployment")

elif selected == "Configuration":
    st.markdown('<h1 class="section-title">⚙️ Configuration</h1>', unsafe_allow_html=True)
    st.markdown("### ⚙️ Customize Your Setup")
    st.markdown("Configure your LibreChat instance with custom settings.")

elif selected == "API Keys":
    st.markdown('<h1 class="section-title">🔑 API Keys</h1>', unsafe_allow_html=True)
    st.markdown("### Managing API Keys")
    st.markdown("How to configure and manage your API keys securely")

elif selected == "Custom Endpoints":
    st.markdown('<h1 class="section-title">🎨 Custom Endpoints</h1>', unsafe_allow_html=True)
    st.markdown("### Setting up Custom Endpoints")
    st.markdown("Configure custom API endpoints for your models")

elif selected == "User Management":
    st.markdown('<h1 class="section-title">👤 User Management</h1>', unsafe_allow_html=True)
    st.markdown("### Managing Users")
    st.markdown("User authentication and authorization setup")

elif selected == "Development":
    st.markdown('<h1 class="section-title">🛠️ Development</h1>', unsafe_allow_html=True)
    st.markdown("### Development Guide")
    st.markdown("Information for developers contributing to LibreChat")

elif selected == "Contributing":
    st.markdown('<h1 class="section-title">🔧 Contributing</h1>', unsafe_allow_html=True)
    st.markdown("### How to Contribute")
    st.markdown("Guidelines for contributing to the project")

elif selected == "Testing":
    st.markdown('<h1 class="section-title">🧪 Testing</h1>', unsafe_allow_html=True)
    st.markdown("### Testing Guide")
    st.markdown("How to run tests and contribute test cases")

elif selected == "Debugging":
    st.markdown('<h1 class="section-title">📊 Debugging</h1>', unsafe_allow_html=True)
    st.markdown("### Debugging Tips")
    st.markdown("Common issues and how to debug them")

elif selected == "API Reference":
    st.markdown('<h1 class="section-title">📖 API Reference</h1>', unsafe_allow_html=True)
    st.markdown("### Complete API Documentation")
    st.markdown("Detailed API reference with examples")

elif selected == "Translation":
    st.markdown('<h1 class="section-title">🌍 Translation</h1>', unsafe_allow_html=True)
    st.markdown("### 🌍 Internationalization")
    st.markdown("Help translate LibreChat into your language.")

elif selected == "FAQ":
    st.markdown('<h1 class="section-title">❓ FAQ</h1>', unsafe_allow_html=True)
    st.markdown("### Frequently Asked Questions")
    st.markdown("Common questions and answers about LibreChat")

# Правая панель "On This Page"
with st.sidebar:
    st.markdown("---")
    st.markdown("**On This Page**")
    st.markdown("📋 Quick Start Guides")
    st.markdown("📖 Explore our Documentation")
    st.markdown("---")
    st.markdown("❓ Question? Give us feedback →")
    st.markdown("📝 Edit this page on GitHub")
