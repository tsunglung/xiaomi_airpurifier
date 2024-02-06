"""
Support for Xiaomi Mi Smart Pedestal Fan.

For more details about this platform, please refer to the documentation
https://home-assistant.io/components/fan.xiaomi_miio/
"""
import enum
from typing import Any, Dict

import click

from miio.click_common import command, format_output
from miio import (  # pylint: disable=import-error
    MiotDevice
)
from miio.device import DeviceStatus
from miio.fan_common import FanException, OperationMode
from .const import MODEL_MOSQ_DAKUO
import logging
_LOGGER = logging.getLogger(__name__)

MIOT_MAPPING = {
    MODEL_MOSQ_DAKUO: {
        "power": {"siid": 6, "piid": 1},
#        "liquid_left": {"siid": 5, "piid": 1},
        "mode": {"siid": 6, "piid": 2}
    }
}


class OperationModeMiot(enum.Enum):
    Normal = 0
    Nature = 1


class MosqStatusMiot(DeviceStatus):
    """Container for status reports for Xiaomi Mosquito Dispeller."""

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Response of a Mosquito Dispeller (ateai.mosq.dakuo):
        {
          'id': 1,
          'result': [
            {'did': 'power', 'siid': 2, 'piid': 1, 'code': 0, 'value': False},
          ],
          'exe_time': 280
        }
        """
        self.data = data
#        _LOGGER.error(self.__dict__)

    @property
    def power(self) -> str:
        """Power state."""
        return "on" if self.data["power"] else "off"

    @property
    def is_on(self) -> bool:
        """True if device is currently on."""
        return self.data["power"]

    @property
    def mode(self) -> OperationMode:
        """Operation mode."""
        return OperationMode[OperationModeMiot(self.data["mode"]).name]

    @property
    def speed(self) -> int:
        """Speed of the motor."""
        return 0 # self.data["fan_speed"]


class Dispeller(MiotDevice):
    mapping = MIOT_MAPPING[MODEL_MOSQ_DAKUO]
    def __init__(
        self,
        ip: str = None,
        token: str = None,
        start_id: int = 0,
        debug: int = 1,
        lazy_discover: bool = True,
        model: str = MODEL_MOSQ_DAKUO,
    ) -> None:
        if model not in MIOT_MAPPING:
            raise FanException("Invalid Dispeller model: %s" % model)

        super().__init__(ip, token, start_id, debug, lazy_discover)
        #self.model = model

    @command(
        default_output=format_output(
            "",
            "Power: {result.power}\n"
            "Operation mode: {result.mode}\n",
        )
    )
    def status(self) -> MosqStatusMiot:
        """Retrieve properties."""
        return MosqStatusMiot(
            {
                prop["did"]: prop["value"] if prop["code"] == 0 else None
                for prop in self.get_properties_for_mapping()
            }
        )

    @command(default_output=format_output("Powering on"))
    def on(self):
        """Power on."""
        return self.set_property("power", True)

    @command(default_output=format_output("Powering off"))
    def off(self):
        """Power off."""
        return self.set_property("power", False)
