#Libraries
import bpy

def bone_layers_UI(self, context, layout):
    layers = context.active_object.data
    box = layout.box()
    box.label(text= "骨骼层", icon= 'RENDERLAYERS')
    box1 = box.box()
    b = box1.row(align=True)
    b.label(text= "面部", icon= 'MODIFIER')
    b = box1.row(align=True)
    b.prop(layers, 'layers', index=0, toggle=True, text='模型主要骨骼') 
    b.prop(layers, 'layers', index=23, toggle=True, text='脸部控制器')

    row = layout.row()
    split = row.split(factor=0.5, align=True)
    c = split.column()
    box1 = box.box()
    box1.label(text= "胳臂", icon= 'MODIFIER')
    b = box1.row(align=True)
    b.prop(layers, 'layers', index=1, toggle=True, text='右臂IK')

    b.prop(layers, 'layers', index=2, toggle=True, text='左臂IK')

    b = box1.row(align=True)

    b.prop(layers, 'layers', index=17, toggle=True, text='右臂FK')

    b.prop(layers, 'layers', index=18, toggle=True, text='左臂FK')

    b = box1.row(align=True)

    b.prop(layers, 'layers', index=5, toggle=True, text='右手手指')

    b.prop(layers, 'layers', index=21, toggle=True, text='左手手指')

    box1 = box.box()
    box1.label(text= "腿部", icon= 'MODIFIER')
    b = box1.row(align=True)
    b.prop(layers, 'layers', index=3, toggle=True, text='右腿IK')
    b.prop(layers, 'layers', index=4, toggle=True, text='左腿IK')
    b = box1.row(align=True)
    b.prop(layers, 'layers', index=19, toggle=True, text='右腿FK')
    b.prop(layers, 'layers', index=20, toggle=True, text='左腿FK')

    box1 = box.box()
    box1.label(text= "微调骨骼", icon= 'MODIFIER')
    b = box1.row(align=True)

    b.prop(layers, 'layers', index=7, toggle=True, text='身体微调')
    b.prop(layers, 'layers', index=16, toggle=True, text='面部微调')
    b = box1.row(align=True)
    b.prop(layers, 'layers', index=8, toggle=True, text='右臂微调')
    b.prop(layers, 'layers', index=9, toggle=True, text='左臂微调')
    b = box1.row(align=True)
    b.prop(layers, 'layers', index=24, toggle=True, text='右腿微调')
    b.prop(layers, 'layers', index=25, toggle=True, text='左腿微调')

    box1 = box.box()
    box1.label(text= "杂项", icon= 'MODIFIER')
    b = box1.row(align=True)
    b.prop(layers, 'layers', index=10, toggle=True, text='肢体扭转')
    b = box1.row(align=True)
    b.prop(layers, 'layers', index=6, toggle=True, text='动态头发')
    b = box1.row(align=True)
    b.prop(layers, 'layers', index=22, toggle=True, text='额外骨骼')
    b = box1.row(align=True)
    b.prop(layers, 'layers', index=26, toggle=True, text='脚部旋转')
    b = box1.row(align=True)
    b.prop(layers, 'layers', index=15, toggle=True, text='表情骨骼')

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