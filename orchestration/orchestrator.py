from AGENTS.scope_agent import run as scope
from AGENTS.data_mapping_agent import run as data_mapping
from AGENTS.modeling_agent import run as modeling
from AGENTS.validation_agent import run as validation
from AGENTS.uncertainty_agent import run as uncertainty
from safety.policy import authorize


def orchestrate(context: dict) -> dict:
    """Run digital-twin specialists and apply fail-closed engineering governance."""
    results = [
        scope(context),
        data_mapping(context),
        modeling(context),
        validation(context),
        uncertainty(context),
    ]
    governance = authorize("digital_twin_release", context)
    return {
        "system": "F117",
        "results": results,
        "governance": governance,
        "release_allowed": governance["allowed"],
        "human_engineering_review_required": True,
        "autonomous_live_control_authority": False,
        "autonomous_validation_certification_authority": False,
    }
