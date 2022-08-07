#====================== BEGIN GPL LICENSE BLOCK ======================
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#======================= END GPL LICENSE BLOCK ========================

from mathutils import *
from bpy.props import *
import bpy
import bmesh
import os
import math
import sys

# Version history
# 1.0.0 - 2022-02-13: Original version.
# 1.0.1 - 2022-04-26: Changed the 3D Viewport tab to "View" -- I had too many tabs to deal with.
# 1.0.2 - 2022-08-07: Misc formatting cleanup before uploading to GitHub.

###############################################################################
SCRIPT_NAME = 'camera_positions'

# Provides the ability to store five camera positions and recall them with a single button click.
#
###############################################################################

bl_info = {
    "name": "Camera Positions",
    "author": "Jeff Boller",
    "version": (1, 0, 2),
    "blender": (2, 93, 0),
    "location": "View3D > Properties > Camera",
    "description": 'Provides the ability to store five camera positions and recall them with a single button click',
    "wiki_url": "https://github.com/sundriftproductions/blenderaddon-camera-positions/wiki",
    "tracker_url": "https://github.com/sundriftproductions/blenderaddon-camera-positions",
    "category": "3D View"}

class CameraPositionsPreferencesPanel(bpy.types.AddonPreferences):
    bl_idname = __module__
    show_save_camera_positions: bpy.props.BoolProperty(name='Show Save Camera Positions', default=True, description='Show the Save Camera Position Buttons')
    position_1_loc_0: bpy.props.FloatProperty(default=0.0)
    position_1_loc_1: bpy.props.FloatProperty(default=0.0)
    position_1_loc_2: bpy.props.FloatProperty(default=0.0)
    position_1_rot_0: bpy.props.FloatProperty(default=0.0)
    position_1_rot_1: bpy.props.FloatProperty(default=0.0)
    position_1_rot_2: bpy.props.FloatProperty(default=0.0)

    position_2_loc_0: bpy.props.FloatProperty(default=0.0)
    position_2_loc_1: bpy.props.FloatProperty(default=0.0)
    position_2_loc_2: bpy.props.FloatProperty(default=0.0)
    position_2_rot_0: bpy.props.FloatProperty(default=0.0)
    position_2_rot_1: bpy.props.FloatProperty(default=0.0)
    position_2_rot_2: bpy.props.FloatProperty(default=0.0)

    position_3_loc_0: bpy.props.FloatProperty(default=0.0)
    position_3_loc_1: bpy.props.FloatProperty(default=0.0)
    position_3_loc_2: bpy.props.FloatProperty(default=0.0)
    position_3_rot_0: bpy.props.FloatProperty(default=0.0)
    position_3_rot_1: bpy.props.FloatProperty(default=0.0)
    position_3_rot_2: bpy.props.FloatProperty(default=0.0)

    position_4_loc_0: bpy.props.FloatProperty(default=0.0)
    position_4_loc_1: bpy.props.FloatProperty(default=0.0)
    position_4_loc_2: bpy.props.FloatProperty(default=0.0)
    position_4_rot_0: bpy.props.FloatProperty(default=0.0)
    position_4_rot_1: bpy.props.FloatProperty(default=0.0)
    position_4_rot_2: bpy.props.FloatProperty(default=0.0)

    position_5_loc_0: bpy.props.FloatProperty(default=0.0)
    position_5_loc_1: bpy.props.FloatProperty(default=0.0)
    position_5_loc_2: bpy.props.FloatProperty(default=0.0)
    position_5_rot_0: bpy.props.FloatProperty(default=0.0)
    position_5_rot_1: bpy.props.FloatProperty(default=0.0)
    position_5_rot_2: bpy.props.FloatProperty(default=0.0)

    def draw(self, context):
        self.layout.label(text="Current values")

class CAMERAPOSITIONS_PT_LoadCameraPreset1(bpy.types.Operator):
    bl_idname = "cp.load_camera_preset_1"
    bl_label = "1"

    def execute(self, context):
        bpy.context.scene.camera.location[0] = bpy.context.preferences.addons['camera_positions'].preferences.position_1_loc_0;
        bpy.context.scene.camera.location[1] = bpy.context.preferences.addons['camera_positions'].preferences.position_1_loc_1;
        bpy.context.scene.camera.location[2] = bpy.context.preferences.addons['camera_positions'].preferences.position_1_loc_2;
        bpy.context.scene.camera.rotation_euler[0] = bpy.context.preferences.addons['camera_positions'].preferences.position_1_rot_0;
        bpy.context.scene.camera.rotation_euler[1] = bpy.context.preferences.addons['camera_positions'].preferences.position_1_rot_1;
        bpy.context.scene.camera.rotation_euler[2] = bpy.context.preferences.addons['camera_positions'].preferences.position_1_rot_2;
        self.report({'INFO'}, 'Loaded Camera Preset 1.')
        return {'FINISHED'}

