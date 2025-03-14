import logging
import os
from datetime import datetime

class Logger:
    """Custom logger for the application."""
    
    def __init__(self):
        self.setup_logger()
    
    def setup_logger(self):
        """Set up the logger configuration."""
        # Create logs directory if it doesn't exist
        if not os.path.exists('logs'):
            os.makedirs('logs')
            
        # Configure logging
        log_filename = f'logs/app_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_filename),
                logging.StreamHandler()
            ]
        )
        
        self.logger = logging.getLogger('DishVisionAI')
    
    def info(self, message: str):
        """Log info level message."""
        self.logger.info(message)
    
    def error(self, message: str):
        """Log error level message."""
        self.logger.error(message)
    
    def warning(self, message: str):
        """Log warning level message."""
        self.logger.warning(message)
    
    def debug(self, message: str):
        """Log debug level message."""
        self.logger.debug(message)

# Create a global logger instance
logger = Logger() 