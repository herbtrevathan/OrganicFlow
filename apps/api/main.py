"""OrganicFlow local API: deterministic demo runtime with backend approval enforcement."""
from __future__ import annotations
from enum import StrEnum
from pathlib import Path
from typing import Any
from uuid import uuid4
import shutil

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="OrganicFlow API", version="0.1.0")

class RunState(StrEnum):
    CREATED="created"; PLANNING="planning"; WAITING_APPROVAL="waiting_for_approval"; RUNNING="running"; COMPLETED="completed"; FAILED="failed"; CANCELED="canceled"

HIGH_IMPACT={"email.send","filesystem.delete","github.pull_request.write","shell.execute","secrets.use"}
RUNS:dict[str,dict[str,Any]]={}

class DraftRequest(BaseModel):
    prompt:str=Field(min_length=8,max_length=4000)
    timezone:str="America/Denver"

class Approval(BaseModel):
    permission:str
    approved:bool

@app.get("/health")
def health(): return {"status":"ok","mode":"local","codex":{"available":bool(shutil.which("codex"))}}

@app.get("/api/codex")
def codex_status():
    binary=shutil.which("codex")
    return {"available":bool(binary),"path":Path(binary).name if binary else None,"safetyModes":["inspect-only","workspace-edit","local-development","repository-automation"]}

@app.post("/api/workflows/draft")
def draft(req:DraftRequest):
    return {"schemaVersion":1,"id":"important-unread-summary","name":"Important unread email summary","enabled":False,"trigger":{"type":"schedule","config":{"timezone":req.timezone,"expression":"0 8 * * 1-5"}},"permissions":["email.read","reminders.create"],"steps":[{"id":"find","type":"email.search","config":{"query":"is:unread importance:high"}},{"id":"summarize","type":"ai.summarize"},{"id":"remind","type":"reminders.create"}],"limits":{"maxRuntimeSeconds":300,"maxSteps":20,"maxRetries":2}}

@app.post("/api/workflows/{workflow_id}/simulate")
def simulate(workflow_id:str):
    run_id=str(uuid4()); RUNS[run_id]={"id":run_id,"workflowId":workflow_id,"state":RunState.COMPLETED,"events":[{"type":"email.searched","count":5},{"type":"summary.created","count":1},{"type":"reminders.created","count":2}],"sanitized":True}
    return RUNS[run_id]

@app.post("/api/runs/{run_id}/approval")
def approval(run_id:str, decision:Approval):
    run=RUNS.get(run_id)
    if not run: raise HTTPException(404,"Run not found")
    if decision.permission in HIGH_IMPACT and not decision.approved:
        run["state"]=RunState.CANCELED
    run.setdefault("approvals",[]).append(decision.model_dump())
    return run

@app.post("/api/actions/{permission}")
def action(permission:str, approved:bool=False):
    if permission in HIGH_IMPACT and not approved: raise HTTPException(403,"Explicit approval required")
    return {"executed":True,"permission":permission}
