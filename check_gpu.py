import torch
import sys

def check_gpu():
    print(f"Python version: {sys.version}")
    print(f"Torch version: {torch.__version__}")
    cuda_available = torch.cuda.is_available()
    print(f"CUDA available: {cuda_available}")
    
    if cuda_available:
        print(f"CUDA device count: {torch.cuda.device_count()}")
        print(f"Current device: {torch.cuda.current_device()}")
        print(f"Device name: {torch.cuda.get_device_name(0)}")
        print(f"Memory allocated: {torch.cuda.memory_allocated(0)}")
    else:
        print("CUDA is NOT available to Torch.")

if __name__ == "__main__":
    check_gpu()
