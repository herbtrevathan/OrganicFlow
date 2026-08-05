from fastapi.testclient import TestClient
from apps.api.main import app
c=TestClient(app)
def test_health(): assert c.get('/health').json()['mode']=='local'
def test_draft_is_disabled_and_safe():
    d=c.post('/api/workflows/draft',json={'prompt':'Every weekday summarize my important unread email'}).json()
    assert d['enabled'] is False and 'email.read' in d['permissions']
def test_high_impact_requires_approval(): assert c.post('/api/actions/email.send').status_code==403
