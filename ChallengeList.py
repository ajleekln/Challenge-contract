
import random
import easygui
import os
import time
import Contract as cn
#using composite pattern 
#---------------- Challenge list ----------------
class IChallengeList: # Component
    
    def get_item(self):
        pass
    def get_time_limit(self):
        pass
    def add (self):
        pass
    def remove (self):
        pass
    def get_count(self):
        pass
    
class ChallengeRequirement (IChallengeList): # Leaf
    def __init__(self, name : str, time_limit : int):
        self.name = name
        self.time_limit = time_limit
        self.max_limit = 24 # time in hours
    
    def get_item (self):
        return self.name
    
    def get_time_limit(self):
        return self.time_limit
    
    def get_count(self):
        return 1
    
class Challenge (IChallengeList): # Composite
    def __init__(self, name : str, time_limit : int):
        self.name = name
        self.time_limit = time_limit # time in seconds
        self.challenge_list = set() 
    
    def get_item (self):
        print(self.name)
        for i in self.challenge_list:
            i.get_item()
            
    def get_time_limit(self):
        time_limt = self.time_limit
        for i in self.challenge_list:
            time_limit += i.get_time_limit()
        return time_limit
    
    def get_count(self):
        count = 1 
        for i in self.challenge_list:
            count += i.get_count()
            
        return count
    
    def add (self, chall : IChallengeList):        
        self.challenge_list.add(chall)
        
    def remove(self, chall : IChallengeList):
        self.challenge_list.discard(chall)
 
#---------------- Time ---------------- 
class TimeConversion:
    def seconds_to_minutes(self, time : int):
        return time / 60
    def seconds_to_hours(self, time : int):
        return self.seconds_to_minutes(time) / 60
    def seconds_to_days(self, time : int):
        return self.seconds_to_hours(time) / 24
    
    def minutes_to_seconds(self, time : int):
        return time * 60
    def minutes_to_hours(self, time : int):
        return time / 60
    def mintues_to_days(self, time : int):
        return self.minutes_to_hours(time) / 24
    
    def hours_to_seconds(self, time : int):
        return self.minutes_to_seconds(time) * 60
    def hours_to_minutes(self, time : int):
        return time * 60
    def hours_to_days(self, time : int):
        return self.hours_to_minutes(time) / 24    
    
    def days_to_seconds(self, time : int):
        return self.hours_to_seconds(time) * 24
    def days_to_minutes(self, time : int):
        return self.days_to_hours(time) * 60
    def days_to_hours(self, time : int):
        return time * 24    
    

class Timer:
    def __init__(self, time = None):
        self.__time = time
        self.__counter = 0
        self.__count_down = False
        
    def get_timer(self):
        return self.__time 
    def start_timer(self):
        self.__count_down = True
    def stop_timer(self):
        self.__count_down = False
    def reset(self):
        self.__counter = 0
        self.stop_timer()
    
    def update(self):
        if self.__count_down:
            self.__counter += 1

#---------------- Consequneces ----------------
class Consequence:
    def __init__(self):
        self.__current_consequence = 0
        self.__text = ""
        self.__enabled = False
        
    def disable_wifi(self):
        self.__text = "Disable wifi network"
        if self.__enabled:
            os.system("netsh interface set interface Wi-Fi disabled")
        print("network wifi is now disabled")
        
    def enable_wifi(self):
        os.system("netsh interface set interface Wi-Fi enabled")
        print("network wifi is now enable")
        
    def turn_off_data(self):
        # mobile version 
        pass
    def donate_to(self):
        self.__text = "donate $5 to a charity or savings"
        # UNDERSTAND THAT THIS IS DANGEROUS
        # will use paypall        
        # good for tax breaks
        if self.__enabled:
            print("donate $5 to a charity or savings")
        
    def No_consequence(self):
        # Do nothing 
        self.__text = "Zero consequence"
        if self.__enabled:
            pass
    
    def block_social_media(self):
        # not sure how to go about this
        pass
    
    def enable(self):
        self.__enabled = True
    def disable(self):
        self.__enabled = False
        
    def random_consequence(self):
        selection = random.randint(0,4)
        
        if selection == 1: 
            self.No_consequence()
        elif selection == 2:
            self.disable_wifi()
        elif selection == 3:
            self.donate_to()
        
    
    def update(self):
        pass
    
    
