import json
import bpy
import os
import sys
import shutil
from bpy.props import EnumProperty


#Custom Functions
from ice_cube import root_folder, dlc_id,dlc_type,dlc_author,bl_info

from ice_cube_data.utils.general_func import GetListIndex, IsVersionUpdated, BlenderVersConvert
from ice_cube_data.utils.file_manage import getFiles, ClearDirectory, GetRootFolder
from ice_cube_data.utils.selectors import isRigSelected
from ice_cube_data.utils.ui_tools import CustomErrorBox
from ice_cube_data.utils.web_tools import CustomLink

#Operator Functions
from .append import append_preset_func, append_default_rig, append_emotion_line_func
from .parenting import parent_left_arm, parent_right_arm, parent_right_leg, parent_left_leg, parent_body_func, parent_head_func
from .os_management import open_user_packs, install_update_func, create_backup_func, load_backup_func, delete_backup_func, download_dlc_func, export_settings_data, import_settings_data, reset_all_settings_func
from .web import check_for_updates_func, refresh_dlc_func


#Custom Libraries
from ice_cube_data.properties import properties

import ice_cube

#file variables
rig_pack_list = []
rig_pack_names = []
rig_id = "ice_cube"


internalfiles = os.path.join(root_folder, "ice_cube_data/internal_files/user_packs/rigs")
user_packs = os.path.normpath(internalfiles)

def RefreshRigList():
    items = []
    items = rig_pack_list
    return items
    
bpy.types.Scene.selected_rig_preset = EnumProperty(
        name = "选中的包",
        items = [('NONE', 'REFRESH','REFRESH')]
        )

#Classes
class refresh_rigs_list(bpy.types.Operator):
    bl_idname = "refresh.rig_list"
    bl_label = "刷新模型列表"
    bl_options = {'REGISTER', 'UNDO'}
    
    
    def execute(self, context):
        #Clearing the old lists
        rig_pack_list.clear()
        rig_pack_names.clear()
        
        #variables
        count = 1

        #Updating the list of installed packs
        for file in getFiles(user_packs):
            description = f"Rig ID: {count}"
            item_descriptor = (file, file, description)
            rig_pack_list.append(item_descriptor)
            rig_pack_names.append(file)
            count += 1
        
        
        #Drawing the custom property
        bpy.types.Scene.selected_rig_preset = EnumProperty(
        name = "选中的模型",
        items = RefreshRigList()
        )

        try:
            context.scene.selected_rig_preset = rig_pack_names[0]
        except:
            pass

        return{'FINISHED'}


class rig_baked_class(bpy.types.Operator): #A boolean that controls whether to use _NORMAL or _BAKED
    """修改已导入模型的烘焙状态"""
    bl_idname = "rig.bakedbutton"
    bl_label = "模型是否已烘焙？"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        obj = context.object

        properties.global_rig_baked = not properties.global_rig_baked
        

        return {'FINISHED'}

class append_preset(bpy.types.Operator):
    """从你的资产库中导入预设或模型"""
    bl_idname = "append.preset"
    bl_label = "导入预设"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        append_preset_func(self, context, properties.global_rig_baked)
        return{'FINISHED'}

class append_defaultrig(bpy.types.Operator): #Appends the default version of the rig
    """向你的场景中追加默认模型"""
    bl_idname = "append.defaultrig"
    bl_label = "Ice Cube [默认]"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        append_default_rig(self, context)
        return{'FINISHED'}

class parent_leftarm(bpy.types.Operator):
    """将物体名后面添加\"_LeftArmChild\"后缀以设置左臂父级"""
    bl_idname = "parent.leftarm"
    bl_label = "左臂父级"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        parent_left_arm(self, context)
        return{'FINISHED'}

class parent_rightarm(bpy.types.Operator):
    """将物体名后面添加\"_RightArmChild\"后缀以设置右臂父级"""
    bl_idname = "parent.rightarm"
    bl_label = "右臂父级"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        parent_right_arm(self, context)
        return{'FINISHED'}

class parent_rightleg(bpy.types.Operator):
    """将物体名后面添加\"_RightLegChild\"后缀以设置右腿父级"""
    bl_idname = "parent.rightleg"
    bl_label = "右腿父级"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        parent_right_leg(self, context)
        return{'FINISHED'}
    
