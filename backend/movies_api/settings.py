from os import getenv
from os.path import dirname, join

from dotenv import load_dotenv
from toml import load

load_dotenv()

root_dir = join(dirname(__file__), "..")

project = load(join(root_dir, "./pyproject.toml"))
poetry = project.get("tool", {}).get("poetry", {})

DATABASE_URL: str = getenv("POSTGRES_DB_URI", "postgres://localhost:5432")