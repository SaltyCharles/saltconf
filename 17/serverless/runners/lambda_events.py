'''
Runner Module for Lambda hack
'''


from __future__ import absolute_import

import logging
import salt.client
import salt.utils.master
import random


log = logging.getLogger(__name__)


def __virtual__():
    return 'lambda_events'


def _get_lambda_host():
    # Get a list of available docker hosts from salt-mine
    # Randomly select one of them

    # Search for all nodes with grain lambda = True

    tgt = 'lambda:True'
    expr_form = 'grain'

    pillar_util = salt.utils.master.MasterPillarUtil(
        tgt,
        expr_form,
        use_cached_grains=True,
        grains_fallback=False,
        opts=__opts__)

    cached_grains = pillar_util.get_minion_grains()
    lambdahosts = cached_grains.keys()

    return random.choice(lambdahosts)


def http_keyword_ingress(http_keyword, func_to_run, lang='python'):

    lambdahost = _get_lambda_host()
    args = []
    salt_cmd = 'cmd.run'
    args.append('docker run -v /code:/code saltme/lambda:v2 {lang} {func_to_run} {http_keyword}'.format(
        http_keyword=http_keyword, lang=lang, func_to_run=func_to_run))
    local = salt.client.get_local_client(__opts__['conf_file'])

    cmdret = local.cmd('{0}'.format(lambdahost), salt_cmd, args)
    ret = {
        "lambdahost": lambdahost,
        "keyword": http_keyword,
        "url": cmdret[lambdahost]
    }

    return ret

# Currently unused
def update_giphy(keyword):

    ret = giphyget(keyword)

    fun = 'state.sls'
    tgt = 'saltmaster'
    expr_form = 'glob'

    arg = ['updatewebpage']
    kwarg = {"pillar": ret}
    local = salt.client.LocalClient()
    #local = salt.client.get_local_client(__opts__['conf_file'])
    cmdret = local.cmd(tgt, expr_form, fun, arg, kwarg)

    return True
