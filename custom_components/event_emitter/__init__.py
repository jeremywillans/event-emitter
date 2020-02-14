""" Event Emmitter """
import logging

_LOGGER = logging.getLogger(__name__)

DOMAIN = "event_emitter"

def setup(hass, config):
    """Set up is called when Home Assistant is loading our component."""

    event_emitter = EventEmitter(hass)
    hass.services.register(DOMAIN, "call", event_emitter.call)

    _LOGGER.debug("Started Event Emitter")

    return True


class EventEmitter(object):
    """Emits a call-service event."""

    def __init__(self, hass):
        """Initialize the data object."""
        self.hass = hass

    def call(self, call):
        """Handle the service call."""