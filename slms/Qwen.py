import os
from openai import OpenAI


class Qwen:
    def generate_terraform_script(user_prompt: str) -> str:
        if not user_prompt:
            return "Prompt is empty"
        client = OpenAI(
            base_url="https://router.huggingface.co/v1",
            api_key=os.environ["HF_TOKEN"],
        )

        completion = client.chat.completions.create(
            model="Qwen/Qwen2.5-Coder-14B:featherless-ai",
            messages=[
                {
                    "role": "user",
                    "content": f"{user_prompt}",
                }
            ],
        )

        print(completion.choices[0].message)