from orchestration.orchestrator import orchestrate

REFERENCE_CONTEXT = {
    "twin_scope_reviewed": True,
    "data_mapping_reviewed": True,
    "model_calibration_reviewed": True,
    "validation_reviewed": True,
    "uncertainty_reviewed": True,
    "cybersecurity_reviewed": True,
    "version_traceability_reviewed": True,
    "qualified_engineering_approval": True,
}

if __name__ == "__main__":
    print(orchestrate(REFERENCE_CONTEXT))
