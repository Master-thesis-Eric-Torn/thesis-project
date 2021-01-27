# realtimeTibber
Get real time data from a Tibber Pulse sensor.

```python
# initialize sensor:
sensor = realTimeTibberSensor(home)
# Start real time subscriptionm, and provide a callback to deal with the data:
sensor.start_rt_subscription(callback)
```

## Usage example:
```python
import tibber
from realtimeTibber import realTimeTibberSensor

APIkey = 'your-tibber-key'
tibber_connection = tibber.Tibber(APIkey)
tibber_connection.sync_update_info()

home = tibber_connection.get_homes()[0]
home.sync_update_info()

# Callback for the real-time data updates
def callback(liveMeasurement):
        print("----")
        print(liveMeasurement)

# If the home has a real-time sensor
if home.has_real_time_consumption:
    sensor = realTimeTibberSensor(home)
    sensor.start_rt_subscription(callback)

tibber_connection.sync_close_connection()
```