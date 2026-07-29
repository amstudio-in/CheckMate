import bpy
from .. import state
from ..validation.severity import Severity

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
        elif not state.UIState.scan_completed:
            results_box.label(text="No scan performed.")
        elif not state.UIState.validation_results:
            results_box.label(text="No issues found.")
        else:
            for result in state.UIState.validation_results:
                if result.severity == Severity.ERROR:
                    icon = "ERROR"
                elif result.severity == Severity.WARNING:
                    icon = "QUESTION"
                else:
                    icon = "INFO"
                results_box.label(text=result.title, icon=icon)