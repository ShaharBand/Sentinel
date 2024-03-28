from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from beanie import PydanticObjectId

    from src.dal.entities.device import Device

from fastapi import APIRouter

from src.controllers.devices import DeviceController

router = APIRouter(prefix="/devices",
                   tags=["devices"],
                   responses={404: {"description": "Not found"}})
device_controller = DeviceController()


@router.get("/")
async def read_devices() -> list[Device]:
    devices = await device_controller.get_all_devices()
    return devices


@router.get("/{device_id}")
async def read_device(device_id: PydanticObjectId) -> Device:
    device = await device_controller.get_device(device_id)
    return device
