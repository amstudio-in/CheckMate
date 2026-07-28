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

        box = layout.box()
        box.label(text="Health Score", icon="INFO")
        box.label(text="--")

        status_box = layout.box()
        status_box.label(text="Project Status", icon="CHECKMARK")
        status_box.label(text="Not Scanned")

        layout.separator()

        layout.operator("checkmate.run_scan", icon="PLAY")

        layout.separator()

        results_box = layout.box()
        results_box.label(text="Validation Results", icon="TEXT")
        results_box.label(text="No scan performed.")