class CAMERAPOSITIONS_PT_LoadCameraPreset2(bpy.types.Operator):
    bl_idname = "cp.load_camera_preset_2"
    bl_label = "2"

    def execute(self, context):
        bpy.context.scene.camera.location[0] = bpy.context.preferences.addons['camera_positions'].preferences.position_2_loc_0;
        bpy.context.scene.camera.location[1] = bpy.context.preferences.addons['camera_positions'].preferences.position_2_loc_1;
        bpy.context.scene.camera.location[2] = bpy.context.preferences.addons['camera_positions'].preferences.position_2_loc_2;
        bpy.context.scene.camera.rotation_euler[0] = bpy.context.preferences.addons['camera_positions'].preferences.position_2_rot_0;
        bpy.context.scene.camera.rotation_euler[1] = bpy.context.preferences.addons['camera_positions'].preferences.position_2_rot_1;
        bpy.context.scene.camera.rotation_euler[2] = bpy.context.preferences.addons['camera_positions'].preferences.position_2_rot_2;
        self.report({'INFO'}, 'Loaded Camera Preset 2.')
        return {'FINISHED'}

class CAMERAPOSITIONS_PT_LoadCameraPreset3(bpy.types.Operator):
    bl_idname = "cp.load_camera_preset_3"
    bl_label = "3"

    def execute(self, context):
        bpy.context.scene.camera.location[0] = bpy.context.preferences.addons['camera_positions'].preferences.position_3_loc_0;
        bpy.context.scene.camera.location[1] = bpy.context.preferences.addons['camera_positions'].preferences.position_3_loc_1;
        bpy.context.scene.camera.location[2] = bpy.context.preferences.addons['camera_positions'].preferences.position_3_loc_2;
        bpy.context.scene.camera.rotation_euler[0] = bpy.context.preferences.addons['camera_positions'].preferences.position_3_rot_0;
        bpy.context.scene.camera.rotation_euler[1] = bpy.context.preferences.addons['camera_positions'].preferences.position_3_rot_1;
        bpy.context.scene.camera.rotation_euler[2] = bpy.context.preferences.addons['camera_positions'].preferences.position_3_rot_2;
        self.report({'INFO'}, 'Loaded Camera Preset 3.')
        return {'FINISHED'}

class CAMERAPOSITIONS_PT_LoadCameraPreset4(bpy.types.Operator):
    bl_idname = "cp.load_camera_preset_4"
    bl_label = "4"

    def execute(self, context):
        bpy.context.scene.camera.location[0] = bpy.context.preferences.addons['camera_positions'].preferences.position_4_loc_0;
        bpy.context.scene.camera.location[1] = bpy.context.preferences.addons['camera_positions'].preferences.position_4_loc_1;
        bpy.context.scene.camera.location[2] = bpy.context.preferences.addons['camera_positions'].preferences.position_4_loc_2;
        bpy.context.scene.camera.rotation_euler[0] = bpy.context.preferences.addons['camera_positions'].preferences.position_4_rot_0;
        bpy.context.scene.camera.rotation_euler[1] = bpy.context.preferences.addons['camera_positions'].preferences.position_4_rot_1;
        bpy.context.scene.camera.rotation_euler[2] = bpy.context.preferences.addons['camera_positions'].preferences.position_4_rot_2;
        self.report({'INFO'}, 'Loaded Camera Preset 4.')
        return {'FINISHED'}

class CAMERAPOSITIONS_PT_LoadCameraPreset5(bpy.types.Operator):
    bl_idname = "cp.load_camera_preset_5"
    bl_label = "5"

    def execute(self, context):
        bpy.context.scene.camera.location[0] = bpy.context.preferences.addons['camera_positions'].preferences.position_5_loc_0;
        bpy.context.scene.camera.location[1] = bpy.context.preferences.addons['camera_positions'].preferences.position_5_loc_1;
        bpy.context.scene.camera.location[2] = bpy.context.preferences.addons['camera_positions'].preferences.position_5_loc_2;
        bpy.context.scene.camera.rotation_euler[0] = bpy.context.preferences.addons['camera_positions'].preferences.position_5_rot_0;
        bpy.context.scene.camera.rotation_euler[1] = bpy.context.preferences.addons['camera_positions'].preferences.position_5_rot_1;
        bpy.context.scene.camera.rotation_euler[2] = bpy.context.preferences.addons['camera_positions'].preferences.position_5_rot_2;
        self.report({'INFO'}, 'Loaded Camera Preset 5.')
        return {'FINISHED'}

