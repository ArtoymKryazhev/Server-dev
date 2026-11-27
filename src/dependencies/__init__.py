from .controllers_dependencies import get_authentication_controller
from .controllers_dependencies import get_authorization_controller
from .controllers_dependencies import get_post_controller
from .controllers_dependencies import get_user_controller

__all__ = [
    'get_authentication_controller',
    'get_authorization_controller',
    'get_post_controller',
    'get_user_controller',
]
