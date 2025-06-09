from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def generate_memo(input_data: dict) -> str:
    """
    Generate a VC memo using OpenAI's GPT-4 model.
    """
    # Get API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OpenAI API key not found! Make sure to:\n"
            "1. Create a .env file in the project root directory\n"
            "2. Add your API key to it like this: OPENAI_API_KEY=your-actual-api-key-here\n"
            "3. Make sure the .env file is in the same directory as app.py"
        )

    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)

    if "description" in input_data:
        prompt = f"""
        Based on the following startup description, generate a detailed venture capital investment memo:

        {input_data['description']}

        Generate a structured memo with the following sections:
        1. Company Overview
        2. Market Opportunity
        3. Problem and Solution
        4. Traction
        5. Team Evaluation
        6. Competitive Landscape
        7. Risks and Challenges
        8. Follow-Up Questions
        9. Final Recommendation
        """
    else:
        prompt = f"""
        Based on the following startup information, generate a detailed venture capital investment memo:

        Founder Background:
        {input_data['founder_background']}

        Problem:
        {input_data['problem']}

        Solution:
        {input_data['solution']}

        Market Size:
        {input_data['market_size']}

        Traction:
        {input_data['traction']}

        Current Funding:
        {input_data['current_funding']}

        Generate a structured memo with the following sections:
        1. Company Overview
        2. Market Opportunity
        3. Problem and Solution
        4. Traction
        5. Team Evaluation
        6. Competitive Landscape
        7. Risks and Challenges
        8. Follow-Up Questions
        9. Final Recommendation
        """

    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are an experienced venture capital analyst who writes detailed, insightful investment memos."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2500
        )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Error calling OpenAI API: {str(e)}")

if __name__ == "__main__":
    # Test the function
    test_input = {"description": "Test startup description"}
    print(generate_memo(test_input)) 