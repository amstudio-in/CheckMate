class UIState:

    is_scanning = False
    
    health_score = "--"
    readiness_status = "Not Scanned"
    issue_summary = "Run a scan to view issues."

    scan_completed = False
    validation_results = []
    validation_report = {}
    expanded_groups = set()