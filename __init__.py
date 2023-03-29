# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy
from bpy.types import Panel, PropertyGroup, Scene, WindowManager, Operator
from bpy.props import (
    IntProperty,
    EnumProperty,
    StringProperty,
    PointerProperty,
)

# ----------- Addon Info ----------- 

bl_info = {
    "name" : "shapesplit",
    "author" : "Mitchell Taylor",
    "description" : "Set vertex groups to shapekeys to create new shapekeys from.",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Interface"
}

# ----------- Operators ----------- 

class shapesplit_ops():
    class exec_shapesplit(Operator):
        """Print object name in Console"""
        bl_idname = "exec_shapesplit"
        bl_label = "Test ShapeSplit Func"

        def execute(self, context):
            print (context.object)
            return {'FINISHED'}

def get_vertex_groups(self, context):
    return bpy.context.active_object

# ----------- Properties ----------- 

def init_properties():
    bpy.types.Scene.vertex_group_dropdown = EnumProperty(
        items = 
            [('TBD', 'TBD', ''),
            ('TBD1', 'TBD', ''),
            ('TBD2', 'TBD', '')],
        default='TBD',
        name="Vertex Group")
    
    bpy.types.Scene.mask_type_dropdown = EnumProperty(
        items = 
            [('none', 'None', 'No masked shape keys are created'),
            ('four_split', '4-Split', 'Splits this shape keys into 4 quadratically separated shape keys'),
            ('upper_lower', 'Upper-Lower', 'Splits this shape keys into 2 upper and lower shape keys'),
            ('left_right', 'Left-Right', 'Splits this shape keys into 2 left and right shape keys')],
        default='none',
        name="Mask Type")
    
def deinit_properties():
    del bpy.types.Scene.vertex_group_dropdown
    del bpy.types.Scene.mask_type_dropdown

    
# ----------- Interface and Registration ----------- 

class shapesplit_ui():
    class Panel(bpy.types.Panel):
        bl_idname = "OBJECT_PT_shapesplit"
        bl_label = "Shape Split"
        bl_space_type = 'VIEW_3D'
        bl_region_type = 'UI'
        bl_category = "VRCFT"

        @classmethod
        def poll(cls, context):
            return (context.active_object is not None and
                context.active_object.type == 'MESH')

        def draw(self, context):
            layout = self.layout
            obj = context.active_object
            scene = context.scene

            layout.label(text="Vertex Groups")

            split_box = layout.box()
            split_col = split_box.column(align=True)
            split_row = split_box.row()

            split_col.label(text="4-Split")
            split_col.prop(scene, "vertex_group_dropdown", text="UpperLeft")
            split_col.prop(scene, "vertex_group_dropdown", text="UpperRight")
            split_col.prop(scene, "vertex_group_dropdown", text="LowerLeft")
            split_col.prop(scene, "vertex_group_dropdown", text="LowerRight")
            split_col.separator(factor=1)

            split_col.label(text="Upper-Lower")
            split_col.prop(scene, "vertex_group_dropdown", text="Upper")
            split_col.prop(scene, "vertex_group_dropdown", text="Lower") 
            split_col.separator(factor=1)

            split_col.label(text="Left-Right")        
            split_col.prop(scene, "vertex_group_dropdown", text="Left")
            split_col.prop(scene, "vertex_group_dropdown", text="Right")

            layout.label(text="Shape Keys")

            shape_box = layout.box()
            shape_col = shape_box.column(align=True)
            shape_row = shape_box.row()

            shape_keys = obj.data.shape_keys
            if shape_keys is not None:
                for key in shape_keys.key_blocks:
                    shape_row = shape_col.row(align=True)
                    shape_row.label(text=key.name)
                    shape_row.prop(scene, "mask_type_dropdown", text="Mask")
                    shape_row = shape_col.row(align=True)

                    print(scene.mask_type_dropdown)

                    if (scene.mask_type_dropdown == 'four_split'):
                        shape_col.label(text="Will split your shape into 4!!!!")

                    if (scene.mask_type_dropdown == 'upper_lower'):
                        shape_col.label(text="Will split your shape vertically!!!!")

                    if (scene.mask_type_dropdown == 'left_right'):
                        shape_col.label(text="Will split your shape horizontally!!!!")

            layout.operator(shapesplit_ops.exec_shapesplit.bl_idname, text="MAGIC", icon="CONSOLE")


def register():
    init_properties()
    bpy.utils.register_class(shapesplit_ui.Panel)

def unregister():
    deinit_properties()
    bpy.utils.unregister_class(shapesplit_ui.Panel)

if __name__ == "__main__":
    register()