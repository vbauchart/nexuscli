# coding: utf-8

"""
    Nexus Repository Manager REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 3.7.0-04
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Page(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'items': 'list[object]',
        'continuation_token': 'str'
    }

    attribute_map = {
        'items': 'items',
        'continuation_token': 'continuationToken'
    }

    def __init__(self, items=None, continuation_token=None):
        """
        Page - a model defined in Swagger
        """

        self._items = None
        self._continuation_token = None

        if items is not None:
          self.items = items
        if continuation_token is not None:
          self.continuation_token = continuation_token

    @property
    def items(self):
        """
        Gets the items of this Page.

        :return: The items of this Page.
        :rtype: list[object]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this Page.

        :param items: The items of this Page.
        :type: list[object]
        """

        self._items = items

    @property
    def continuation_token(self):
        """
        Gets the continuation_token of this Page.

        :return: The continuation_token of this Page.
        :rtype: str
        """
        return self._continuation_token

    @continuation_token.setter
    def continuation_token(self, continuation_token):
        """
        Sets the continuation_token of this Page.

        :param continuation_token: The continuation_token of this Page.
        :type: str
        """

        self._continuation_token = continuation_token

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Page):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
