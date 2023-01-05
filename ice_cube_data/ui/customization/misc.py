#Libraries
import bpy

def custom_misc_UI(self, context, layout, obj):
    box = layout.box()
    box.label(text= "WIP MISC尚未完工的杂项", icon= 'COLLAPSEMENU')
    box.label(text= "WARNING: ALL FEATURES HERE ARE EXPERIMENTAL ", icon= 'ERROR')
    box.label(text= "AND MAY CAUSE PROBLEMS!", icon= 'ERROR')
    box.label(text= "警告：所有在此处的特性均为测试性质", icon= 'ERROR')
    box.label(text= "同时可能会导致问题！", icon= 'ERROR')
    b = box.row(align=True)
    if obj.get("line_mouth") == 0:
        b.prop(obj, "line_mouth", icon = "LAYER_USED", text = "卡通嘴部")
    else:
        b.prop(obj, "line_mouth", icon = "LAYER_ACTIVE", text = "卡通嘴部")
    b = box.row(align=True)
    b.operator("append.emotion")

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