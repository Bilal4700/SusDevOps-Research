import anthropic
from dotenv import load_dotenv
import os
load_dotenv()


class Claude:
    def generate_terraform_script(user_prompt: str) -> str:
        client = anthropic.Anthropic(api_key=os.environ.get("CLAUDE_API_KEY"))

        if not user_prompt:
            return "Prompt is empty"

        message = client.messages.create(
            model="claude-opus-4-20250514",
            max_tokens=1000,
            messages=[
                {
                    "role": "user",
                    "content": f"{user_prompt}"
                }
            ]
        )
        return message.content