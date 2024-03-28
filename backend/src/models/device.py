from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from beanie import PydanticObjectId

    from src.dal.entities.device import Device

from src.dal.repositories.device import DeviceRepository


class DeviceModel:
    def __init__(self):
        self.device_repo = DeviceRepository()

    async def create_device(self, device_data: dict) -> Device:
        return await self.device_repo.create_device(device_data)

    async def get_device_by_id(self, device_id: PydanticObjectId) -> Device:
        return await self.device_repo.get_device_by_id(device_id)

    async def get_all_devices(self) -> list[Device]:
        return await self.device_repo.get_all_devices()

    async def get_devices_by_os_type(self, os_type: str) -> list[Device]:
        return await self.device_repo.get_devices_by_os_type(os_type)

    async def update_device(self, device_id: PydanticObjectId, updated_data: dict) -> bool:
        return await self.device_repo.update_device(device_id, updated_data)

    async def remove_device_by_id(self, device_id: PydanticObjectId) -> bool:
        return await self.device_repo.remove_device_by_id(device_id)
