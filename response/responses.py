from . import constants

INVALID_ACCESS = {
    "message"   : constants.INVALID_ACCESS,
    "data"      : [],
    "status"    : constants.STATUS_CODE_INVALID_ACCESS
}

SUCCESS_FULL = {
    "message"   : constants.SUCCESSFULL,
    "data"      : [],
    "status"    : constants.STATUS_CODE_SUCCESS
}

SHOW_ERROR_OCCURED = {
    "message"   : constants.SHOW_ERROR_OCCURED,
    "data"      : [],
    "status"    : constants.STATUS_CODE_SHOW_ERROR_OCCURED
}