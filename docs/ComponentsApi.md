# nexuscli.ComponentsApi

All URIs are relative to *https://localhost/service/siesta/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_component**](ComponentsApi.md#delete_component) | **DELETE** /rest/beta/components/{id} | Delete a single component
[**get_component_by_id**](ComponentsApi.md#get_component_by_id) | **GET** /rest/beta/components/{id} | Get a single component
[**get_components**](ComponentsApi.md#get_components) | **GET** /rest/beta/components | List components


# **delete_component**
> delete_component(id)

Delete a single component



### Example 
```python
from __future__ import print_function
import time
import nexuscli
from nexuscli.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
nexuscli.configuration.username = 'YOUR_USERNAME'
nexuscli.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = nexuscli.ComponentsApi()
id = 'id_example' # str | ID of the component to delete

try: 
    # Delete a single component
    api_instance.delete_component(id)
except ApiException as e:
    print("Exception when calling ComponentsApi->delete_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the component to delete | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_component_by_id**
> ComponentXO get_component_by_id(id)

Get a single component



### Example 
```python
from __future__ import print_function
import time
import nexuscli
from nexuscli.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
nexuscli.configuration.username = 'YOUR_USERNAME'
nexuscli.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = nexuscli.ComponentsApi()
id = 'id_example' # str | ID of the component to retrieve

try: 
    # Get a single component
    api_response = api_instance.get_component_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->get_component_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the component to retrieve | 

### Return type

[**ComponentXO**](ComponentXO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_components**
> PageComponentXO get_components(repository_id, continuation_token=continuation_token)

List components



### Example 
```python
from __future__ import print_function
import time
import nexuscli
from nexuscli.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
nexuscli.configuration.username = 'YOUR_USERNAME'
nexuscli.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = nexuscli.ComponentsApi()
repository_id = 'repository_id_example' # str | ID of the repository from which you would like to retrieve components
continuation_token = 'continuation_token_example' # str | A token returned by a prior request. If present, the next page of results are returned (optional)

try: 
    # List components
    api_response = api_instance.get_components(repository_id, continuation_token=continuation_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->get_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| ID of the repository from which you would like to retrieve components | 
 **continuation_token** | **str**| A token returned by a prior request. If present, the next page of results are returned | [optional] 

### Return type

[**PageComponentXO**](PageComponentXO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

