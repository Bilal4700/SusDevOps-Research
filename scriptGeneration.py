import service

def generate_terraform_script(prompt: str) -> str:
    print("")
    choose_llm = input("\nChoose LLM:\n\n1. openai\n2. gemini\n3. claude\n\nor SLM:\n\n4. qwen\n5. gemma\n6. deepseek\nChoice: ")
    if choose_llm == "1" or choose_llm.lower() == "openai":
        openai_terraform_script = service.get_OPENAI_terraform_script(prompt)
        return(openai_terraform_script)
    elif choose_llm == "2" or choose_llm.lower() == "gemini":
        gemini_terraform_script = service.get_GEMINI_terraform_script(prompt)
        return(gemini_terraform_script)
    elif choose_llm == "3" or choose_llm.lower() == "claude":
        claude_terraform_script = service.get_CLAUDE_terraform_script(prompt)
        return(claude_terraform_script)
    elif choose_llm == "4" or choose_llm.lower() == "qwen":
        qwen_terraform_script = service.get_QWEN_terraform_script(prompt)
        return(qwen_terraform_script)
    elif choose_llm == "5" or choose_llm.lower() == "gemma":
        gemma_terraform_script = service.get_GEMMA_terraform_script(prompt)
        return(gemma_terraform_script)
    elif choose_llm == "6" or choose_llm.lower() == "deepseek":
        deepseek_terraform_script = service.get_DEEPSEEK_terraform_script(prompt)
        return(deepseek_terraform_script)
    else:
        return("Invalid choice. Please select 'openai', 'gemini', 'claude', 'qwen', 'gemma', or 'deepseek'.")

