import pytest
import time
from modpoll.mqtt_task import MqttHandler


def test_mqtt_task_setup():
    mqtt_handler = MqttHandler(
        name="test_mqtt",
        host="mqtt.eclipseprojects.io",
        port=1883,
        user=None,
        password=None,
        clientid="test_client",
        qos=0,
        subscribe_topics=["test/topic"],
    )

    assert mqtt_handler.setup()

    # Test MQTT client properties
    assert mqtt_handler.mqtt_client is not None
    assert mqtt_handler.host == "mqtt.eclipseprojects.io"
    assert mqtt_handler.port == 1883

    # Clean up
    mqtt_handler.close()


@pytest.mark.integration
def test_mqtt_task_connect():
    mqtt_handler = MqttHandler(
        name="test_mqtt",
        host="mqtt.eclipseprojects.io",
        port=1883,
        user=None,
        password=None,
        clientid="test_client",
        qos=0,
    )

    assert mqtt_handler.setup()
    assert mqtt_handler.connect()

    # Add a short delay to allow the connection to establish
    time.sleep(1)

    # Test connection
    assert mqtt_handler.is_connected()

    # Clean up
    mqtt_handler.close()
