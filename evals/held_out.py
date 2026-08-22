from orchestration.orchestrator import orchestrate


def base():
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


SCENARIOS = [
    ({}, False),
    (base(), True),
    ({**base(), "qualified_engineering_approval": False}, False),
    ({**base(), "data_quality_gap": True}, False),
    ({**base(), "synchronization_gap": True}, False),
    ({**base(), "calibration_gap": True}, False),
    ({**base(), "validation_gap": True}, False),
    ({**base(), "uncertainty_exceeds_limit": True}, False),
    ({**base(), "live_control_coupling_risk": True}, False),
    ({**base(), "cybersecurity_risk": True}, False),
]


def main():
    passed = 0
    for context, expected in SCENARIOS:
        passed += orchestrate(context)["release_allowed"] is expected
    print(f"held-out: {passed}/{len(SCENARIOS)} passed")
    raise SystemExit(0 if passed == len(SCENARIOS) else 1)


if __name__ == "__main__":
    main()
