import reflex as rx

config = rx.Config(
    app_name="app",
    frontend_port=5000,  # dokku exposes port 5000 by default
    backend_port=8000,
)
