#!/usr/bin/python

from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import re


search_api = swagger_client.SearchApi()
asset_api = swagger_client.AssetsApi()
repo_id = 'app-docker'
#component_name ='database'
component_name = None

try:
        # Delete a single asset
        assets=search_api.search_assets(repository=repo_id)
except ApiException as e:
        print("Exception when calling get_components %s\n" % e)

if assets.continuation_token is not None:
    raise Exception('continuationToken is not supported yet')

for asset in assets.items:
    result=re.compile('^v2/(.+)/manifests/(.+)$').match(asset.path).groups()
    if len(result) != 2:
        raise Exception('Unable to parse asset path')
    name=result[0]
    tag=result[1]
    #print("%s:%s"%(name, tag))

    is_branch = re.compile('^\d+-\w+')
    if is_branch.match(tag):
        try:
            print('FOUND asset : %s'%asset.path)
            #asset_api.delete_asset(asset.id)
        except ApiException as e:
            print('Exception when calling delete :%s'%e)



