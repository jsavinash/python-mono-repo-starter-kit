from typer import Typer
app = Typer(add_completion=False)

@app.command()
def main():
    print("Hello from user!")

if __name__ == "__main__":  # pragma: no cover
    app()

