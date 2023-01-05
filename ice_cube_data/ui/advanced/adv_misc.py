import bpy
from ice_cube_data.properties import properties

def advanced_misc_UI(self, context, layout, obj):
    box = layout.box()
    box.label(text="杂项", icon='ACTION')
    b = box.row(align=True)
    box_sub_1 = box.box()
    box_sub_1.label(text="数据设置", icon='SETTINGS')
    bs1 = box_sub_1.row(align=True)
    bs1.prop(obj,"prop_clipboard",text="使用剪贴板？")
    bs1.prop(obj,"ipaneltab7",text="")
    if obj.get("ipaneltab7") == 0:
        if obj.get("prop_clipboard") == False:
            bs1 = box_sub_1.row(align=True)
            bs1.prop(obj,"export_settings_filepath",text="导出文件路径",icon='EXPORT')
            bs1 = box_sub_1.row(align=True)
            bs1.prop(obj,"export_settings_name",text="文件名",icon='INFO')
        bs1 = box_sub_1.row(align=True)
        if obj.get("prop_clipboard") == True:
            bs1.operator("export.settings", text="导出到剪贴板")
        else:
            bs1.operator("export.settings", text="导出到文件")
    
    elif obj.get("ipaneltab7") == 1:
        if obj.get("prop_clipboard") == False:
            bs1 = box_sub_1.row(align=True)
            bs1.prop(obj,"import_settings_filepath",text="导入文件",icon='EXPORT')
        bs1 = box_sub_1.row(align=True)
        if obj.get("prop_clipboard") == True:
            bs1.operator("import.settings", text="从剪贴板导入")
        else:
            bs1.operator("import.settings", text="从文件导入")
    bs1 = box_sub_1.row(align=True)
    bs1.operator("reset.settings", text="恢复默认设置")

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
