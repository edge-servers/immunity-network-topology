from immunity_network_topology.tests.test_admin import TestAdmin as BaseTestAdmin
from immunity_network_topology.tests.test_admin import (
    TestMultitenantAdmin as BaseTestMultitenantAdmin,
)
from immunity_network_topology.tests.test_api import TestApi as BaseTestApi
from immunity_network_topology.tests.test_link import TestLink as BaseTestLink
from immunity_network_topology.tests.test_node import TestNode as BaseTestNode
from immunity_network_topology.tests.test_snapshot import (
    TestSnapshot as BaseTestSnapshot,
)
from immunity_network_topology.tests.test_topology import (
    TestTopology as BaseTestTopology,
)
from immunity_network_topology.tests.test_upgrader_script import (
    TestUpgradeFromDjangoNetjsongraph as BaseTestUpgradeFromDjangoNetjsongraph,
)
from immunity_network_topology.tests.test_users_integration import (
    TestUsersIntegration as BaseTestUsersIntegration,
)
from immunity_network_topology.tests.test_utils import TestUtils as BaseTestUtils
from immunity_network_topology.tests.test_visualizer import (
    TestVisualizer as BaseTestVisualizer,
)


class TestAdmin(BaseTestAdmin):
    module = 'immunity2.sample_network_topology'
    app_label = 'sample_network_topology'


class TestMultitenantAdmin(BaseTestMultitenantAdmin):
    app_label = 'sample_network_topology'


class TestApi(BaseTestApi):
    pass


class TestLink(BaseTestLink):
    pass


class TestNode(BaseTestNode):
    pass


class TestTopology(BaseTestTopology):
    pass


class TestUtils(BaseTestUtils):
    pass


class TestVisualizer(BaseTestVisualizer):
    pass


class TestSnapshot(BaseTestSnapshot):
    pass


class TestUpgradeFromDjangoNetjsongraph(BaseTestUpgradeFromDjangoNetjsongraph):
    pass


class TestUsersIntegration(BaseTestUsersIntegration):
    pass


del BaseTestAdmin
del BaseTestMultitenantAdmin
del BaseTestApi
del BaseTestLink
del BaseTestNode
del BaseTestSnapshot
del BaseTestTopology
del BaseTestUtils
del BaseTestVisualizer
del BaseTestUpgradeFromDjangoNetjsongraph
del BaseTestUsersIntegration
