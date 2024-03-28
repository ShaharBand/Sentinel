from pydantic import StrictStr

from src.dal.entities.device import Device


class LinuxDevice(Device):
    linux_distribution: StrictStr
    linux_kernel_version: StrictStr
