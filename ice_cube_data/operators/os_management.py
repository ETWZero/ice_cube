import os
import subprocess
import bpy
from sys import platform
import json
from urllib import request
import zipfile
import shutil
import distutils.dir_util
import datetime
import pathlib

from ice_cube import root_folder, latest_dlc, github_url

from ice_cube_data.utils.ui_tools import CustomErrorBox
from ice_cube_data.utils.file_manage import ClearDirectory, getFiles, open_json
from ice_cube_data.utils.general_func import GetListIndex, getIndexCustom

properties_to_export = ["r_arm_ik","l_arm_ik","r_leg_ik","l_leg_ik","ankle_r","ankle_l","stretch_leg_r","stretch_leg_l","stretch_arm_r","stretch_arm_l","fingers_r","fingers_l","wrist_lock_r","wrist_lock_l","eyelashes","wireframe","jaw","round_jaw","bevelmouth","teeth_cartoon","antilag","teeth_bool","tongue","facerig",
    "leg_deform","body_deforms","dynamichair","eyebrowdeform","togglepupil","togglegradient","togglesparkle1","togglesparkle2","toggleemission","toggle_1","toggle_2","squaremouth","mouthrotate","toggle_3","toggle_4","breastswitch","line_mouth","baked_rig","global_head_rotation","squish_arm_r","squish_arm_l","squish_leg_r",
    "squish_leg_l","squish_body","squish_head","breastshape","jaw_strength","bevelmouthstrength","leg_taper_strength","hip","upperbodywidth","lowerbodywidth","bulge_arm_r","bulge_arm_l","bulge_leg_r","bulge_leg_l","eyebrowheight","eyebrowtaper1","eyebrowtaper2","leg_taper_strength2","armtaper","bodybulge","eyedepth","mouthdepth",
    "innermouthdepth","breastsize","breastweight","bodytopround","breath","armtype_enum","bendstyle","arm_ik_parent_r","arm_ik_parent_l"]

def open_user_packs(self, context):
    #addon location
    #opens a popup if you're using windows
    if platform == "win32":
        asset_directory_win = root_folder+"\\ice_cube_data\\internal_files\\user_packs"
        subprocess.Popen(fr'explorer "{asset_directory_win}"')
    #opens a popup if you're using mac os
    elif platform == "darwin":
        asset_directory_mac = root_folder+"/ice_cube_data/internal_files/user_packs/"
        subprocess.call(["open", "-R", asset_directory_mac])
    #opens a popup if you're using linux
    elif platform == "linux" or platform == "linux2":
        asset_directory_linux = root_folder+"/ice_cube_data/internal_files/user_packs/"
        subprocess.Popen(['xdg-open', asset_directory_linux])
    else:
        CustomErrorBox(message="在Discord上请联系“DarthLilo#4103”以寻求帮助。", title="未知操作系统", icon='ERROR')

    return{'FINISHED'}

