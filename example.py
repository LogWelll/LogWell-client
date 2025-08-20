import logging
from logwell_client.handler import LogServiceHandler, Endpoint

# Configure root logger
logger = logging.getLogger("my-app")
logger.setLevel(logging.DEBUG)

# Add your custom handler
handler = LogServiceHandler(base_url="http://localhost:8000", api_key="key1")
logger.addHandler(handler)

# Standard logging works as usual
logger.info(
    "Hello world!", extra={"tag": "tag1", "endpoint": Endpoint.NonBlocking}
)  # will be sent via your microservice
logger.error("Something went wrong", extra={"tenant": "customerA"})
