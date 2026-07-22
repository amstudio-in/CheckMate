import bpy


class CHECKMATE_PT_MainPanel(bpy.types.Panel):
    """Main CheckMate panel"""

    bl_label = "CheckMate"
    bl_idname = "CHECKMATE_PT_main_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "CheckMate"

    def draw(self, context):
        layout = self.layout

        layout.label(text="Welcome to CheckMate")