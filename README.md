# VC Memo Generator

A Streamlit web application that generates venture capital investment memos using OpenAI's GPT-4 API. This project is under active development

## Features

- Generate structured VC memos from either free-form text or a structured form
- Powered by OpenAI's GPT-4 for high-quality analysis
- Export memos to PDF format
- Clean, modern web interface

## Prerequisites

- Python 3.8+
- wkhtmltopdf (required for PDF generation)

### Installing wkhtmltopdf

- **Windows**: Download and install from [wkhtmltopdf downloads](https://wkhtmltopdf.org/downloads.html)
- **macOS**: `brew install wkhtmltopdf`
- **Linux**: `sudo apt-get install wkhtmltopdf`

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
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser and navigate to `http://localhost:8501`

3. Choose your input method:
   - Free-form text: Enter a detailed description of your startup
   - Structured form: Fill in specific details about your startup

4. Click "Generate Memo" to create the investment memo

5. Use the "Export as PDF" button to download the memo as a PDF file

## Project Structure

- `app.py` - Main Streamlit application
- `memo_generator.py` - Handles GPT-4 API calls and memo generation
- `pdf_exporter.py` - PDF export functionality
- `requirements.txt` - Project dependencies

## License

MIT 

TechHealth AI is a healthcare technology startup that has developed an AI-powered diagnostic platform for early disease detection. Our system analyzes medical imaging data (X-rays, MRIs, CT scans) using advanced deep learning algorithms to detect potential health issues before they become severe.

Founded by Dr. Sarah Chen (former Head of AI at Stanford Medical Center) and Tom Rodriguez (ex-Google AI engineer), our team combines deep healthcare expertise with cutting-edge AI capabilities. We've already partnered with 5 major hospitals for pilot programs and have processed over 50,000 scans with a 94% accuracy rate.

The global medical imaging market is projected to reach $45B by 2025. Our initial focus is on lung cancer detection, where early diagnosis can improve survival rates by up to 70%. We've secured $2M in seed funding from leading healthcare VCs and have filed 3 patents for our core technology.

Current traction:
- 5 hospital partnerships
- 50,000+ scans processed
- $500K in pilot contracts
- 94% accuracy rate (validated by independent studies)
- FDA approval process initiated

We're raising a Series A round of $10M to expand our hospital network, obtain FDA approval, and develop detection capabilities for additional diseases. 