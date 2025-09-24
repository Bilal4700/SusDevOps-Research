import scriptGeneration
from CarbonFootPrint import OpenAi_CE, Gemini_CE, Claude_CE, Qwen_CE, Gemma_CE, DeepSeek_CE


prompt = """
Generate a single file with exactly two resources:

hcp_service_principal named workload_sp with a name attribute set to "my-app-runtime".

hcp_iam_workload_identity_provider named example with:

name = "aws-example"

service_principal = hcp_service_principal.workload_sp.resource_name

description = "Allow my-app on AWS to act as my-app-runtime service principal"

aws block containing account_id = "123456789012"

conditional_access = "aws.arn matches `^arn:aws:sts::123456789012:assumed-role/my-app-role`"

Rules:
- Output only valid Terraform code in HCL format.
- No XML/JSON/Markdown/comments/explanations.
- Do not include explanations, comments, variables, outputs, or extra text.
- Indent with exactly 2 spaces.
- Resource names, attributes, and values must match exactly.
"""

if __name__ == "__main__":

    def get_prompt() -> str:
        return prompt
    
    initial_prompt = get_prompt()

    print("")
    choice = input("Do you want to generate script or calculate carbon emissions? (1/2): ")

    if choice == "1":
        script = scriptGeneration.generate_terraform_script(initial_prompt)
        print("Generated Terraform Script:")
        print(script)

    elif choice == "2":
        input_llm = input("\nChoose LLM, you want get carbon footprint for:\n\n1. openai\n2. gemini\n3. claude\n\nor SLM:\n\n4. qwen\n5. gemma\n6. deepseek\nChoice: ")
        if input_llm == "1" or input_llm.lower() == "openai":
            OpenAi_CE.print_carbon_footprint(initial_prompt)

        elif input_llm == "2" or input_llm.lower() == "gemini":
            Gemini_CE.print_carbon_footprint(initial_prompt)
        elif input_llm == "3" or input_llm.lower() == "claude":
            Claude_CE.print_carbon_footprint(initial_prompt)
        elif input_llm == "4" or input_llm.lower() == "qwen":
            Qwen_CE.print_carbon_footprint(initial_prompt)
        elif input_llm == "5" or input_llm.lower() == "gemma":
            Gemma_CE.print_carbon_footprint(initial_prompt)
        elif input_llm == "6" or input_llm.lower() == "deepseek":
            DeepSeek_CE.print_carbon_footprint(initial_prompt)
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, 5, or 6.")
    else:
        print("Invalid choice. Please select 1 or 2.")