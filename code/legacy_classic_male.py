
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
# code segment for : Classic (m) Create-A-Mesh (Clothing Edition) A Poses.dkp
import bpy
from . import utils
from . import rigutils
# --------------------------------------------------------------------------------------------
# merge_groups
# --------------------------------------------------------------------------------------------
def merge_groups(group=None, target=None, mesh=None, report=False):
    meshObj = mesh
    if isinstance(mesh, str):
        meshObj = bpy.data.objects[mesh]
    if group not in meshObj.vertex_groups:
        if report == True:
            print("The reskin bone/group doesn't exist in the mesh:", group)
        return False
    if target not in meshObj.vertex_groups:
        meshObj.vertex_groups.new(name=target)
    group_input = {}
    group_input[group] = None
    group_input[target] = None
    temp = utils.get_temp_name()
    while temp in meshObj.vertex_groups:
        temp = utils.get_temp_name()
    vertex_weights = {}
    for vert in meshObj.data.vertices:
        if len(vert.groups):  
            for item in vert.groups:
                vg = meshObj.vertex_groups[item.group]
                if vg.name in group_input:
                    if vert.index in vertex_weights:    
                        vertex_weights[vert.index] += vg.weight(vert.index)
                    else:
                        vertex_weights[vert.index] = vg.weight(vert.index)
    for key in vertex_weights.keys():
        if (vertex_weights[key] > 1.0): vertex_weights[key] = 1.0
    vgroup = meshObj.vertex_groups.new(name=temp)
    for key, value in vertex_weights.items():
        vgroup.add([key], value ,'REPLACE')
    grp_del = meshObj.vertex_groups[group]
    meshObj.vertex_groups.remove(grp_del)
    grp_del = meshObj.vertex_groups[target]
    meshObj.vertex_groups.remove(grp_del)
    meshObj.vertex_groups[temp].name = target
    return True
# --------------------------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------------------------
armObj = utils.has_armature()
if armObj == False:
    print("Devkit code runs but armature is missing, returning without results")
else:
    bad_bones = ['mSpine1', 'mSpine2', 'mSpine3', 'mSpine4']
    group = 'mPelvis'
    mesh_list = rigutils.get_associated_mesh(armObj)
    for meshObj in  mesh_list:
        # Make sure we only record bones we can change and if this list is empty move onto the next mesh.
        qualified = []
        for bone in bad_bones:
            if bone in meshObj.vertex_groups:
                qualified.append(bone)
        if len(qualified) == 0:
            print("Skipping", meshObj.name)
            continue
        print("Processing weights for mesh", meshObj.name)
        for rbone in qualified:
            print("merging", rbone, "to", group)
            merge_groups(group=rbone, target=group, mesh=meshObj, report=True)

print("Code processing exists!")
# --------------------------------------------------------------------------------------------
#
# --------------------------------------------------------------------------------------------
