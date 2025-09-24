from google import genai
from dotenv import load_dotenv
import os
load_dotenv()


class Gemini:
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY")
    )

    def generate_terraform_script(user_prompt: str) -> str:
        if not user_prompt:
            return "Prompt is empty"

        prompt = f"{user_prompt}"
        completion = Gemini.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[prompt]
        )

        return completion.text