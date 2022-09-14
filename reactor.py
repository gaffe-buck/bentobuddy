
# Bento Buddy
#
# Copyright (C) 2012 - 2022 - Critters
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/ .



import bpy
import traceback
import mathutils

print("-----------------")
print("reactor.py loaded")
print("-----------------")





if 1 == 1:

    props = {}

    
    props["help"] = "http://critters.xyz/help/bentobuddy/reactor.html"

    
    props['poll_enabled'] = False
    props['poll_time'] = 0.2



def poll():
    print("reactor::poll :", props['poll_time'])
    if props['poll_enabled'] == True:
        return props['poll_time']
    return None



def get_director(armature):
    pass
    return True











def deposit(source=None, target=None):
    print("deposit code commented out")
































def follow(source=None, target=None):
    print("follow code commented out")
    path_to = {}
    frame_show_1 = 0
    frame_show_2 = 0



























    path_to['correction'] = True
    path_to['display_start'] = frame_show_1
    path_to['display_end'] = frame_show_2


    return True






def repeat(source=None, frames=[]):
    print("repeat code commented out")

    frame_results = {}

















    return frame_results







def projection(path_obj=None, target=None):





























































    return True








