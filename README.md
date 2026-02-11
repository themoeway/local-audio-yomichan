## Running with Docker (No Anki)

The original `local-audio-yomichan` setup plays audio only on the same machine where the server is running. This works well for a desktop Anki workflow, but doesn't work if that machine is powered off, which is a problem for me as I frequently do my cards on my phone.

This fork exists to make `local-audio-yomichan` runnable as a standalone, headless HTTP service in Docker, so card audio remains available even when the desktop is turned off.

### Requirements
- Docker or Docker Compose
- `user_files` directory containing audio data (can be found in the original repo)

### Docker Compose Example

```yaml
services:
  local-audio-yomichan:
    image: ghcr.io/ellesper/local-audio-yomichan:latest
    container_name: local-audio-yomichan
    ports:
      - "5050:5050"
    environment:
      - WO_ANKI=1
      - PYTHONUNBUFFERED=1
    volumes:
      - /mnt/cache/appdata/local-audio-yomichan/user_files:/app/plugin/user_files:rw
    restart: unless-stopped
