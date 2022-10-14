
# Bento Buddy
#
# Copyright (C) 2012 - 2022 - Critters LLC
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




if 1 == 1:

    props = {}

    props["help"] = "https://critters.xyz/help/bentobuddy/puppeteer.html"

    props["master"] = None 




def get_master(armature, report=False):
    OBJ = armature
    if isinstance(armature, str):
        OBJ = bpy.data.objects[armature]

    
    masRig = OBJ.get('bb_puppet_master')
    minions = OBJ.get('bb_puppet_minions')
    if masRig == None and minions == None:
        if report == True:
            print("puppet::get_master reports : not in the set")
        return False
    if masRig != None and minions != None:
        if report == True:
            print("puppet::get_master reports : provided object contains both data sets for master and puppet, this is invalid.")
        return False
    if masRig != None:
        return masRig
    
    if minions != None:
        return OBJ

    if report == True:
        print("puppet::get_master reports : fall-through, this shouldn't happen.")

    return False




