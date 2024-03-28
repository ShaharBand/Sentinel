from pydantic import StrictStr

from src.dal.entities.device import Device


class WindowsDevice(Device):
    windows_version: StrictStr
    windows_update_status: StrictStr
