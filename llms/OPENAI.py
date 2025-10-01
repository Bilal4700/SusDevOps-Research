from openai import OpenAI # type: ignore
from dotenv import load_dotenv
import os
load_dotenv()


class OpenAi:
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY")
    )

    @staticmethod
    def generate_terraform_script(user_prompt: str) -> str:
        if not user_prompt:
            return "Prompt is empty"

        prompt = f"{user_prompt}"
        completion = OpenAi.client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[{"role": "user", "content": prompt}]
        )

        # Extract the text content (don't print the object)
        content = completion.choices[0].message.content or ""

        # Extract token usage (may vary by router / model)
        usage = {
            "prompt_tokens": getattr(completion.usage, "prompt_tokens", None),
            "completion_tokens": getattr(completion.usage, "completion_tokens", None),
            "total_tokens": getattr(completion.usage, "total_tokens", None),
        }

        return content, usage


if __name__ == "__main__":
    openai = OpenAi()
    prompt = """

    Generate a terraform script that has following features/specifications: 

    Terraform module which creates Transit Gateway resources on AWS.

    Rules:
    - Make a very simple structure.
    - Output only valid Terraform code in HCL format.
    - No XML/JSON/Markdown/comments/explanations.
    - Do not include explanations, comments, variables, outputs, or extra text.
    - Indent with exactly 2 spaces.
    """
    
    content, usage = openai.generate_terraform_script(prompt)
    print(f"this is content {content}")
    print(f'This is usage {usage}')

    
