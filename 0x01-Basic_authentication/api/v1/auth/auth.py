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
        return False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        return None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        return None
        """
        return None
