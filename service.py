import llms.OpenAi as OPENAI
import llms.Gemini as GEMINI
import llms.Claude as CLAUDE
import slms.Qwen as QWEN
import slms.Gemma as GEMMA
import slms.DeepSeek as DEEPSEEK


def get_OPENAI_terraform_script(prompt: str) -> str:
    text, usage = OPENAI.OpenAi.generate_terraform_script(prompt)
    return text, usage

def get_GEMINI_terraform_script(prompt: str) -> str:
    text, usage = GEMINI.Gemini.generate_terraform_script(prompt)
    return text, usage

def get_CLAUDE_terraform_script(prompt: str) -> str:
    text, usage = CLAUDE.Claude.generate_terraform_script(prompt)
    return text, usage

def get_QWEN_terraform_script(prompt: str):
    text, usage = QWEN.Qwen.generate_terraform_script(prompt)
    return text, usage

def get_GEMMA_terraform_script(prompt: str) -> str:
    text, usage = GEMMA.Gemma.generate_terraform_script(prompt)
    return text, usage





