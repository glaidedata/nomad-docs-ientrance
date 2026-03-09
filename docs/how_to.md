# NOMAD Oasis Maintenance Guide ([CLIENT_NAME] Deployment)
<span style="display: block; margin-top: -0.55em; margin-bottom: 0.45em; font-size: 1.150em; color: gray;"><em>Created by</em> <a href="https://www.glaidedata.com/" target="_blank" rel="noopener"><img src="assets/glaide_logo_long_white.png" alt="Glaide logo" style="height: 1.986em; vertical-align: middle;" /></a></span>

This document describes the operational and maintenance procedures for the NOMAD Oasis instance deployed on the [CLIENT_NAME] server. It covers updating software components, managing images, handling certificates, applying configuration changes, and performing routine system checks.

## 1. Updating the NOMAD Oasis Software

### 1.1 Updating the Deployment Repository
The [CLIENT_NAME] deployment uses the following repository:

**Deployment Repository:** [[GITHUB_REPO_URL]]([GITHUB_REPO_URL])

Any changes to plugin configuration, included/excluded modules, image-writing configuration, or deployment files (e.g., `nomad.yaml`, plugin folders) must be committed into this repository. 

Commit or merge actions to the repository automatically trigger the image-building process via GitHub Actions.

### 1.2 Image Building and Publishing
When activity occurs on the GitHub repository:

* Pushing to `main` builds and publishes `[GHCR_IMAGE_PATH]:main`
* Publishing a Release (tagged version) builds and publishes `[GHCR_IMAGE_PATH]:vX.Y.Z` (e.g. `v1.0.0`). A tagged version produces a stable, reproducible, frozen build.

### 1.3 Updating the Running Deployment
The server deployment uses the images specified in `docker-compose.yaml`. To update the deployed Oasis:

1. Edit `docker-compose.yaml` and ensure image references match the intended build, e.g.: `[GHCR_IMAGE_PATH]:v1.0.0` (or use `:main`).
2. Pull the updated images on the server: `docker compose pull`
3. Restart containers: `docker compose up -d`
4. Verify active images: `docker compose images`

## 2. Versioning and Release Policy

### 2.1 Recommended Practice

* Production servers should use tagged versions (`v1.0.0`, `v1.1.0`, etc.).
* `main` should only be used during development or testing, as it changes continuously.
* Each new stable configuration should result in a GitHub Release.

### 2.2 Creating a Release
Releases should be created through the GitHub web interface:

1. Open Releases → Draft a new release
2. Assign a tag (e.g., `v1.1.0`)
3. Publish the release
4. GitHub Actions automatically builds and publishes the release image

This ensures fully reproducible deployments.

## 3. Updating Configuration Files on the Server
Configuration updates should be made in the GitHub repository whenever possible.
Local modifications to deployment files on the server should be avoided.

### 3.1 Viewing local changes
`git diff`

### 3.2 If remote changes exist
Before pulling updates, commit or stash local changes:

`git add .`
`git commit -m "Local modifications"`
`git pull`

or:

`git stash`
`git pull`
`git stash pop`

## 4. SSL Certificate Renewal
The [CLIENT_NAME] Oasis instance uses CA-issued TLS certificates.

### 4.1 Renewal Process Overview

1. Obtain renewal certificates.
2. Replace certificate files inside the repository (usually under `/ssl/`).
    If the key is encrypted, decrypt it:
    - `sudo mv selfsigned.key selfsigned.key.encrypted`
    - `sudo openssl pkey -in selfsigned.key.encrypted -out selfsigned.key`

3. Apply correct permissions:
    - `sudo chown root:root selfsigned.*` 
    - `sudo chmod 600 selfsigned.key`
    - `sudo chmod 644 selfsigned.crt`

4. Restart proxy:
`docker compose restart proxy`

5. Verify HTTPS:
`curl -I https://<server>`

## 5. Regular System Maintenance Tasks

### 5.1 Check system resource usage

- `df -h       # disk usage`
- `free -h     # memory`
- `docker ps   # running containers`
- `docker logs <container>`

### 5.2 Restarting the Oasis

- `docker compose down`
- `docker compose up -d`

### 5.3 Cleaning unused Docker images

- `docker image prune -a`

(Use with care — only after verifying which images are in use.)

## 6. Backup and Restore Strategy

### 6.1 Recommended backup items

- NOMAD data volume (`.volumes/fs`)
- MongoDB data volume
- Elasticsearch indices
- Uploaded files
- User-generated metadata
- SSL certificates
- `docker-compose.yaml + .env`

## 7. Troubleshooting

### 7.1 Check logs

- `docker compose logs app`
- `docker compose logs proxy`
- `docker compose logs worker`
- `docker compose logs north`

### 7.2 Image is not updating / UI shows old version
If old content or a previous version of the user interface appears after an update, check the following:

1. Is the image tag correct in `docker-compose.yaml`?
2. Was the image pulled correctly?
    - `docker compose pull`
    - `docker compose images`
3. Were the containers restarted?
    - `docker compose up -d`
4. Are the packages publicly visible in the container registry?
5. **Clear the Browser Cache** (most common cause of outdated UI)
    Web browsers cache static UI files (JavaScript, CSS) very aggressively. As a result, the old UI often appears even if the server is already delivering the new version.

    Hard Reload (browser reloads files without using cache):
    - Ctrl + F5
    - Shift + F5
    - Ctrl + Shift + R

    Clear cache completely:
    - Ctrl + Shift + Del

    Alternative quick tests:
    - Open the URL in an incognito/private window
    - Use a different browser

    In most cases, a browser cache reload is sufficient to make the updated UI visible.

## 8. Deployment Workflow Summary

1. Update code in the deployment repository.
2. Commit and push changes.
3. CI/CD Pipeline builds the image.
4. Create a GitHub Release for stable versions.
5. Update `docker-compose.yaml` on the server.
6. Pull and restart containers.
7. Verify functionality.