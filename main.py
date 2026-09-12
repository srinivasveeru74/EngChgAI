from fastapi import FastAPI
from app.connectors.enovia_sim import EnoviaSim
from app.connectors.sharepoint_sim import SharePointSim
from app.scoring import score_co
from app.models import ChangeOrder

app = FastAPI(title=“Readiness Pilot”)
enovia, sp = EnoviaSim(), SharePointSim()

@app.get(“/api/readiness/{co_id}”)
def readiness(co_id: str):
    co = ChangeOrder(**enovia.get_change_order(co_id))
    r = score_co(co)
    sp.log_result(co_id, r.score, r.route, r.failures)
    return {“co”: co_id, “score”: r.score,
            “route”: r.route, “missing”: r.failures}