class parent_leftleg(bpy.types.Operator):
    """将物体名后面添加\"_LeftLegChild\"后缀以设置左腿父级"""
    bl_idname = "parent.leftleg"
    bl_label = "左腿父级"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        parent_left_leg(self, context)
        return{'FINISHED'}
        
class parent_body(bpy.types.Operator):
    """将物体名后面添加\"_BodyChild\"后缀以设置身体父级"""
    bl_idname = "parent.body"
    bl_label = "身体父级"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        parent_body_func(self, context)
        return{'FINISHED'}

class parent_head(bpy.types.Operator):
    """将物体名后面添加\"_HeadChild\"后缀以设置头部父级"""
    bl_idname = "parent.head"
    bl_label = "头部父级"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        parent_head_func(self, context)
        return{'FINISHED'}
    
class lilocredits(bpy.types.Operator):
    """打开作者的信息页面"""
    bl_idname = "lilocredits.link"
    bl_label = "关于作者"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        CustomLink("https://darthlilo.carrd.co/")
        
        return {'FINISHED'}

class discord_link(bpy.types.Operator):
    """打开作者的Discord聊天服务器"""
    bl_idname = "discordserver.link"
    bl_label = "加入Discord聊天服务器！"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
    
        CustomLink("https://discord.gg/3G44QQM")
        
        return {'FINISHED'}

class download_template_1(bpy.types.Operator):
    """从我的Discord服务器下载一个资产包模板"""
    bl_idname = "template1.download"
    bl_label = "下载资产包模板"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
    
        CustomLink("https://cdn.discordapp.com/attachments/978737749995683851/978737884897107968/template_asset_pack.zip")
        
        return {'FINISHED'}

class download_template_2(bpy.types.Operator):
    """下载一个模型包模板"""
    bl_idname = "template2.download"
    bl_label = "下载模型包模板"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
    
        CustomLink("https://cdn.discordapp.com/attachments/978737749995683851/978744989691555850/template_rig_pack.zip")
        
        return {'FINISHED'}

class open_wiki(bpy.types.Operator):
    """打开Ice Cube Wiki"""
    bl_idname = "wiki.open"
    bl_label = "Ice Cube Wiki"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        CustomLink("https://darthlilo.gitbook.io/ice-cube/")
        
        return{'FINISHED'}

class open_custom_presets(bpy.types.Operator):
    """打开DLC文件夹"""
    bl_idname = "custom_presets.open"
    bl_label = "打开DLC文件夹"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        open_user_packs(self, context)
        return{'FINISHED'}

class append_emotion_line(bpy.types.Operator):
    """Appends an emotion line to the rig***向模型追加表情线"""
    bl_idname = "append.emotion"
    bl_label = "Append Emotion Line***追加表情线"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        append_emotion_line_func(self, context)
        return{'FINISHED'}

class check_for_updates(bpy.types.Operator):
    """检查Ice Cube GitHub的更新"""
    bl_idname = "check.updates"
    bl_label = "检查更新"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        ice_cube.update_available = check_for_updates_func(self, context)
        return{'FINISHED'}

class install_update(bpy.types.Operator):
    """从GitHub安装最新版本"""
    bl_idname = "install.update"
    bl_label = "安装最新版本"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        install_update_func(self, context)
        return{'FINISHED'}

class open_update_page(bpy.types.Operator):
    """打开Ice Cube网站"""
    bl_idname = "open.update"
    bl_label = "打开Ice Cube网站"
    bl_options = {'REGISTER', 'UNDO'}



    def execute(self, context):
        CustomLink("https://ice-cube-beta.carrd.co/")
        properties.update_available = False
        return{'FINISHED'}

class create_backup(bpy.types.Operator):
    """创建当前安装版本的备份"""
    bl_idname = "create.backup"
    bl_label = "创建备份"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        create_backup_func(self, context)
        return{'FINISHED'}

class load_backup(bpy.types.Operator):
    """从备份文件夹中读取选中的备份文件"""
    bl_idname = "load.backup"
    bl_label = "读取备份"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        load_backup_func(self, context)
        return{'FINISHED'}
    
