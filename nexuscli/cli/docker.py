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

def yes_or_no(question):
    while "the answer is invalid":
        reply = str(raw_input(question+' (y/n): ')).lower().strip()
        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            return False

def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--repo", help="Repository ID", action="store")
    parser.add_argument("-b", "--bin-format", help="binary format (docker,maven2,raw,pypi,...)", action="store")
    parser.add_argument("-c", "--component", help="Component name", action="store")
    parser.add_argument("-p", "--path", help="Path of component", action="store")
    parser.add_argument("-f", "--filter", help="REGEX filter on 'name:tag'", action="store")
    parser.add_argument("-k", "--insecure", help="Allow connect on untrusted CA", action="store_true")
    parser.add_argument("-v", "--verbose", help="Be verbose", action="store_true")
    parser.add_argument("-y", "--yes", help="Assume yes to all questions", action="store_true")
    parser.add_argument("action", help="list,delete", action="store")
    args = parser.parse_args()

    if args.insecure:
        nexuscli.configuration.verify_ssl = False
        urllib3.disable_warnings()

    nexuscli.configuration.host = os.environ['REGISTRY_URL'] + '/service/siesta'
    nexuscli.configuration.username = os.environ['REGISTRY_USERNAME']
    nexuscli.configuration.password = os.environ['REGISTRY_PASSWORD']
    nexuscli.configuration.debug = args.verbose


    if args.action not in ['list','delete','noop']:
        parser.print_help()

    action = args.action
    repo_id = args.repo
    component_name = args.component
    filter_pattern = args.filter
    binary_format = args.bin_format
    component_path = args.path
    ask_confirmation = not args.yes

    search_api = nexuscli.SearchApi()

    search_args = {}
    if binary_format:
        search_args['format'] = binary_format
    if repo_id:
        search_args['repository'] = repo_id
    if component_name:
        search_args['name'] = component_name

    if not yes_or_no('This will destory selected images on repository, are you sure?'):
        print('bye bye')
        exit(1)

    items = []
    try:
        while True:
            assets=search_api.search_assets(**search_args)
            items += assets.items
            if assets.continuation_token is None:
                break
            search_args['continuation_token'] = assets.continuation_token

    except ApiException as e:
        print("Exception when calling get_components %s\n" % e)
        exit(1)


    asset_api = nexuscli.AssetsApi()
    re_filter = re.compile(filter_pattern)
    for asset in items:

        if filter_pattern:
            result_filter = re_filter.search(asset.path)
            if not result_filter:
                continue

        if action == 'list':
            print(asset.path)
        elif action == 'delete':
            try:
                asset_api.delete_asset(asset.id)
            except ApiException as e:
                print('Exception when calling delete :%s'%e)


if __name__ == "__main__":
    main()
