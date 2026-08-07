from pathlib import Path

import yaml


def test_compose_declares_coarse_grained_services_and_separate_data_ownership() -> None:
    root = Path(__file__).resolve().parents[2]
    compose = yaml.safe_load((root / "docker-compose.yml").read_text(encoding="utf-8"))
    services = compose["services"]

    assert {"kafka", "market-data", "analysis", "api"} <= set(services)
    assert "storage-service" not in services
    assert services["market-data"]["environment"]["KAFKA_BOOTSTRAP_SERVERS"] == "kafka:29092"
    assert services["analysis"]["environment"]["KAFKA_BOOTSTRAP_SERVERS"] == "kafka:29092"
    assert services["api"]["environment"]["API_ENABLE_BROKER_CONNECTIONS"] == "false"
    assert services["api"]["environment"]["API_ENABLE_SCHEDULER"] == "false"
    assert services["api"]["environment"]["EXECUTION_GATEWAY_URL"].endswith(":8293")

    market_volumes = set(services["market-data"]["volumes"])
    api_volumes = set(services["api"]["volumes"])
    assert market_volumes.isdisjoint(api_volumes)
