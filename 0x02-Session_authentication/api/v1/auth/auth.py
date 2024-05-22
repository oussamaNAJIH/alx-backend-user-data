#!/usr/bin/env python3
"""
This module for Auth class
"""
from flask import request
from typing import List, TypeVar
from api.v1.views.users import User


class Auth():
    """
    class Auth
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check if authentication is required for the given path.
        Returns True if path is None or excluded_paths is None or empty.
        Returns False if path is in excluded_paths or if path+"/"
        is in excluded_paths.
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path in excluded_paths or f"{path}/" in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Return the Authorization header value from the request.
        Returns None if request is None or if the Authorization header
        is not present.
        Otherwise, returns the value of the Authorization header.
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """
        return None
        """
        return None

    def session_cookie(self, request=None):
        """
        returns a cookie value from a request
        """
        if request is None:
            return None
        return request.cookies.get('_my_session_id')