def install_update_func(self, context):
    #sets up variables
    install_loc = root_folder+""
    downloads_folder = root_folder+"/downloads"
    backups_folders = root_folder+"/backups"
    can_backup = False
    #checks if the downloads folder exists, if not, create one.
    if os.path.exists(downloads_folder):
        print("路径已找到")
    else:
        os.mkdir(downloads_folder)
        print("创建下载文件夹")

    download_folder = os.path.normpath(downloads_folder)
    backups_folders = os.path.normpath(backups_folders)

    #checking if there's an up to date backup
    backups_list = {}
    for file in getFiles(backups_folders):
        creation_date = pathlib.Path(f"{backups_folders}/{file}").stat().st_mtime
        creation_date = "".join(str(datetime.datetime.fromtimestamp(creation_date)).split(" ")[0].split("-"))
        backups_list[file] = creation_date
    
    cur_time = "".join(str(datetime.datetime.now()).split(" ")[0].split("-"))
    
    for entry in backups_list:
        if backups_list[entry] == cur_time:
            can_backup = True
            break
    
    if can_backup == False:
        CustomErrorBox("Please create an up-to-date backup before updating!在更新之前，请创建一个最新版本的备份！","找不到已更新的备份！","ERROR")
        return{'FINISHED'}
    

    #clear folder
    ClearDirectory(download_folder)

    download_file_loc = str(download_folder+"/latest_release.zip")

    github_repo = json.loads(request.urlopen(github_url).read().decode())
    github_zip = github_repo['zipball_url']

    #download the zip
    try:
        request.urlretrieve(github_zip, download_file_loc)
        print("File Downloaded!文件已下载！")
    except Exception as e:
        CustomErrorBox(str(e), "在下载更新时发生了错误。", icon="CANCEL")
        print("在下载文件时发生了错误。")
    #unzips the file
    try:
        print(f"解压文件")
        with zipfile.ZipFile(download_file_loc, 'r') as zip_ref:
            zip_ref.extractall(download_folder)
        print("Successfully Unzipped File!")
        #removes the zip
        os.remove(download_file_loc)
        #if there's an old Ice Cube, remove it
        try:
            shutil.rmtree(download_folder+"/Ice Cube")
        except:
            pass
        print("Cleaned Folder")
    except Exception as e:
        CustomErrorBox(str(e), "在解压更新文件时发生了错误。", icon="CANCEL")
        print("Unknown Error")
    #Rename the downloaded file to Ice Cube
    for file in getFiles(download_folder):
        filepath = str(f"{download_folder}/{file}")
        renamed_file = str(f"{download_folder}/Ice Cube")
        os.rename(filepath, renamed_file)
    
    #Install the downloaded addon
    try:
        distutils.dir_util.copy_tree(download_folder+"/Ice Cube", install_loc)
        print("Finished Install!")
        CustomErrorBox("已成功安装更新！在继续操作前请重启Blender！","更新完成",'INFO')
    except Exception as e:
        print("Error Completing Install.")
        CustomErrorBox(str(e),"在安装更新时发生了问题。",'ERROR')

    return{'FINISHED'}

def create_backup_func(self, context):
    #sets up variables
    obj = context.object
    virtual_ice_cube = root_folder+""
    virtual_ice_cube = os.path.normpath(virtual_ice_cube)
    backups_folder = root_folder+"/backups"

    files = []
    files_nopath = []
    folders = []
    folders_nopath = []

    backup_name = obj.backup_name
    #check for a folder in the backups folder with the name entered, if none, create it.
    if obj.get("backup_name"):
        if obj.get("backup_name") == "":
            backups_folder = os.path.dirname(backups_folder)+"/backups/main"
            if os.path.exists(backups_folder) is False:
                os.mkdir(backups_folder)
        else:
            backups_folder = os.path.dirname(backups_folder)+"/backups/"+backup_name
            if os.path.exists(backups_folder) is False:
                os.mkdir(backups_folder)
    else:
        backups_folder = os.path.dirname(backups_folder)+"/backups/main"
        if os.path.exists(backups_folder):
            pass
        else:
            os.mkdir(backups_folder)
    
    #list of files to backup
    files_to_backup = ["__init__.py","main.py"]
    for file in files_to_backup:
        file_w_path = os.path.normpath(f"{root_folder}/{file}")
        files.append(file_w_path)
        files_nopath.append(file)
    

    #list of folders to backup
    folders_to_backup = ["ice_cube_data"]
    for folder in folders_to_backup:
        folder_w_path = os.path.normpath(f"{root_folder}/{folder}")
        folders.append(folder_w_path)
        folders_nopath.append(folder)




    print(files_nopath)
    print(folders_nopath)

    print(files)
    print(folders)

    #Actual Backing Up
    try:
        for file in files_nopath:
            file_nopy = file.split(".")[0]
            shutil.copy(f"{virtual_ice_cube}/{file}", f"{backups_folder}/{files_nopath[GetListIndex(file_nopy, files_nopath)]}")

        for folder in folders_nopath:
            try:
                os.mkdir(f"{backups_folder}/{folders_nopath[GetListIndex(folder, folders_nopath)]}")
            except:
                pass
            
        for folder in folders_nopath:
            distutils.dir_util.copy_tree(f"{virtual_ice_cube}/{folder}", f"{backups_folder}/{folder}")
        if obj.get("backup_name"):
            if obj.get("backup_name") == "":
                backup_name = "main"
            else:
                pass
        else:
            backup_name = "main"
        CustomErrorBox(f"创建备份： [{backup_name}]", "创建备份", 'INFO')
    except:
        CustomErrorBox(f"产生了一个错误: [{backup_name}]", "未知错误", 'ERROR')
    
    downloads_path = f"{root_folder}/ice_cube_data/ui/advanced/downloads.py"
    exec(open(downloads_path).read())

    return{'FINISHED'}

