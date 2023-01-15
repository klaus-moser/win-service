import time
from SMWinservice import SMWinservice


class PythonCornerExample(SMWinservice):
    _svc_name_ = 'My Service Name'
    _svc_display_name_ = 'My Service display name'
    _svc_description_ = 'My Service Description'

    def start(self):
        """Start the service"""
        self.isrunning = True

    def stop(self):
        """Stop the service"""
        self.isrunning = False

    def main(self):
        """Main service loop. This is where work is done!"""

        while self.isrunning:
            pass
            # code here
            time.sleep(3)


if __name__ == '__main__':
    PythonCornerExample.parse_command_line()
