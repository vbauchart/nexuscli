# swagger_client.ReadonlyApi

All URIs are relative to *https://localhost/service/siesta/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**force_release**](ReadonlyApi.md#force_release) | **POST** /rest/beta/read-only/force-release | Forcibly release read-only
[**freeze**](ReadonlyApi.md#freeze) | **POST** /rest/beta/read-only/freeze | Enable read-only
[**get**](ReadonlyApi.md#get) | **GET** /rest/beta/read-only | Get read-only state
[**release**](ReadonlyApi.md#release) | **POST** /rest/beta/read-only/release | Release read-only


# **force_release**
> force_release()

Forcibly release read-only

Forcibly release read-only status, including System initiated tasks. Warning: may result in data loss.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReadonlyApi()

try: 
    # Forcibly release read-only
    api_instance.force_release()
except ApiException as e:
    print("Exception when calling ReadonlyApi->force_release: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **freeze**
> freeze()

Enable read-only



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReadonlyApi()

try: 
    # Enable read-only
    api_instance.freeze()
except ApiException as e:
    print("Exception when calling ReadonlyApi->freeze: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> ReadOnlyState get()

Get read-only state



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReadonlyApi()

try: 
    # Get read-only state
    api_response = api_instance.get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReadonlyApi->get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ReadOnlyState**](ReadOnlyState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release**
> release()

Release read-only

Release administrator initiated read-only status. Will not release read-only caused by system tasks.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReadonlyApi()

try: 
    # Release read-only
    api_instance.release()
except ApiException as e:
    print("Exception when calling ReadonlyApi->release: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

