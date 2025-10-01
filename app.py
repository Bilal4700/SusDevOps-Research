
from CarbonFootPrint import OpenAi_CE, Gemini_CE, Claude_CE, Qwen_CE, Gemma_CE, DeepSeek_CE

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

def print_script_and_emission(script, emission):
    print("This is Script:\n")
    print(script)
    print(f'Emission in kg: {emission}')



if __name__ == "__main__":
    
    initial_prompt = get_prompt()

    print("")


    choose_llm = input("\nChoose LLM:\n\n1. openai\n2. gemini\n3. claude\n\nor SLM:\n\n4. qwen\n5. gemma\n6. deepseek\nChoice: ")

    # 4 and 6 servers are down
    if choose_llm == "1" or choose_llm.lower() == "openai":
        output, emissions_kg = OpenAi_CE.get_llm_with_local_emissions(initial_prompt)
        print_script_and_emission(output,emissions_kg)

    elif choose_llm == "2" or choose_llm.lower() == "gemini":
        output, emissions_kg = Gemini_CE.get_llm_with_local_emissions(initial_prompt)
        print_script_and_emission(output,emissions_kg)

    elif choose_llm == "3" or choose_llm.lower() == "claude":
        output, emissions_kg = Claude_CE.get_llm_with_local_emissions(initial_prompt)
        print_script_and_emission(output,emissions_kg)

    elif choose_llm == "4" or choose_llm.lower() == "qwen":
        output, emissions_kg = Qwen_CE.get_slm_with_local_emissions(initial_prompt)
        print_script_and_emission(output,emissions_kg)

    elif choose_llm == "5" or choose_llm.lower() == "gemma":
        output, emissions_kg = Gemma_CE.get_slm_with_local_emissions(initial_prompt)
        print_script_and_emission(output,emissions_kg)

    elif choose_llm == "6" or choose_llm.lower() == "deepseek":
        output, emissions_kg = DeepSeek_CE.get_slm_with_local_emissions(initial_prompt)
        print_script_and_emission(output,emissions_kg)

    else:
        print("Invalid choice. Please select 1, 2, 3, 4, 5, or 6.")
