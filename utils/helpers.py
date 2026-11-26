import uuid
def unique_email(): return f"qa.automation.{uuid.uuid4().hex[:12]}@example.com"
