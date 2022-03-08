class NormalizeData:
    OS_NAMES = ['Winodws', 'Linux', 'CentOS', 'Ubuntu', 'Mac 10.1']
    P_ID_TYPE_AGENT_VM = "4"
    P_ID_TYPE_AGENT_PC = "8"
    P_ID_TYPE_AGENT_SCA = "64"
    P_ID_TYPE_AGENT_VM_PC = "12"
    P_ID_TYPE_AGENT_VM_SCA = "68"
    P_ID_TYPE_AGENT_PC_SCA = "72"
    P_ID_TYPE_AGENT_VM_PC_SCA = "76"
    P_ID_TYPE_EC2_VM = "1"
    P_ID_TYPE_EC2_PC = "2"
    P_ID_TYPE_EC2_SCA = "128"
    P_ID_TYPE_EC2_VM_PC = "3"
    P_ID_TYPE_EC2_VM_SCA = "129"
    P_ID_TYPE_EC2_PC_SCA = "130"
    P_ID_TYPE_EC2_VM_PC_SCA = "131"
    P_ID_TYPE_None = "None"

    CONTAINER_VM = "VM"
    CONTAINER_PC = "PC"
    CONTAINER_SCA = "SCA"
    CONTAINER_VM_PC = "PCVM"
    CONTAINER_VM_SCA = "SCAVM"
    CONTAINER_PC_SCA = "PCSCA"
    CONTAINER_VM_PC_SCA = "PCSCAVM"

    kernel_list = {
        "Linux 2.6.32-642.15.1.el6.x86_64": "2.6.32-642.15.1",
        "Linux 2.6.32-504.16.2.el6.x86_64": "2.6.32-504.16.2",
        "Linux 2.6.32-573.12.1.el6.x86_64": "2.6.32-573.12.1",
        "Linux 2.6.32-573.22.1.el6.x86_64": "2.6.32-573.22.1",
        "Linux 2.6.32-573.8.1.el6.x86_64": "2.6.32-573.8.1"
    }

    DEVICE_TYPE_WIN = "windows"
    DEVICE_TYPE_LINUX = "linux"
    DEVICE_TYPE_LINUX_UBUNTU = "linux_ubuntu"
    DEVICE_TYPE_MAC = "macosx"
    DEVICE_TYPE_AIX = "aix"

    V_STATUS_NEW = 1
    V_STATUS_ACTIVE = 2
    V_STATUS_FIXED = 3
    V_STATUS_RE_OPENED = 4
