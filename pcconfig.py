import pynecone as pc

class WealthConfig(pc.Config):
    pass

config = WealthConfig(
    app_name="wealth",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)