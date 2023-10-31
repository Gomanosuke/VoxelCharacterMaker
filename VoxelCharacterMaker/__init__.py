import bpy
import os
import shutil
from bpy_extras.io_utils import ImportHelper, ExportHelper
from bpy.props import StringProperty
from bpy.types import Operator, Panel

bl_info = {
    "name": "VoxelCharacterMaker",
    "author": "Gomanosuke",
    "version": (1, 0, 1),
    "blender": (2, 80, 0),
    "location": "View3D > Tools",
    "description": "Tools to assist in the creation of voxel characters",
    "category": "Object",
}

def get_library_path():
    script_file = os.path.realpath(__file__)
    directory = os.path.dirname(script_file)
    return os.path.join(directory, "library.blend")

def import_armature(filepath, armature_name):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return None

    try:
        with bpy.data.libraries.load(filepath, link=False) as (data_from, data_to):
            data_to.objects = [name for name in data_from.objects if name == armature_name]

        for obj in data_to.objects:
            bpy.context.collection.objects.link(obj)
            return obj
    except Exception as e:
        print(f"Failed to load armature: {e}")
        return None

def parent_to_armature(armature, mesh_obj):
    bpy.context.view_layer.objects.active = armature
    mesh_obj.select_set(True)
    armature.select_set(True)
    bpy.ops.object.parent_set(type='ARMATURE_AUTO')

def move_and_merge_vertices(mesh_obj):
    bpy.context.view_layer.objects.active = mesh_obj
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.remove_doubles()
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.shade_flat()


class ImportArmatureOperator(bpy.types.Operator):
    """Import Armature and Parent"""
    bl_idname = "object.import_armature_op"
    bl_label = "アーマチュアのセットアップ"

    def execute(self, context):
        library_path = get_library_path()
        armature_name = 'Armature'

        if context.selected_objects:
            selected_obj = context.selected_objects[0]
            if selected_obj.type == 'MESH':
                move_and_merge_vertices(selected_obj)
                armature = import_armature(library_path, armature_name)
                bpy.ops.mesh.customdata_custom_splitnormals_clear()
                if armature:
                    parent_to_armature(armature, selected_obj)
                else:
                    self.report({'WARNING'}, "Failed to load the armature.")
                    return {'CANCELLED'}
            else:
                self.report({'WARNING'}, "Selected object is not a mesh.")
                return {'CANCELLED'}
        else:
            self.report({'WARNING'}, "No object selected.")
            return {'CANCELLED'}

        return {'FINISHED'}

class scale_StartingBlock(bpy.types.Operator):
    """Scale the Armature"""
    bl_idname = "object.starting_block_op"
    bl_label = "コアブロック"

    def execute(self, context):
        armature = next((obj for obj in bpy.context.scene.objects if obj.type == 'ARMATURE'), None)
        if armature:
            armature.scale = (0.29,0.29,0.29)
        else:
            self.report({'WARNING'}, "No armature found in the scene.")
            return {'CANCELLED'}
        
        library_path = get_library_path()
        bpy.ops.wm.append(
            filepath=os.path.join(library_path, "Object", "startblock"),
            directory=os.path.join(library_path, "Object"),
            filename="startblock"
        )

        return {'FINISHED'}
    
class scale_Log(bpy.types.Operator):
    """Scale the Armature"""
    bl_idname = "object.log_op"
    bl_label = "丸太"

    def execute(self, context):
        armature = next((obj for obj in bpy.context.scene.objects if obj.type == 'ARMATURE'), None)
        if armature:
            armature.scale = (1.8,1.8,1.8)
        else:
            self.report({'WARNING'}, "No armature found in the scene.")
            return {'CANCELLED'}
        
        library_path = get_library_path()
        bpy.ops.wm.append(
            filepath=os.path.join(library_path, "Object", "log"),
            directory=os.path.join(library_path, "Object"),
            filename="log"
        )
        
        return {'FINISHED'}
    
class scale_Log_short(bpy.types.Operator):
    """Scale the Armature"""
    bl_idname = "object.log_short_op"
    bl_label = "短縮丸太"

    def execute(self, context):
        armature = next((obj for obj in bpy.context.scene.objects if obj.type == 'ARMATURE'), None)
        if armature:
            armature.scale = (1.8,1.8,1.8)
        else:
            self.report({'WARNING'}, "No armature found in the scene.")
            return {'CANCELLED'}
        
        library_path = get_library_path()
        bpy.ops.wm.append(
            filepath=os.path.join(library_path, "Object", "log_short"),
            directory=os.path.join(library_path, "Object"),
            filename="log_short"
        )
        
        return {'FINISHED'}
    
