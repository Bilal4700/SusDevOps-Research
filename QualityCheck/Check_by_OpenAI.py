from openai import OpenAI # type: ignore
from dotenv import load_dotenv
import os
load_dotenv()


class OpenAiCheck:
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY_FOR_CHECK")
    )

    @staticmethod
    def compare_terraform_script(comparison_prompt) -> str:
        if not comparison_prompt:
            print("Prompt not provided")

        prompt = f"{comparison_prompt}"
        completion = OpenAiCheck.client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[{"role": "user", "content": prompt}]
        )

        # Extract the text content (don't print the object)
        content = completion.choices[0].message.content or ""

        return content


