# VC Memo Generator

A modern Streamlit web application that generates venture capital investment memos using OpenAI's GPT-4 API.

## Features

- Generate structured VC memos from either free-form text or a structured form
- Powered by OpenAI's GPT-4 for high-quality analysis
- Export memos to PDF format using reportlab (no external dependencies required)
- Clean, modern web interface with professional styling
- Real-time memo generation with proper markdown formatting

## Prerequisites

- Python 3.8+
- OpenAI API key

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd vc-memo-generator
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_actual_api_key_here
```

You can get an API key from: https://platform.openai.com/api-keys

## Usage

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser and navigate to `http://localhost:8501`

3. Choose your input method:
   - **FREE-FORM TEXT**: Enter a detailed description of your startup
   - **STRUCTURED FORM**: Fill in specific details about your startup using the form fields

4. Click "GENERATE MEMO" to create the investment memo

5. Use the "EXPORT PDF" button to download the memo as a PDF file

## Project Structure

- `app.py` - Main Streamlit application with modern UI
- `memo_generator.py` - Handles GPT-4 API calls and memo generation
- `pdf_exporter.py` - PDF export functionality using reportlab
- `requirements.txt` - Project dependencies
- `clear_cache.py` - Utility script to clear Python cache

## Dependencies

- **streamlit** - Web application framework
- **openai** - OpenAI API integration
- **python-dotenv** - Environment variable management
- **reportlab** - PDF generation (no external dependencies required)
- **python-slugify** - String processing
- **markdown2** - Markdown processing for better text formatting

## Troubleshooting

### API Key Issues
If you see an error about the OpenAI API key:
1. Make sure you've created a `.env` file in the project root
2. Verify your API key is correct and has sufficient credits
3. Restart the Streamlit app after adding/changing the API key

### Python Cache Issues
If you encounter import errors, run:
```bash
python clear_cache.py
```

## Contact

- Built by @Wali-Hasan. Open to feedback, contributions, and collabs.