import json
import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger1")
def http_trigger1(req: func.HttpRequest) -> func.HttpResponse: 
    """HTTP Azure Function.
    Expects JSON with lipoprotein lipase (LPL) cholesterol intake (or query params as fallback).
    Returns a JSON classification of LPL cholesterol level.
    """
    # Prefer JSON body; fall back to query parameters for convenience
    try:
        data = req.get_json()
    except ValueError:
        data = {}

    args = req.params

    lpl = data.get("lpl", args.get("lpl"))

    # Presence check
    if lpl is None:
        return func.HttpResponse(
           body= json.dumps({"error": "'lpl' is required."}),
            status_code=400,
            headers={"Content-Type": "application/json"},
        )

    # Type/convert check
    try:
        lpl_val = float(lpl)
    except (TypeError, ValueError):
        return func.HttpResponse(
            body= json.dumps({"error": "'lpl' must be a number."}),
            status_code=400,
            headers={"Content-Type": "application/json"},
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
        "lpl intake": lpl,
        "status": status,
        "category": category,
    }

    return func.HttpResponse(
        body= json.dumps(payload), 
        status_code=200, 
        headers={"Content-Type": "application/json"}
    )