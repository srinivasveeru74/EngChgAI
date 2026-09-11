from dataclasses import dataclass
 
RULES = [
    ("ho_complete",   30, lambda co: co.ho_fields_missing == 0),
    ("pn_approved",   25, lambda co: co.unapproved_pns == 0),
    ("oms_bom_match", 25, lambda co: co.oms_bom_deltas == 0),
    ("owner_named",   10, lambda co: bool(co.owner)),
    ("rohs_flagged",  10, lambda co: co.rohs_flag_present),
]
 
@dataclass
class Result:
    score: int
    failures: list
    route: str
 
def score_co(co) -> Result:
    total, failed = 0, []
    for name, weight, check in RULES:
        if check(co):
            total += weight
        else:
            failed.append(name)
    route = "ROUTE" if total >= 85 else "HOLD"
    return Result(score=total, failures=failed, route=route
