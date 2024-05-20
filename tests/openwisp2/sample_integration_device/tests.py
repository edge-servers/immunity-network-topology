import swapper

from immunity_network_topology.integrations.device.tests.test_integration import (
    TestAdmin as BaseTestAdmin,
)
from immunity_network_topology.integrations.device.tests.test_integration import (
    TestControllerIntegration as BaseTestControllerIntegration,
)
from immunity_network_topology.integrations.device.tests.test_integration import (
    TestMonitoringIntegration as BaseTestMonitoringIntegration,
)

DeviceNode = swapper.load_model('topology_device', 'DeviceNode')


class TestControllerIntegration(BaseTestControllerIntegration):
    def test_device_node_custom(self):
        self.assertTrue(DeviceNode().is_test)


class TestMonitoringIntegration(BaseTestMonitoringIntegration):
    pass


class TestAdmin(BaseTestAdmin):
    module = 'immunity2.sample_network_topology'
    app_label = 'sample_network_topology'


del BaseTestControllerIntegration
del BaseTestMonitoringIntegration
del BaseTestAdmin
