import time
import servicemanager


class MyService:
    """Service to customize."""

    def stop(self):
        """Stop the service."""
        self.running = False

    def run(self):
        """Main service loop."""

        self.running = True

        while self.running:
            #  This is where work is done!
            time.sleep(3)
            servicemanager.LogInfoMsg("Service running...")
