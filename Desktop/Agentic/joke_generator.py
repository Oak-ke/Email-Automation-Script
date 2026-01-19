import os
import json
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("Error: GOOGLE_API_KEY not found in environment variables.")
    print("Please create a .env file and add your GOOGLE_API_KEY=your_key_here")
    exit(1)

# Initialize the client with the new SDK
client = genai.Client(api_key=api_key)
model_id = 'gemini-2.0-flash' # Using 2.0-flash for better stability in early 2026

def research_and_generate_jokes():
    regions = ["Nigeria", "Kenya", "Egypt", "South Africa"]
    jokes_queue = []

    print("Starting research and joke generation...")

    prompt = """
    Act as a cultural researcher and comedian expert in African trends. 
    For each of the following countries: Nigeria, Kenya, Egypt, and South Africa:
    1. Research the top 3-5 trending cultural or social topics as of late 2025/early 2026.
    2. Based on these trends, generate TWO high-context, viral-ready jokes:
       - One for the 'Morning' slot (8 AM)
       - One for the 'Evening' slot (6 PM)
    3. The jokes must respect local nuances, use appropriate regional slang or cultural references, and be genuinely funny.
    4. Ensure the jokes are respectful and suitable for a wide audience.

    Output the result EXCLUSIVELY as a JSON array of objects with the following structure:
    [
      {
        "country": "Country Name",
        "trending_topics": ["Topic 1", "Topic 2", "Topic 3"],
        "jokes": [
          {
            "slot": "Morning",
            "text": "The morning joke text",
            "posted": false
          },
          {
            "slot": "Evening",
            "text": "The evening joke text",
            "posted": false
          }
        ]
      },
      ...
    ]
    """

    try:
        response = client.models.generate_content(model=model_id, contents=prompt)
        # Handle cases where response.text might be None
        if not response.text:
            print("Error: The model returned an empty response. Check safety filters or model access.")
            print(f"Full response: {response}")
            return
            
        content = response.text.strip()
        if content.startswith("```json"):
            content = content[7:-3].strip()
        elif content.startswith("```"):
            content = content[3:-3].strip()
            
        try:
            jokes_data = json.loads(content)
        except json.JSONDecodeError as je:
            print(f"Failed to parse JSON: {je}")
            print(f"Content: {content}")
            return
        
        with open("jokes_queue.json", "w", encoding="utf-8") as f:
            json.dump(jokes_data, f, indent=4, ensure_ascii=False)
            
        print("Successfully generated jokes and saved to jokes_queue.json")
        for entry in jokes_data:
            print(f"\n--- {entry['country']} ---")
            print(f"Trends: {', '.join(entry['trending_topics'])}")
            for j in entry['jokes']:
                print(f"[{j['slot']}] Joke: {j['text']}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    research_and_generate_jokes()
