import requests
import logging
import json
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import TEMP_CELSIUS

_LOGGER = logging.getLogger(__name__)

# API URL de Puertos del Estado (reemplaza con el endpoint correcto)
API_URL = "https://puertos.es/api_endpoint"  # Ejemplo

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Configura la plataforma del sensor."""
    add_entities([PuertosDelEstadoSensor()])

class PuertosDelEstadoSensor(SensorEntity):
    """Representa un sensor que recoge datos de Puertos del Estado."""

    def __init__(self):
        """Inicializa el sensor."""
        self._state = None
        self.update()

    @property
    def name(self):
        """Devuelve el nombre del sensor."""
        return "Puertos del Estado Data"

    @property
    def state(self):
        """Devuelve el estado actual del sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Devuelve la unidad de medida."""
        return "m"  # Ejemplo: metros para la altura de las olas

    def update(self):
        """Actualiza el estado del sensor con datos de la API."""
        try:
            response = requests.get(API_URL)
            response.raise_for_status()
            data = response.json()

            # Extrae los datos necesarios (ejemplo: altura de las olas)
            self._state = data.get("valor")  # Ajusta según la estructura de la API

        except requests.exceptions.RequestException as e:
            _LOGGER.error(f"Error al obtener datos de Puertos del Estado: {e}")
            self._state = None
