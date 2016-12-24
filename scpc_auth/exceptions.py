from scpc_core.exceptions import SystemException


class EmailAlreadyRegisteredException(SystemException):
    code = 'email_already_registered'