class scale_Cannon(bpy.types.Operator):
    """Scale the Armature"""
    bl_idname = "object.cannon_op"
    bl_label = "大砲"

    def execute(self, context):
        armature = next((obj for obj in bpy.context.scene.objects if obj.type == 'ARMATURE'), None)
        if armature:
            armature.scale = (4.4,4.4,4.4)
        else:
            self.report({'WARNING'}, "No armature found in the scene.")
            return {'CANCELLED'}
        
        library_path = get_library_path()
        bpy.ops.wm.append(
            filepath=os.path.join(library_path, "Object", "cannon"),
            directory=os.path.join(library_path, "Object"),
            filename="cannon"
        )

        return {'FINISHED'}
    
class scale_Bomb(bpy.types.Operator):
    """Scale the Armature"""
    bl_idname = "object.bomb_op"
    bl_label = "ボム"

    def execute(self, context):
        armature = next((obj for obj in bpy.context.scene.objects if obj.type == 'ARMATURE'), None)
        if armature:
            armature.scale = (0.95,0.95,0.95)
        else:
            self.report({'WARNING'}, "No armature found in the scene.")
            return {'CANCELLED'}
        
        library_path = get_library_path()
        bpy.ops.wm.append(
            filepath=os.path.join(library_path, "Object", "bomb"),
            directory=os.path.join(library_path, "Object"),
            filename="bomb"
        )

        return {'FINISHED'}
    
class scale_Ballast(bpy.types.Operator):
    """Scale the Armature"""
    bl_idname = "object.ballast_op"
    bl_label = "バラスト"

    def execute(self, context):
        armature = next((obj for obj in bpy.context.scene.objects if obj.type == 'ARMATURE'), None)
        if armature:
            armature.scale = (2,2,2)
        else:
            self.report({'WARNING'}, "No armature found in the scene.")
            return {'CANCELLED'}
        
        library_path = get_library_path()
        bpy.ops.wm.append(
            filepath=os.path.join(library_path, "Object", "ballast"),
            directory=os.path.join(library_path, "Object"),
            filename="ballast"
        )

        return {'FINISHED'}
    
class scale_first(bpy.types.Operator):
    """Scale the Armature"""
    bl_idname = "object.first_op"
    bl_label = "FPSMod"

    def execute(self, context):
        armature = next((obj for obj in bpy.context.scene.objects if obj.type == 'ARMATURE'), None)
        if armature:
            armature.scale = (1.47,1.47,1.47)
        else:
            self.report({'WARNING'}, "No armature found in the scene.")
            return {'CANCELLED'}
        
        library_path = get_library_path()
        bpy.ops.wm.append(
            filepath=os.path.join(library_path, "Object", "controller"),
            directory=os.path.join(library_path, "Object"),
            filename="controller"
        )
        return {'FINISHED'}

class CreateDirectoriesOperator(bpy.types.Operator):
    """Create Directories"""
    bl_idname = "object.create_directories_op"
    bl_label = "スキンフォルダの作成"

    def execute(self, context):
        base_path = context.scene.my_tool.path
        character_name = context.scene.my_tool.name
        image_path = context.scene.my_tool.image_path

        if not os.path.isdir(base_path):
            self.report({'WARNING'}, "Invalid base path.")
            return {'CANCELLED'}

        character_path = os.path.join(base_path, character_name)
        os.makedirs(character_path, exist_ok=True)

        os.makedirs(os.path.join(character_path, "StartingBlock"), exist_ok=True)
        shutil.copy(image_path, os.path.join(character_path, "StartingBlock"))
        os.makedirs(os.path.join(character_path, "Log"), exist_ok=True)
        shutil.copy(image_path, os.path.join(character_path, "Log"))
        os.makedirs(os.path.join(character_path, "Log", "short"), exist_ok=True)
        shutil.copy(image_path, os.path.join(character_path, "Log", "short"))
        os.makedirs(os.path.join(character_path, "Cannon"), exist_ok=True)
        shutil.copy(image_path, os.path.join(character_path, "Cannon"))
        os.makedirs(os.path.join(character_path, "Bomb"), exist_ok=True)
        shutil.copy(image_path, os.path.join(character_path, "Bomb"))
        os.makedirs(os.path.join(character_path, "Ballast"), exist_ok=True)
        shutil.copy(image_path, os.path.join(character_path, "Ballast"))
        os.makedirs(os.path.join(character_path, "33989506-e12a-4614-81c9-7ad8211d2e23-1"), exist_ok=True)
        shutil.copy(image_path, os.path.join(character_path, "33989506-e12a-4614-81c9-7ad8211d2e23-1"))

        self.report({'INFO'}, f"Directories created at {character_path}")
        return {'FINISHED'}

