
from CarbonFootPrint import  CodeCarbon
import service
import sys



def get_prompt() -> str:
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
    
    return prompt

def print_output_emission_timeElapsed(output, emissions, elapsed):
    print("This is output\n")
    print(output)
    print("")
    print("This is emission\n")
    print(emissions)
    print("")
    print("This is elapsed Time")
    print(elapsed)



if __name__ == "__main__":
    
    initial_prompt = get_prompt()

    choice = input(
        "\nChoose LLM:\n\n"
        "1. openai\n2. gemini\n3. claude\n\nor SLM:\n\n"
        "4. qwen\n5. gemma\nChoice: "
    ).strip()

    # Map choices to your service callables (all must be defined in service)
    call_options = {
        "1": service.get_OPENAI_terraform_script,
        "2": service.get_GEMINI_terraform_script,
        "3": service.get_CLAUDE_terraform_script,
        "4": service.get_QWEN_terraform_script,
        "5": service.get_GEMMA_terraform_script,
    }

    project_name_options = {
        "1": "OpenAI",
        "2": "Gemini",
        "3": "Claude",
        "4": "Qwen",
        "5": "Gemma",
    }

    _model_call = call_options.get(choice)
    _project_name = project_name_options.get(choice)
    if _model_call is None:
        print("Invalid choice. Please run again and choose 1–6.")
        sys.exit(1)
    
    """
    tracking_mode:     "machine" measure the power consumptions of the entire machine (default)
                       "process" try and isolate the tracked processes in isolation
    """

    output, emissions, elapsed = CodeCarbon.run_with_local_emissions(
        prompt=get_prompt(),
        model_call=_model_call,  
        tracking_mode="process",
        project_name= _project_name,
        output_dir="Output",
    )
    
    print_output_emission_timeElapsed(output, emissions, elapsed)
    