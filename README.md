
  

# Getting Started

  

## Prerequisites

  

Before you begin, ensure you have Docker installed on your system. Docker is required to build and run the application in a containerized environment. If you do not have Docker installed, you can download and install it from the [official Docker website](https://www.docker.com/get-started).

  

To verify that Docker is installed correctly, you can run the following command in your terminal:

  

```bash

docker  --version

```

  

You should see output indicating the version of Docker that is installed.

  

## Cloning the Repository

  

First, you need to clone the repository to your local machine. Run the following command:

  

```bash

gh repo clone ArielBM/TI-IS-Backend

```

  

## Creating the .env File

  

Navigate to the root directory of the cloned repository and create a `.env` file. This file should contain the following environment variables:

  

```env

SFTP_HOST=host

SFTP_PORT=port

SFTP_USER=user

SFTP_PASSWORD=pass

```

  

Replace `host`, `port`, `user`, and `pass` with your actual SFTP server details.

  

## Building the Docker Image

  

Once Docker is installed, you can build the Docker image for the application. This image contains all the necessary dependencies and configurations.

  

To build the Docker image, navigate to the root directory of the project and run:

  

```bash

docker  build  -t  my_app_image  .

```

  

This command will build the Docker image based on the instructions in the `Dockerfile`.

  

## Running the Application

  

After building the image, you can run the container using the following command:

  

```bash

docker  run  -it  my_app_image

```

  

The `crond` service will also start, which is configured to run the `main.py` script once a day.

  

## Additional Information

  

-  **Cron Job Configuration:** The `crond` service is configured to execute `main.py` every day at midnight (00:00). The logs for this cron job can be found in `/var/log/cron.log` inside the container.

-  **Accessing the Container:** If you need to access the running container for debugging or other purposes, you can use the following command:

  

```bash

docker exec -it <container_name> /bin/sh

```

  

Replace `<container_name>` with the actual name of your container, which can be found using `docker ps`.

  

## Troubleshooting

  

If you encounter any issues, please ensure that:

  

1. Docker is installed and running on your system.

2. The Docker daemon has the appropriate permissions to build and run containers.

3. The Docker image builds successfully without errors.

  

For further assistance, please refer to the [Docker documentation](https://docs.docker.com/).