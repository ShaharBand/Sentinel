import pytest


@pytest.fixture
def device_fixture():
    pass


def test_insert_and_find_device_by_id(device_fixture):
    test_device = device_fixture

    pass
    """
    found_device = DeviceModel.get_device_by_id(test_device.id)

    assert found_device.id == test_device.id
    assert found_device.name == test_device.name
    assert found_device.description == test_device.description
    assert found_device.address == test_device.address
    assert found_device.os_type == test_device.os_type
    assert found_device.last_scan_date == test_device.last_scan_date
    """
