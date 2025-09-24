from google import genai
from dotenv import load_dotenv
import os
load_dotenv()


class Gemma:
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY")
    )

    def generate_terraform_script(user_prompt: str) -> str:
        if not user_prompt:
            return "Prompt is empty"

        prompt = f"{user_prompt}"
        completion = Gemma.client.models.generate_content(
            model="gemma-3n-e2b-it",
            contents=[prompt]
        )

        return completion.text