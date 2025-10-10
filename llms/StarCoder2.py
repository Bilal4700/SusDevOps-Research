# starcoder_mlx.py
from mlx_lm import load, generate


class StarCoder2:

    @staticmethod
    def generate_terraform_script(user_prompt: str) -> str:
        model, tokenizer = load("mlx-community/starcoder2-7b-4bit")

        content = generate(model, tokenizer, user_prompt)
        # Not defined yet, might not be needed
        usage = ""

        return content, usage

if __name__ == "__main__":
    sc = StarCoder2()
    prompt = """

    "Write a Python script that uploads a local file to a Google Cloud Storage bucket.\n"
    "Requirements:\n"
    "- Use google-cloud-storage client library\n"
    "- Read bucket name and local path from command line args\n"
    "- If object name not provided, use the basename of the file\n"
    "Output only Python code, no comments or markdown.\n"
    "Begin with: import"

    """
    
    content, usage = sc.generate_terraform_script(prompt)
    print(f"this is content {content}")
    print(f'This is usage {usage}')
