import bpy
for i in range(0,5):
     cubos=bpy.ops.mesh.primitive_cube_add(location=(0,0,0))
     nombre="Cubo"+str(i)
     bpy.context.object.name=nombre
     bpy.data.objects[nombre].location=(i,0,0)
     
     nombrezx1="Cubozx1_"+str(i)
     bpy.context.object.name=nombrezx1
     bpy.data.objects[nombrezx1].location=(i,0,1)
     
     nombrezx2="Cubozx2_"+str(i)
     bpy.context.object.name=nombrezx2
     bpy.data.objects[nombrezx2].location=(i,0,2)
     
     nombrezx3="Cubozx3_"+str(i)
     bpy.context.object.name=nombrezx3
     bpy.data.objects[nombrezx3].location=(i,0,3)
     
     nombrezx4="Cubozx4_"+str(i)
     bpy.context.object.name=nombrezx4
     bpy.data.objects[nombrezx4].location=(i,0,4)