class ImportOBJ(bpy.types.Operator, ImportHelper):
    """Import a OBJ File"""
    bl_idname = "import_test.obj"
    bl_label = "Import OBJ"
    
    filter_glob: StringProperty(
        default="*.obj",
        options={'HIDDEN'}
    )

    def execute(self, context):
        bpy.ops.import_scene.obj(filepath=self.filepath)
        return {'FINISHED'}
    
class export_StartingBlock(bpy.types.Operator):
    """Export a OBJ File"""
    bl_idname = "object.start_ex_op"
    bl_label = "コアブロック"

    def execute(self, context):
        export_path = os.path.join(context.scene.my_tool.path, context.scene.my_tool.name, "StartingBlock", "startingBlock")
        if not export_path.lower().endswith('.obj'):
            export_path += '.obj'
        bpy.ops.export_scene.obj(filepath=export_path, use_selection=True)
        return {'FINISHED'}
    
class export_Log(bpy.types.Operator):

    """Export a OBJ File"""
    bl_idname = "object.log_ex_op"
    bl_label = "丸太"

    def execute(self, context):
        export_path = os.path.join(context.scene.my_tool.path, context.scene.my_tool.name, "Log", "log")
        if not export_path.lower().endswith('.obj'):
            export_path += '.obj'
        bpy.ops.export_scene.obj(filepath=export_path, use_selection=True)
        return {'FINISHED'}
    
class export_Log_short(bpy.types.Operator):

    """Export a OBJ File"""
    bl_idname = "object.log_ex_short_op"
    bl_label = "短縮丸太"

    def execute(self, context):
        export_path = os.path.join(context.scene.my_tool.path, context.scene.my_tool.name, "Log", "short", "log")
        if not export_path.lower().endswith('.obj'):
            export_path += '.obj'
        bpy.ops.export_scene.obj(filepath=export_path, use_selection=True)
        return {'FINISHED'}

class export_Cannon(bpy.types.Operator):

    """Export a OBJ File"""
    bl_idname = "object.cannon_ex_op"
    bl_label = "大砲"

    def execute(self, context):
        export_path = os.path.join(context.scene.my_tool.path, context.scene.my_tool.name, "Cannon", "cannon")
        if not export_path.lower().endswith('.obj'):
            export_path += '.obj'
        bpy.ops.export_scene.obj(filepath=export_path, use_selection=True)
        return {'FINISHED'}
    
class export_Bomb(bpy.types.Operator):

    """Export a OBJ File"""
    bl_idname = "object.bomb_ex_op"
    bl_label = "ボム"

    def execute(self, context):
        export_path = os.path.join(context.scene.my_tool.path, context.scene.my_tool.name, "Bomb", "bomb")
        if not export_path.lower().endswith('.obj'):
            export_path += '.obj'
        bpy.ops.export_scene.obj(filepath=export_path, use_selection=True)
        return {'FINISHED'}

class export_Ballast(bpy.types.Operator):

    """Export a OBJ File"""
    bl_idname = "object.ballast_ex_op"
    bl_label = "バラスト"

    def execute(self, context):
        export_path = os.path.join(context.scene.my_tool.path, context.scene.my_tool.name, "Ballast", "ballast")
        if not export_path.lower().endswith('.obj'):
            export_path += '.obj'
        bpy.ops.export_scene.obj(filepath=export_path, use_selection=True)
        return {'FINISHED'}

class export_First(bpy.types.Operator):

    """Export a OBJ File"""
    bl_idname = "object.first_ex_op"
    bl_label = "FPSMod"

    def execute(self, context):
        export_path = os.path.join(context.scene.my_tool.path, context.scene.my_tool.name, "33989506-e12a-4614-81c9-7ad8211d2e23-1", "first_parson_controller")
        if not export_path.lower().endswith('.obj'):
            export_path += '.obj'
        bpy.ops.export_scene.obj(filepath=export_path, use_selection=True)
        return {'FINISHED'}

