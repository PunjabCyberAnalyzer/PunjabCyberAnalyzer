import streamlit as st
# Hide Streamlit's default "Fork me on GitHub" button
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    a[href^="https://github.com"] {visibility: hidden !important;}
    .css-eczf16 {display: none !important;}  /* Sometimes GitHub link uses this */
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Set page configuration with viewport meta tag for mobile responsiveness
st.set_page_config(
    page_title="Punjab Softwares - Advanced Technology Solutions",
    page_icon="🔧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Add viewport meta tag to ensure proper scaling on mobile devices
st.markdown("""
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
""", unsafe_allow_html=True)

# Custom CSS with adjustments for mobile stability
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    .stDeployButton {display:none;}
    footer {visibility: hidden;}
    .stApp > header {visibility: hidden;}
    
    /* Global styles */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        text-align: center;
    }
    
    html, body {
        width: 100%;
        overflow-x: hidden; /* Prevent horizontal scrolling */
    }
    
    .stApp {
        background: linear-gradient(135deg, #000000 0%, #1a1a1a 50%, #000000 100%);
        font-family: 'Inter', sans-serif;
        color: #ffffff;
        position: relative;
        min-height: 100vh;
        overflow-x: hidden; /* Ensure no horizontal overflow */
        scrollbar-width: thin;
        scrollbar-color: #888 #333;
    }
    
    .stApp::-webkit-scrollbar {
        width: 8px;
    }
    
    .stApp::-webkit-scrollbar-track {
        background: #333;
    }
    
    .stApp::-webkit-scrollbar-thumb {
        background-color: #888;
        border-radius: 4px;
        border: 2px solid #333;
    }
    
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(circle at 25% 25%, rgba(255,255,255,0.1) 0%, transparent 50%),
            radial-gradient(circle at 75% 75%, rgba(255,255,255,0.05) 0%, transparent 50%);
        animation: backgroundMove 20s ease-in-out infinite;
        pointer-events: none;
        z-index: -1;
    }
    
    @keyframes backgroundMove {
        0%, 100% { transform: translateX(0) translateY(0); }
        33% { transform: translateX(-20px) translateY(-20px); }
        66% { transform: translateX(20px) translateY(20px); }
    }
    
    /* Header styles */
    .header-container {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        width: 100%;
        background: transparent;
        backdrop-filter: blur(20px);
        border-bottom: 1px solid rgba(255,255,255,0.1);
        z-index: 1000;
        padding: 1rem 2rem;
        box-shadow: 0 4px 30px rgba(0,0,0,0.2);
        margin: 0;
    }
    
    .header-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .logo-section {
        display: flex;
        align-items: center;
        gap: 15px;
    }
    
    .logo-icon {
        width: 60px;
        height: 60px;
        background: linear-gradient(135deg, #ffffff 0%, #cccccc 100%);
        border-radius: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 28px;
        color: #000000;
        font-weight: 900;
        animation: logoPulse 2s ease-in-out infinite;
        box-shadow: 0 0 20px rgba(255,255,255,0.3);
    }
    
    @keyframes logoPulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    .logo-text h1 {
        font-size: 32px;
        font-weight: 900;
        color: #ffffff;
        letter-spacing: -0.5px;
        margin: 0;
        text-transform: uppercase;
    }
    
    .logo-text p {
        font-size: 16px;
        color: #888888;
        font-weight: 500;
        margin: 0;
        letter-spacing: 1px;
    }
    
    .nav-menu {
        display: flex;
        gap: 40px;
        align-items: center;
        justify-content: center;
    }
    
    .nav-item {
        color: #cccccc;
        font-weight: 600;
        font-size: 16px;
        cursor: pointer;
        transition: all 0.3s ease;
        position: relative;
        padding: 8px 0;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .nav-item:hover {
        color: #ffffff;
        transform: translateY(-3px);
    }
    
    .nav-item::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 0;
        height: 3px;
        background: linear-gradient(90deg, #ffffff 0%, #cccccc 100%);
        transition: width 0.3s ease;
    }
    
    .nav-item:hover::after {
        width: 100%;
    }
    
    /* Name section below header */
    .name-section {
        position: relative;
        margin-top: 80px;
        padding: 30px 20px;
        max-width: 1200px;
        margin-left: auto;
        margin-right: auto;
        animation: fadeInScale 2s ease-in-out infinite;
    }
    
    .company-name {
        font-family: 'Poppins', sans-serif;
        font-size: 100px;
        font-weight: 900;
        background: linear-gradient(135deg, #e0f7fa 0%, #b0bec5 50%, #78909c 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1.1;
        margin: 0 0 15px 0;
        letter-spacing: 6px;
        text-transform: uppercase;
        text-shadow: 2px 2px 10px rgba(255, 255, 255, 0.3);
        animation: glow 3s ease-in-out infinite;
    }
    
    .name-subtitle {
        font-family: 'Poppins', sans-serif;
        font-size: 36px;
        color: #e0f7fa;
        font-weight: 700;
        margin-bottom: 15px;
        text-transform: uppercase;
        text-shadow: 1px 1px 5px rgba(255, 255, 255, 0.2);
        animation: slideUp 2s ease-in-out infinite;
    }
    
    .name-text {
        font-family: 'Poppins', sans-serif;
        font-size: 22px;
        color: #b0bec5;
        font-weight: 500;
        margin-bottom: 10px;
        line-height: 1.6;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.3);
    }
    
    .name-motivation {
        font-family: 'Poppins', sans-serif;
        font-size: 20px;
        color: #78909c;
        font-style: italic;
        font-weight: 400;
        margin-bottom: 10px;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
    }
    
    .name-future {
        font-family: 'Poppins', sans-serif;
        font-size: 18px;
        color: #607d8b;
        font-weight: 600;
        margin-bottom: 10px;
        text-transform: uppercase;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
    }
    
    .name-laptop {
        font-family: 'Poppins', sans-serif;
        font-size: 16px;
        color: #546e7a;
        font-weight: 500;
        margin-bottom: 15px;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
    }
    
    .name-tuned {
        font-family: 'Poppins', sans-serif;
        font-size: 18px;
        color: #90a4ae;
        font-weight: 500;
        margin-bottom: 15px;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
    }
    
    @keyframes fadeInScale {
        0%, 100% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.02); opacity: 0.95; }
    }
    
    @keyframes glow {
        0%, 100% { text-shadow: 2px 2px 10px rgba(224, 247, 250, 0.5); }
        50% { text-shadow: 2px 2px 15px rgba(176, 190, 197, 0.7); }
    }
    
    @keyframes slideUp {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-5px); }
    }
    
    /* Hero section */
    .hero-section {
        padding: 40px 20px;
        text-align: center;
        max-width: 1000px;
        margin-left: auto;
        margin-right: auto;
    }
    
    .hero-subtitle {
        font-size: 24px;
        color: #cccccc;
        font-weight: 400;
        line-height: 1.6;
        margin-bottom: 30px;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
        animation: fadeInUp 1s ease-out 0.2s both;
    }
    
    .motivation-text {
        font-size: 20px;
        color: #999999;
        font-style: italic;
        font-weight: 300;
        margin-bottom: 15px;
        animation: fadeInUp 1s ease-out 0.4s both;
    }
    
    .future-text {
        font-size: 18px;
        color: #777777;
        margin-bottom: 15px;
        animation: fadeInUp 1s ease-out 0.6s both;
    }
    
    .laptop-text {
        font-size: 16px;
        color: #666666;
        font-weight: 600;
        margin-bottom: 40px;
        animation: fadeInUp 1s ease-out 0.8s both;
        text-transform: uppercase;
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Section styling */
    .section-container {
        padding: 40px 20px;
        max-width: 900px;
        margin: 0 auto;
        text-align: center;
        background: linear-gradient(135deg, rgba(255,255,255,0.08) 0%, rgba(255,255,255,0.03) 100%);
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.15);
        backdrop-filter: blur(20px);
        transition: all 0.3s ease;
        animation: fadeInUp 0.8s ease-out;
    }
    
    .section-container:hover {
        transform: translateY(-10px);
        box-shadow: 0 25px 50px rgba(0,0,0,0.3);
        border-color: rgba(255,255,255,0.3);
    }
    
    .section-title {
        font-size: 48px;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 20px;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 2px;
        animation: fadeInUp 0.8s ease-out;
    }
    
    .section-subtitle {
        font-size: 20px;
        color: #cccccc;
        font-weight: 400;
        line-height: 1.6;
        margin-bottom: 40px;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
        animation: fadeInUp 0.8s ease-out 0.2s both;
    }
    
    /* Button styling */
    .custom-button {
        background: linear-gradient(135deg, #ffffff 0%, #cccccc 100%);
        color: #000000;
        font-weight: 600;
        font-size: 18px;
        padding: 15px 30px;
        border-radius: 10px;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        animation: fadeInUp 0.8s ease-out 0.4s both;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-left: auto;
        margin-right: auto;
        display: block;
    }
    
    .custom-button:hover {
        transform: translateY(-4px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
        background: linear-gradient(135deg, #cccccc 0%, #ffffff 100%);
    }
    
    /* Feature grid */
    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 30px;
        margin: 40px 0;
        max-width: 900px;
        margin-left: auto;
        margin-right: auto;
        justify-items: center;
    }
    
    .feature-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.08) 0%, rgba(255,255,255,0.03) 100%);
        border-radius: 15px;
        padding: 30px;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.1);
        transition: all 0.3s ease;
        animation: fadeInUp 0.8s ease-out both;
        max-width: 300px;
    }
    
    .feature-card:hover {
        transform: translateY(-6px);
        border-color: rgba(255,255,255,0.3);
        background: linear-gradient(135deg, rgba(255,255,255,0.12) 0%, rgba(255,255,255,0.06) 100%);
    }
    
    .highlighted-feature-card {
        background: linear-gradient(135deg, #ffffff 0%, #cccccc 100%);
        border-radius: 15px;
        padding: 30px;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.3);
        transition: all 0.3s ease;
        animation: fadeInUp 0.8s ease-out both;
        max-width: 300px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
    }
    
    .highlighted-feature-card:hover {
        transform: translateY(-6px);
        background: linear-gradient(135deg, #cccccc 0%, #ffffff 100%);
        box-shadow: 0 15px 30px rgba(0,0,0,0.4);
    }
    
    .highlighted-feature-card .feature-icon {
        font-size: 36px;
        margin-bottom: 20px;
        display: block;
        color: #000000;
    }
    
    .highlighted-feature-card .feature-title {
        font-size: 20px;
        font-weight: 700;
        color: #000000;
        margin-bottom: 12px;
        text-transform: uppercase;
    }
    
    .highlighted-feature-card .feature-text {
        font-size: 15px;
        color: #333333;
        line-height: 1.6;
    }
    
    .feature-icon {
        font-size: 36px;
        margin-bottom: 20px;
        display: block;
    }
    
    .feature-title {
        font-size: 20px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 12px;
        text-transform: uppercase;
    }
    
    .feature-text {
        font-size: 15px;
        color: #cccccc;
        line-height: 1.6;
    }
    
    /* Contact section */
    .contact-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 30px;
        margin: 40px 0;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
        justify-items: center;
    }
    
    .contact-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.08) 0%, rgba(255,255,255,0.03) 100%);
        border-radius: 15px;
        padding: 35px;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.15);
        transition: all 0.3s ease;
        animation: fadeInUp 0.8s ease-out both;
        max-width: 400px;
    }
    
    .contact-card:hover {
        transform: translateY(-6px);
        border-color: rgba(255,255,255,0.3);
        box-shadow: 0 15px 30px rgba(0,0,0,0.2);
    }
    
    .contact-icon {
        font-size: 36px;
        margin-bottom: 20px;
        display: block;
    }
    
    .contact-title {
        font-size: 22px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 12px;
        text-transform: uppercase;
    }
    
    .contact-info {
        font-size: 16px;
        color: #ffffff;
        font-weight: 600;
        margin-top: 12px;
    }
    
    /* About and Privacy sections */
    .info-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.08) 0%, rgba(255,255,255,0.03) 100%);
        border-radius: 15px;
        padding: 35px;
        margin: 25px auto;
        border: 1px solid rgba(255,255,255,0.15);
        animation: fadeInUp 0.8s ease-out both;
        max-width: 900px;
    }
    
    .info-title {
        font-size: 24px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 15px;
        text-align: center;
        text-transform: uppercase;
    }
    
    .info-text {
        font-size: 16px;
        color: #cccccc;
        line-height: 1.7;
        text-align: center;
    }
    
    /* Footer */
    .footer-section {
        padding: 80px 0;
        border-top: 1px solid rgba(255,255,255,0.1);
        text-align: center;
        background: #000000;
        width: 100%;
    }
    
    .footer-title {
        font-size: 28px;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 10px;
        text-transform: uppercase;
    }
    
    .footer-subtitle {
        font-size: 35px;
        color: #888888;
        margin-bottom: 20px;
    }
    
    .footer-text {
        color: #666666;
        font-size: 20px;
    }
    
    /* Footer Social Container */
    .footer-social-container {
        padding: 50px 0;
        background: #000000;
        border-top: 0px solid rgba(255,255,255,0.1);
        text-align: center;
        width: 100%;
    }
    
    .social-icons {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 10px;
    }
    
    .social-icon {
        font-size: 30px;
        color: #ffffff;
        transition: all 0.3s ease;
        text-decoration: none;
    }
    
    .social-icon:hover {
        transform: scale(1.2);
    }
    
    /* Enhanced responsive design for mobile */
    @media (max-width: 768px) {
        html, body {
            width: 100%;
            overflow-x: hidden; /* Prevent horizontal scrolling on mobile */
        }
        
        .stApp {
            overflow-x: hidden; /* Ensure no horizontal overflow */
        }
        
        .company-name {
            font-size: 50px;
        }
        
        .name-subtitle {
            font-size: 20px;
        }
        
        .name-text {
            font-size: 16px;
        }
        
        .name-motivation {
            font-size: 14px;
        }
        
        .name-future {
            font-size: 12px;
        }
        
        .name-laptop {
            font-size: 12px;
        }
        
        .name-tuned {
            font-size: 12px;
        }
        
        .section-title {
            font-size: 32px;
        }
        
        .nav-menu {
            display: none;
        }
        
        .header-content {
            justify-content: center;
        }
        
        .nav-item {
            font-size: 14px;
            padding: 8px 0;
        }
        
        .features-grid {
            grid-template-columns: 1fr;
        }
        
        .contact-grid {
            grid-template-columns: 1fr;
        }
        
        .social-icon {
            font-size: 24px;
        }
        
        /* Ensure containers fit within viewport */
        .section-container,
        .name-section,
        .hero-section,
        .info-card,
        .footer-section,
        .footer-social-container {
            width: 100%;
            max-width: 100%;
            padding: 20px 10px;
            margin: 0 auto;
        }
        
        /* Adjust button sizes for mobile */
        .custom-button {
            font-size: 16px;
            padding: 10px 20px;
        }
        
        /* Ensure feature and contact cards fit on mobile */
        .feature-card,
        .highlighted-feature-card,
        .contact-card {
            max-width: 100%;
            width: 100%;
            padding: 20px;
        }
    }
    
    @media (max-width: 480px) {
        .company-name {
            font-size: 36px;
            letter-spacing: 2px;
        }
        
        .section-title {
            font-size: 24px;
        }
        
        .custom-button {
            font-size: 14px;
            padding: 8px 16px;
        }
        
        .logo-icon {
            width: 50px;
            height: 50px;
            font-size: 24px;
        }
        
        .logo-text h1 {
            font-size: 24px;
        }
        
        .logo-text p {
            font-size: 14px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

def create_header():
    """Create professional header with navigation"""
    st.markdown("""
    <div class="header-container">
        <div class="header-content">
            <div class="logo-section">
                <div class="logo-icon">PS</div>
                <div class="logo-text">
                    <h1>PUNJAB SOFTWARES</h1>
                    <p>Technological Innovation & Analysis</p>
                </div>
            </div>
            <div class="nav-menu">
                <div class="nav-item">Home</div>
                <div class="nav-item">Softwares</div>
                <div class="nav-item">Support Team</div>
                <div class="nav-item">About Us</div>
                <div class="nav-item">Privacy</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_name_section():
    """Create section for company name and related text below header"""
    st.markdown("""
    <div class="name-section">
        <h1 class="company-name">PUNJAB SOFTWARES</h1>
        <p class="name-subtitle">CDR ANALYZER</p>
        <p class="name-text">
            Pioneering the future of technology with innovative software solutions and advanced cyber analysis tools.
        </p>
        <p class="name-motivation">"Empowering progress through technological excellence"</p>
        <p class="name-future">Anticipate our upcoming software innovations - Transforming the digital landscape!</p>
        <p class="name-laptop">USE LAPTOP OR PC FOR BETTER VIEW</p>
        <p class="name-tuned">Stay tuned for our upcoming services and software – more powerful tools are on the way!</p>
    </div>
    """, unsafe_allow_html=True)

def create_hero_section():
    """Create hero section with messaging"""
    st.markdown("""
    <div class="hero-section">
        <!-- Hero section content removed as per request to move to name section -->
    </div>
    """, unsafe_allow_html=True)

def create_software_section():
    """Create software solutions section with container"""
    st.markdown("""
    <div class="section-container">
        <h2 class="section-title">Our Software Solutions</h2>
        <div class="info-card">
            <p class="info-text">
                Cutting-edge tools designed to address modern cybersecurity challenges and digital forensics needs.
            </p>
        </div>
        <div class="info-card">
            <h3 class="info-title">CDR ANALYZER</h3>
            <p class="info-text">
                Advanced Call Detail Record analysis tool for comprehensive telecommunication data investigation.
            </p>
            <a href="https://punjabcyberanalyzer.streamlit.app/" target="_blank">
                <button class="custom-button">Launch CDR Analyzer Now</button>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_support_section():
    """Create support team section with container"""
    st.markdown("""
    <div class="section-container">
        <h2 class="section-title">Support Team</h2>
        <div class="info-card">
            <p class="info-text">
                24/7 professional support to ensure your technological success and seamless operations.
            </p>
        </div>
        <div class="contact-grid">
            <div class="contact-card">
                <div class="contact-icon">💬</div>
                <h3 class="contact-title">WhatsApp Support</h3>
                <p class="feature-text">Instant technical assistance through direct communication channels.</p>
                <a href="https://wa.me/03309653269" target="_blank">
                    <button class="custom-button">Contact Us on WhatsApp</button>
                </a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_innovations_section():
    """Create innovations section with container"""
    st.markdown("""
    <div class="section-container">
        <h2 class="section-title">Our Innovations</h2>
        <div class="info-card">
            <p class="info-text">
                Pushing the boundaries of technology with groundbreaking solutions for the future.
            </p>
        </div>
        <div class="features-grid">
            <div class="highlighted-feature-card">
                <div class="feature-icon">🚀</div>
                <h4 class="feature-title">AI Integration</h4>
                <p class="feature-text">Harnessing artificial intelligence for smarter, more efficient software solutions.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_about_section():
    """Create about us section with container"""
    st.markdown("""
    <div class="section-container">
        <h2 class="section-title">About Us</h2>
        <div class="info-card">
            <p class="info-text">
                Driving technological advancement through innovation and expertise.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_privacy_section():
    """Create privacy policy section with container"""
    st.markdown("""
    <div class="section-container">
        <h2 class="section-title">Privacy Policy</h2>
        <div class="info-card">
            <p class="info-text">
                Committed to safeguarding your data with industry-leading security practices.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_footer():
    """Create professional footer"""
    st.markdown("""
    <div class="footer-section">
        <h3 class="footer-title">PUNJAB SOFTWARES</h3>
        <p class="footer-subtitle">Technological Innovation & Analysis</p>
        <p class="footer-text">© 2025 Punjab Softwares. All rights reserved.</p>
        <p class="footer-text">Empowering the future with advanced software solutions</p>
    </div>
    <div class="footer-social-container">
        <div class="social-icons">
            <a href="https://wa.me/03309653269" target="_blank" class="social-icon"><i class="fab fa-whatsapp"></i></a>
            <a href="https://www.facebook.com/share/g/19QDE5Cstd/" target="_blank" class="social-icon"><i class="fab fa-facebook-f"></i></a>
            <a href="http://www.youtube.com/@PUNJABCYBERANALYZER" target="_blank" class="social-icon"><i class="fab fa-youtube"></i></a>
            <a href="https://t.me" target="_blank" class="social-icon"><i class="fab fa-telegram-plane"></i></a>
            <a href="https://x.com" target="_blank" class="social-icon"><i class="fab fa-x-twitter"></i></a>
        </div>
    </div>
    """, unsafe_allow_html=True)

def main():
    """Main application function"""
    load_css()
    create_header()
    create_name_section()
    create_software_section()
    create_innovations_section()
    create_support_section()
    create_about_section()
    create_privacy_section()
    create_footer()

if __name__ == "__main__":
    main()
