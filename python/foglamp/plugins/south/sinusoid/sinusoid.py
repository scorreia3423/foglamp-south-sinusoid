# -*- coding: utf-8 -*-

# FOGLAMP_BEGIN
# See: http://foglamp.readthedocs.io/
# FOGLAMP_END

""" Module for Sinusoid async plugin """

import asyncio
import copy
import uuid
import datetime

from foglamp.common import logger
from foglamp.plugins.common import utils
from foglamp.services.south import exceptions
from foglamp.services.south.ingest import Ingest


__author__ = "Ashish Jabble"
__copyright__ = "Copyright (c) 2018 Dianomic Systems"
__license__ = "Apache 2.0"
__version__ = "${VERSION}"


_DEFAULT_CONFIG = {
    'plugin': {
        'description': 'Sinusoid async plugin',
        'type': 'string',
        'default': 'sinusoid'
    },
    'dataPointsPerSec': {
        'description': 'Data points per second',
        'type': 'integer',
        'default': "1"
    }
}

_LOGGER = logger.setup(__name__, level=20)
index = -1


def plugin_info():
    """ Returns information about the plugin.
    Args:
    Returns:
        dict: plugin information
    Raises:
    """

    return {
        'name': 'Sinusoid plugin',
        'version': '1.0',
        'mode': 'async',
        'type': 'south',
        'interface': '1.0',
        'config': _DEFAULT_CONFIG
    }


def plugin_init(config):
    """ Initialise the plugin.
    Args:
        config: JSON configuration document for the South plugin configuration category
    Returns:
        data: JSON object to be used in future calls to the plugin
    Raises:
    """
    data = copy.deepcopy(config)
    return data


def plugin_start(handle):
    """ Extracts data from the sinusoid and returns it in a JSON document as a Python dict.
    Available for async mode only.

    Args:
        handle: handle returned by the plugin initialisation call
    Returns:
        a sinusoid reading in a JSON document, as a Python dict, if it is available
        None - If no reading is available
    Raises:
        TimeoutError
    """
    pi = [
        0.0,
        0.104528463,
        0.207911691,
        0.309016994,
        0.406736643,
        0.5,
        0.587785252,
        0.669130606,
        0.743144825,
        0.809016994,
        0.866025404,
        0.913545458,
        0.951056516,
        0.978147601,
        0.994521895,
        1.0,
        0.994521895,
        0.978147601,
        0.951056516,
        0.913545458,
        0.866025404,
        0.809016994,
        0.743144825,
        0.669130606,
        0.587785252,
        0.5,
        0.406736643,
        0.309016994,
        0.207911691,
        0.104528463,
        1.22515E-16,
        -0.104528463,
        -0.207911691,
        -0.309016994,
        -0.406736643,
        -0.5,
        -0.587785252,
        -0.669130606,
        -0.743144825,
        -0.809016994,
        -0.866025404,
        -0.913545458,
        -0.951056516,
        -0.978147601,
        -0.994521895,
        -1.0,
        -0.994521895,
        -0.978147601,
        -0.951056516,
        -0.913545458,
        -0.866025404,
        -0.809016994,
        -0.743144825,
        -0.669130606,
        -0.587785252,
        -0.5,
        -0.406736643,
        -0.309016994,
        -0.207911691,
        -0.104528463
    ]

    def generate_data():
        global index
        while index >= -1:
            # index exceeds, reset to default
            if index >= 59:
                index = -1
            index += 1
            yield pi[index]

    async def save_data():
        try:
            while True:
                # TODO: Use utils.local_timestamp() and this will be used once v1.3 debian package release
                # https://github.com/foglamp/FogLAMP/commit/66dead988152cd3724eba6b4288b630cfa6a2e30
                time_stamp = str(datetime.datetime.now(datetime.timezone.utc).astimezone())  # utils.local_timestamp()
                data = {
                    'asset': 'sinusoid',
                    'timestamp': time_stamp,
                    'key': str(uuid.uuid4()),
                    'readings': {
                        "pi": next(generate_data())
                    }
                }

                await Ingest.add_readings(asset='{}'.format(data['asset']),
                                          timestamp=data['timestamp'], key=data['key'],
                                          readings=data['readings'])

                await asyncio.sleep(1/(int(handle['dataPointsPerSec']['value'])))

        except asyncio.CancelledError:
            pass

        except (Exception, RuntimeError) as ex:
            _LOGGER.exception("Sinusoid exception: {}".format(str(ex)))
            raise exceptions.DataRetrievalError(ex)

    asyncio.ensure_future(save_data())


def plugin_reconfigure(handle, new_config):
    """ Reconfigures the plugin

    Args:
        handle: handle returned by the plugin initialisation call
        new_config: JSON object representing the new configuration category for the category
    Returns:
        new_handle: new handle to be used in the future calls
    """
    _LOGGER.info("Old config for sinusoid plugin {} \n new config {}".format(handle, new_config))

    # Find diff between old config and new config
    diff = utils.get_diff(handle, new_config)

    # Plugin should re-initialize and restart if key configuration is changed
    if 'dataPointsPerSec' in diff:
        _plugin_stop(handle)
        new_handle = plugin_init(new_config)
        new_handle['restart'] = 'yes'
        _LOGGER.info("Restarting Sinusoid plugin due to change in configuration key [{}]".format(', '.join(diff)))
    else:
        new_handle = copy.deepcopy(handle)
        new_handle['restart'] = 'no'

    return new_handle


def _plugin_stop(handle):
    """ Stops the plugin doing required cleanup, to be called prior to the South plugin service being shut down.

    Args:
        handle: handle returned by the plugin initialisation call
    Returns:
        None
    """
    _LOGGER.info('sinusoid disconnected.')


def plugin_shutdown(handle):
    """ Shutdowns the plugin doing required cleanup, to be called prior to the South plugin service being shut down.

    Args:
        handle: handle returned by the plugin initialisation call
    Returns:
        plugin stop
    """
    _plugin_stop(handle)
    _LOGGER.info('sinusoid plugin shut down.')
