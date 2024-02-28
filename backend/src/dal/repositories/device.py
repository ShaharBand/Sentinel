from beanie import PydanticObjectId

from src.dal.entities.device import Device
from src.dal.entities.devices import *

DEVICE_CLASS_MAP = {
    "windows": WindowsDevice,
    "linux": LinuxDevice,
}


class DeviceFactory:
    @staticmethod
    def create_device(device_data: dict) -> Device:
        os_type = device_data.pop('os_type').lower()
        if os_type in DEVICE_CLASS_MAP:
            device = DEVICE_CLASS_MAP[os_type](**device_data)
            return device
        return Device(**device_data)


class DeviceRepository:
    @staticmethod
    async def create_device(device_data: dict) -> Device:
        new_device = DeviceFactory.create_device(device_data)
        await new_device.insert()
        return new_device

    @staticmethod
    async def get_device_by_id(device_id: PydanticObjectId) -> Device:
        return await Device.get(device_id)

    @staticmethod
    async def get_all_devices() -> list[Device]:
        return await Device.find().to_list()

    @staticmethod
    async def get_devices_by_os_type(os_type: str) -> list[Device]:
        # TODO: testing this will be required i am not sure
        if os_type.lower() in DEVICE_CLASS_MAP:
            device_class = DEVICE_CLASS_MAP[os_type.lower()]
            return await device_class.find().to_list()
        return []

    @staticmethod
    async def update_device(device_id: PydanticObjectId, updated_data: dict) -> bool:
        device = await Device.get(device_id)
        if device:
            for key, value in updated_data.items():
                setattr(device, key, value)
            await device.update()
            return True
        return False

    @staticmethod
    async def remove_device_by_id(device_id: PydanticObjectId) -> bool:
        device = await Device.get(device_id)
        if device:
            await device.delete()
            return True
        return False
