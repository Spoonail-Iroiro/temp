import json

class Config:
    config = None
    def __init__(self):
        pass

    @classmethod
    def load_config(cls, path):
        with open(path,"r") as f:
            cls.config = json.load(f)

    @classmethod
    def save_config(cls, path):
        with open(path,"w") as f:
            json.dump(cls.config, f, indent=4)

