import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

class DeepSeek:
    def generate_terraform_script(user_prompt: str) -> str:
        if not user_prompt:
            return "Prompt is empty"
        client = OpenAI(
            base_url="https://router.huggingface.co/v1",
            api_key=os.environ["HF_TOKEN"],
        )

        completion = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B:nscale",
            messages=[
                {
                    "role": "user",
                    "content": f"{user_prompt}",
                }
            ],
        )

        print(completion.choices[0].message)