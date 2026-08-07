import pytest

from app.services.simulation_service import SimulationService


def test_pre_registered_job_has_queryable_queued_state():
    service = SimulationService()

    sim_id = service.pre_register("aapl", "ORB_FVG_ENGULFING")
    job = service.get_job(sim_id)

    assert job is not None
    assert job["symbol"] == "AAPL"
    assert job["status"] == "queued"
    assert service.is_pending(sim_id)
    assert service.get_result(sim_id) is None


def test_failed_job_is_retained_instead_of_turning_into_404():
    service = SimulationService()
    sim_id = service.pre_register("SPY", "ORB_FVG_ENGULFING")

    service._set_job_state(sim_id, "failed", error="provider unavailable")
    job = service.get_job(sim_id)

    assert job is not None
    assert job["status"] == "failed"
    assert job["error"] == "provider unavailable"
    assert not service.is_pending(sim_id)


def test_active_job_capacity_is_fail_closed():
    service = SimulationService(max_active_jobs=1)

    service.pre_register("AAPL", "ORB_FVG_ENGULFING")
    with pytest.raises(ValueError, match="capacity"):
        service.pre_register("MSFT", "ORB_FVG_ENGULFING")
