"""
GPU Manager — Lazy-loaded torch with graceful fallback.
If torch is not installed, all GPU features degrade to CPU/NumPy silently.
"""
import logging

logger = logging.getLogger(__name__)

_torch = None

def _get_torch():
    global _torch
    if _torch is None:
        try:
            import torch as _t
            _torch = _t
        except ImportError:
            _torch = False  # Sentinel: tried and failed
            logger.info("PyTorch not installed — GPU acceleration disabled. Using NumPy fallback.")
    return _torch if _torch is not False else None


class GPUManager:
    _instance = None
    _device = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GPUManager, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        torch = _get_torch()
        if torch is not None:
            if torch.cuda.is_available():
                self._device = torch.device("cuda")
                logger.info(f"CUDA is available. Using GPU: {torch.cuda.get_device_name(0)}")
            else:
                self._device = torch.device("cpu")
                logger.info("CUDA is not available. Falling back to CPU (torch installed).")
        else:
            self._device = None
            logger.info("GPU Manager: torch not available — all operations will use NumPy.")

    @property
    def device(self):
        return self._device

    @property
    def available(self) -> bool:
        return self._device is not None

    def to_device(self, tensor):
        if self._device is None:
            raise RuntimeError("torch is not installed")
        return tensor.to(self._device)

    def get_torch_device_str(self):
        torch = _get_torch()
        if torch is None:
            return "cpu"
        return "cuda" if torch.cuda.is_available() else "cpu"

gpu_manager = GPUManager()
device = gpu_manager.device
