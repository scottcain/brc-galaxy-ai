# Running Gemini CLI in Docker

This Dockerfile allows you to run `gemini` in a containerized environment.

### 1. Build the image
```bash
docker build -t gemini-cli -f Dockerfile.gemini .
```

### 2. Run the container
To run the CLI interactively:
```bash
docker run -it 
  -v $(pwd):/app 
  -e GEMINI_API_KEY=YOUR_API_KEY_HERE 
  gemini-cli
```

### 3. Run in YOLO mode (No permission prompts)
To run a command and have it execute without asking for permission:
```bash
docker run -it 
  -v $(pwd):/app 
  -e GEMINI_API_KEY=YOUR_API_KEY_HERE 
  gemini-cli -p "Analyze this directory and fix bugs" --approval-mode=yolo
```

### Notes
- **Volume Mounting:** `-v $(pwd):/app` mounts your current directory into the container so Gemini can see and modify your files.
- **API Key:** Ensure you provide your `GEMINI_API_KEY` as an environment variable.
- **Shell Commands:** The container includes `curl`, `git`, and `python3`. If your project needs more (e.g., `go`, `rust`, `java`), add them to the `RUN apt-get install` section in the `Dockerfile.gemini`.
