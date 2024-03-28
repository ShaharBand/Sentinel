from datetime import datetime

from beanie import Document
from pydantic import StrictStr, IPvAnyAddress


class Device(Document):
    name: StrictStr
    os_type: StrictStr
    ip_address: IPvAnyAddress
    description: StrictStr
    last_update: datetime
    registration_date: datetime

    class Meta:
        collection_name = "device"

    def __repr__(self):
        return f'Device(id={self.id}, name={self.name}, os_type={self.os_type}, ip_address={self.ip_address})'



