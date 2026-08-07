"""Compatibility guard for the retired standalone storage consumer.

Tick persistence now belongs exclusively to market_data_gateway.  Keeping a
second DuckDB writer would reintroduce the cross-process locking this
architecture removes.
"""


def main() -> None:
    raise SystemExit(
        "storage_service was retired: start services.market_data_gateway.main "
        "which owns tick storage and its transactional outbox"
    )


if __name__ == "__main__":
    main()
