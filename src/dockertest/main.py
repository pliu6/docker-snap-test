import time
import os
import errno
import subprocess
import docker


def main():
    print 'start testing...'

    # start a container?
    client = docker.Client(base_url="unix://var/run/docker.sock", version='auto')

    host_conf = client.create_host_config(
        network_mode='bridge',
        restart_policy={'MaximumRetryCount': 5, 'Name': 'on-failure'},
        publish_all_ports=False,
        privileged=False,
    )

    try:
        container = client.create_container(
            image="nginx:latest", name="nginx", host_config=host_conf
        )
        client.start(container.get('Id'))
        print "Successfully started chute with Id: {}".format(str(container.get('Id')))
    except Exception as e:
        raise e

    info = client.inspect_container("nginx")
    pid = info['State']['Pid']
    print "pid = {}".format(pid)

    try:
        os.makedirs('/var/run/netns')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise e

    cmd = ['ln', '-s', '/proc/{}/ns/net'.format(pid),
            '/var/run/netns/{}'.format(pid)]
    print "Calling: {}".format(" ".join(cmd))
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)

    env = {
        "PATH": os.environ.get("PATH", "/bin")
    }
    env['PATH'] += ":" + '/snap/bin'    

    cmd = ['pipework', 'vphy0.067d', '-i', 'wlan0', 'nginx',  '192.168.1.100/24']
    print("Calling: {}".format(" ".join(cmd)))
    try:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, env=env)
        for line in proc.stdout:
            print "pipework: {}".format(line.strip())
        for line in proc.stderr:
            print "pipework: {}".format(line.strip())
    except OSError as e:
        print 'Command "{}" failed'.format(" ".join(cmd))
        raise e

    time.sleep(300)

if __name__ == "__main__":
    main()
