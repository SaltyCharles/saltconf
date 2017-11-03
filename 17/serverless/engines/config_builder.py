# This is a config builder that runs more or less continuously and
# just updates the salt configuration based on what we find in manfiests


import os
import glob
import time
import yaml
import pprint

import logging

# Import Salt modules
# TODO make these avaliable to engines?!
import salt.serializers.yaml

log = logging.getLogger(__name__)

# hardcode manifest dir for demo!
MANIFEST_DIR = '/code'
DEMO_PILLAR = '/srv/pillar/saltconf.sls'

def start():
    while True:
        # Start looking in the manifest directory for manifests
        for fn_ in glob.glob(MANIFEST_DIR + '/*'):
            if os.path.split(fn_)[-1]  == 'manifest.yml':
                try:
                    with open(fn_, 'rb') as fh_:
                        manifest_data = yaml.load(fh_)
                        fh_.close()
                except Exception as exc:
                    log.error('This demo is going quite badly. {0}'.format(exc))

                for faas_func in manifest_data:
                    # Ensure that pillar data is set

                    # Get current pillar data if it exists
                    # TODO hardcoded for demo
                    with open(DEMO_PILLAR, 'w+') as fh_:
                        pillar_data = yaml.load(fh_)
                        for faas_func in manifest_data:
                            if not pillar_data or faas_func not in pillar_data:
                                fh_.write(salt.serializers.yaml.serialize(manifest_data[faas_func]))




        # Hang out and check back every so often
        time.sleep(1)
