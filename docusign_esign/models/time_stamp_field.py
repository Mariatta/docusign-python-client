# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TimeStampField(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'document_security_store': 'DocumentSecurityStore',
        'max_time_stamp_signature_length': 'str',
        'time_stamp_field_name': 'str'
    }

    attribute_map = {
        'document_security_store': 'documentSecurityStore',
        'max_time_stamp_signature_length': 'maxTimeStampSignatureLength',
        'time_stamp_field_name': 'timeStampFieldName'
    }

    def __init__(self, document_security_store=None, max_time_stamp_signature_length=None, time_stamp_field_name=None):  # noqa: E501
        """TimeStampField - a model defined in Swagger"""  # noqa: E501

        self._document_security_store = None
        self._max_time_stamp_signature_length = None
        self._time_stamp_field_name = None
        self.discriminator = None

        if document_security_store is not None:
            self.document_security_store = document_security_store
        if max_time_stamp_signature_length is not None:
            self.max_time_stamp_signature_length = max_time_stamp_signature_length
        if time_stamp_field_name is not None:
            self.time_stamp_field_name = time_stamp_field_name

    @property
    def document_security_store(self):
        """Gets the document_security_store of this TimeStampField.  # noqa: E501


        :return: The document_security_store of this TimeStampField.  # noqa: E501
        :rtype: DocumentSecurityStore
        """
        return self._document_security_store

    @document_security_store.setter
    def document_security_store(self, document_security_store):
        """Sets the document_security_store of this TimeStampField.


        :param document_security_store: The document_security_store of this TimeStampField.  # noqa: E501
        :type: DocumentSecurityStore
        """

        self._document_security_store = document_security_store

    @property
    def max_time_stamp_signature_length(self):
        """Gets the max_time_stamp_signature_length of this TimeStampField.  # noqa: E501

          # noqa: E501

        :return: The max_time_stamp_signature_length of this TimeStampField.  # noqa: E501
        :rtype: str
        """
        return self._max_time_stamp_signature_length

    @max_time_stamp_signature_length.setter
    def max_time_stamp_signature_length(self, max_time_stamp_signature_length):
        """Sets the max_time_stamp_signature_length of this TimeStampField.

          # noqa: E501

        :param max_time_stamp_signature_length: The max_time_stamp_signature_length of this TimeStampField.  # noqa: E501
        :type: str
        """

        self._max_time_stamp_signature_length = max_time_stamp_signature_length

    @property
    def time_stamp_field_name(self):
        """Gets the time_stamp_field_name of this TimeStampField.  # noqa: E501

          # noqa: E501

        :return: The time_stamp_field_name of this TimeStampField.  # noqa: E501
        :rtype: str
        """
        return self._time_stamp_field_name

    @time_stamp_field_name.setter
    def time_stamp_field_name(self, time_stamp_field_name):
        """Sets the time_stamp_field_name of this TimeStampField.

          # noqa: E501

        :param time_stamp_field_name: The time_stamp_field_name of this TimeStampField.  # noqa: E501
        :type: str
        """

        self._time_stamp_field_name = time_stamp_field_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(TimeStampField, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TimeStampField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