class delete_backup(bpy.types.Operator):
    """删除选中的备份"""
    bl_idname = "delete.backup"
    bl_label = "删除备份"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        delete_backup_func(self, context)
        return{'FINISHED'}

class refresh_dlc(bpy.types.Operator):
    """检查Ice Cube GitHub的最新DLC"""
    bl_idname = "refresh.dlc"
    bl_label = "更新DLC"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        refresh_dlc_func(self, context)

        print(f"DLC IDs : {dlc_id}\nDLC TYPE : {dlc_type}\nDLC AUTHOR : {dlc_author}")
        downloads_path = f"{root_folder}/ice_cube_data/ui/advanced/downloads.py"
        exec(open(downloads_path).read())
        
        return{'FINISHED'}

class download_dlc(bpy.types.Operator):
    """下载选中的DLC"""
    bl_idname = "download.dlc"
    bl_label = "下载DLC"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        download_dlc_func(self, context, dlc_id)
        return{'FINISHED'}

class export_settings_data_class(bpy.types.Operator):
    """导出当前模型的设置"""
    bl_idname = "export.settings"
    bl_label = "导出设置"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        export_settings_data(self, context)
        return{'FINISHED'}

class import_settings_data_class(bpy.types.Operator):
    """从文件或剪贴板导入模型设置"""
    bl_idname = "import.settings"
    bl_label = "导入设置"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        import_settings_data(self, context)
        return{'FINISHED'}

class update_backups_list(bpy.types.Operator):
    """更新当前列表的备份！"""
    bl_idname = "update.backups"
    bl_label = "更新备份"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        downloads_path = f"{root_folder}/ice_cube_data/ui/advanced/downloads.py"
        exec(open(downloads_path).read())
        return{'FINISHED'}

class reset_all_settings(bpy.types.Operator):
    """重置模型的所有设置！"""
    bl_idname = "reset.settings"
    bl_label = "重置模型设置"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        reset_all_settings_func(self,context)
        return{'FINISHED'}

