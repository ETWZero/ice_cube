#Libraries
import bpy

def parenting_UI(self, context, layout, rig_baked):
    box = layout.box()
    obj = context.object
                
    b = box.row(align=True)
    b.operator("parent.head", text="头部父级")
    b = box.row(align=True)
    if obj.get("Body_Bend_Half") == True:
        b.prop(obj, "Body_Bend_Half", text="",icon='SORT_ASC')
    else:
        b.prop(obj, "Body_Bend_Half", text="",icon='SORT_DESC')
    b.operator("parent.body", text="身体父级")
    if obj.get("Body_Bend_Half") == True:
        b.prop(obj, "Body_Bend_Half", text="",icon='SORT_ASC')
    else:
        b.prop(obj, "Body_Bend_Half", text="",icon='SORT_DESC')
    b = box.row(align=True)

    if obj.get("R_A_Half") == True:
        b.prop(obj, "R_A_Half", text="",icon='SORT_ASC')
    else:
        b.prop(obj, "R_A_Half", text="",icon='SORT_DESC')

    b.operator("parent.rightarm", text="右臂父级")
    b.operator("parent.leftarm", text="左臂父级")

    if obj.get("L_A_Half") == True:
        b.prop(obj, "L_A_Half", text="",icon='SORT_ASC')
    else:
        b.prop(obj, "L_A_Half", text="",icon='SORT_DESC')

    b = box.row(align=True)
    if obj.get("R_L_Half") == True:
        b.prop(obj, "R_L_Half", text="",icon='SORT_ASC')
    else:
        b.prop(obj, "R_L_Half", text="",icon='SORT_DESC')
    b.operator("parent.rightleg", text="右腿父级")
    b.operator("parent.leftleg", text="左腿父级")

    if obj.get("L_L_Half") == True:
        b.prop(obj, "L_L_Half", text="",icon='SORT_ASC')
    else:
        b.prop(obj, "L_L_Half", text="",icon='SORT_DESC')

    
    box = layout.box()
    box.label(text= "重要信息", icon= 'HELP')
    b = box.row(align=True)
    b = box.row(align=True)
    ###
    b.label(text= "为了确保对模型添加父级关系时能继承所有特性，")
    b = box.row(align=True)
    b.label(text= "请在物体后面添加合适的后缀，之后点击相应的按钮。")
    b = box.row(align=True)
    ###
    b = box.row(align=True)
    b.label(text= "Head Suffix头部后缀: \"_HeadChild\"", icon= 'OUTLINER_OB_ARMATURE')
    b = box.row(align=True)
    b.label(text= "Body Suffix身体后缀: \"_BodyChild\"", icon= 'OUTLINER_OB_ARMATURE')
    b = box.row(align=True)
    b.label(text= "Right Arm Suffix右臂后缀: \"_RightArmChild\"", icon= 'OUTLINER_OB_ARMATURE')
    b = box.row(align=True)
    b.label(text= "Left Arm Suffix左臂后缀: \"_LeftArmChild\"", icon= 'OUTLINER_OB_ARMATURE')
    b = box.row(align=True)
    b.label(text= "Right Leg Suffix右腿后缀: \"_RightLegChild\"", icon= 'OUTLINER_OB_ARMATURE')
    b = box.row(align=True)
    b.label(text= "Left Leg Suffix左腿后缀: \"_LeftLegChild\"", icon= 'OUTLINER_OB_ARMATURE')
    b = box.row(align=True)
    ###
    b = box.row(align=True)
    b.label(text= "如果你需要忽略掉特定肢体的弯曲，")
    b = box.row(align=True)
    b.label(text="只需要在上面的后缀后面添加\"_IgnoreBend\"后缀，")
    b = box.row(align=True)
    b.label(text="同时确保已经选择上方还是下方的父级。")
    ###

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