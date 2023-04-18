### Using windows Server 2019 within an Organization
1.Computer networks and the Internet in the 1990s
   * PCs (client) connected to other computers across a computer network
   * Obtained access to shares resources
2. Server: computer that shared the resource
   * On-premises servers, cloud servers, rackmount servers, blade servers
3. Rach servers (1U and 2U)
   * Storage area network (SAN) devices, uninterruptible power supply (UPS) devices
### Understanding Windows Server Virtualization
1. Virtualization
   * Process of running more than one operating system at the same time on a single computer
   * Requires hypervisor software
2. Type 2 hypervisors run on top of an existing workstation operating system
3. Type 1 hypervisors interact with the hardware directly
   * Contain a small operating system to manage the hypervisor configuration and virtual machines
   * Example: Microsoft Hyper-V
4. Hypervisor requirements
   * Hypervisor acceleration
   * Second Level Address Translation (SLAT) extensions
      * Designed to reduce the overhead in a hypervisor CPU
      * Easing the management of a hypervisor memory
   * Intel-V
6. Virtual machine configuration file
   * Stores within a file specific to the hypervisor
7. Operating system virtual hard disk file
   * Thick provisioning: allocates fixes space for the file when created
   * Thin provisioning: dynamically allocating space as needed
8. On-premises and cloud operating systems
   * Virtual machines with virtual hard disk files hosted on a SAN within the organization or cloud data center
9. Nested virtualization
   * Running other virtual machines within an existing virtual machine
   * Example: Hyper-V
   * Provides ability to implement a more complex virtualization structure
   * Provides ability to create complex virtualization structure on Windows 10 PCs for learning and testing purposes
### Understanding Windows Containers
1. Sandboxing
   * Enclosing executed Web apps in a way that isolates them from Web apps running within other containers and the underlying operating system
2. Docker: common container software
3. Windows Containers: Windows Server component needed to use Dicker
4. Kernel: core operating system component
5. Hyper-V containers
   * Provide additional performance and security features to Web apps
### Windows Server 2019 Features
1. Active Directory
   * Provides single sign- on using domain and domain controller environment
   * Windows Server as an Active Directory domain controller
      * Provides single sign-on for other computers joined to a domain
   * Contains Group Policy and Active Directory Certificate Services features
2. Azure Active Directory
   * Service hosted within Microsoft’s Azure cloud
   * Provides Active Directory services to an organization
3. Security
   * Microsoft Defender Advanced Threat Protection (ATP)
      * Performs deeper inspection of files and processes
   * Shielded virtual machines feature protects Hyper-V virtual hard disk files
   * More emphasis on Internet Information Services (IIS) Web server software
   * Additional basic security features
      * File and folder permissions, security policies, encryption of data, event auditing, various authentication methods, server management and monitoring tools
4. Volume and filesystem features
   * NTFS features
      * Built-in support for file and folder permissions, compression, Encrypting File System (EFS) encryption, user quotas, data deduplication, journaling, self-healing capability
   * ReFS v3 features
      * Data deduplication, improved performance with Storage Spaces
   * Storage Replicas have better performance
   * Storage Migration Service simplifies the moving of data
5. Performance and reliability features
   * Privileged mode
   * Protected processes
   * Multitasking
   * Multithreading
   * Processor scalability
   * Server clustering
      * Ability to increase access to server resources. Provide failover fault tolerance. If one server fails, the other servers can still respond to the client.
6. Administration tools manage the servers and services on the network
   * Server Manager
      * Monitors and manages server local configurations or network servers
      * MMC snap-in performs most configurations
   * Windows PowerShell: uses cmdlet to refer to each command
      * Provides features for computers running Windows and Windows Server
   * Windows Admin Center: not installed by default
      * Web-based management tool new to Windows Server 2019
7. Small footprint installation options
   * Install Server 2019 with a minimal set of services, features, and functionality
   * Produces a smaller attack surface
   * More suitable for cloud environments
      * Uses far less server storage, memory, and processor resources
      * Can be installed within a virtual machine or used as a container
   * Windows Server 2019 offers two small footprint installation options
      * Server Core: Use sconfig.cmd command to configure
      * Nano Server
8. Hybrid cloud features
   * Hybrid cloud
      * Integration between on-premises Windows Servers and Windows Servers and services running within the Azure cloud
   * Windows Server Azure Network Adapter feature
   * Azure Backup feature
   * Azure Update Management feature
   * Azure Site Recovery feature
   * Kubernetes software coordinates container execution
9. Linux application support
   * Web apps running in the cloud run within Linux containers
   * Microdift’s Windows Subsystem for Linux (WSL)
      * Makes it easier for Web app developers to create and test Linux apps on their Windows 10 PCs
### Windows Server 2019 Editions
1. Windows Storage Server 2019
   * Cannot be purchased directly from Microsoft
   * OEMs can offer Windows Storage Server 2019 on the server-based products they sell
   * Windows Storage Server 2019 turns a server into a central storage center for data in an organization
      * Takes advantage of the storage utilities offered in Windows Server 2019
2. Microsoft Hyper-V Server 2019
   * Hyper-V hypervisor
   * Free to download and use
      * Wach Windows Server virtual machine running it requires a valid license
      * Note: Linux virtual machines do not require a license
   * Installs a small footprint version of Windows Server
      * Contains a PowerShell interface for creating and managing virtual machines
### Preparing for a Windows Server2019 Installation
1. Perform advanced planning
2. Review and exceed minimum hardware requirements
3. Consider capacity planning questions
4. Consider processing speed, paying attention to the number of processors
5. Ensure server had enough memory for the applications that it will host
6. Consider the amount and type of storage
   * Redundant Array of Independent Desks (RAID) in the BIOS of the server
   * Additional hard dials, SSDs, virtual machine hard disk files
