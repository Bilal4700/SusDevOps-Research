from openai import OpenAI # type: ignore
from dotenv import load_dotenv
import os
load_dotenv()


class OpenAi:
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY")
    )

    @staticmethod
    def generate_terraform_script(user_prompt: str) -> str:
        if not user_prompt:
            return "Prompt is empty"

        prompt = f"{user_prompt}"
        completion = OpenAi.client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[{"role": "user", "content": prompt}]
        )

        # Extract the text content (don't print the object)
        content = completion.choices[0].message.content or ""

        # Extract token usage (may vary by router / model)
        usage = {
            "prompt_tokens": getattr(completion.usage, "prompt_tokens", None),
            "completion_tokens": getattr(completion.usage, "completion_tokens", None),
            "total_tokens": getattr(completion.usage, "total_tokens", None),
        }

        return content, usage


if __name__ == "__main__":
    openai = OpenAi()
    prompt = """

    Give me a list of all the essential Terraform input variables, provider arguments, and resource arguments I should define if I want to generate a Terraform configuration for [RESOURCE / GOAL] (e.g., a VPC on AWS). Include their names, data types, and example values.

    module "cluster" {
  source  = "terraform-aws-modules/rds-aurora/aws"

  name           = "test-aurora-db-postgres96"
  engine         = "aurora-postgresql"
  engine_version = "14.5"
  instance_class = "db.r6g.large"
  instances = {
    one = {}
    2 = {
      instance_class = "db.r6g.2xlarge"
    }
  }

  vpc_id               = "vpc-12345678"
  db_subnet_group_name = "db-subnet-group"
  security_group_rules = {
    ex1_ingress = {
      cidr_blocks = ["10.20.0.0/20"]
    }
    ex1_ingress = {
      source_security_group_id = "sg-12345678"
    }
  }

  storage_encrypted   = true
  apply_immediately   = true
  monitoring_interval = 10

  enabled_cloudwatch_logs_exports = ["postgresql"]

  tags = {
    Environment = "dev"
    Terraform   = "true"
  }
}
    """
    
    content, usage = openai.generate_terraform_script(prompt)
    print(f"this is content {content}")
    print(f'This is usage {usage}')

    
