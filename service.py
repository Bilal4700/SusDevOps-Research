import llms.OpenAi as OPENAI
import llms.Gemini as GEMINI
import llms.Claude as CLAUDE
import slms.Qwen as QWEN
import slms.Gemma as GEMMA
import slms.DeepSeek as DEEPSEEK


def get_OPENAI_terraform_script(prompt: str) -> str:
    return OPENAI.OpenAi.generate_terraform_script(prompt)

def get_GEMINI_terraform_script(prompt: str) -> str:
    return GEMINI.Gemini.generate_terraform_script(prompt)

def get_CLAUDE_terraform_script(prompt: str) -> str:
    return CLAUDE.Claude.generate_terraform_script(prompt)

def get_QWEN_terraform_script(prompt: str) -> str:
    return QWEN.Qwen.generate_terraform_script(prompt)

def get_GEMMA_terraform_script(prompt: str) -> str:
    return GEMMA.Gemma.generate_terraform_script(prompt)

def get_DEEPSEEK_terraform_script(prompt: str) -> str:
    return DEEPSEEK.DeepSeek.generate_terraform_script(prompt)






