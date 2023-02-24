Implementing Hyper-V
* Virtualization
   * Allows efficient use of hardware by running multiple guest operating systems (virtual machines) simultaneously
   * Requires a hypervisor
   * Hyper-V is type 1 hypervisor
Installing Hyper-V
* Ensure virtualization extensions with SLAT support installed
* Use the Add Roles and Features Wizard
   * Add the Hyper-V role
   * Select one or more network interfaces
   * Enable the live migration of virtual machines
   * Enter the location of the files comprising each virtual machine
   * Reboot the computer twice to complete installation
* Use PowerShell or the graphical Hyper-V Manager tool to manage Hyper-V
Understanding Virtual Networks
* Physical networks use wireless access point (WAP) and switch devices
* Hypervisor
   * Provides physical network access to virtual machines
   * Allows for the creation of additional virtual networks
* Hyper-V defines three types of virtual switches
   * External virtual switch
   * Internal virtual switch
   * Private virtual switch
* Create and modify a virtual switch
   * Select Virtual Switch Manager within the Actions pane of Hyper-V Manager
   * New virtual network switch option is highlights by default
   * Create an external or internal virtual switch
   * Associated virtual network interface is displayed
   * Access the properties of the physical network interface
      * Hyper-V extensible Virtual Switch protocol is enabled
Creating Virtual Machines
* Prerequisites: Hyper-V installed and virtual machines configured
* Can create a new virtual machine within Hyper-V Manager
   * Select New from the Actions pane
   * Select Virtual Machine to start the New Virtual Machine Wizard
      * Clicking Finish creates a generation 2 virtual machine
      * Clicking Next leads to configuration setting prompts
Configuring Virtual Machines
* Configuring a Generation 2 Virtual Machine
* Can change default hardware in the Hardware and Management section
   * Boot order for hardware devices within the UEFI BIOS
   * Configure UEFI security
   * Modify memory configuration
   * Specify advanced processor capabilities
   * Can change SCSI controller hardware
   * Define ISO image file associated with the virtual DVD drive
* Can change default hardware in the Hardware and Management section
   * Can associate the network interface with a virtual switch
      * Can optionally enable and set a VLAN identification number
   * Can select Hardware Acceleration or Advanced Features to configure optional network interface components
* All non-hardware-related configuration for a Generation 2 virtual machine
   * Performed within the Management section of virtual machine settings
* Configuring a Generation 1 Virtual Machine
* Identical areas for Generations 1 and 2 virtual machines
   * Management section
   * Configuration of the memory, processor, virtual hard disk drive, and network adapter settings within the Hardware section
* Several key differences exist within the Hardware section when configuring a Generation 1 virtual machine
Working with Virtual Machines
* Preferred way to boot a newly created virtual machine
   * Click Connect in the Actions pane
   * Obtain the Virtual Machine Connection window
      * Click Start within this window to boot the virtual machine
* Perform key actions within the virtual machine
   * Use associated toolbar buttons on the Virtual Machine Connection window
   * Use the Actions pane of Hyper-V manager
* Can view information for a running virtual machine within Hyper-V Manager
Managing Hyper-V Features
* Check points
   * Used to revert the state of a virtual machine to a previous point in time
   * Created before making potentially problematic modifications
   * Checkpoint file has .avhdx suffix
   * Two mechanisms for creating checkpoints
      * Standard and production
   * Backup services
      * Volume Shadow Copy Service (VSS) or File System Freeze (fsfreeze)
* Live Migration
   * Moves a virtual machine to another server running Hyper-V within the same Active Directory domain
   * Use the Move Wizard
   * Two options
      * Move the virtual machine
      * Move the virtual machine’s storage
   * Can enable Live Migration if not configured during the installation of Hyper-V
* Replication
   * Creates a copy of a virtual machine on a destination Hyper-V host
      * Within the same Active Directory domain
      * Continually updated as changes are made
   * Used if there is hardware failure on Hyper-V host
   * Requirement: target Hyper-V host must have replication enabled
   * Click Hyper-V Settings within the Actions pane of Hyper-V manager
      * Select the Replication Configuration node under the Server section
Rapid Server Deployment
* Minimizes time to install a new server
* Two methods
   * Copy a virtual machine template
   * Perform a network installation using Windows Deployment Services (WDS)
Using Virtual Machine Templates
* Creating a virtual machine template
   * Consider minimum hardware settings and virtual machine template name
   * Perform normal installation of Windows Server 2019 to virtual hard disk
      * Optionally install server roles and features
   * Remove unique server information using the System Preparation Tool
   * Use the Out-of-Box Experience (OOBE) wizard to generate new computer name and unique identifiers
   * Create a virtual machine template for later use and export it
* Importing a virtual machine template
   * Open the Import Virtual Machine wizard
      * Specify folder containing the virtual machine template to import
      * Select the virtual machine template
      * Choose to create a copy of the virtual machine
      * Specify the virtual machine configuration and hard disk files
      * Click Finish to create a new virtual machine
      * Rename machine, configure settings, and start guest operating system
      * Complete the OOBE wizard
Using Windows Deployment Services
* Windows Deployment Services (WDS) used in conjunction with WIM files
   * Deploys Windows operating systems to computers configured to boot using a PXE-capable network interface
* The IP multicast feature simultaneously boots several computers
   * Can then install an operating system from a WDS server
* To implement rapid server deployment using WDS
   * Install WDS
   * Configure WDS to respond to client computers using the appropriate boot and install images
* Installing WDS
   * Open Server Manager
   * Select the Windows Deployment Services role
   * Add Roles and Features Wizard starts
   * Select the two required role services for full WDS functionality
      * Deployment Server
      * Transport Server
* Configuring WDS
   * Use the Windows Deployment Services tool
   * Right-click server object
   * Click Configure Server to open the Windows Deployment Services Configuration Wizard
   * Select prompt to integrate WDS with an Active Directory domain
   * Choose folder used to store WDS configuration and WIM images
      * Change folder for performance reasons
   * Configure the DHCP integration options
   * Select how the server should respond to PXE requests from computers on the network
      * Select Respond to all client computers (known and unknown)
   * Click Next and then click Finish to complete the initial WDs configuration
   * Add a boot image
   * Add an install image
* Starting a WDS installation
   * Right-click the server within the Windows Deployment Services console
   * Select All Tasks, then click Start to allow the WDS service to respond to PXE requests
* Before starting a system, verify network interface is at the top of the boot order
* WDS and DHCP provide IP address, and a prompt to start a WDS installation
   * Prompt is F12 key (legacy system) or Enter key (modern system)
   * Boot image downloads from the WDS server to start the installation process