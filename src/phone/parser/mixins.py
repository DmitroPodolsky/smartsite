from dataclasses import dataclass
from typing import Any, ClassVar


@dataclass
class MandatoryCharacteristicsMixin:
    """
    Mixin Mixin class for representing mandatory characteristics of a smartphone.
    """
    mandatory_attrs: ClassVar[list[str]] = [
        'series',
        'screen_diagonal',
        'screen_refresh_rate',
        'number_of_cores',
        'internal_memory',
        'ram',
        ]
    
    def __getattribute__(self, name: str) -> Any:
        """
        Get attribute and ensure that mandatory attributes are set.
        """
        attribute = super().__getattribute__(name)
        if type(attribute) is dict:
            return attribute
    
        for mandatory_attr in super().__getattribute__('mandatory_attrs'):
            value = super().__getattribute__(mandatory_attr)
            if value is None:
                raise ValueError(f"{name} is required but not set")
        return attribute


@dataclass
class UkrToEngMixin:
    """
    Mixin class for representing Ukrainian to English translations of smartphone characteristics.
    """
    ukrainian_to_english: ClassVar[dict[str, str]] = {
    # Основне
    'Серія': 'series',
    'Рік випуску': 'release_year',
    'Операційна система': 'operating_system',
    #Зв'язок
    'Кількість SIM-карт': 'number_of_sim_cards',
    'Тип SIM-карти': 'sim_card_type',
    'Тип слоту': 'slot_type',
    "Стандарти зв'язку": 'connection_standards',
    #Тип екрану
    'Тип екрану' : 'screen_type',
    'Діагональ екрану' : 'screen_diagonal',
    'Роздільна здатність екрану' : 'screen_resolution',
    'Роздільна здатність екрана, PX' : 'screen_resolution_px',
    'Частота оновлення екрану' : 'screen_refresh_rate',
    'Щільність пікселів, PPI' : 'pixel_density_ppi',
    'Захист скла' : 'glass_protection',
    'Кількість кольорів' : 'number_of_colors',
    'Співвідношення сторін' : 'aspect_ratio',
    'Співвідношення екран/корпус' : 'screen_to_body_ratio',
    'Додатково' : 'additional',
    #Процесор
    'Процесор' : 'processor',
    'Кількість ядер' : 'number_of_cores',
    'Частота процесора' : 'processor_frequency',
    'Графічний процесор' : 'graphics_processor',
    'Смартфон для геймінгу' : 'gaming_smartphone',
    #Пам'ять
    "Внутрішня пам'ять" : 'internal_memory',
    "Оперативна пам'ять" : 'ram',
    "Підтримка карток пам'яті" : 'memory_card_support',
    #Основна камера
    'Основна камера' : 'main_camera',
    'Кількість модулів основної камери' : 'number_of_main_camera_modules',
    'Діафрагма' : 'aperture',
    'Запис відео' : 'video_recording',
    'Автофокусування' : 'autofocus',
    'Стабілізація' : 'stabilization',
    'Спалах' : 'flash',
    'Особливості' : 'features',
    #Фронтальна камера
    'Фронтальна камера' : 'front_camera',
    'Запис відео' : 'video_recording',
    'Особливості' : 'features',
    #Бездротови технологии
    'Wi-Fi' : 'wi_fi',
    'Супутникова система' : 'satellite_system',
    'Bluetooth' : 'bluetooth',
    'NFC' : 'nfc',
    'Інфрачервоний порт' : 'infrared_port',
    #Акумулятор
    'Ємність аккумулятора' : 'battery_capacity',
    'Тип акумулятора' : 'battery_type',
    'Швидка зарядка' : 'fast_charging',
    'Бездротова зарядка' : 'wireless_charging',
    'Особливості' : 'features',
    'Автономна робота': 'autonomous_work', 
    #Корпус
    'Матеріал корпуса' : 'body_material',
    'Стандарт захисту' : 'protection_standard',
    'Захист корпусу' : 'body_protection',
    'Датчики' : 'sensors',
    'Біометричний захист' : 'biometric_protection',
    'Інтерфейси та підключення' : 'interfaces_and_connections',
    'Стилус' : 'stylus',
    'Особливості телефону' : 'phone_features',
    'Колір' : 'color',
    #Физични характеристики
    'Вага' : 'weight',
    'Габарити (ВхШхГ)' : 'dimensions_hxwxd',
    'Комплектація' : 'package_contents',
    'Юридична інформація' : 'legal_information',
    #Штучний интелект
    'AI' : 'ai',
    #Завантаження
    'Iнструкцiя' : 'instructions',
    }


