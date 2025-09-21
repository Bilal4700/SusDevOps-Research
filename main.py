import llms.OPENAI as OPENAI

def initial_prompt():
    return "What is a Terraform script to create a VPC with public and private subnets in AWS?"

def get_terraform_script(prompt: str) -> str:
    return OPENAI.OPENAI.generate_terraform_script(prompt)

if __name__ == "__main__":
    prompt = initial_prompt()
    terraform_script = get_terraform_script(prompt)
    print(terraform_script)
