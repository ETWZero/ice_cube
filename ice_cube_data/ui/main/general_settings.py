#Libraries
import bpy

def general_settings_main_UI(self, context, layout, obj, icon):
    box = layout.box()
    pcoll = icon["main"]
    box.label(text= "通用设置", icon= 'TOOL_SETTINGS')
    
    box1 = box.box()
    box1.label(text= "杂项", icon= 'FILE_CACHE')
    b = box1.row(align=True)
    b.prop(obj, "bendstyle", expand=True, text = "棱角弯曲")
    b = box1.row(align=True)
    b.prop(obj, "mouthtypes", expand=True)
    b = box1.row(align=True)
    b.prop(obj, "facerig", toggle=True, text = "面部控制器")
    b = box1.row(align=True)
    b.prop(obj, "antilag", text = "优化操作帧率")
    b.prop(obj, "wireframe", text = "线框")
    b = box1.row(align=True)
    b.prop(obj, "mouthrotate", text = "嘴部旋转")
    b.prop(obj, "global_head_rotation", text = "全局头部旋转")
    b = box1.row(align=True)
    preset = box1.box()
    b = preset.row(align=True)
    b.prop(obj, "toggle_1", text = "切换1")
    b.prop(obj, "toggle_2", text = "切换2")
    b = preset.row(align=True)
    b.prop(obj, "toggle_3", text = "切换3")
    b.prop(obj, "toggle_4", text = "切换4")
    
    box1 = box.box()
    my_icon = pcoll["Steve"]
    if obj.get("armtype_enum") == 0:
        box1.label(text= "Arms", icon_value=my_icon.icon_id)
    my_icon = pcoll["Alex"]
    if obj.get("armtype_enum") == 1:
        box1.label(text= "Arms", icon_value=my_icon.icon_id)
    my_icon = pcoll["DarthLilo"]
    if obj.get("armtype_enum") == 2:
        box1.label(text= "Arms", icon_value=my_icon.icon_id)
    b = box1.row(align=True)
    b.prop(obj, "armtype_enum", expand=True)
    b = box1.row(align=True)
    b.prop(obj, "r_arm_ik", toggle=True, text = "右臂IK")
    b.prop(obj, "l_arm_ik", toggle=True, text = "左臂IK")
    b = box1.row(align=True)
    if obj.get("r_arm_ik") == 1:
        stretchR = b.row(align=True)
        stretchR.prop(obj, "stretch_arm_r", toggle=True, text = "右臂拉伸")
    else:
        stretchR = b.row(align=True)
        stretchR.prop(obj, "stretch_arm_r", toggle=True, text = "右臂拉伸")
        stretchR.enabled = False
    

    if obj.get("l_arm_ik") == 1:
        stretchL = b.row(align=True)
        stretchL.prop(obj, "stretch_arm_l", toggle=True, text = "左臂拉伸")
    else:
        stretchL = b.row(align=True)
        stretchL.prop(obj, "stretch_arm_l", toggle=True, text = "左臂拉伸")
        stretchL.enabled = False
    
    b = box1.row(align=True)
    b.prop(obj, "fingers_r", toggle=True, text = "右手手指")
    
    b.prop(obj, "fingers_l", toggle=True, text = "左手手指")
    b = box1.row(align=True)
    b.prop(obj, "thumbfill_R", text = "右手拇指填充",toggle=True)
    b.prop(obj, "thumbfill_L", text = "左手拇指填充",toggle=True)
    b = box1.row(align=True)
    b.prop(obj, "wrist_lock_r", toggle=True, text = "右手手腕锁定")
    b.prop(obj, "wrist_lock_l", toggle=True, text = "左手手腕锁定")
    b = box1.row(align=True)
    b.prop(obj, "arm_ik_parent_r", text = "")
    b.prop(obj, "arm_ik_parent_l", text = "")
    
    box1 = box.box()
    box1.label(text= "Legs", icon= 'FILE_CACHE')
    b = box1.row(align=True)
    b.prop(obj, "r_leg_ik", toggle=True, text = "右腿IK")
    b.prop(obj, "l_leg_ik", toggle=True, text = "左腿IK")
    b = box1.row(align=True)
    b.prop(obj, "ankle_r", toggle=True, text = "右腿脚腕")
    b.prop(obj, "ankle_l", toggle=True, text = "左腿脚腕")
    b = box1.row(align=True)
    if obj.get("r_leg_ik") == 1:
        stretchRL = b.row(align=True)
        stretchRL.prop(obj, "stretch_leg_r", toggle=True, text = "右腿拉伸")
    else:
        stretchRL = b.row(align=True)
        stretchRL.prop(obj, "stretch_leg_r", toggle=True, text = "右腿拉伸")
        stretchRL.enabled=False
    if obj.get("l_leg_ik") == 1:
        stretchLL = b.row(align=True)
        stretchLL.prop(obj, "stretch_leg_l", toggle=True, text = "左腿拉伸")
    else:
        stretchLL = b.row(align=True)
        stretchLL.prop(obj, "stretch_leg_l", toggle=True, text = "左腿拉伸")
        stretchLL.enabled=False

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