def load_backup_func(self, context):
    #set up the variables
    obj = context.object
    virtual_ice_cube = root_folder+""
    selected_backup = getattr(obj,"backups_list")
    backups_folder = root_folder+"/backups/"+selected_backup
    #check if you've entered a backup name, if not, give a prompt, if so, check if that folder exists and create one if it doesn't exist.
    if obj.get("backup_name"):
        if obj.get("backup_name") == "":
            CustomErrorBox("未找到备份","选择错误",'ERROR')
        else:
            if os.path.exists(backups_folder):
                distutils.dir_util.copy_tree(backups_folder, virtual_ice_cube)
                CustomErrorBox(f"加载备份：[{selected_backup}]，重启Blender以加载修改！", "加载备份", 'INFO')
            else:
                CustomErrorBox("无效的备份","选择错误",'ERROR')
    else:
        CustomErrorBox("未找到备份","选择错误",'ERROR')


    return{'FINISHED'}

def delete_backup_func(self, context):
        #set up variables
        obj = context.object
        virtual_ice_cube = root_folder+""
        virtual_ice_cube = os.path.normpath(virtual_ice_cube)
        backups_folder = root_folder+"/backups"

        selected_backup = getattr(obj,"backups_list")
        #check if you've entered a name, if not, give a prompt, if so, delete the entered name if a backup exists for it
        backup_to_remove = os.path.dirname(backups_folder)+"/backups/"+selected_backup
        if os.path.exists(backup_to_remove) and backup_to_remove != backups_folder and backup_to_remove != backups_folder+"/":
            shutil.rmtree(backup_to_remove)
            CustomErrorBox(f"删除备份：[{selected_backup}]", "删除备份", 'INFO')
        else:
            CustomErrorBox("未找到备份","无效备份",'ERROR')

        downloads_path = f"{root_folder}/ice_cube_data/ui/advanced/downloads.py"
        exec(open(downloads_path).read())

        return{'FINISHED'}

def download_dlc_func(self, context, dlc_id):
        obj = context.object
        selected_dlc = getattr(obj,"dlc_list")
        if selected_dlc == "":
            CustomErrorBox("选择一个有效的DLC！","无效的DLC",'ERROR')
            return{'FINISHED'}
        #gets the latest data from the github "dlc_list.json" file
        github_repo = json.loads(request.urlopen(latest_dlc).read().decode())
        #checks if you entered the name of a valid DLC
        try:
            #sets up variables depending on what is entered in the textbox
            for dlc in github_repo:
                dlc_number = getIndexCustom(selected_dlc,dlc_id)
                dlc_type = github_repo[dlc_number]['dlc_type']
                dlc_id_name = github_repo[dlc_number]['dlc_id']
                dlc_download = github_repo[dlc_number]['download_link']
                downloads_folder = root_folder+"/downloads"
                dlc_folder = root_folder+"/ice_cube_data/internal_files/user_packs/"+dlc_type+"/"+dlc_id_name
            #checks if a folder for the selected dlc exists, if not, create one.
            if os.path.exists(dlc_folder):
                print("Path Found")
            else:
                os.mkdir(dlc_folder)
                print(f"Created {dlc_id_name} Folder")
            download_folder = os.path.normpath(downloads_folder)
            #clear folder
            ClearDirectory(download_folder)
            
            download_file_loc = str(download_folder+"/dlc.zip")

            #download the zip
            try:
                request.urlretrieve(dlc_download, download_file_loc)
                print("File Downloaded!")
            except:
                CustomErrorBox("发生了一个未知的错误。下载取消。","下载错误","ERROR")
            #unzips the file
            try:
                print(f"Unzipping File")
                try:
                    shutil.rmtree(download_folder+"/"+dlc_id_name)
                except:
                    pass
                with zipfile.ZipFile(download_file_loc, 'r') as zip_ref:
                    zip_ref.extractall(download_folder)
                print("Successfully Unzipped File!")
                #remove the zip file when done
                os.remove(download_file_loc)
                print("Cleaned Folder")
            except:
                print("Unknown Error")
            
            try:
                #install the new DLC
                distutils.dir_util.copy_tree(download_folder+"/"+dlc_id_name, dlc_folder)
                print("Finished Install!")
                CustomErrorBox("DLC安装成功！","更新完成",'INFO')
            except:
                print("Error Completing Install.")
                CustomErrorBox("在安装时发生了一个错误。","更新取消",'ERROR')

        except:
            CustomErrorBox("无效的DLC","选择错误",'ERROR')

        return{'FINISHED'}

