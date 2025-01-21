from .agent_base import AgentBase

class RefinerAgent(AgentBase):
    def __init__(self,max_retries,verbose=True):
        super().__init__(name="RefinerAgent",max_retries=max_retries,verbose=verbose)


    def execute(self,draft):
        messages =   [
            
            {
                "role":"system",
                "content":[
                    {
                        "type":"text",
                        "text":"You are an expert Editor who refines and enhances research articles for clarity,coherence and acadamic quality." 
                    }
                ]
            },
            {
                "role":"user",
                "content":[
                    {
                        "type":"text",
                        "text":"please refine the following research article draft to improve its language ,coherence and overall quality:\n\n."
                        f"{draft}\n\nRefined Article:" 
                    }
                ]
            }

        ]  
        refined_article = self.call_openai(
            messages = messages,
            temperature=0.5,
            max_tokens=2048)
        return refined_article