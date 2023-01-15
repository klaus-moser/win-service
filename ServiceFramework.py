import sys
import servicemanager
import win32service
import win32serviceutil

from service import MyService


class MyServiceFramework(win32serviceutil.ServiceFramework):

    _svc_name_ = 'My service name'
    _svc_display_name_ = 'My service display name'
    _svc_description_ = 'My service description'

    def SvcStop(self):
        """Stop the service"""

        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.service_impl.stop()
        self.ReportServiceStatus(win32service.SERVICE_STOPPED)

    def SvcDoRun(self):
        """Start the service; does not return until stopped"""

        self.ReportServiceStatus(win32service.SERVICE_START_PENDING)
        self.service_impl = MyService()
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)

        # Run the service
        self.service_impl.run()


def init():
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(MyServiceFramework)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(MyServiceFramework)


if __name__ == '__main__':
    init()
