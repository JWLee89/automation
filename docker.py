import os
import subprocess


def install():
    """
    Install docker on your device
    :return:
    """
    # Install dependencies
    os.system('sudo apt-get update')
    os.system('sudo apt-get install ca-certificates curl gnupg lsb-release')
    # Add Docker’s official GPG key:
    os.system('curl -fsSL https://download.docker.com/linux/ubuntu/gpg '
              '| sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg')
    # Setup stable repository
    os.system(' echo \ "deb [arch=$(dpkg --print-architecture) '
              'signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] '
              'https://download.docker.com/linux/ubuntu \
              $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null')

    # Install docker engine
    os.system('sudo apt-get update')
    os.system('sudo apt-get install docker-ce docker-ce-cli containerd.io')
    # add to docker group
    os.system('sudo usermod -aG docker $USER')


def install_docker_compose(version='1.29.2'):
    """
    Install docker-compose
    :return:
    """
    docker_install_cmd = f'sudo curl -L "https://github.com/docker/compose/releases/download/{version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose'
    subprocess.run(docker_install_cmd.split())
    os.system('sudo chmod +x /usr/local/bin/docker-compose')


if __name__ == '__main__':
    install()
