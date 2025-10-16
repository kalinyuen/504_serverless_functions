import json
import functions_framework

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Expects JSON with lipoprotein lipase (LPL) cholesterol intake (or query params as fallback).
    Returns a JSON classification of LPL cholesterol level.
    """
    # Prefer JSON body; fall back to query parameters for convenience
    data = request.get_json(silent=True) or {}
    args = request.args or {}

    lpl = data.get("lpl", args.get("lpl"))

    # Presence check
    if lpl is None:
        return (
            json.dumps({"error": "'lpl' is required."}),
            400,
            {"Content-Type": "application/json"},
        )

    # Type/convert check
    try:
        lpl_val = float(lpl)
    except (TypeError, ValueError):
        return (
            json.dumps({"error": "'lpl' must be a number."}),
            400,
            {"Content-Type": "application/json"},
        )

    # Conditional statements of LPL level conditions
    if lpl_val <100:
        status = "optimal"
        category = "Optimal (<100 mg/dL)"
    elif lpl_val <130:
        status = "borderline high"
        category = "Borderline High (100-130 mg/dL)"
    else:
        status = "high"
        category = "High (>=160 mg/dL)"

    payload = {
        "lpl intake": lpl_val,
        "status": status,
        "category": category,
    }

    return json.dumps(payload), 200, {"Content-Type": "application/json"}