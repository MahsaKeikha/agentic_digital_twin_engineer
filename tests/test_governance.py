from orchestration.orchestrator import orchestrate
from safety.policy import authorize


def valid_context():
    return {
        "twin_scope_reviewed": True,
        "data_mapping_reviewed": True,
        "model_calibration_reviewed": True,
        "validation_reviewed": True,
        "uncertainty_reviewed": True,
        "cybersecurity_reviewed": True,
        "version_traceability_reviewed": True,
        "qualified_engineering_approval": True,
    }


def test_complete_review_can_release_analysis_package():
    result = orchestrate(valid_context())
    assert result["release_allowed"] is True
    assert result["autonomous_live_control_authority"] is False


def test_missing_engineering_approval_fails_closed():
    context = valid_context()
    context["qualified_engineering_approval"] = False
    assert orchestrate(context)["release_allowed"] is False


def test_live_control_connection_is_never_autonomous():
    assert authorize("connect_live_control", valid_context())["allowed"] is False


def test_data_quality_gap_blocks_release():
    context = valid_context()
    context["data_quality_gap"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_calibration_gap_blocks_release():
    context = valid_context()
    context["calibration_gap"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_validation_gap_blocks_release():
    context = valid_context()
    context["validation_gap"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_cybersecurity_risk_blocks_release():
    context = valid_context()
    context["cybersecurity_risk"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_version_traceability_gap_blocks_release():
    context = valid_context()
    context["version_traceability_gap"] = True
    assert orchestrate(context)["release_allowed"] is False
