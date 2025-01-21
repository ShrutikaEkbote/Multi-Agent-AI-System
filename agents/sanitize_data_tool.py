from .agent_base import AgentBase

class SanitizeDataTool(AgentBase):
    def __init__(self,max_retries,verbose=True):
        super().__init__(name="SanitizeDataTool",max_retries=max_retries,verbose=verbose)


    def execute(self,medical_data):
        messages =   [
            {"role":"system","content":"You are an AI assitant that sanitizes medical data by removing protected health information(PHI)."},
            {
                "role":"user",
                "content":(
                    "remove all PHI from the following data:\n\n"
                    f"{medical_data}\n\nSanitized Data:"
                )
            }
        ]  
        sanitized_Data = self.call_openai(messages,max_tokens=300)
        return sanitized_Data
    