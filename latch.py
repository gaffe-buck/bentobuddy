
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

import os
import bpy
import sys
import time
import mathutils
from . import rigutils
from . import utils




if 1 == 1:

    props = {}

    
    
    
    props['latch_waiting'] = None






def get_director(object):
    OBJ = object
    if isinstance(object, str):
        OBJ = bpy.data.objects[object]

    
    
    aObj = OBJ.get('bb_latch_actor', None)
    dObj = OBJ.get('bb_latch_director', None)

    
    
    if aObj == None and dObj == None:
        return False

    
    if aObj != None:
        return OBJ

    
    if dObj.name not in bpy.context.scene.objects:
        return False

    
    return dObj













def attach(inRig=None, outRig=None):
    state = utils.get_state()

    
    inrig_layer_state = rigutils.get_layer_state(inRig)
    outrig_layer_state = rigutils.get_layer_state(outRig)

    
    
    for boneObj in  inRig.data.bones:
        boneObj.hide = False
    for boneObj in  outRig.data.bones:
        boneObj.hide = False

    rename_map = outRig['bb_onemap_rename'].to_dict()



    print("returning early for testing")
    return True


    
    rigutils.align_bones(inRig=inRig, outRig=outRig, apply=True)


    

    
    
    

    
    rename_rev = {}
    for bone in rename_map:
        tbone = rename_map[bone]
        rename_rev[tbone] = bone

    
    rigutils.add_controllers(
        source=outRig, target=inRig,
        bone_map=rename_map, constraint="COPY_LOCATION",
        target_space='LOCAL', owner_space='LOCAL_WITH_PARENT',
        influence=1, name="bb_latch_constraints",
        )

    
        
        
        
        

    
    
    rigutils.add_controllers(
        source=outRig, target=inRig,
        bone_map=rename_map, constraint="CHILD_OF",
        target_space='LOCAL', owner_space='LOCAL_WITH_PARENT',
        influence=1, name="bb_latch_constraints",
        location_x=False, location_y=False, location_z=False,
        rotation_x=True, rotation_y=True, rotation_z=True,
        scale_x=False, scale_y=False, scale_z=False,
        )

    utils.set_state(state)
    rigutils.set_layer_state(armature=outRig, state=outrig_layer_state)
    rigutils.set_layer_state(armature=inRig, state=inrig_layer_state)

    return True







