import streamlit as st
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Add the current directory to Python path
current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

# Import local modules
from memo_generator import generate_memo
from pdf_exporter import export_to_pdf

# Load environment variables
load_dotenv()

# Set page configuration and custom styles
st.set_page_config(
    page_title="VC Memo Generator",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    /* Main container */
    .main {
        background-color: #ffffff;
    }
    
    /* Headers */
    h1 {
        color: #1a1a1a !important;
        font-size: 3.5em !important;
        font-weight: 800 !important;
        margin-bottom: 1em !important;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    /* Radio buttons */
    .stRadio > label {
        color: #1a1a1a !important;
        font-weight: 600 !important;
        font-size: 1.2em !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Text areas */
    .stTextArea textarea {
        background-color: #ffffff !important;
        border: 2px solid #2563eb !important;
        border-radius: 10px !important;
        padding: 15px !important;
        font-size: 1.1em !important;
        color: #1a1a1a !important;
        font-family: 'Arial', sans-serif !important;
    }
    
    .stTextArea textarea:focus {
        border-color: #1d4ed8 !important;
        box-shadow: 0 0 10px rgba(37, 99, 235, 0.2) !important;
        background-color: #ffffff !important;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: #000000 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 15px 30px !important;
        font-size: 1.1em !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        width: 100% !important;
        max-width: 300px !important;
        margin: 0 auto !important;
        display: block !important;
    }
    
    /* Override Streamlit's default button styling */
    .stButton > button > div {
        color: #ffffff !important;
        display: block !important;
    }

    .stButton > button > div > p {
        color: #ffffff !important;
        display: block !important;
    }

    .stButton > button:hover {
        background-color: #1a1a1a !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2) !important;
    }
    
    /* Download button */
    .stDownloadButton > button {
        background-color: #000000 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 15px 30px !important;
        font-size: 1.1em !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        width: 100% !important;
        max-width: 300px !important;
        margin: 0 auto !important;
        display: block !important;
    }

    /* Override Streamlit's default download button styling */
    .stDownloadButton > button > div {
        color: #ffffff !important;
        display: block !important;
    }

    .stDownloadButton > button > div > p {
        color: #ffffff !important;
        display: block !important;
    }
    
    .stDownloadButton > button:hover {
        background-color: #1a1a1a !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2) !important;
    }
    
    /* Success messages */
    .stSuccess {
        background-color: #000000 !important;
        color: #ffffff !important;
        padding: 20px !important;
        border-radius: 8px !important;
        font-weight: 500 !important;
        text-align: center !important;
        max-width: 300px !important;
        margin: 1em auto !important;
    }
    
    /* Error messages */
    .stAlert {
        background-color: #dc2626 !important;
        color: white !important;
        padding: 20px !important;
        border-radius: 10px !important;
    }
    
    /* Generated memo section */
    .memo-section {
        background-color: #ffffff;
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        margin-top: 2em;
        border: 2px solid #2563eb;
    }
    
    .memo-section h1, .memo-section h2, .memo-section h3 {
        color: #1a1a1a !important;
        margin-bottom: 1em;
        font-weight: 600;
    }
    
    .memo-section p {
        color: #1a1a1a !important;
        font-size: 1.1em;
        line-height: 1.6;
        margin-bottom: 1em;
    }
    
    /* Dividers */
    hr {
        border: none;
        height: 3px;
        background-color: #2563eb;
        margin: 2em 0;
    }
    
    /* Labels */
    label {
        color: #1a1a1a !important;
        font-weight: 600 !important;
        font-size: 1.1em !important;
        margin-bottom: 0.5em !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: #2563eb !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 10px 20px !important;
        font-weight: 600 !important;
        letter-spacing: 1px;
    }

    /* Radio button text */
    .stRadio div[role="radiogroup"] label {
        color: #1a1a1a !important;
        font-weight: 600 !important;
    }

    /* Make sure all text is visible */
    p, span, div {
        color: #1a1a1a !important;
    }

    /* Button text override to ensure visibility */
    .stButton > button span {
        color: #ffffff !important;
        display: inline-block !important;
    }
    
    .stDownloadButton > button span {
        color: #ffffff !important;
        display: inline-block !important;
    }

    /* Spinner text */
    .stSpinner > div {
        color: #2563eb !important;
        font-weight: 600 !important;
    }

    /* Center container for buttons */
    .button-container {
        display: flex;
        justify-content: center;
        width: 100%;
        margin: 1em 0;
    }
</style>
""", unsafe_allow_html=True)

def init_session_state():
    if 'memo' not in st.session_state:
        st.session_state.memo = None

def check_api_key():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key == "your-api-key-here":
        st.error("""
        OpenAI API key not found or not set!
        
        Please follow these steps:
        1. Create a `.env` file in the project root directory
        2. Add your API key to it like this: `OPENAI_API_KEY=your-actual-api-key-here`
        3. Restart the Streamlit app
        
        You can get an API key from: https://platform.openai.com/api-keys
        """)
        st.stop()

def main():
    init_session_state()
    
    # Title with solid color
    st.markdown('<h1 style="color: #1a1a1a;">VC MEMO GENERATOR</h1>', unsafe_allow_html=True)
    
    # Check API key before proceeding
    check_api_key()
    
    # Create three columns for better layout
    left_col, center_col, right_col = st.columns([1, 2, 1])
    
    with center_col:
        # Input method selection with custom styling
        input_method = st.radio(
            "SELECT INPUT METHOD",
            ["FREE-FORM TEXT", "STRUCTURED FORM"],
            key="input_method"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if "FREE-FORM" in input_method:
            startup_description = st.text_area(
                "STARTUP DESCRIPTION",
                height=300,
                placeholder="Describe your startup's story, team, product, market, and traction..."
            )
            input_data = {"description": startup_description} if startup_description else None
        else:
            with st.expander("STARTUP DETAILS", expanded=True):
                founder_background = st.text_area("FOUNDER BACKGROUND", height=100)
                problem = st.text_area("PROBLEM", height=100)
                solution = st.text_area("SOLUTION", height=100)
                market_size = st.text_area("MARKET SIZE", height=100)
                traction = st.text_area("TRACTION", height=100)
                current_funding = st.text_area("CURRENT FUNDING", height=100)
            
            input_data = {
                "founder_background": founder_background,
                "problem": problem,
                "solution": solution,
                "market_size": market_size,
                "traction": traction,
                "current_funding": current_funding
            } if all([founder_background, problem, solution, market_size, traction, current_funding]) else None

        st.markdown("<br>", unsafe_allow_html=True)
        
        # Center the Generate Memo button
        st.markdown('<div class="button-container">', unsafe_allow_html=True)
        if st.button("GENERATE MEMO"):
            if input_data:
                try:
                    with st.spinner("Crafting your investment memo..."):
                        memo = generate_memo(input_data)
                        st.session_state.memo = memo
                except Exception as e:
                    st.error(f"Error generating memo: {str(e)}")
            else:
                st.error("Please fill in all required fields")
        st.markdown('</div>', unsafe_allow_html=True)

    # Display the generated memo
    if st.session_state.memo:
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown('<div class="memo-section">', unsafe_allow_html=True)
        st.markdown('<h2 style="color: #1a1a1a;">INVESTMENT MEMO</h2>', unsafe_allow_html=True)
        st.markdown(st.session_state.memo)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Center the download button
        st.markdown('<div class="button-container">', unsafe_allow_html=True)
        if st.download_button(
            label="EXPORT PDF",
            data=export_to_pdf(st.session_state.memo),
            file_name="vc_memo.pdf",
            mime="application/pdf"
        ):
            st.success("PDF exported successfully!")
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main() 