class CAMERAPOSITIONS_PT_SaveCameraPreset1(bpy.types.Operator):
    bl_idname = "cp.save_camera_preset_1"
    bl_label = "1"

    def execute(self, context):
        bpy.context.preferences.addons['camera_positions'].preferences.position_1_loc_0 = bpy.context.scene.camera.location[0];
        bpy.context.preferences.addons['camera_positions'].preferences.position_1_loc_1 = bpy.context.scene.camera.location[1];
        bpy.context.preferences.addons['camera_positions'].preferences.position_1_loc_2 = bpy.context.scene.camera.location[2];
        bpy.context.preferences.addons['camera_positions'].preferences.position_1_rot_0 = bpy.context.scene.camera.rotation_euler[0];
        bpy.context.preferences.addons['camera_positions'].preferences.position_1_rot_1 = bpy.context.scene.camera.rotation_euler[1];
        bpy.context.preferences.addons['camera_positions'].preferences.position_1_rot_2 = bpy.context.scene.camera.rotation_euler[2];
        self.report({'INFO'}, 'Saved Camera Preset 1.')
        return {'FINISHED'}

class CAMERAPOSITIONS_PT_SaveCameraPreset2(bpy.types.Operator):
    bl_idname = "cp.save_camera_preset_2"
    bl_label = "2"

    def execute(self, context):
        bpy.context.preferences.addons['camera_positions'].preferences.position_2_loc_0 = bpy.context.scene.camera.location[0];
        bpy.context.preferences.addons['camera_positions'].preferences.position_2_loc_1 = bpy.context.scene.camera.location[1];
        bpy.context.preferences.addons['camera_positions'].preferences.position_2_loc_2 = bpy.context.scene.camera.location[2];
        bpy.context.preferences.addons['camera_positions'].preferences.position_2_rot_0 = bpy.context.scene.camera.rotation_euler[0];
        bpy.context.preferences.addons['camera_positions'].preferences.position_2_rot_1 = bpy.context.scene.camera.rotation_euler[1];
        bpy.context.preferences.addons['camera_positions'].preferences.position_2_rot_2 = bpy.context.scene.camera.rotation_euler[2];
        self.report({'INFO'}, 'Saved Camera Preset 2.')
        return {'FINISHED'}

class CAMERAPOSITIONS_PT_SaveCameraPreset3(bpy.types.Operator):
    bl_idname = "cp.save_camera_preset_3"
    bl_label = "3"

    def execute(self, context):
        bpy.context.preferences.addons['camera_positions'].preferences.position_3_loc_0 = bpy.context.scene.camera.location[0];
        bpy.context.preferences.addons['camera_positions'].preferences.position_3_loc_1 = bpy.context.scene.camera.location[1];
        bpy.context.preferences.addons['camera_positions'].preferences.position_3_loc_2 = bpy.context.scene.camera.location[2];
        bpy.context.preferences.addons['camera_positions'].preferences.position_3_rot_0 = bpy.context.scene.camera.rotation_euler[0];
        bpy.context.preferences.addons['camera_positions'].preferences.position_3_rot_1 = bpy.context.scene.camera.rotation_euler[1];
        bpy.context.preferences.addons['camera_positions'].preferences.position_3_rot_2 = bpy.context.scene.camera.rotation_euler[2];
        self.report({'INFO'}, 'Saved Camera Preset 3.')
        return {'FINISHED'}

class CAMERAPOSITIONS_PT_SaveCameraPreset4(bpy.types.Operator):
    bl_idname = "cp.save_camera_preset_4"
    bl_label = "4"

    def execute(self, context):
        bpy.context.preferences.addons['camera_positions'].preferences.position_4_loc_0 = bpy.context.scene.camera.location[0];
        bpy.context.preferences.addons['camera_positions'].preferences.position_4_loc_1 = bpy.context.scene.camera.location[1];
        bpy.context.preferences.addons['camera_positions'].preferences.position_4_loc_2 = bpy.context.scene.camera.location[2];
        bpy.context.preferences.addons['camera_positions'].preferences.position_4_rot_0 = bpy.context.scene.camera.rotation_euler[0];
        bpy.context.preferences.addons['camera_positions'].preferences.position_4_rot_1 = bpy.context.scene.camera.rotation_euler[1];
        bpy.context.preferences.addons['camera_positions'].preferences.position_4_rot_2 = bpy.context.scene.camera.rotation_euler[2];
        self.report({'INFO'}, 'Saved Camera Preset 4.')
        return {'FINISHED'}

