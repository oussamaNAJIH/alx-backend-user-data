#!/usr/bin/env python3
"""
This module for BasicAuth class
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """
    BasicAuth inherits from Auth class
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        returns the Base64 part of the Authorization
        header for a Basic Authentication
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if authorization_header[0: 6] != "Basic ":
            return None
        data_to_encode = (authorization_header[6: ]).encode('utf-8')
        return base64.b64encode(data_to_encode).decode('utf-8')
