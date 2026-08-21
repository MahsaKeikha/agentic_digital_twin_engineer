from AGENTS.scope_agent import run as a1
from AGENTS.data_mapping_agent import run as a2
from AGENTS.modeling_agent import run as a3
from AGENTS.validation_agent import run as a4
from AGENTS.uncertainty_agent import run as a5
def orchestrate(c): return [a(c) for a in (a1,a2,a3,a4,a5)]