class generate_asset_pack(bpy.types.Operator):
    """生成资产包"""
    bl_idname = "generate.asest_pack"
    bl_label = "生成资产包"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        obj = context.object
        scene = context.scene
        if obj.get("ipaneltab6") is 0:
            #CHECKING FOR VARS
            if obj.asset_pack_name != "" and obj.entry_name_asset != "" and obj.asset_author != "" and obj.asset_version != "" and os.path.exists(obj.target_thumbnail_generate) is True:
                #folder generation
                inventory = f"{root_folder}/ice_cube_data/internal_files/user_packs/inventory"

                asset_pack_path = f"{inventory}/{obj.asset_pack_name}"

                list_of_dirs_to_gen = ["","assets","thumbnails",f"assets/{obj.entry_name_asset}"]

                for folder in list_of_dirs_to_gen:
                    if os.path.exists(f"{asset_pack_path}/{folder}") is False:
                        os.mkdir(f"{asset_pack_path}/{folder}")

                #settings json generation
                settings_json_data = {
                    "pack_name": obj.asset_pack_name,
                    "author": obj.asset_author,
                    "version": obj.asset_version,
                	"default": obj.entry_name_asset
                }

                #info json generation
                info_json_data = {
                    "asset_name": obj.entry_name_asset,
                    "author": obj.asset_author,
                    "asset_version": obj.asset_version
                }

                converted_settings_json = json.dumps(settings_json_data,indent=4)
                with open(f"{asset_pack_path}/settings.json", "w") as json_file:
                    json_file.write(converted_settings_json)

                converted_info_json = json.dumps(info_json_data,indent=4)
                with open(f"{asset_pack_path}/assets/{obj.entry_name_asset}/info.json", "w") as json_file:
                    json_file.write(converted_info_json)


                #saving a copy of the file
                if bpy.data.is_saved is True and obj.asset_pack_name != "" and obj.entry_name_asset != "":
                    filepath = f"{inventory}/{obj.asset_pack_name}/assets/{obj.entry_name_asset}/{obj.entry_name_asset}.blend"
                    bpy.ops.wm.save_as_mainfile(filepath=filepath,copy=True)

                #thumbnail management
                if obj.target_thumbnail_generate != "" and str(obj.target_thumbnail_generate).__contains__(".png"): #Copy Thumbnail
                    shutil.copyfile(obj.target_thumbnail_generate,f"{inventory}/{obj.asset_pack_name}/thumbnails/{obj.entry_name_asset}.png")

            elif obj.asset_pack_name == "":
                CustomErrorBox("请输入资产包的名称！",'无效的名称','ERROR')
                return{'FINISHED'}
            elif obj.entry_name_asset == "":
                CustomErrorBox("请输入资产名称！","无效的名称",'ERROR')
                return{'FINISHED'}
            elif obj.asset_author == "":
                CustomErrorBox("请输入作者名称！","无效的作者名称",'ERROR')
                return{'FINISHED'}
            elif obj.asset_version == "":
                CustomErrorBox("请输入有效的版本号！","无效的版本号",'ERROR')
                return{'FINISHED'}
            elif os.path.exists(obj.target_thumbnail_generate) is False:
                CustomErrorBox("请选择一个有效的缩略图！")
                return{'FINISHED'}

        if obj.get("ipaneltab6") is 1:
            #CHECKING FOR VARS
            if obj.asset_pack_name != "" and obj.entry_name_asset != "" and obj.asset_author != "" and obj.asset_version != "":
                
                if obj.has_baked_version is True and os.path.exists(obj.baked_version_filepath) is False:
                    CustomErrorBox("请输入一个有效的烘焙文件路径！",'无效的缩略图','ERROR')
                    return{'FINISHED'}
                
                if os.path.exists(obj.target_thumbnail_generate) is False and obj.generate_thumbnail is False:
                    CustomErrorBox("无效的缩略图路径！",'无效的缩略图路径','ERROR')
                    return{'FINISHED'}

                #folder generation
                rigs = f"{root_folder}/ice_cube_data/internal_files/user_packs/rigs"

                rig_pack_path = f"{rigs}/{obj.asset_pack_name}"

                list_of_dirs_to_gen = ["","rigs","thumbnails",f"rigs/{obj.entry_name_asset}"]

                for folder in list_of_dirs_to_gen:
                    if os.path.exists(f"{rig_pack_path}/{folder}") is False:
                        os.mkdir(f"{rig_pack_path}/{folder}")

                #settings json generation
                settings_json_data = {
                    "pack_name": obj.asset_pack_name,
                    "author": obj.asset_author,
                    "version": obj.asset_version,
                	"default": obj.entry_name_asset
                }

                #info json generation
                info_json_data = {
                    "rig_name": obj.entry_name_asset,
                	"base_rig": "Ice Cube",
                	"base_rig_vers": BlenderVersConvert(bl_info['version']),
                    "author": obj.asset_author,
                    "rig_version": obj.asset_version,
                	"has_baked": f"{obj.has_baked_version}"
                }

                converted_settings_json = json.dumps(settings_json_data,indent=4)
                with open(f"{rig_pack_path}/settings.json", "w") as json_file:
                    json_file.write(converted_settings_json)

                converted_info_json = json.dumps(info_json_data,indent=4)
                with open(f"{rig_pack_path}/rigs/{obj.entry_name_asset}/info.json", "w") as json_file:
                    json_file.write(converted_info_json)


                #saving a copy of the file
                if bpy.data.is_saved is True:
                    filepath = f"{rigs}/{obj.asset_pack_name}/rigs/{obj.entry_name_asset}/{obj.entry_name_asset}_NORMAL.blend"
                    bpy.ops.wm.save_as_mainfile(filepath=filepath,copy=True)
                
                if obj.has_baked_version is True:
                    baked_path = f"{rigs}/{obj.asset_pack_name}/rigs/{obj.entry_name_asset}/{obj.entry_name_asset}_BAKED.blend"
                    shutil.copyfile(obj.baked_version_filepath,baked_path)

                #thumbnail management
                if obj.target_thumbnail_generate != "" and str(obj.target_thumbnail_generate).__contains__(".png"): #Copy Thumbnail
                    shutil.copyfile(obj.target_thumbnail_generate,f"{rigs}/{obj.asset_pack_name}/thumbnails/{obj.entry_name_asset}.png")

                #generating thumbnail
                if obj.generate_thumbnail is True:

                    

                    #setting save loc
                    sce = bpy.context.scene.name
                    org_save_loc = bpy.data.scenes[sce].render.filepath
                    bpy.data.scenes[sce].render.filepath = f"{rig_pack_path}/thumbnails/{obj.entry_name_asset}.png"

                    #generating camera
                    camera_data = bpy.data.cameras.new(name='AutoGenCam')
                    camera_object = bpy.data.objects.new('AutoGenCam', camera_data)
                    bpy.context.scene.collection.objects.link(camera_object)

                    #setting camera data
                    auto_cam = bpy.data.objects["AutoGenCam"]
                    auto_cam.location = (3.53542, -7.55179, 2.08197)
                    auto_cam.rotation_euler = (1.5252,-0.0000,0.4321)
                    bpy.data.cameras["AutoGenCam"].lens = 80

                    #setting resolution
                    for scene_thing in bpy.data.scenes:
                        org_trans_setting = scene_thing.render.film_transparent
                        org_res_x = scene_thing.render.resolution_x
                        org_res_y = scene_thing.render.resolution_y
                        scene_thing.render.resolution_x = 1920
                        scene_thing.render.resolution_y = 1920
                        scene_thing.render.film_transparent = True
                        scene_thing.camera = auto_cam
                    
                    #setting view
                    for area in bpy.context.screen.areas:
                        if area.type == 'VIEW_3D':
                            area.spaces[0].region_3d.view_perspective = 'CAMERA'
                            break
                    
                    #setting solid mode
                    old_shading = bpy.context.space_data.shading.type
                    bpy.context.space_data.shading.type = 'SOLID'



                    #disabling overlays
                    bpy.context.space_data.overlay.show_overlays = False

                    #rendering img
                    bpy.ops.render.opengl(write_still=True)

                    #fixing scene

                    bpy.context.space_data.overlay.show_overlays = True

                    bpy.data.objects.remove(auto_cam)
                    bpy.data.cameras.remove(bpy.data.cameras["AutoGenCam"])

                    bpy.data.scenes[sce].render.filepath = org_save_loc

                    for scene_thing in bpy.data.scenes:
                        scene_thing.render.film_transparent = org_trans_setting
                        scene_thing.render.resolution_x = org_res_x
                        scene_thing.render.resolution_y = org_res_y
                    
                    bpy.context.space_data.shading.type = old_shading
                    

            elif obj.asset_pack_name == "":
                CustomErrorBox("请输入资产包的名称！",'无效的名称','ERROR')
                return{'FINISHED'}
            elif obj.entry_name_asset == "":
                CustomErrorBox("请输入资产名称！","无效的名称",'ERROR')
                return{'FINISHED'}
            elif obj.asset_author == "":
                CustomErrorBox("请输入作者名称！","无效的作者名",'ERROR')
                return{'FINISHED'}
            elif obj.asset_version == "":
                CustomErrorBox("请输入有效的版本号！","无效的版本号",'ERROR')
                return{'FINISHED'}
            elif os.path.exists(obj.target_thumbnail_generate) is False and obj.generate_thumbnail is False:
                CustomErrorBox("请选择一个有效的缩略图！","无效的缩略图",'ERROR')
                return{'FINISHED'}

        return{'FINISHED'}

classes = [
    refresh_rigs_list,
    rig_baked_class,
    append_preset,
    append_defaultrig,
    parent_leftarm,
    parent_rightarm,
    parent_rightleg,
    parent_leftleg,
    parent_body,
    parent_head,
    lilocredits,
    discord_link,
    download_template_1,
    download_template_2,
    open_wiki,
    open_custom_presets,
    append_emotion_line,
    check_for_updates,
    install_update,
    open_update_page,
    create_backup,
    load_backup,
    delete_backup,
    refresh_dlc,
    download_dlc,
    export_settings_data_class,
    import_settings_data_class,
    update_backups_list,
    reset_all_settings,
    generate_asset_pack,
           ]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__=="__main__":
    register()