#---------------- Challenge System ----------------
class ChallengeSystem:
    def __init__(self):
        self.challenge_list = Challenge('NAME', 0)
        self.__decline_limit = 3
        self.__current_challenge = None
        self.__points = ScorePoints()
        
    def remove_challenge(self, challenge):
        self.challenge_list.remove(challenge)
    def add_challenge(self, challenge):
        self.challenge_list.add(Challenge)
        
    def add_requirement(self, challenge):
        pass
    
    def assign_consequence(self, challenge : IChallengeList, consequence: Consequence):
        pass
   
    def administer_challenge(self):
        """
        randomly choose a challenge among all set challenges and prepares 
        the request for the user to accept the challenge & consequence
        """
        self.__current_challenge =  None # randomly get challenge
        
    def challenge_request(self):
        """ 
        show gui interface of challenge
            - show available decline limit
            - accept button
            - reject button
        """
        pass
    
    def accept_challenge(self):
        pass
    def decline_challenge(self):
        pass
    def set_decline_limit(self, limit : int):
        self.__decline_limit = limit
    
    def update(self):
        pass
    
class ScorePoints:
    def __init__(self):
        self.__points = 0
    
    def get_points(self):
        return self.__points
    
    def add(self, points : int):
        con = cn.Contract(self)
        # precondition
        con.require("is an integer", isinstance(points, int))
        con.require("positive integer", points >= 0)
        # ---------- implementation ----------
        self.__points += points
        # -------------------------------------
        # postcondition
        con.ensure("points properly adjusted",
                   self.__points == (con.old("self.__points") + points))   
        
    def subtract(self, points : int):
        con = cn.Contract(self)
        # precondition
        con.require("is an integer", isinstance(points, int))
        con.require("positive integer", points >= 0)
        # ---------- implementation ----------
        if points >= self.__points:
            self.__points = 0
        else:
            self.__points -= points
      # -------------------------------------
        # postcondition
        con.ensure("points properly adjusted",
                    con.implies(points >= self.__points, self.__points == 0),
                    con.implies(points < self.__points, self.__points == (con.old("self.__points") - points) ))
class UserInfo:
    
    def __init__(self, firstname : str, lastname : str):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__phone_number = ""
    
    def set_phone_number(self, number : str):
        con = cn.Contract(self)
        con.require("correct format", 
                    len(number) == 10,
                    number.isdigit(),
                    isinstance(number, str))
        
        self.__phone_number = number
    
    def set_name(self, first : str, last : str):
        self.__firstname = first
        self.__lastname = last
        
    def get_firstname(self):
        return self.__firstname
    def get_lastname(self):
        return self.__lastname
    def get_phone_number(self):
        return self.__phone_number
        
"""
Goal & Requirements: 
 To create an mobile app that would ping out mission impossible style challenges personally
 "assigned by the user". 
 
 The user would periodically be assigned missions 'randomly' throughout their preset "challenge
 'time zones'", if the choose to accept it. 
 
 Every challenge will have a 'time limit' and a 'consequence' (upon failure). 
 
 
Design:

--------------------------------------
|                                    |                                      
| CHALLENGE                          |
|                                    |
|                                    |
|   [  PICTURE  ]                    |
|                                    |
|                                    |
|                                    |
|   Description: DO ...              |
|                                    |
|                                    |
|     Failure: ...                   |
|                                    |
|    ...                             |
|                                    |
|                                    |
|     [ACCEPT]   [DECLINE] [limit]   |
|                                    |
|                                    |
|                                    |
--------------------------------------

"""


