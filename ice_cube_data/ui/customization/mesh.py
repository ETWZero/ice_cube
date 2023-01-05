#Libraries
import bpy

def custom_mesh_UI(self, context, layout, obj):
    box = layout.box()
    box.label(text= "形变", icon= 'OUTLINER_OB_MESH')
    box1 = box.box()
    box1.label(text= "凹凸", icon= 'MESH_ICOSPHERE')
    b = box1.row(align=True)
    if obj.get("bodybulge") == 0:
        b.prop(obj, "bodybulge", icon = "LAYER_USED", text = "身体凹凸")
    else:
        b.prop(obj, "bodybulge", icon = "LAYER_ACTIVE", text = "身体凸起")
    b = box1.row(align=True)
    if obj.get("bulge_arm_r") == 0:
        b.prop(obj, "bulge_arm_r", icon = "LAYER_USED", text = "右臂凹凸")
    else:
        b.prop(obj, "bulge_arm_r", icon = "LAYER_ACTIVE", text = "右臂凹凸")
    if obj.get("bulge_arm_l") == 0:
        b.prop(obj, "bulge_arm_l", icon = "LAYER_USED", text = "左臂凹凸")
    else:
        b.prop(obj, "bulge_arm_l", icon = "LAYER_ACTIVE", text = "左臂凹凸")
    b = box1.row(align=True)
    if obj.get("bulge_leg_r") == 0:
        b.prop(obj, "bulge_leg_r", icon = "LAYER_USED", text = "右腿凹凸")
    else:
        b.prop(obj, "bulge_leg_r", icon = "LAYER_ACTIVE", text = "右腿凹凸")
    if obj.get("bulge_arm_l") == 0:
        b.prop(obj, "bulge_leg_l", icon = "LAYER_USED", text = "左腿凹凸")
    else:
        b.prop(obj, "bulge_leg_l", icon = "LAYER_ACTIVE", text = "左腿凹凸")
        
    box1 = box.box()
    box1.label(text= "Squish挤压", icon= 'OUTLINER_OB_LATTICE')
    b = box1.row(align=True)
    if obj.get("squish_body") == 0:
        b.prop(obj, "squish_body", icon = "LAYER_USED", text = "身体挤压")
    else:
        b.prop(obj, "squish_body", icon = "LAYER_ACTIVE", text = "身体挤压")
    if obj.get("squish_head") == 0:
        b.prop(obj, "squish_head", icon = "LAYER_USED", text = "身体挤压")
    else:
        b.prop(obj, "squish_head", icon = "LAYER_ACTIVE", text = "身体挤压")
    b = box1.row(align=True)
    if obj.get("squish_arm_r") == 0:
        b.prop(obj, "squish_arm_r", icon = "LAYER_USED", text = "右臂挤压")
    else:
        b.prop(obj, "squish_arm_r", icon = "LAYER_ACTIVE", text = "右臂挤压")
    if obj.get("squish_arm_l") == 0:
        b.prop(obj, "squish_arm_l", icon = "LAYER_USED", text = "左臂挤压")
    else:
        b.prop(obj, "squish_arm_l", icon = "LAYER_ACTIVE", text = "左臂挤压")
    b = box1.row(align=True)
    if obj.get("squish_leg_r") == 0:
        b.prop(obj, "squish_leg_r", icon = "LAYER_USED", text = "右腿挤压")
    else:
        b.prop(obj, "squish_leg_r", icon = "LAYER_ACTIVE", text = "右腿挤压")
    if obj.get("squish_arm_l") == 0:
        b.prop(obj, "squish_leg_l", icon = "LAYER_USED", text = "左腿挤压")
    else:
        b.prop(obj, "squish_leg_l", icon = "LAYER_ACTIVE", text = "左腿挤压")
        
    box1 = box.box()
    box1.label(text= "锥化", icon= 'EDITMODE_HLT')
    b = box1.row(align=True)
    if obj.get("leg_deform") == 0:
        b.prop(obj, "leg_deform", icon = "RIGHTARROW", text = "肢体形变")
    else:
        b.prop(obj, "leg_deform", icon = "DOWNARROW_HLT", text = "肢体形变")
        b = box1.row(align=True)
        b.prop(obj, "armtaper", icon = "LAYER_USED", text = "手臂锥化强度")
        b = box1.row(align=True)
        b.prop(obj, "leg_taper_strength", icon = "LAYER_USED", text = "腿部下侧锥化强度")
        b = box1.row(align=True)
        b.prop(obj, "leg_taper_strength2", icon = "LAYER_USED", text = "腿部上侧锥化强度")
    b = box1.row(align=True)
    if obj.get("body_deforms") == 0:
        b.prop(obj, "body_deforms", icon = "RIGHTARROW", text = "身体形变")
    else:
        b.prop(obj, "body_deforms", icon = "DOWNARROW_HLT", text = "身体形变")
        b = box1.row(align=True)
        if obj.get("breastswitch") == 0:
            b.prop(obj, "breastswitch", icon = "RIGHTARROW", text = "胸部")
        else:
            b.prop(obj, "breastswitch", icon = "DOWNARROW_HLT", text = "胸部")
            b = box1.row(align=True)
            b.prop(obj, "breastsize", text = "尺寸")
            b.prop(obj, "breastweight", text = "权重")
            b = box1.row(align=True)
            b.prop(obj, "breastshape", text = "形状")

        b = box1.row(align=True)
        if obj.get("hip") == 0:
            b.prop(obj, "hip", icon = "RIGHTARROW", text = "腰部")
        else:
            b.prop(obj, "hip", icon = "DOWNARROW_HLT", text = "腰部")
        b = box1.row(align=True)
        b.prop(obj, "upperbodywidth", icon = "DOWNARROW_HLT", text = "肩膀宽度")
        b = box1.row(align=True)
        if obj.get("lowerbodywidth") == 0:
            b.prop(obj, "lowerbodywidth", icon = "RIGHTARROW", text = "臀部（正常）")
        else:
            if obj.get("lowerbodywidth") < 0:
                b.prop(obj, "lowerbodywidth", text = "臀部（宽）")
            elif obj.get("lowerbodywidth") > 0:
                b.prop(obj, "lowerbodywidth", text = "臀部（窄）")
            else:
                b.prop(obj, "lowerbodywidth", text = "臀部（正常）")
        b.prop(obj, "bodytopround", icon = "RIGHTARROW", text = "躯体上部圆化")
    b = box1.row(align=True)
    if obj.get("eyebrowdeform") == 0:
        b.prop(obj, "eyebrowdeform", icon = "RIGHTARROW", text = "眉毛形变")
    else:
        b.prop(obj, "eyebrowdeform", icon = "DOWNARROW_HLT", text = "眉毛形变")
        b = box1.row(align=True)
        b.prop(obj, "eyebrowheight", text = "眉毛长度")
        b.prop(obj, "eyebrowlength", text = "眉毛宽度")
        b = box1.row(align=True)
        b.prop(obj, "eyebrowtaper1", text = "眉毛锥化参数1")
        b.prop(obj, "eyebrowtaper2", text = "眉毛锥化参数2")
    box1 = box.box()
    box1.label(text= "Face", icon= 'CAMERA_STEREO')
    b = box1.row(align=True)
    b.prop(obj, "eyedepth", text = "眼睛深度")
    b = box1.row(align=True)
    b.prop(obj, "mouthdepth", text = "嘴部深度")
    b.prop(obj, "innermouthdepth", text = "内侧嘴部深度")

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