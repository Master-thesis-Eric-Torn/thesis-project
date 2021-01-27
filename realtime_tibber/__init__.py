import tibber
import asyncio
import logging

_LOGGER = logging.getLogger(__name__)
POWER_WATT = "Watt" # Unsure

class realTimeTibberSensor:
  """Representation of a Tibber sensor for real time consumption."""

  def __init__(self, tibber_home):
    self.home = tibber_home
    self._last_updated = None
    self._power_state = None
    self._is_available = False
    self._device_state_attributes = {}
    self._name = tibber_home.info["viewer"]["home"]["appNickname"]
    if self._name is None:
        self._name = tibber_home.info["viewer"]["home"]["address"].get(
            "address1", ""
        )

  def start_rt_subscription(self, callback):
    self._callback = callback
    loop = asyncio.get_event_loop()
    loop.create_task(self.home.rt_subscribe(loop, self._async_callback))
    loop.run_forever()

  async def _async_callback(self, payload=None):
    """Handle received data, then pass to passed callback function"""
    errors = payload.get("errors")
    if errors:
        _LOGGER.error(errors[0])
        return
    data = payload.get("data")
    if data is None:
        return
    live_measurement = data.get("liveMeasurement")
    if live_measurement is None:
        return

    self._power_state = live_measurement["power"]
    for key, value in live_measurement.items():
        if value is None:
            continue
        self._device_state_attributes[key] = value

    # Pass live_measurement to the provided callback function
    self._callback(live_measurement)

  @property
  def device_state_attributes(self):
      """Return the state attributes."""
      return self._device_state_attributes

  @property
  def power_state(self):
      """Return the power state of the device."""
      return self._power_state

  @property
  def available(self):
      """Return True if entity is available."""
      return self._tibber_home.rt_subscription_running

  @property
  def name(self):
      """Return the name of the sensor."""
      return f"Real time consumption {self._name}"

  @property
  def device_id(self):
      """Return the ID of the physical device this sensor is part of."""
      home = self._tibber_home.info["viewer"]["home"]
      return home["meteringPointData"]["consumptionEan"]

  @property
  def unit_of_measurement(self):
      """Return the unit of measurement of this entity."""
      return POWER_WATT
  