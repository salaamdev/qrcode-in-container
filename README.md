# Running a qrcode generator in docker

**This is a personal project that i used to remind myself basic docker commands.**

## How to run

```bash

# clone this repo first

# Build the docker image
docker build -t qrcode_generator .

# Run the docker image
# Linux/Windows - Bash
docker run --rm -v "$(pwd -W)":/app qrcode-generator

# Windows - CMD
docker run --rm -v "%cd%":/app qrcode-generator
```
