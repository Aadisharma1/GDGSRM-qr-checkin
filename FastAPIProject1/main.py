
from fastapi import FastAPI
from app.routes import auth, events, registration, admin

app = FastAPI(title="QR-Based Event Check-In System")

# Include Routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(events.router, prefix="/events", tags=["Events"])
app.include_router(registration.router, prefix="/registration", tags=["Registration"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
