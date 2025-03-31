class Config:
    def __init__(self, env_path: str = ".env"):
        self.env_path = env_path
        self.load_env()
        
    def load_env(self):
        with open(self.env_file) as f:
            for line in f:
                if line.startswith('#') or not line.strip():
                    continue
                # https://stackoverflow.com/a/51904059
                # if 'export' not in line:
                #     continue
                # Remove leading `export `, if you have those
                # then, split name / value pair
                # key, value = line.replace('export ', '', 1).strip().split('=', 1)
                key, value = line.strip().split('=', 1)
                # os.environ[key] = value  # Load to local environ
                # env_vars[key] = value # Save to a dict, initialized env_vars = {}
                setattr(self, key.lower(), value)

config = Config()
