module.exports = {
  apps: [
    {
      name: "fastapi-app",
      script: "uvicorn",
      args: "app.main:app --host 0.0.0.0 --port 8000",
      interpreter: "python3",
      autorestart: true,
      watch: false
    }
  ]
};
