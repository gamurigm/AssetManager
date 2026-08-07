from app.core.runtime_policy import APIRuntimePolicy


def test_default_policy_keeps_broker_connections_out_of_api_process() -> None:
    policy = APIRuntimePolicy.from_mapping({})

    assert policy.kafka_fanout_enabled is True
    assert policy.scheduler_enabled is False
    assert policy.broker_connections_enabled is False


def test_runtime_policy_parses_explicit_boolean_flags() -> None:
    policy = APIRuntimePolicy.from_mapping(
        {
            "API_ENABLE_KAFKA_FANOUT": "false",
            "API_ENABLE_SCHEDULER": "yes",
            "API_ENABLE_BROKER_CONNECTIONS": "1",
        }
    )

    assert policy.kafka_fanout_enabled is False
    assert policy.scheduler_enabled is True
    assert policy.broker_connections_enabled is True
