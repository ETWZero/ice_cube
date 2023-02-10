import bpy

from bpy.props import (StringProperty,
                        BoolProperty,
                        IntProperty,
                        FloatProperty,
                        EnumProperty,
                        )  

from ice_cube_data.systems import inventory_system
                 

#war crimewar crimewar crimewar crimewar crimewar crime fuck you

#Bool Prop

bpy.types.Object.r_arm_ik = BoolProperty(
name="r_arm_ik", description="启用右臂的IK控制", default=False)
    
bpy.types.Object.l_arm_ik = BoolProperty(
name="l_arm_ik", description="启用左臂的IK控制", default=False)
    
bpy.types.Object.r_leg_ik = BoolProperty(
name="r_leg_ik", description="启用右腿的IK控制", default=True)
    
bpy.types.Object.l_leg_ik = BoolProperty(
name="l_leg_ik", description="启用左腿的IK控制", default=True)
    
bpy.types.Object.ankle_r = BoolProperty(
name="ankle_r", description="右脚脚腕", default=True)
    
bpy.types.Object.ankle_l = BoolProperty(
name="ankle_l", description="左脚脚腕", default=True)
    
bpy.types.Object.stretch_leg_r = BoolProperty(
name="stretch_leg_r", description="右腿拉伸", default=True)
    
bpy.types.Object.stretch_leg_l = BoolProperty(
name="stretch_leg_l", description="左腿拉伸", default=True)
    
bpy.types.Object.stretch_arm_r = BoolProperty(
name="stretch_arm_r", description="右臂拉伸", default=False)
    
bpy.types.Object.stretch_arm_l = BoolProperty(
name="stretch_arm_l", description="左臂拉伸", default=False)
    
bpy.types.Object.fingers_r = BoolProperty(
name="fingers_r", description="右手手指", default=False)
    
bpy.types.Object.fingers_l = BoolProperty(
name="fingers_l", description="左手手指", default=False)

bpy.types.Object.wrist_lock_r = BoolProperty(
name="wrist_lock_r", description="锁定右手手腕", default=False)

bpy.types.Object.wrist_lock_l = BoolProperty(
name="wrist_lock_l", description="锁定左手手腕", default=False)

bpy.types.Object.eyelashes = BoolProperty(
name="eyelashes", description="启用睫毛", default=False)

bpy.types.Object.wireframe = BoolProperty(
name="wireframe", description="启用线框预览", default=False)

bpy.types.Object.jaw = BoolProperty(
name="jaw", description="启用下颌", default=False)

bpy.types.Object.round_jaw = BoolProperty(
name="round_jaw", description="圆化下颌", default=False)

bpy.types.Object.bevelmouth = BoolProperty(
name="bevelmouth", description="启用嘴部倒角", default=False)

bpy.types.Object.teeth_cartoon = BoolProperty(
name="teeth_cartoon", description="启用牙齿倒角", default=False)

bpy.types.Object.antilag = BoolProperty(
name="antilag", description="让模型操作更流畅", default=False)

bpy.types.Object.teeth_bool = BoolProperty(
name="teeth_bool", description="是否允许牙齿穿过头部的网格", default=False)

bpy.types.Object.tongue = BoolProperty(
name="tongue", description="启用舌头", default=False)

bpy.types.Object.facerig = BoolProperty(
name="facerig", description="启用面部表情模型", default=True)

bpy.types.Object.leg_deform = BoolProperty(
name="leg_deform", description="启用手臂形变", default=False)

bpy.types.Object.body_deforms = BoolProperty(
name="body_deforms", description="启用身体形变", default=False)

bpy.types.Object.dynamichair = BoolProperty(
name="dynamichair", description="启用动态头发", default=False)

bpy.types.Object.eyebrowdeform = BoolProperty(
name="eyebrowdeform", description="启用眼睛形变", default=False)

bpy.types.Object.togglepupil = BoolProperty(
name="togglepupil", description="切换瞳孔", default=True)

bpy.types.Object.togglegradient = BoolProperty(
name="togglegradient", description="切换渐变", default=False)

bpy.types.Object.togglesparkle1 = BoolProperty(
name="togglesparkle1", description="切换高光1", default=True)

bpy.types.Object.togglesparkle2 = BoolProperty(
name="togglesparkle2", description="切换高光2", default=True)

bpy.types.Object.toggleemission = BoolProperty(
name="toggleemission", description="切换自发光", default=True)

