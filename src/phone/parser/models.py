from dataclasses import dataclass


from mixins import MandatoryCharacteristicsMixin
from mixins import UkrToEngMixin
from mixins import BasicCharacteristicsMixin
from mixins import ConnectivityCharacteristicsMixin
from mixins import ScreenCharacteristicsMixin
from mixins import ProcessorCharacteristicsMixin
from mixins import MemoryCharacteristicsMixin
from mixins import MainCameraCharacteristicsMixin
from mixins import FrontCameraCharacteristicsMixin
from mixins import WirelessTechnologyCharacteristicsMixin
from mixins import BatteryCharacteristicsMixin
from mixins import BodyCharacteristicsMixin
from mixins import PhysicalCharacteristicsMixin
from mixins import AICharacteristicsMixin
from mixins import DownloadCharacteristicsMixin


@dataclass
class SmartphoneCharacteristics(MandatoryCharacteristicsMixin,
                                UkrToEngMixin,
                                BasicCharacteristicsMixin,
                                ConnectivityCharacteristicsMixin,
                                ScreenCharacteristicsMixin,
                                ProcessorCharacteristicsMixin,
                                MemoryCharacteristicsMixin,
                                MainCameraCharacteristicsMixin,
                                FrontCameraCharacteristicsMixin,
                                WirelessTechnologyCharacteristicsMixin,
                                BatteryCharacteristicsMixin,
                                BodyCharacteristicsMixin,
                                PhysicalCharacteristicsMixin,
                                AICharacteristicsMixin,
                                DownloadCharacteristicsMixin,):
    """
    Class for representing characteristics of a smartphone.

    This class inherits attributes from multiple other mixin classes representing various categories of characteristics.
    """
    pass
