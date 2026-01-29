import os
from typer import Typer
from dotenv import load_dotenv
from rich.console import Console

#Internal dependencies
from core.print import printAnything
from shared.numberUtils import addTwoNumbers

load_dotenv()
app = Typer(add_completion=False)

@app.command()
def main():
    print("Hello from user!")
    printAnything()
    addTwoNumbers(1,2)
    # Now you can access your environment variables using os.getenv
    debug = os.getenv('DEBUG')
    secret_key = os.getenv('SECRET_KEY')
    database_url = os.getenv('DATABASE_URL')
    Console().print(f"Debug: {debug}\n Secret key: {secret_key}\n Database URL: {database_url}")

if __name__ == "__main__":  # pragma: no cover
    app()



