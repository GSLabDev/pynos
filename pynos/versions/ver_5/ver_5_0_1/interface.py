"""
Copyright 2015 Brocade Communications Systems, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import pynos.utilities
from pynos.versions.base.interface import Interface as InterfaceBase
from pynos.versions.ver_6.ver_6_0_1.yang.brocade_mac_address_table \
    import brocade_mac_address_table


class Interface(InterfaceBase):
    """
    The Interface class holds all the actions assocaiated with the Interfaces
    of a NOS device.

    Attributes:
        None
    """

    def __init__(self, callback):
        """
        Interface init function.

        Args:
            callback: Callback function that will be called for each action.

        Returns:
            Interface Object

        Raises:
            None
        """
        self._callback = callback
        self._mac_address_table = brocade_mac_address_table(
            callback=pynos.utilities.return_xml
        )

    def mac_move_detect_enable(self, **kwargs):
        raise NotImplementedError
