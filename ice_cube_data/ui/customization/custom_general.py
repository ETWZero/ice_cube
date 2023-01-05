#Libraries
import bpy

def customization_general_UI(self, context, layout, obj):
    box = layout.box()
    box.label(text= "通用", icon= 'SETTINGS')
    b = box.row(align=True)
    if obj.get("eyelashes") == 0:
        b.prop(obj, "eyelashes", icon = "LAYER_USED", text = "睫毛")
    else:
        b.prop(obj, "eyelashes", icon = "LAYER_ACTIVE", text = "睫毛")
    b = box.row(align=True)
    if obj.get("jaw") == 0:
        b.prop(obj, "jaw", icon = "RIGHTARROW", text = "下巴")
    else:
        b.prop(obj, "jaw", icon = "DOWNARROW_HLT", text = "下巴设置")
        if obj.get("round_jaw") == 0:
            b.prop(obj, "round_jaw", icon = "LAYER_USED", text = "平展")
        else:
            b.prop(obj, "round_jaw", icon = "LAYER_ACTIVE", text = "圆滑")
        b = box.row(align=True)
        b.prop(obj, "jaw_strength", text = "Strength", slider = True)
    b = box.row(align=True)
    if obj.get("bevelmouth") == 0:
        b.prop(obj, "bevelmouth", icon = "RIGHTARROW", text = "倒角")
    else:
        b.prop(obj, "bevelmouth", icon = "DOWNARROW_HLT", text = "倒角")
        b = box.row(align=True)
        b.prop(obj, "bevelmouthstrength", text = "嘴部倒角力度", slider = True)
    b = box.row(align=True)
    if obj.get("teeth_cartoon") == 0:
        b.prop(obj, "teeth_cartoon", icon = "LAYER_USED", text = "卡通牙齿")
    else:
        b.prop(obj, "teeth_cartoon", icon = "LAYER_ACTIVE", text = "卡通牙齿")
    if obj.get("teeth_bool") == 0:
        b.prop(obj, "teeth_bool", icon = "LAYER_USED", text = "布尔牙齿")
    else:
        b.prop(obj, "teeth_bool", icon = "LAYER_ACTIVE", text = "布尔牙齿")
    b = box.row(align=True)
    if obj.get("tongue") == 0:
        b.prop(obj, "tongue", icon = "LAYER_USED", text = "舌头")
    else:
        b.prop(obj, "tongue", icon = "LAYER_ACTIVE", text = "舌头")
    if obj.get("dynamichair") == 0:
        b.prop(obj, "dynamichair", icon = "LAYER_USED", text = "动态头发")
    else:
        b.prop(obj, "dynamichair", icon = "LAYER_ACTIVE", text = "动态头发")

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