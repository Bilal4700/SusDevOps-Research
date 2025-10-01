import anthropic
from dotenv import load_dotenv
import os
load_dotenv()


class Claude:

    @staticmethod
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
        content = message.content[0].text

        usage = {
            "prompt_tokens": message.usage.input_tokens,
            "completion_tokens": message.usage.output_tokens,
            "total_tokens": message.usage.input_tokens + message.usage.output_tokens,
        }

        return content, usage
    


if __name__ == "__main__":
    claude = Claude()

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
    
    content, usage = claude.generate_terraform_script(prompt)
    print(f"this is content \n{content}")
    print(f'This is usage {usage}')
