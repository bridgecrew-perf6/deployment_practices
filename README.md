# Deployment Practices
## Docker
I have added a basic example of Docker usage, with the usage of Docker volumes to store the logs/data in the disk.
{{< highlight html >}}
docker volume create --driver local --name varlogs --opt type=none --opt device=/var/folder_name/ --opt o=uid=root,gid=root --opt o=bind
{{< /highlight >}}
Docker container can be run with the following command along with an environment file containing the cofigurable parameters as well:

{{< highlight html >}}
docker run -itd --restart unless-stopped --name image_name --env-file env.txt -v varlogs:/var/folder_name -h=hostname_01 hub.docker.com_docker_iamge_path
{{< /highlight >}}

{{< highlight html >}}
docker logs -f image_name
{{< /highlight >}}

## Vault
I have added a basic example of Vault usage in python, where you can easily store the credentials in the vault.
