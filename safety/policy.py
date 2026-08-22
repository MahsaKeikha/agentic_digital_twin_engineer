"""Fail-closed engineering governance for F117 Digital Twin Engineer."""

PROTECTED_ACTIONS = {
    "deploy_model",
    "connect_live_control",
    "change_operating_limit",
    "certify_validation",
    "write_control_setpoint",
    "override_safety_interlock",
}

REQUIRED_REVIEWS = (
    "twin_scope_reviewed",
    "data_mapping_reviewed",
    "model_calibration_reviewed",
    "validation_reviewed",
    "uncertainty_reviewed",
    "cybersecurity_reviewed",
    "version_traceability_reviewed",
    "qualified_engineering_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "binding control or certification authority is outside reference-system scope"}

    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required digital-twin review", "missing": missing}

    blockers = []
    if context.get("data_quality_gap"):
        blockers.append("source data quality or mapping gap unresolved")
    if context.get("synchronization_gap"):
        blockers.append("physical-to-digital synchronization gap unresolved")
    if context.get("calibration_gap"):
        blockers.append("model calibration gap unresolved")
    if context.get("validation_gap"):
        blockers.append("validation evidence is incomplete or out of scope")
    if context.get("uncertainty_exceeds_limit"):
        blockers.append("model uncertainty exceeds reviewed operating bounds")
    if context.get("live_control_coupling_risk"):
        blockers.append("unsafe or unreviewed live-control coupling risk detected")
    if context.get("cybersecurity_risk"):
        blockers.append("cybersecurity or access-control risk unresolved")
    if context.get("version_traceability_gap"):
        blockers.append("model, data, or configuration version traceability incomplete")

    if blockers:
        return {"allowed": False, "reason": "digital-twin governance blocker", "blockers": blockers}

    return {"allowed": True, "reason": "digital-twin analysis package approved after qualified human review"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS


def enforce(action: str, approved: bool) -> None:
    if review_required(action) and not approved:
        raise PermissionError("Qualified human approval is required for this action.")
