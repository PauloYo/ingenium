MODELS = []
ASSISTANTS = []

class Assistant:
    def __init__(self, name, system_prompt, model, temperature):
        self.name = name
        self.system_prompt = system_prompt
        self.model = model 
        self.temperature = temperature


def create_assistant(name, system_prompt, model, temperature=0.7):
    if not name or not system_prompt or not model:
        raise ValueError("Name, system_prompt, and model are required to create an assistant.")
    return Assistant(name, system_prompt, model, temperature)

def list_models():
    return MODELS

def list_assistants():
    return ASSISTANTS

