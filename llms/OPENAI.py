from openai import OpenAI # type: ignore
from dotenv import load_dotenv
import os
load_dotenv()


class OPENAI:
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY")
    )

    def generate_terraform_script(user_prompt: str) -> str:
        if not user_prompt:
            return "Prompt is empty"

        prompt = f"{user_prompt}"
        completion = OPENAI.client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[{"role": "user", "content": prompt}]
        )

        return completion.choices[0].message.content
    
