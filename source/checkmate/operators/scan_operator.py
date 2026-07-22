print("Loading scan_operator.py")

import bpy


class CHECKMATE_OT_RunScan(bpy.types.Operator):
    """Run CheckMate project scan"""

    bl_idname = "checkmate.run_scan"
    bl_label = "Run Scan"
    bl_description = "Scan the current Blender project"

    def execute(self, context):
        self.report({'INFO'}, "Scan started.")
        return {'FINISHED'}