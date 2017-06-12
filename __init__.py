# __init__.py - Starting of our application

from flask import Flask
from flask_ask import Ask, statement, question
from vsphereapi import *

app = Flask(__name__)
ask = Ask(app, "/vghetto_control")


@app.route('/')
def homepage():
    return "VMware Control Center Alexa Skill"


@ask.launch
def start_skill():
    welcome_message = 'vSphere Control Center is online'
    return question(welcome_message)


@ask.intent("VMCountIntent")
def share_count():
    counting = vm_count()
    count_msg = 'The total number of virtual machines in this \
                Virtual Center Server is {}'.format(counting)
    return question(count_msg)


@ask.intent("ApplianceHealthIntent")
def share_vcenter_health():
    health = get_vcenter_health_status()
    health_msg = 'The current health of the \
                  vCenter appliance is {}'.format(health)
    return question(health_msg)


@ask.intent("HostClustersIntent")
def share_hosts_in_clusters():
    hosts = get_cluster()
    host_msg = 'Current hosts in clusters are {}'.format(hosts)


@ask.intent("VCenterBuildIntent")
def share_vcenter_build():
    (version, build) = get_vcenter_build()
    build_msg = "vCenter Server is running " \
                + format(version) + " using build " + build
    return question(build_msg)


@ask.intent("HostClusterStatusIntent")
def share_cluster_status():
    (drs, ha, vsan) = get_cluster_status()
    if drs:
        drs_msg = "DRS is enabled, "
    else:
        drs_msg = "DRS is disabled, "

    if ha:
        ha_msg = "High Availablity is enabled "
    else:
        ha_msg = "High Availablity is disabled "

    if vsan:
        vsan_msg = "and Virtual SAN is enabled"
    else:
        vsan_msg = "and Virtual SAN is disabled"

    cluster_msg = drs_msg + ha_msg + vsan_msg
    return question(cluster_msg)


@ask.intent("VSANClusterIntent")
def share_vsan_version():
    version = get_vsan_version()
    vsan_msg = "Virtual SAN is running version " + version
    return question(vsan_msg)


@ask.intent("PersonalIntent")
def share_vsan_version():
    return question("you are not too shabby yourself William")


if __name__ == '__main__':
    app.run(debug=True)