bpy.types.Object.toggle_1 = BoolProperty(
name="Toggle 1", description="切换一，默认开启", default=True)

bpy.types.Object.toggle_2 = BoolProperty(
name="Toggle 2", description="切换二，默认关闭", default=False)

bpy.types.Object.mouthrotate = BoolProperty(
name="mouthrotate", description="基于位置旋转嘴部边缘", default=False)

bpy.types.Object.toggle_3 = BoolProperty(
name="Toggle 3", description="切换三，默认关闭", default=False)

bpy.types.Object.toggle_4 = BoolProperty(
name="Toggle 4", description="切换四，默认关闭", default=False)

bpy.types.Object.breastswitch = BoolProperty(
name="breastswitch", description="启用骨骼以控制胸部大小Enables bones for controlling chest sizes", default=False)

bpy.types.Object.line_mouth = BoolProperty(
name="line_mouth", description="显示或隐藏卡通化的嘴部", default=False)

bpy.types.Object.baked_rig = BoolProperty(
name="baked_rig", description="取决于导入的模型是否应该被烘焙", default=False)

bpy.types.Object.global_head_rotation = BoolProperty(
name="global_head_rotation", description="启用或禁用头部的全局旋转", default=False)

bpy.types.Object.prop_clipboard = BoolProperty(
name="prop_clipboard", description="设置内容存储于文件或复制到剪贴板", default=False)

bpy.types.Object.R_A_Half = BoolProperty(
    name = "R_A_Half", description="决定当前网格的父级为右臂的上半部分还是下半部分",default=False)

bpy.types.Object.L_A_Half = BoolProperty(
    name = "L_A_Half", description="决定当前网格的父级为左臂的上半部分还是下半部分",default=False)

bpy.types.Object.R_L_Half = BoolProperty(
    name = "R_L_Half", description="决定当前网格的父级为右腿的上半部分还是下半部分",default=False)

bpy.types.Object.L_L_Half = BoolProperty(
    name = "L_L_Half", description="决定当前网格的父级为左腿的上半部分还是下半部分",default=False)

bpy.types.Object.Body_Bend_Half = BoolProperty(
    name = "Body_Bend_Half", description="决定当前网格的父级为身体的上半部分还是下半部分",default=False)

bpy.types.Object.generate_thumbnail = BoolProperty(
    name = "generate_thumbnail", description="决定是否生成一个当前场景的缩略图",default=False)

bpy.types.Object.has_baked_version = BoolProperty(
    name = "has_baked_version", description="决定在info.json内存储是否烘焙的信息",default=False)

bpy.types.Object.thumbfill_L = BoolProperty(
    name = "thumbfill_L", description="切换左手的手指间隙",default=True)

bpy.types.Object.thumbfill_R = BoolProperty(
    name = "thumbfill_R", description="切换右手的手指间隙",default=True)


global_rig_baked = False
global_parent_half = False
update_available = False




#Sring Prop


#Int Prop

bpy.types.Object.squish_arm_r = IntProperty(
name="squish_arm_r", description="右臂挤压Right Arm Squish", default=0, min=0, max=1)

bpy.types.Object.squish_arm_l = IntProperty(
name="squish_arm_l", description="左臂挤压Left Arm Squish", default=0, min=0, max=1)

bpy.types.Object.squish_leg_r = IntProperty(
name="squish_leg_r", description="右腿挤压Right Leg Squish", default=0, min=0, max=1)

bpy.types.Object.squish_leg_l = IntProperty(
name="squish_leg_l", description="L左腿挤压eft Leg Squish", default=0, min=0, max=1)

bpy.types.Object.squish_body = IntProperty(
name="squish_body", description="身体挤压Body Squish", default=0, min=0, max=1)

bpy.types.Object.squish_head = IntProperty(
name="squish_head", description="头部挤压Head Squish", default=0, min=0, max=1)

bpy.types.Object.breastshape = IntProperty(
name="breast_shape", description="胸部向下延伸一点像素", default=0, min=0, max=1)

#Float Prop

bpy.types.Object.jaw_strength = FloatProperty(
name="jaw_strength", description="改变下颌的影响程度", default=1, min=0, max=1)

bpy.types.Object.bevelmouthstrength = FloatProperty(
name="bevelmouthstrength", description="改变倒角的力度", default=1, min=0, max=1)

bpy.types.Object.leg_taper_strength = FloatProperty(
name="leg_taper_strength", description="改变锥化的力度", default=0, min=-1, max=1)