### Installing Windows Server 2019
1. Installation broken into three separate tasks
   * Obtaining installation media
   * Starting the installation process
   * Completing the installation process
### Obtaining Installation Media
1. Common method used to install Windows Server
   * Booting a computer or virtual machine from installation media
      * Bootable DVD or USB flash drive or ISO file
   * Use disk-burning software to download ISO image: Burnaware or Rufus
   * Download the correct Windows Server 2019 ISO image file
### Starting the Installation Process
1. Ensure BIOS boot order if necessary
2. Create a new virtual machine within a virtualization configuration program
   * Attack an ISO image file to the virtual DVD drive within the virtual machine
   * Configure the virtual machine BIOS boot order
      * Boot from a DVD before the virtual hard disk file
   * Start virtual machine within the virtual machine software
      * Machine boots ISO image attached to the virtual DVD
   * Installation process starts
### Completing the Installation Process
1. First step: enter regional locale and keyboard format
2. Second step: choose whether to start an installation or repair a system
3. Third step: select desired Windows Server 2019 edition
   * Accept the Microsoft license terms for Windows Server 2039
4. Fourth step: select installation type - custom or upgrade
   * Normally, select Custom installation for new installation
5. Fifth step: select Windows Server operating system storage location
6. Reboot and specify a password for the local Administrator user account
### Post-Installation Configuration
1. Key configuration tasks following any Windows Server 2019 installation
   * Setting the correct time and time zone
   * Configuring the Internet Protocol (IP) on the server’s network interfaces
   * Configuring the firewall
   * Changing the default computer name and domain membership
   * Installing a modern Web browser
   * Activating the Windows Server operating system
### Setting the Correct Time and Time Zone
1. Within Server Manager
   * Navigate to Local Server
   * Select the hyperlink to Time Zone in the Properties window
2. Within the Windows Server Configuration Wizard on Server Core
   * Select option 9
### Configuring the Network
1. Requirements to connect computer to a network
   * Network interface, protocol, packets, routers, and other devices on a network
2. Three default Windows protocols
   * TCP/IP, UDP/IP, ICMP
3. TCP  ensures retransmission of lost packets
4. IP network participant requires a valid Internet Protocol (IP) address
   * IP version 4 (IPv4)
   * IP version 6 (IPv6)
5. Understanding IPv4
6. Participation on an IPv4
   * Requires valid IP address and a subnet mask
   * Originally required configuration of a default gateway
   * Unicast communication: from one computer to another computer using IP
   * OctetsL most common format for IPv4 addresses
   * IPv4 address’s two parts: network ID and host ID
   * IPv4 address must be configured with a subnet mask
7. Understanding IPv6
   * Accommodates far more IP addresses: uses 128 bits to identify computers
   * IP addresses written using 8 colon-delimited 16-bit hexadecimal numbers
   * IPv6 addresses can be expresses several ways
   * Adopted by small Internet-connected devices
      * Collectively referred to as the Internet of Things (IoT)
      * Uses Teredo protocol to work within IPv4-only networks
8. Proxy servers and Network Address Translation (NAT) routers allow more IPv4 addresses
9. Configuring IP on a network interface
   * Automatic from Dynamic Host Configuration Protocol (DHCP) pr Boot Protocol (BOOTP) server
10. Process varied on IPv4 or IPv6 networks
11. Automatic address assignment features
   * Automatic Private IP Addressing (APIPA)
   * Internet Control Message Protocol version 6 (ICMPv6)
12. Can manually configure IP on a network interface within Server Manager
### Configuring the Firewall
1. Perimeter network or demilitarized zone (DMZ)
   * Contains severs surrounded by routers
   * Routers implement advanced firewall capabilities for traffic passing into network
2. Disable or modify DMZ servers’ firewall configurations within Server Manager
   * Navigate to Local Server
   * Select hyperlink next to Windows Defender Firewall in the Properties window
### Changing the Default Computer Name and Domain Membership
1. Installation adding randomly generated computer name for he server
2. Change within Server Manager
   * Navigate to Local Server
   * Select hyperlink next to Computer name in the Properties window
   * Click the Change button and supply a new computer name
3. Change within Windows Server Configuration Wizard on Server Core
   * Select option
4. Finish by joining the server to a domain
### Installing a Modern Web Browser
1. Default Windows Server 2019 Web Browser: Internet Explorer
   * Provided for legacy application support only
2. INternet Explorer Enhanced Security Configuration (IE ESC) blocks Websites
3. Disable IE ESC within Server Manager
   * Navigate to Local Server
   * Select hyperlink next to IE Enhanced Security Configuration in the Properties window
   * Disable IE ESC for all users or system administrators
### Activating the Windows Server Operating System
1. Automatic activation performed based on Generic Volume License Key (GVLK)
   * Requires organization’s Key Management Services (KMS) installed on a network server
   * Requires Active Directory-based Activation role installed on a domain controller within the domain
2. Organization can purchase a retail product key or Multiple Activation Key (MAK)
3. Activation within Server Manager by navigating to Local Server
   * Select hyperlink next to Product ID in the Properties window
   * Enter license key and click Activate to complete the activation process
### Selecting a Windows Server 2019 Lab Environment
1. Hands-On Projects within this book will require Hyper-V
2. Can install Windows Server 2019 directly on a computer
   * Not necessarily practical
3. Can use Windows 10 Professional, Enterprise, and Education editions
   * These releases provide support for Hyper-V and nested virtualization