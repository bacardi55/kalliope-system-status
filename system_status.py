import psutil
import platform
import datetime

import logging

from kalliope.core.NeuronModule import NeuronModule, InvalidParameterException

logging.basicConfig()
logger = logging.getLogger("kalliope")

class System_status(NeuronModule):
    def __init__(self, **kwargs):
        super(SystemStatus, self).__init__(**kwargs)

        os, name, version, _, _, _ = platform.uname()
        version = version.split('-')[0]
        cores = psutil.cpu_count()
        cpu_percent = psutil.cpu_percent()
        memory_percent = psutil.virtual_memory()[2]
        disk_percent = psutil.disk_usage('/')[3]
        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
        running_since = boot_time.strftime("%A %d. %B %Y")
        response = "I am currently running on %s version %s.  " %(os, version)
        response += "This system is named %s and has %s CPU cores.  " %(name, cores)
        response += "Current CPU utilization is %s percent.  " %cpu_percent
        response += "Current memory utilization is %s percent." %memory_percent

        print(response)

        self.message = response



