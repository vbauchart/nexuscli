# nexuscli.ScriptApi

All URIs are relative to *https://localhost/service/siesta/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add**](ScriptApi.md#add) | **POST** /rest/v1/script | Add a new script
[**browse**](ScriptApi.md#browse) | **GET** /rest/v1/script | List all stored scripts
[**delete**](ScriptApi.md#delete) | **DELETE** /rest/v1/script/{name} | Delete stored script by name
[**edit**](ScriptApi.md#edit) | **PUT** /rest/v1/script/{name} | Update stored script by name
[**read**](ScriptApi.md#read) | **GET** /rest/v1/script/{name} | Read stored script by name
[**run1**](ScriptApi.md#run1) | **POST** /rest/v1/script/{name}/run | Run stored script by name


# **add**
> add(body=body)

Add a new script



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
api_instance = nexuscli.ScriptApi()
body = nexuscli.ScriptXO() # ScriptXO |  (optional)

try: 
    # Add a new script
    api_instance.add(body=body)
except ApiException as e:
    print("Exception when calling ScriptApi->add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScriptXO**](ScriptXO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **browse**
> list[ScriptXO] browse()

List all stored scripts



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
api_instance = nexuscli.ScriptApi()

try: 
    # List all stored scripts
    api_response = api_instance.browse()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScriptApi->browse: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ScriptXO]**](ScriptXO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(name)

Delete stored script by name



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
api_instance = nexuscli.ScriptApi()
name = 'name_example' # str | 

try: 
    # Delete stored script by name
    api_instance.delete(name)
except ApiException as e:
    print("Exception when calling ScriptApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit**
> edit(name, body=body)

Update stored script by name



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
api_instance = nexuscli.ScriptApi()
name = 'name_example' # str | 
body = nexuscli.ScriptXO() # ScriptXO |  (optional)

try: 
    # Update stored script by name
    api_instance.edit(name, body=body)
except ApiException as e:
    print("Exception when calling ScriptApi->edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **body** | [**ScriptXO**](ScriptXO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read**
> ScriptXO read(name)

Read stored script by name



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
api_instance = nexuscli.ScriptApi()
name = 'name_example' # str | 

try: 
    # Read stored script by name
    api_response = api_instance.read(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScriptApi->read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**ScriptXO**](ScriptXO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run1**
> ScriptResultXO run1(name, body=body)

Run stored script by name



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
api_instance = nexuscli.ScriptApi()
name = 'name_example' # str | 
body = 'body_example' # str |  (optional)

try: 
    # Run stored script by name
    api_response = api_instance.run1(name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScriptApi->run1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

[**ScriptResultXO**](ScriptResultXO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