def export_settings_data(self, context):

    obj = context.object
    wm = bpy.context.window_manager

    
    filepath = obj.export_settings_filepath
    filename = obj.export_settings_name

    if obj.get("prop_clipboard") == True:
        json_name = filename
    else:
        json_name = "default"

    json_data = {
        "name" : json_name,
        "prop_data" : {}
    }

    for prop in properties_to_export:
        try:
            json_data["prop_data"][prop] = getattr(obj, prop)
        except:
            pass
    converted_json_data = json.dumps(json_data,indent=4)

    if obj.get("prop_clipboard") == True:
        wm.clipboard = f"{converted_json_data}"
    elif obj.get("prop_clipboard") == False:
        if filepath == "":
            CustomErrorBox("请选择一个有效的文件路径！","无效的文件路径",'ERROR')
            return{'FINISHED'}
        if filename == "":
            CustomErrorBox("请输入一个有效的文件名","无效的文件名",'ERROR')
            return{'FINISHED'}
        with open(f"{filepath}/{filename}.ice_cube_data", "w") as json_file:
            json_file.write(converted_json_data)

    return{'FINISHED'}

def import_settings_data(self, context):
    obj = context.object
    wm = bpy.context.window_manager
    filepath = obj.import_settings_filepath

    if obj.get("prop_clipboard") == True:
        settings_json_data = ""
        settings_name = ""
        prop_data = ""
        try:
            settings_json_data = json.loads(wm.clipboard)
        except:
            CustomErrorBox("请在尝试导入之前导出设置数据！","无效的剪贴板数据",'ERROR')
            return{'FINISHED'}
        try:
            settings_name = settings_json_data['name']
            prop_data = settings_json_data['prop_data']
        except:
            CustomErrorBox("请在尝试导入之前导出设置数据！","无效的剪贴板数据",'ERROR')
            return{'FINISHED'}
        
        for prop in prop_data:
            try:
                setattr(obj, prop, prop_data[prop])
            except:
                pass
        CustomErrorBox("成功地加载来自剪贴板的设置数据！\n交互一下场景以更新数据！","导入设置",'INFO')
    
    elif obj.get("prop_clipboard") == False:
        settings_json_data = ""
        settings_name = ""
        prop_data = ""

        try:
            settings_json_data = open_json(filepath)
        except:
            CustomErrorBox("请选择一个有效的设置文件！","无效的文件！",'ERROR')
            return{'FINISHED'}
        
        prop_data = settings_json_data['prop_data']

        for prop in prop_data:
            try:
                setattr(obj, prop, prop_data[prop])
                print(f"{prop} == {prop_data[prop]}")
            except:
                pass
        CustomErrorBox(f"成功地从[{settings_json_data['name']}.ice_cube_data]导入了设置数据！\n交互一下场景以更新数据！","导入设置",'INFO')
        

    return{'FINISHED'}

def reset_all_settings_func(self, context):
    obj = context.object

    settings_json_data = ""
    settings_name = ""
    prop_data = ""

    settings_json_data = open_json(f"{root_folder}/ice_cube_data/internal_files/default_settings.ice_cube_data")
    
    prop_data = settings_json_data['prop_data']

    for prop in prop_data:
        try:
            setattr(obj, prop, prop_data[prop])
            print(f"{prop} == {prop_data[prop]}")
        except:
            pass
    CustomErrorBox(f"成功地重置了所有设置数据！\n交互一下场景以更新数据！","导入设置",'INFO')
        

    return{'FINISHED'}


classes = [
           ]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__=="__main__":
    register()