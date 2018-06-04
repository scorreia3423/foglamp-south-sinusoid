# -*- coding: utf-8 -*-

# FOGLAMP_BEGIN
# See: http://foglamp.readthedocs.io/
# FOGLAMP_END

import pytest

from foglamp.plugins.south.sinusoid import sinusoid

__author__ = "Ashish Jabble"
__copyright__ = "Copyright (c) 2017 OSIsoft, LLC"
__license__ = "Apache 2.0"
__version__ = "${VERSION}"


def test_plugin_info():
    assert sinusoid.plugin_info() == {
        'name': 'Sinusoid plugin',
        'version': '1.0',
        'mode': 'async',
        'type': 'south',
        'interface': '1.0',
        'config': sinusoid._DEFAULT_CONFIG
    }


@pytest.mark.skip(reason="To be implemented")
def test_plugin_init():
    pass


@pytest.mark.skip(reason="To be implemented")
def test_plugin_start():
    pass


@pytest.mark.skip(reason="To be implemented")
def test_plugin_reconfigure():
    pass


@pytest.mark.skip(reason="To be implemented")
def test_plugin_stop():
    pass


@pytest.mark.skip(reason="To be implemented")
def test_plugin_shutdown():
    pass