@dataclass
class BasicCharacteristicsMixin:
    """
    Mixin class for representing basic characteristics of a smartphone.
    """
    # Основне
    series: str | None = None
    release_year: str | None = None
    operating_system: str | None = None


@dataclass
class ConnectivityCharacteristicsMixin:
    """
    Mixin """
    # Зв'язок
    number_of_sim_cards: str | None = None
    sim_card_type: str | None = None
    slot_type: str | None = None
    connection_standards: str | None = None


@dataclass
class ScreenCharacteristicsMixin:
    """
    Mixin class for representing screen characteristics of a smartphone.
    """
    # Тип екрану
    screen_type: str | None = None
    screen_diagonal: str | None = None
    screen_resolution: str | None = None
    screen_resolution_px: str | None = None
    screen_refresh_rate: str | None = None
    pixel_density_ppi: str | None = None
    glass_protection: str | None = None
    number_of_colors: str | None = None
    aspect_ratio: str | None = None
    screen_to_body_ratio: str | None = None
    additional: str | None = None


@dataclass
class ProcessorCharacteristicsMixin:
    """
    Mixin class for representing processor characteristics of a smartphone.
    """
    # Процесор
    processor: str | None = None
    number_of_cores: str | None = None
    processor_frequency: str | None = None
    graphics_processor: str | None = None
    gaming_smartphone: str | None = None


@dataclass
class MemoryCharacteristicsMixin:
    """
    Mixin class for representing memory characteristics of a smartphone.
    """
    # Пам'ять
    internal_memory: str | None = None
    ram: str | None = None
    memory_card_support: str | None = None


@dataclass
class MainCameraCharacteristicsMixin:
    """
    Mixin class for representing main camera characteristics of a smartphone.
    """
    # Основна камера
    main_camera: str | None = None
    number_of_main_camera_modules: str | None = None
    aperture: str | None = None
    video_recording: str | None = None
    autofocus: str | None = None
    stabilization: str | None = None
    flash: str | None = None
    features: str | None = None


@dataclass
class FrontCameraCharacteristicsMixin:
    """
    Mixin class for representing front camera characteristics of a smartphone.
    """
    # Фронтальна камера
    front_camera: str | None = None
    video_recording: str | None = None
    features: str | None = None


@dataclass
class WirelessTechnologyCharacteristicsMixin:
    """
    Mixin class for representing wireless technology characteristics of a smartphone.
    """
    # Бездротові технології
    wi_fi: str | None = None
    satellite_system: str | None = None
    bluetooth: str | None = None
    nfc: str | None = None
    infrared_port: str | None = None


@dataclass
class BatteryCharacteristicsMixin:
    """
    Mixin class for representing battery characteristics of a smartphone.
    """
    # Акумулятор
    battery_capacity: str | None = None
    battery_type: str | None = None
    fast_charging: str | None = None
    wireless_charging: str | None = None
    features: str | None = None
    autonomous_work: str | None = None


@dataclass
class BodyCharacteristicsMixin:
    """
    Mixin class for representing body characteristics of a smartphone.
    """
    # Корпус
    body_material: str | None = None
    protection_standard: str | None = None
    body_protection: str | None = None
    sensors: str | None = None
    biometric_protection: str | None = None
    interfaces_and_connections: str | None = None
    stylus: str | None = None
    phone_features: str | None = None
    color: str | None = None


@dataclass
class PhysicalCharacteristicsMixin:
    """
    Mixin class for representing physical characteristics of a smartphone.
    """
    # Фізичні характеристики
    weight: str | None = None
    dimensions_hxwxd: str | None = None
    package_contents: str | None = None
    legal_information: str | None = None


@dataclass
class AICharacteristicsMixin:
    """
    Mixin class for representing AI characteristics of a smartphone.
    """
    # Штучний інтелект
    ai: str | None = None


@dataclass
class DownloadCharacteristicsMixin:
    """
    Mixin class for representing download characteristics of a smartphone.
    """
    # Завантаження
    instructions: str | None = None
