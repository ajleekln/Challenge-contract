# Errors

# Contract Errors
class invalid_variable_type(Exception):
    """ name type must be of type String """
    pass  
class variable_not_found(Exception):
    """variable must be within old version of class"""
    pass
class old_reference_in_precondition(Exception):
    """ old variable cannot be used in precondition (require)"""
    pass        
class invalid_name_type(Exception):
    """ name type must be of type String """
    pass        
class contract_error_precondition(Exception):
    """ precondition contract is not satisfied"""
    pass        
class ensure_referenced_before_require(Exception):
    """ postcondition cannot be called before precondition"""
    pass
class contract_error_postcondition(Exception):
    """ postcondition contract is not satisfied"""
    pass    

# Map Errors
class NotInMapError(Exception):
    """ Entity is not in the map"""
    pass