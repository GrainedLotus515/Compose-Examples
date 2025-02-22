https://github.com/epoupon/lms

The music and config folders must be created before starting up the compose stack. Here are some commands to do so:
```bash
# first create the folders
sudo mkdir -p ${DOCKER_VOLUME_STORAGE:-/mnt/docker-volumes}/lms/{music,configs}

# now adjust permissions
sudo chown -R 1000:1000 ${DOCKER_VOLUME_STORAGE:-/mnt/docker-volumes}/lms/
sudo chmod -R 775 ${DOCKER_VOLUME_STORAGE:-/mnt/docker-volumes}/lms/
```