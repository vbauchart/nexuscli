#!/usr/bin/python

from __future__ import print_function
import time
import nexuscli
from nexuscli.rest import ApiException
from pprint import pprint
import re
import os
import urllib3
import argparse


def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--repo", help="Repository ID", action="store")
    parser.add_argument("-c", "--component", help="Component name", action="store")
    parser.add_argument("-l", "--list-assets", help="list assets", action="store_true")
    parser.add_argument("-k", "--insecure", help="Allow connect on untrusted CA", action="store_true")
    parser.add_argument("-v", "--verbose", help="Be verbose", action="store_true")
    parser.add_argument("-d", "--delete-pattern",
                help="Delete assets with TAG matching pattern (regex)", action="store")
    parser.add_argument("-n", "--dry-run", help="Do nothing, just print",
            action="store_true")
    args = parser.parse_args()

    if args.insecure:
        nexuscli.configuration.verify_ssl = False
        urllib3.disable_warnings()

    nexuscli.configuration.host = os.environ['REGISTRY_URL'] + '/service/siesta'
    nexuscli.configuration.username = os.environ['REGISTRY_USERNAME']
    nexuscli.configuration.password = os.environ['REGISTRY_PASSWORD']
    nexuscli.configuration.debug = args.verbose

    print_list = args.list_assets
    dry_run = args.dry_run
    repo_id = args.repo
    component_name = args.component
    delete_pattern = args.delete_pattern


    search_api = nexuscli.SearchApi()

    search_args = { 'format': 'docker'}
    if repo_id:
        search_args['repository'] = repo_id
    if component_name:
        search_args['name'] = component_name

    try:
            assets=search_api.search_assets(**search_args)
    except ApiException as e:
            print("Exception when calling get_components %s\n" % e)
            exit(1)

    if assets.continuation_token:
        raise Exception('list too long (continuationToken not implemented yet)')

    asset_api = nexuscli.AssetsApi()
    for asset in assets.items:

        re_name_tag=re.compile('^v2/(.+)/manifests/(.+)$')
        result_sre=re_name_tag.match(asset.path)
        if not result_sre:
            continue

        result=result_sre.groups()
        if len(result) != 2:
            raise Exception('Unable to parse asset path %s'%asset.path)
        name=result[0]
        tag=result[1]

        if print_list:
            print('%s:%s'%(name,tag))

        if delete_pattern:
            re_is_branch = re.compile(delete_pattern)
            if re_is_branch.search(tag):
                print('DELETE asset : %s'%asset.path)
                if not dry_run:
                    try:
                        asset_api.delete_asset(asset.id)
                    except ApiException as e:
                        print('Exception when calling delete :%s'%e)


if __name__ == "__main__":
    main()
