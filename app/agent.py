from google import genai
client = genai.Client()  # NO API KEY

def summarize_text(text: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Summarize this in 3 lines:\n\n{text}"
    )
    return response.text