class CAMERAPOSITIONS_PT_SaveCameraPreset5(bpy.types.Operator):
    bl_idname = "cp.save_camera_preset_5"
    bl_label = "5"

    def execute(self, context):
        bpy.context.preferences.addons['camera_positions'].preferences.position_5_loc_0 = bpy.context.scene.camera.location[0];
        bpy.context.preferences.addons['camera_positions'].preferences.position_5_loc_1 = bpy.context.scene.camera.location[1];
        bpy.context.preferences.addons['camera_positions'].preferences.position_5_loc_2 = bpy.context.scene.camera.location[2];
        bpy.context.preferences.addons['camera_positions'].preferences.position_5_rot_0 = bpy.context.scene.camera.rotation_euler[0];
        bpy.context.preferences.addons['camera_positions'].preferences.position_5_rot_1 = bpy.context.scene.camera.rotation_euler[1];
        bpy.context.preferences.addons['camera_positions'].preferences.position_5_rot_2 = bpy.context.scene.camera.rotation_euler[2];
        self.report({'INFO'}, 'Saved Camera Preset 5.')
        return {'FINISHED'}

class CAMERAPOSITIONS_PT_Main(bpy.types.Panel):
    bl_idname = "CAMERAPOSITIONS_PT_Main"
    bl_label = "Camera Positions"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "View"

    def draw(self, context):
        if bpy.context.scene.camera != None:
            box = self.layout.box()
            row = box.row()
            row.scale_y = 0.6
            row.label(text="Load Camera Position",icon='VIEW_CAMERA')
            row = box.row(align=True)
            row.scale_y = 0.6
            row.operator("cp.load_camera_preset_1")
            row.operator("cp.load_camera_preset_2")
            row.operator("cp.load_camera_preset_3")
            row.operator("cp.load_camera_preset_4")
            row.operator("cp.load_camera_preset_5")

            row = self.layout.row(align=True)
            row.prop(bpy.context.preferences.addons['camera_positions'].preferences, "show_save_camera_positions")

            if bpy.context.preferences.addons['camera_positions'].preferences.show_save_camera_positions == True:
                box = self.layout.box()
                row = box.row()
                row.scale_y = 0.6
                row.label(text="Save Camera Position", icon='REC')
                row = box.row(align=True)
                row.scale_y = 0.6
                row.operator("cp.save_camera_preset_1")
                row.operator("cp.save_camera_preset_2")
                row.operator("cp.save_camera_preset_3")
                row.operator("cp.save_camera_preset_4")
                row.operator("cp.save_camera_preset_5")
        else:
            box = self.layout.box()
            row = box.row()
            row.scale_y = 0.6
            row.label(text="There is no Camera object in this scene.")

def register():
    bpy.utils.register_class(CameraPositionsPreferencesPanel)
    bpy.utils.register_class(CAMERAPOSITIONS_PT_Main)
    bpy.utils.register_class(CAMERAPOSITIONS_PT_LoadCameraPreset1)
    bpy.utils.register_class(CAMERAPOSITIONS_PT_LoadCameraPreset2)
    bpy.utils.register_class(CAMERAPOSITIONS_PT_LoadCameraPreset3)
    bpy.utils.register_class(CAMERAPOSITIONS_PT_LoadCameraPreset4)
    bpy.utils.register_class(CAMERAPOSITIONS_PT_LoadCameraPreset5)
    bpy.utils.register_class(CAMERAPOSITIONS_PT_SaveCameraPreset1)
    bpy.utils.register_class(CAMERAPOSITIONS_PT_SaveCameraPreset2)
    bpy.utils.register_class(CAMERAPOSITIONS_PT_SaveCameraPreset3)
    bpy.utils.register_class(CAMERAPOSITIONS_PT_SaveCameraPreset4)
    bpy.utils.register_class(CAMERAPOSITIONS_PT_SaveCameraPreset5)

def unregister():
    bpy.utils.unregister_class(CameraPositionsPreferencesPanel)
    bpy.utils.unregister_class(CAMERAPOSITIONS_PT_Main)
    bpy.utils.unregister_class(CAMERAPOSITIONS_PT_LoadCameraPreset1)
    bpy.utils.unregister_class(CAMERAPOSITIONS_PT_LoadCameraPreset2)
    bpy.utils.unregister_class(CAMERAPOSITIONS_PT_LoadCameraPreset3)
    bpy.utils.unregister_class(CAMERAPOSITIONS_PT_LoadCameraPreset4)
    bpy.utils.unregister_class(CAMERAPOSITIONS_PT_LoadCameraPreset5)
    bpy.utils.unregister_class(CAMERAPOSITIONS_PT_SaveCameraPreset1)
    bpy.utils.unregister_class(CAMERAPOSITIONS_PT_SaveCameraPreset2)
    bpy.utils.unregister_class(CAMERAPOSITIONS_PT_SaveCameraPreset3)
    bpy.utils.unregister_class(CAMERAPOSITIONS_PT_SaveCameraPreset4)
    bpy.utils.unregister_class(CAMERAPOSITIONS_PT_SaveCameraPreset5)

if __name__ == "__main__":
    register()
