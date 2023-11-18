def get_seches():
    return "SELECT to_json(result) FROM (SELECT * FROM sech) result"

def get_sech(num_sech: int) -> str:
    return f"SELECT to_json(result) FROM (SELECT * FROM sech WHERE sech.num_sech = {num_sech}) result"