bpy.types.Object.hip = FloatProperty(
name="hip", description="改变臀部大小", default=0, min=0 ,max=1.5)

bpy.types.Object.upperbodywidth = FloatProperty(
name="upperbodywidth", description="启用身体形变", default=0, min=0 ,max=1)

bpy.types.Object.lowerbodywidth = FloatProperty(
name="lowerbodywidth", description="启用身体形变", default=0, min=-1 ,max=1)

bpy.types.Object.bulge_arm_r = FloatProperty(
name="bulge_arm_r", description="右臂膨胀", default=0, min=0, max=1)

bpy.types.Object.bulge_arm_l = FloatProperty(
name="bulge_arm_l", description="左臂膨胀", default=0, min=0, max=1)

bpy.types.Object.bulge_leg_r = FloatProperty(
name="bulge_leg_r", description="右腿膨胀", default=0, min=0, max=1)

bpy.types.Object.bulge_leg_l = FloatProperty(
name="bulge_leg_l", description="左腿膨胀", default=0, min=0, max=1)

bpy.types.Object.eyebrowheight = FloatProperty(
name="eyebrowheight", description="改变眉毛的高度", default=0, min=-.5 ,max=1)

bpy.types.Object.eyebrowlength = FloatProperty(
name="eyebrowlength", description="改变眉毛的长度", default=0, min=-1 ,max=1)

bpy.types.Object.eyebrowtaper1 = FloatProperty(
name="eyebrowtaper1", description="改变眉毛的锥化程度", default=0, min=-.5 ,max=1)

bpy.types.Object.eyebrowtaper2 = FloatProperty(
name="eyebrowtaper2", description="改变眉毛的锥化程度", default=0, min=-.5 ,max=1)

bpy.types.Object.leg_taper_strength2 = FloatProperty(
name="leg_taper_strength2", description="改变上侧腿部的锥化程度", default=0, min=-1, max=1)

bpy.types.Object.armtaper = FloatProperty(
name="armtaper", description="改变上侧手臂的锥化程度", default=0, min=-1, max=1)

bpy.types.Object.bodybulge = FloatProperty(
    name="bodybulge", description="身体膨胀", default=0, min=0, max=1)

bpy.types.Object.eyedepth = FloatProperty(
    name="eyedepth", description="眼睛深度", default=0, min=-1, max=1)

bpy.types.Object.mouthdepth = FloatProperty(
    name="mouthdepth", description="嘴部深度", default=0, min=-1, max=1)

bpy.types.Object.innermouthdepth = FloatProperty(
    name="innermouthdepth", description="嘴部内侧深度", default=0, min=0, max=1)

bpy.types.Object.breastsize = FloatProperty(
    name="breastsize", description="胸部大小", default=0, min=0, max=2)
    
bpy.types.Object.breastweight = FloatProperty(
    name="breastweight", description="胸部权重", default=0, min=0, max=1)

bpy.types.Object.bodytopround = FloatProperty(
    name="bodytopround", description="圆化上侧身体", default=0, min=0, max=2)

#Enum Prop 

bpy.types.Object.armtype_enum = EnumProperty(
    name = "改变胳膊的形状",
    default = 'one',
    items = [('one', 'Steve', '4x4'),
             ('two', 'Alex', '4x3'),
             ('three', '3x3胳膊', '3x3')
             ])
             
bpy.types.Object.ipaneltab1 = EnumProperty(
    name = "haha tab",
    default = 'one',
    items = [('one', '主要', '包含基础设置'),
             ('two', '自定义', '包含自定义设置'),
             ('three', '材质', '材质自定义'),
             ('four', '高级', '仅为熟练使用的用户所设计')
             ])
             
bpy.types.Object.ipaneltab2 = EnumProperty(
    name = "haha tab",
    default = 'one',
    items = [('one', '骨骼层', '基于骨骼层切换骨骼的可见性'),
             ('two', '一般设定', '模型的基础设置')
             ])
             
bpy.types.Object.ipaneltab3 = EnumProperty(
    name = "haha tab",
    default = 'one',
    items = [('one', '一般设定', '基础的自定义'),
             ('two', '网格', '网格的自定义'),
             ('three', '杂项', '杂项设置页面')
             ])
             
bpy.types.Object.ipaneltab4 = EnumProperty(
    name = "haha tab",
    default = 'one',
    items = [('one', '皮肤', '皮肤的材质'),
             ('two', '眼睛', '眼睛的材质'),
             ('three', '杂项', '杂项')
             ])
             
