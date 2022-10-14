
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
from . import mod_settings
from .mod_settings import *



















def get_fcurve_data(armature):

    armObj = bpy.data.objects[armature]
    actionObj = armObj.animation_data.action
    fcurves = actionObj.fcurves

    
    
    
    
    
    
    
    fcurve_paths = {}
    for boneObj in armObj.data.bones:
        path_key = 'pose.bones["' + boneObj.name + '"]'
        fcurve_paths[path_key] = boneObj.name

    
    frame_data = {}

    
    
    
    
    for fc in fcurves:
        
        
        dp, i = fc.data_path, fc.array_index

        
        
        bone_path, delimiter, transform_type = dp.rpartition('.')

        
        
        if bone_path not in fcurve_paths:
            continue

        
        
        
        real_bone = fcurve_paths[bone_path]

        
        rot_mode = armObj.pose.bones[real_bone].rotation_mode

        
        
        
        

        
        

        if transform_type == 'rotation_quaternion' and rot_mode == 'QUATERNION':
            loc_rot = 'rot'
        elif transform_type == 'rotation_euler' and rot_mode != 'QUATERNION':
            loc_rot = 'rot'
        elif transform_type == 'location':
            loc_rot = 'loc'
        else:
            if bb_settings['debug'] == True:
                print("incompatible transform type:", transform_type, rot_mode)
            continue

        
        if real_bone not in frame_data:
            frame_data[real_bone] = {}
        if 'rot' not in frame_data[real_bone]: frame_data[real_bone]['rot'] = {}
        if 'loc' not in frame_data[real_bone]: frame_data[real_bone]['loc'] = {}

        
        
        if loc_rot not in frame_data[real_bone]:
            frame_data[real_bone][loc_rot] = {}

        
        
        for kfp in fc.keyframe_points:

            kfp_interpolation = kfp.interpolation
            kfp_easing = kfp.easing
            kfp_frame = int(kfp.co[0])
            kfp_value = kfp.co[1]

            frame_data[real_bone][loc_rot][kfp_frame] = {
                "value": kfp_value,
                "easing": kfp_easing,
                "interpolation": kfp_interpolation,
            }

    return frame_data







def set_interpolation(armature="", mode="BEZIER"):
    armObj = bpy.data.objects[armature]
    actionObj = armObj.animation_data.action
    fcurves = actionObj.fcurves

    pose_paths = {}
    for boneObj in bpy.context.selected_pose_bones:
        path_key = 'pose.bones["' + boneObj.name + '"]'
        pose_paths[path_key] = boneObj.name

    found = False

    for fc in fcurves:
        dp, i = fc.data_path, fc.array_index
        bone_path, delimiter, transform_type = dp.rpartition('.')
        if bone_path in pose_paths:
            found = True
            
            for kfp in fc.keyframe_points:
                kfp.interpolation = mode
                
                
                

    return found









