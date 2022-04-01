# deployment_practices
Deployment practices


docker volume create --driver local --name varlogs --opt type=none --opt device=/var/folder_name/ --opt o=uid=root,gid=root --opt o=bind

docker run -itd --restart unless-stopped --name image_name --env-file env.txt -v varlogs:/var/folder_name -h=`hostname`_01 hub.docker.com_docker_iamge_path

docker logs -f image_name

