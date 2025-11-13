import os

class Config:

    def __init__(self):
        self._print_config = self._get_print_config()
        self._log_config = self._get_log_config()

    def _get_log_config(self):
        log_config = dict()
        log_config["DEBUG"] = os.environ.get("DEBUG", "False")
        return log_config

    def _get_print_config(self):
        print_config = dict()
        print_config["MESSAGE"] = os.environ.get("MESSAGE", "Hello World!")
        return print_config

    def get_log_config(self):
        return self._log_config
    
    def get_print_config(self):
        return self._print_config
