# Contracts
"""
inspired by EIFFEL PROGRAMMING LANGUAGE design by contract
"""
import copy
import inspect
import ErrorExceptions as err
class Contract (object):
    def __init__(self, a_class):
        self.__old_used = False
        self.__class_instance = copy.deepcopy(a_class)
        self.__old_variables = [value for value in vars(self.__class_instance).items()]
        self.__is_require = False
        self.__is_ensure = False
        
    def __var_str (self, var):
        v = str(var)
        v_name = str(self.__class_instance.__class__.__name__)
        
        return "self." + v.replace(" "+ v_name, "")
    
    def old (self, var):
        # var = string representation of variable wanted

        self.__old_used = True
        

        if type(var) is not str:
            name_error = True
            raise err.invalid_variable_type("type(var) must be of type String, type(var) is invalid type {}, ".format(type(var)))
        
        
        # searching for variable with name of 'var'
        for name in range(len(self.__old_variables)):
            if self.__var_str(self.__old_variables[name][0]) == var:
                return self.__old_variables[name][1]
        
        raise err.variable_not_found("ERROR '" + str(var) + "' not found")
    
    def implies (self, p, q):
        if p and not q:
            return False
        return True
    
    
    def require (self, name, *conditions):

        self.__is_require = True
        
        # ensure is referenced before require 
        if self.__is_ensure:
            raise err.ensure_referenced_before_require("Postcondition (ensure) cannot be referenced before precondition (require)")
        
        if type(name) is not str:
            name_error = True
            raise err.invalid_name_type("Error - type(name) must be of type String, type(name) is invalid type {}, ".format(type(name)))
        
        elif self.__old_used:
            #print ("Error - old variables cannot be used in - require")
            raise err.old_reference_in_precondition("Error - old variables cannot be used in - require")
        else:
            out = True
            
            for cond in conditions:
                out = out and cond 
                
                if not out :
                    raise err.contract_error_precondition("CONTRACT ERROR ({}) - require".format(name))
                else:
                    return out
    def ensure (self, name, *conditions):
        self.__is_ensure = True         
        
        
        if type(name) is not str:
            raise err.invalid_name_type("Error - type(name) must be of type String, type(name) is invalid type {}, ".format(type(name)))
            
        out = True
        for cond in conditions:
            out = out and cond
            
        if not out:
            raise err.contract_error_postcondition("CONTRACT ERROR ({}) - ensure".format(name))
        else: 
            return out
        
        
    
#Testing Contract

class Dummy (object):
    def __init__(self):
        self.__x = 5
        self.__y = 5
        
        self.row = 6
        self.col = 6
        
        self.name = "dummy"
        self.name2 = "dummy"
        
    def set_row (self, r):
        con = Contract(self)
        con.require ("not negative",
                     r > 0)
        self.row = r
        
        con.ensure ("valid output", 
                    self.row == r)
        
    def get_wrong_row (self):
        con = Contract(self)

        self.row += 1
 
        con.ensure ("unchanged output",
                    con.old("self.row") == self.row)
"""
dummy = Dummy()

dummy.set_row(2)
dummy.set_row(-1)
print ("--- BREAK POINT ---")
dummy.get_wrong_row()
"""