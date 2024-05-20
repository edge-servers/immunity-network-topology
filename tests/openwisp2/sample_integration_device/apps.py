from immunity_network_topology.integrations.device.apps import (
    ImmunityTopologyDeviceConfig as BaseAppConfig,
)


class ImmunityTopologyDeviceConfig(BaseAppConfig):
    name = 'immunity2.sample_integration_device'
    label = 'sample_integration_device'


del BaseAppConfig
