# swagger_client.AssetsApi

All URIs are relative to *https://localhost/service/siesta/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_asset**](AssetsApi.md#delete_asset) | **DELETE** /rest/beta/assets/{id} | Delete a single asset
[**get_asset_by_id**](AssetsApi.md#get_asset_by_id) | **GET** /rest/beta/assets/{id} | Get a single asset
[**get_assets**](AssetsApi.md#get_assets) | **GET** /rest/beta/assets | List assets


# **delete_asset**
> delete_asset(id)

Delete a single asset



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
id = 'id_example' # str | Id of the asset to delete

try: 
    # Delete a single asset
    api_instance.delete_asset(id)
except ApiException as e:
    print("Exception when calling AssetsApi->delete_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the asset to delete | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_by_id**
> AssetXO get_asset_by_id(id)

Get a single asset



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
id = 'id_example' # str | Id of the asset to get

try: 
    # Get a single asset
    api_response = api_instance.get_asset_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->get_asset_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the asset to get | 

### Return type

[**AssetXO**](AssetXO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assets**
> PageAssetXO get_assets(repository_id, continuation_token=continuation_token)

List assets



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
repository_id = 'repository_id_example' # str | ID of the repository from which you would like to retrieve assets.
continuation_token = 'continuation_token_example' # str | A token returned by a prior request. If present, the next page of results are returned (optional)

try: 
    # List assets
    api_response = api_instance.get_assets(repository_id, continuation_token=continuation_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->get_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| ID of the repository from which you would like to retrieve assets. | 
 **continuation_token** | **str**| A token returned by a prior request. If present, the next page of results are returned | [optional] 

### Return type

[**PageAssetXO**](PageAssetXO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

