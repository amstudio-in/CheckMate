import bpy
from .. import state

def finish_scan():
    state.UIState.is_scanning = False
    
    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            area.tag_redraw()
    
    return None

class CHECKMATE_OT_RunScan(bpy.types.Operator):
    """Run CheckMate project scan"""

    bl_idname = "checkmate.run_scan"
    bl_label = "Run Scan"
    bl_description = "Scan the current Blender project"

    def execute(self, context):
        state.UIState.is_scanning = True
        for window in bpy.context.window_manager.windows:
            for area in window.screen.areas:
                area.tag_redraw()

        bpy.app.timers.register(finish_scan, first_interval=2.0)
        self.report({'INFO'}, "Scan started.")
        return {'FINISHED'}