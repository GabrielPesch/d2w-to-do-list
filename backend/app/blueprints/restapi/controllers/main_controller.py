from ..controllers import main
import os
from dotenv import load_dotenv

load_dotenv()


@main.route("/", methods=["GET"])
def hello():
    return {f"api working in port {os.environ['PORT']}": "true"}
