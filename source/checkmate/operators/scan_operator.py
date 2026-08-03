import bpy
from .. import state
from ..engine.validation_engine import ValidationEngine
from ..engine.scoring_engine import ScoringEngine
from ..engine.report_engine import ReportEngine


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

        engine = ValidationEngine()
        results = engine.run()

        report_engine = ReportEngine()
        report = report_engine.build(results)

        score_engine = ScoringEngine()
        score = score_engine.calculate(results)
        status = score_engine.get_readiness_status(
            score,
            results
        )
        summary = score_engine.get_score_summary(results)

        state.UIState.health_score = str(score)
        state.UIState.readiness_status = status
        state.UIState.issue_summary = summary
        state.UIState.validation_results = results
        state.UIState.validation_report = report
        state.UIState.scan_completed = True
        
        for window in bpy.context.window_manager.windows:
            for area in window.screen.areas:
                area.tag_redraw()

        bpy.app.timers.register(finish_scan, first_interval=2.0)
        self.report({'INFO'}, "Scan started.")
        return {'FINISHED'}