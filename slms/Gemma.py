from google import genai
from dotenv import load_dotenv
import os
load_dotenv()


class Gemma:
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY")
    )

    @staticmethod
    def generate_terraform_script(user_prompt: str) -> str:
        if not user_prompt:
            return "Prompt is empty"

        prompt = f"{user_prompt}"
        completion = Gemma.client.models.generate_content(
            model="gemma-3n-e2b-it",
            contents=[prompt]
        )

        content = completion.text
        usage = {
            "prompt_tokens": getattr(completion.usage_metadata, "prompt_token_count", None),
            "completion_tokens": getattr(completion.usage_metadata, "candidates_token_count", None),
            "total_tokens": getattr(completion.usage_metadata, "total_token_count", None),

        }
        return content , usage
    

if __name__ == "__main__":

    gemma = Gemma()
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
    text, usage = gemma.generate_terraform_script(prompt)
    print(text)          # <-- actual Terraform HCL
    print("usage:", usage)


