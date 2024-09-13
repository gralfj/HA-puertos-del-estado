# Home Assistant Sensor for Puertos del Estado Open Data

This Home Assistant custom component allows you to integrate the open data from **Puertos del Estado** into your Home Assistant instance as sensors. You can monitor maritime and oceanographic conditions, such as tides, waves, and meteorological data, directly from the official data provided by **Puertos del Estado**.

## Features
- Real-time data from Puertos del Estado open data API.
- Integration with Home Assistant sensors.
- Monitor maritime conditions including tides, wave height, and wind speed.

## Installation

1. Clone this repository or download the ZIP file and extract it into the `custom_components` directory of your Home Assistant configuration.

    ```bash
    git clone https://github.com/yourusername/ha-puertos-del-estado.git
    ```

    Your Home Assistant configuration directory should look like this:

    ```
    └── custom_components
        └── puertos_del_estado
            ├── __init__.py
            ├── manifest.json
            └── sensor.py
    ```

2. Add the sensor platform to your `configuration.yaml`:

    ```yaml
    sensor:
      - platform: puertos_del_estado
    ```

3. Restart Home Assistant.

## Configuration

- **API_URL**: You will need to configure the API endpoint that you want to use from Puertos del Estado.
- The sensor will automatically update with the latest available data from the API.

## Usage

Once installed and configured, new sensors will be available in Home Assistant that provide live data for the configured ports or maritime areas. These can be used in automations, dashboards, and monitoring systems.

## Example

Here is an example of the sensor showing **wave height** from a port:

```yaml
sensor:
  - platform: puertos_del_estado
    name: "Wave Height Sensor"
    unit_of_measurement: "m"
