import torch
import logging

logger = logging.getLogger(__name__)

class GPUManager:
    _instance = None
    _device = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GPUManager, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        if torch.cuda.is_available():
            self._device = torch.device("cuda")
            logger.info(f"CUDA is available. Using GPU: {torch.cuda.get_device_name(0)}")
        else:
            self._device = torch.device("cpu")
            logger.info("CUDA is not available. Falling back to CPU.")

    @property
    def device(self):
        return self._device

    def to_device(self, tensor: torch.Tensor):
        return tensor.to(self._device)

    def get_torch_device_str(self):
        return "cuda" if torch.cuda.is_available() else "cpu"

gpu_manager = GPUManager()
device = gpu_manager.device
