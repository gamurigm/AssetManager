"""Transport-neutral request contracts for broker execution."""

from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, Field


class ExecutionOrderRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    signal_id: str = Field(
        min_length=8,
        max_length=128,
        pattern=r"^[A-Za-z0-9_.:=+-]+$",
    )
    expert_id: str = Field(
        min_length=2,
        max_length=64,
        pattern=r"^[A-Za-z0-9_.-]+$",
    )
    symbol: str = Field(
        min_length=1,
        max_length=32,
        pattern=r"^[A-Za-z0-9._-]+$",
    )
    side: Literal["BUY", "SELL"]
    volume: float = Field(gt=0)
    observed_at_epoch: int = Field(gt=0)
    sl: Optional[float] = Field(default=None, gt=0)
    tp: Optional[float] = Field(default=None, gt=0)
    deviation: Optional[int] = Field(default=None, ge=0, le=1000)
    magic: Optional[int] = Field(default=None, ge=1, le=2_147_483_647)
    comment: str = Field(default="AssetManager EA", max_length=31)
    confirm_live: bool = False


class ExecutionExpertSignalRequest(ExecutionOrderRequest):
    execute: bool = False


class KillSwitchRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    reason: str = Field(min_length=5, max_length=500)


class KillSwitchResetRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    confirm: Literal["RESET"]
