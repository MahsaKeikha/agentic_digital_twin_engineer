def authorize(action,human_approved=False):
 c={"deploy_model","connect_live_control","change_operating_limit","certify_validation"}
 return human_approved if action in c else True