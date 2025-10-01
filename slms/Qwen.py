from dotenv import load_dotenv
import os
from openai import OpenAI


load_dotenv()
class Qwen:

    @staticmethod
    def generate_terraform_script(user_prompt: str) -> str:
        if not user_prompt:
            return "Prompt is empty"
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.environ["QWEN_API_KEY"],
        )

        completion = client.chat.completions.create(
            # model="Qwen/Qwen2.5-Coder-14B:featherless-ai",
            model = "qwen/qwen2.5-vl-72b-instruct:free",
            messages=[
                {
                    "role": "user",
                    "content": f"{user_prompt}",
                }
            ],
        )

        # Extract the text content (don't print the object)
        content = completion.choices[0].message.content

        # Extract token usage (may vary by router / model)
        usage = {
            "prompt_tokens": getattr(completion.usage, "prompt_tokens", None),
            "completion_tokens": getattr(completion.usage, "completion_tokens", None),
            "total_tokens": getattr(completion.usage, "total_tokens", None),

        }

        return content, usage


if __name__ == "__main__":

    qwen = Qwen()
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
    text, usage = qwen.generate_terraform_script(prompt)
    print(text)          # <-- actual Terraform HCL
    print("usage:", usage)