class MyProperties(bpy.types.PropertyGroup):
    path: bpy.props.StringProperty(
        name="Skin Folder Path",
        description="Path to the folder",
        default="",
        maxlen=1024,
        subtype='DIR_PATH'
    )
    name: bpy.props.StringProperty(
        name="Character Name",
        description="Name of the character",
        default=""
    )
    image_path: bpy.props.StringProperty(
        name="Texture Path",
        description="Path to the image file",
        default="",
        maxlen=1024,
        subtype='FILE_PATH'
    )

class ImportArmaturePanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "VoxelCharacterMaker"
    bl_idname = "OBJECT_PT_import_armature_more"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'VoxelCharacterMaker'

    def draw(self, context):
        layout = self.layout
        my_tool = context.scene.my_tool

        layout.label(text="セットアップ")
        layout.prop(my_tool, "path")
        layout.prop(my_tool, "image_path")
        layout.prop(my_tool, "name")
        layout.operator("object.create_directories_op")
        layout.operator(ImportOBJ.bl_idname, text="Import OBJ")
        layout.operator("object.import_armature_op")

        layout.separator()
        layout.label(text="テンプレートのインポートとスケール変更")
        layout.operator("object.starting_block_op")
        layout.operator("object.log_op")
        layout.operator("object.log_short_op")
        layout.operator("object.cannon_op")
        layout.operator("object.bomb_op")
        layout.operator("object.ballast_op")
        layout.operator("object.first_op")

        layout.separator()
        layout.label(text="エクスポート")
        layout.operator("object.start_ex_op")
        layout.operator("object.log_ex_op")
        layout.operator("object.log_ex_short_op")
        layout.operator("object.cannon_ex_op")
        layout.operator("object.bomb_ex_op")
        layout.operator("object.ballast_ex_op")
        layout.operator("object.first_ex_op")


def register():
    bpy.utils.register_class(ImportArmatureOperator)
    bpy.utils.register_class(CreateDirectoriesOperator)
    bpy.utils.register_class(MyProperties)
    bpy.utils.register_class(ImportArmaturePanel)

    bpy.utils.register_class(scale_StartingBlock)
    bpy.utils.register_class(scale_Log)
    bpy.utils.register_class(scale_Log_short)
    bpy.utils.register_class(scale_Cannon)
    bpy.utils.register_class(scale_Bomb)
    bpy.utils.register_class(scale_Ballast)
    bpy.utils.register_class(scale_first)

    bpy.utils.register_class(ImportOBJ)

    bpy.utils.register_class(export_StartingBlock)
    bpy.utils.register_class(export_Log)
    bpy.utils.register_class(export_Log_short)
    bpy.utils.register_class(export_Cannon)
    bpy.utils.register_class(export_Bomb)
    bpy.utils.register_class(export_Ballast)
    bpy.utils.register_class(export_First)

    bpy.types.Scene.my_tool = bpy.props.PointerProperty(type=MyProperties)

def unregister():
    bpy.utils.unregister_class(ImportArmatureOperator)
    bpy.utils.unregister_class(CreateDirectoriesOperator)
    bpy.utils.unregister_class(MyProperties)
    bpy.utils.unregister_class(ImportArmaturePanel)

    bpy.utils.unregister_class(scale_StartingBlock)
    bpy.utils.unregister_class(scale_Log)
    bpy.utils.unregister_class(scale_Log_short)
    bpy.utils.unregister_class(scale_Cannon)
    bpy.utils.unregister_class(scale_Bomb)
    bpy.utils.unregister_class(scale_Ballast)
    bpy.utils.unregister_class(scale_first)

    bpy.utils.unregister_class(ImportOBJ)

    bpy.utils.unregister_class(export_StartingBlock)
    bpy.utils.unregister_class(export_Log)
    bpy.utils.unregister_class(export_Log_short)
    bpy.utils.unregister_class(export_Cannon)
    bpy.utils.unregister_class(export_Bomb)
    bpy.utils.unregister_class(export_Ballast)
    bpy.utils.unregister_class(export_First)

    del bpy.types.Scene.my_tool


if __name__ == "__main__":
    register()