bpy.types.Object.ipaneltab5 = EnumProperty(
    name = "haha tab",
    default = 'one',
    items = [('one', 'DLC', 'DLC管理菜单'),
             ('two', '父级', '高级父级选项菜单'),
             ('three', '下载', '一个管理下载内容的菜单'),
             ('four', '杂项', '杂项功能菜单')
             ])

bpy.types.Object.ipaneltab6 = EnumProperty(
    name = "haha tab",
    default = 'one',
    items = [('one', '资产', '资产追加菜单'),
             ('two', '预设', '预设追加菜单')
             ])

bpy.types.Object.ipaneltab7 = EnumProperty(
    name = "haha tab",
    default = 'one',
    items = [('one', '导出', '导出设置'),
             ('two', '导入', '导入设置')
             ])

bpy.types.Object.bendstyle = EnumProperty(
    name = "haha tab",
    default = 'one',
    items = [('one', '锐边', '手臂和胳膊的弯曲是尖锐的'),
             ('two', '圆滑', '手臂和胳膊的弯曲时平滑的')
             ])
             
bpy.types.Object.arm_ik_parent_r = EnumProperty(
    name = "haha tab",
    default = 'one',
    items = [('zero', '无', '父级IK'),
             ('one', '根部', '父级IK'),
             ('two', '腰部', '父级IK'),
             ('three', '躯干', '父级IK')
             ])

bpy.types.Object.arm_ik_parent_l = EnumProperty(
    name = "haha tab",
    default = 'one',
    items = [('zero', '无', '父级IK'),
             ('one', '根部', '父级IK'),
             ('two', '腰部', '父级IK'),
             ('three', '躯干', '父级IK')
             ])

bpy.types.Object.dlc_menu_switcher = EnumProperty(
    name = "DLC菜单切换",
    default = 'one',
    items = [
             ('one', '追加', '追加已经下载的资产'),
             ('two', '下载', '下载新资产'),
             ('three', '生成', '生成资产包')
             ])

bpy.types.Object.emissioneye = EnumProperty(
    name = "眼睛自发光",
    default= 'one',
    items = [
             ('one', '两者', '两者'),
             ('two', '右眼', '右眼'),
             ('three', '左眼', '左眼')
             ]
)

bpy.types.Object.mouthtypes = EnumProperty(
    name = "嘴部类型",
    default= 'one',
    items = [
             ('one', 'Ice Cube', 'Ice Cube'),
             ('two', 'Mine-Imator', 'Mine-Imator'),
             ('three', '方形', '放行')
             ]
)

#string properties
bpy.types.Scene.minecraft_username = StringProperty(name="username", description="用户名槽位", default="")

bpy.types.Object.backup_name = StringProperty(name="backup_name", description="备份名称", default="")

bpy.types.Object.dlc_name_load = StringProperty(name="dlc_name_load", description="DLC名称加载", default="")

bpy.types.Object.export_settings_filepath = StringProperty(
    name="export_settings_filepath",
    description="定义导出设置的文件位置",
    subtype='DIR_PATH',
    default="")

bpy.types.Object.import_settings_filepath = StringProperty(
    name="export_settings_filepath",
    description="定义导出设置的文件位置",
    subtype='FILE_PATH',
    default="")

bpy.types.Object.export_settings_name = StringProperty(
    name="export_settings_name",
    description="定义导出设置的文件名称",
    default="")

bpy.types.Object.target_thumbnail_generate = StringProperty(
    name="target_thumbnail_generate",
    description="定义生成资产包的一个PNG文件预览",
    subtype='FILE_PATH',
    default="")

bpy.types.Object.asset_pack_name = StringProperty(
    name="asset_pack_name",
    description="定义生成资产包的名称",
    default="Pack Name")

bpy.types.Object.entry_name_asset = StringProperty(
    name="entry_name_asset",
    description="定义资产包入口的名称",
    default="Entry Name")

bpy.types.Object.asset_author = StringProperty(
    name="asset_author",
    description="定义setting.json里作者名称字段的内容",
    default="Your Name")

bpy.types.Object.asset_version = StringProperty(
    name="asset_version",
    description="定义setting.json里的版本号",
    default="1.0.0")

bpy.types.Object.baked_version_filepath = StringProperty(
    name="baked_version_filepath",
    description="定义已烘焙版本的文件路径",
    subtype='FILE_PATH',
    default="")

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