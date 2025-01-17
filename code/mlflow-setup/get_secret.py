import click
from google.cloud import secretmanager
from dotenv import load_dotenv

load_dotenv()

@click.command()
@click.option("--version", type=str, required=True, default="latest")
@click.option("--project", type=str, required=True)
@click.option("--secret", type=str, required=True)
def main(version: str, project: str, secret: str) -> None:
    client = secretmanager.SecretManagerServiceClient()
    response = client.access_secret_version(
        request={"name": f"projects/{project}/secrets/{secret}/versions/{version}"}
    )
    payload = response.payload.data.decode("UTF-8")
    print(payload, end="")


if __name__ == "__main__":
    main()