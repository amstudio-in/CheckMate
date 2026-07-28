import bpy
from .. import state

class CHECKMATE_PT_MainPanel(bpy.types.Panel):
    """Main CheckMate panel"""

    bl_label = "CheckMate"
    bl_idname = "CHECKMATE_PT_main_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "CheckMate"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Project Validation Assistant")
        layout.separator()

        box = layout.box()
        box.label(text="Health Score", icon="INFO")
        if state.UIState.is_scanning:
            box.label(text="Calculating...")
        else:
            box.label(text=state.UIState.health_score)

        status_box = layout.box()
        status_box.label(text="Readiness Status", icon="CHECKMARK")
        if state.UIState.is_scanning:
            status_box.label(text="Scanning...")
        else:
            status_box.label(text=state.UIState.readiness_status)

        issue_box = layout.box()
        issue_box.label(text="Issue Summary", icon="ERROR")
        if state.UIState.is_scanning:
            issue_box.label(text="Analyzing...")
        else:
            issue_box.label(text=state.UIState.issue_summary)

        layout.separator()

        if state.UIState.is_scanning:
            row = layout.row()
            row.enabled = False
            row.operator(
                "checkmate.run_scan",
                text="Scanning...",
                icon="TIME"
            )
        else:
            layout.operator(
                "checkmate.run_scan",
                text="Run Scan",
                icon="PLAY"
            )

        layout.separator()

        results_box = layout.box()
        results_box.label(text="Validation Results", icon="TEXT")
        if state.UIState.is_scanning:
            results_box.label(text="Checking project...")
        else:
            results_box.label(text=state.UIState.validation_results)