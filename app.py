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
    
    # Инициализация состояния
    if 'expanded_sections' not in st.session_state:
        st.session_state.expanded_sections = {
            'get_started': True,  # Открыт по умолчанию
            'features': False,
            'local_installation': False,
            'remote_hosting': False,
            'configuration': False,
            'development': False,
            'documentation': False
        }
    
    if 'selected_page' not in st.session_state:
        st.session_state.selected_page = 'Get Started'
    
    # Основное меню с возможностью раскрытия
    main_menu_options = ["Get Started", "Features", "Local Installation", "Remote Hosting", "Configuration"]
    main_menu_icons = ["play-circle", "star", "laptop", "cloud", "gear"]
    
    # Создаем основное меню
    selected_main = option_menu(
        menu_title=None,
        options=main_menu_options,
        icons=main_menu_icons,
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#64748b", "font-size": "18px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#f1f5f9"},
            "nav-link-selected": {"background-color": "#dbeafe", "color": "#2563eb"},
        }
    )
    
    # Подменю для каждой секции
    if selected_main == "Get Started":
        st.session_state.expanded_sections['get_started'] = True
        with st.container():
            sub_selected = option_menu(
                menu_title=None,
                options=["Overview", "Quick Start", "Setup Guide", "First Steps"],
                icons=["house", "lightning", "tools", "1-circle"],
                default_index=0,
                styles={
                    "container": {"padding": "0!important", "background-color": "#f8fafc", "margin-left": "10px"},
                    "icon": {"color": "#94a3b8", "font-size": "14px"}, 
                    "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "padding-left": "20px", "--hover-color": "#e2e8f0"},
                    "nav-link-selected": {"background-color": "#e0f2fe", "color": "#0369a1"},
                }
            )
            if sub_selected == "Overview":
                st.session_state.selected_page = 'Get Started'
            elif sub_selected == "Quick Start":
                st.session_state.selected_page = 'Quick Start'
            elif sub_selected == "Setup Guide":
                st.session_state.selected_page = 'Setup Guide'
            elif sub_selected == "First Steps":
                st.session_state.selected_page = 'First Steps'
    
    elif selected_main == "Features":
        st.session_state.expanded_sections['features'] = True
        with st.container():
            sub_selected = option_menu(
                menu_title=None,
                options=["Overview", "AI Models", "Chat Features", "Plugins"],
                icons=["star", "robot", "chat", "plug"],
                default_index=0,
                styles={
                    "container": {"padding": "0!important", "background-color": "#f8fafc", "margin-left": "10px"},
                    "icon": {"color": "#94a3b8", "font-size": "14px"}, 
                    "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "padding-left": "20px", "--hover-color": "#e2e8f0"},
                    "nav-link-selected": {"background-color": "#e0f2fe", "color": "#0369a1"},
                }
            )
            if sub_selected == "Overview":
                st.session_state.selected_page = 'Features'
            elif sub_selected == "AI Models":
                st.session_state.selected_page = 'AI Models'
            elif sub_selected == "Chat Features":
                st.session_state.selected_page = 'Chat Features'
            elif sub_selected == "Plugins":
                st.session_state.selected_page = 'Plugins'
    
    elif selected_main == "Local Installation":
        st.session_state.expanded_sections['local_installation'] = True
        with st.container():
            sub_selected = option_menu(
                menu_title=None,
                options=["Overview", "Docker", "NPM", "Helm Chart"],
                icons=["laptop", "box", "package", "gear"],
                default_index=0,
                styles={
                    "container": {"padding": "0!important", "background-color": "#f8fafc", "margin-left": "10px"},
                    "icon": {"color": "#94a3b8", "font-size": "14px"}, 
                    "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "padding-left": "20px", "--hover-color": "#e2e8f0"},
                    "nav-link-selected": {"background-color": "#e0f2fe", "color": "#0369a1"},
                }
            )
            if sub_selected == "Overview":
                st.session_state.selected_page = 'Local Installation'
            elif sub_selected == "Docker":
                st.session_state.selected_page = 'Docker'
            elif sub_selected == "NPM":
                st.session_state.selected_page = 'NPM'
            elif sub_selected == "Helm Chart":
                st.session_state.selected_page = 'Helm Chart'
    
    elif selected_main == "Remote Hosting":
        st.session_state.expanded_sections['remote_hosting'] = True
        with st.container():
            sub_selected = option_menu(
                menu_title=None,
                options=["Overview", "Railway", "Heroku", "Azure"],
                icons=["cloud", "train", "triangle", "microsoft"],
                default_index=0,
                styles={
                    "container": {"padding": "0!important", "background-color": "#f8fafc", "margin-left": "10px"},
                    "icon": {"color": "#94a3b8", "font-size": "14px"}, 
                    "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "padding-left": "20px", "--hover-color": "#e2e8f0"},
                    "nav-link-selected": {"background-color": "#e0f2fe", "color": "#0369a1"},
                }
            )
            if sub_selected == "Overview":
                st.session_state.selected_page = 'Remote Hosting'
            elif sub_selected == "Railway":
                st.session_state.selected_page = 'Railway'
            elif sub_selected == "Heroku":
                st.session_state.selected_page = 'Heroku'
            elif sub_selected == "Azure":
                st.session_state.selected_page = 'Azure'
    
    elif selected_main == "Configuration":
        st.session_state.expanded_sections['configuration'] = True
        with st.container():
            sub_selected = option_menu(
                menu_title=None,
                options=["Overview", "API Keys", "Custom Endpoints", "User Management"],
                icons=["gear", "key", "link", "people"],
                default_index=0,
                styles={
                    "container": {"padding": "0!important", "background-color": "#f8fafc", "margin-left": "10px"},
                    "icon": {"color": "#94a3b8", "font-size": "14px"}, 
                    "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "padding-left": "20px", "--hover-color": "#e2e8f0"},
                    "nav-link-selected": {"background-color": "#e0f2fe", "color": "#0369a1"},
                }
            )
            if sub_selected == "Overview":
                st.session_state.selected_page = 'Configuration'
            elif sub_selected == "API Keys":
                st.session_state.selected_page = 'API Keys'
            elif sub_selected == "Custom Endpoints":
                st.session_state.selected_page = 'Custom Endpoints'
            elif sub_selected == "User Management":
                st.session_state.selected_page = 'User Management'
    
    # Дополнительные разделы
    st.markdown("---")
    
    # Дополнительное меню
    additional_menu = option_menu(
        menu_title="Resources",
        options=["Development", "Documentation", "Translation"],
        icons=["code-slash", "book", "translate"],
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#64748b", "font-size": "16px"}, 
            "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#f1f5f9"},
            "nav-link-selected": {"background-color": "#dbeafe", "color": "#2563eb"},
        }
    )
    
    # Обработка дополнительного меню
    if additional_menu == "Development":
        st.session_state.selected_page = 'Development'
    elif additional_menu == "Documentation":
        st.session_state.selected_page = 'API Reference'
    elif additional_menu == "Translation":
        st.session_state.selected_page = 'Translation'
    
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

elif selected == "First Steps":
    st.markdown('<h1 class="section-title">🚀 First Steps</h1>', unsafe_allow_html=True)
    st.markdown("### Your first steps with LibreChat")
    st.markdown("1. Create your first chat")
    st.markdown("2. Configure AI models")
    st.markdown("3. Explore features")
    st.markdown("4. Join the community")

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
