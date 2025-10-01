from google import genai
from dotenv import load_dotenv
import os
load_dotenv()


class Gemini:
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY")
    )

    @staticmethod
    def generate_terraform_script(user_prompt: str) -> str:
        if not user_prompt:
            return "Prompt is empty"

        prompt = f"{user_prompt}"
        completion = Gemini.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[prompt]
        )

        # Extract the text content (don't print the object)
        content = completion.text 

        # Extract token usage (may vary by router / model)
        usage = {
            "prompt_tokens": getattr(completion.usage_metadata, "prompt_token_count", None),
            "completion_tokens": getattr(completion.usage_metadata, "candidates_token_count", None),
            "total_tokens": (
                completion.usage_metadata.prompt_token_count +
                completion.usage_metadata.candidates_token_count
            ),

        }

        return content, usage

if __name__ == "__main__":
    gemini = Gemini()

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
    
    content, usage = gemini.generate_terraform_script(prompt)
    print(f"this is content \n{content}")
    print(f'This is usage {usage}')
