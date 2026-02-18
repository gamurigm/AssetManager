import logging
import sys
import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("MMAM")

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.perf_counter()
        
        # Log request
        path = request.url.path
        if request.query_params:
            path += f"?{request.query_params}"
        
        logger.info(f"Incoming {request.method} {path}")
        
        try:
            response = await call_next(request)
            process_time = time.perf_counter() - start_time
            
            # Log response
            logger.info(
                f"Completed {request.method} {path} | Status: {response.status_code} | Time: {process_time:.4f}s"
            )
            return response
        except Exception as e:
            process_time = time.perf_counter() - start_time
            logger.error(
                f"Failed {request.method} {path} | Error: {str(e)} | Time: {process_time:.4f}s"
            )
            raise e
