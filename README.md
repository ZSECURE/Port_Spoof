# Port_Spoof

## Using Docker CLI
Manually build and run thr Docker container using Docker CLI:

### Build the Docker image:

```bash
docker build -t port-spoof .
```
### Run the Docker container:

```bash
docker run --network host --cap-add NET_ADMIN --restart always -d port-spoof
```
* `--network host`: Uses the host's network stack.
* `--cap-add NET_ADMIN`: Adds network administration capabilities to the container.
* `--restart always`: Ensures the container restarts automatically unless it is explicitly stopped.
* `-d`: Runs the container in detached mode.

## Verifying the Container is Running
After running your container, you can check its status with:

``` bash
docker ps
```
This command lists all running containers. Look for your port-spoof container in the list to confirm it's up and running.

By following these steps, you should be able to use Docker CLI to manage your Docker containers effectively.
