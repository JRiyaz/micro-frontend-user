def get_auth_storage(req: "Request"):
    return req.app.state.auth_db
