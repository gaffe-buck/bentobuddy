
import os
import bpy
import sys
import math
import time
import tempfile
import traceback
import mathutils

from . import utils
#from . import globals

from .presets import skeleton as skel

# ------------------------------------------------------------------------------------------------
# get bone chains
# ------------------------------------------------------------------------------------------------
def get_bone_chains(armature=None):

    armObj = armature

    if armature == None:
        print("rigutils::get_bone_chains - no armature sent")
        return False

    if isinstance(armature, str):
        armObj = bpy.data.objects[armature]

    # Get a list of end bones so I can walk back from them and find their chain length to pelvis.
    end_bones = {}
    for boneObj in armObj.data.bones:
        if len(boneObj.children) > 0:
            next
        bone = boneObj.name
        end_bones[bone] = {}
        count = 1
        chain = []
        boneParent = boneObj.parent
        end_bones[bone]['chain'] = {}
        while boneParent:
            count += 1
            parent = boneParent.name
            end_bones[bone]['chain'][parent] = {"count": count}
            boneParent = boneParent.parent
        end_bones[bone]['total'] = count

    return end_bones

# ------------------------------------------------------------------------------------------------
#
# ------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------
#
# ------------------------------------------------------------------------------------------------













