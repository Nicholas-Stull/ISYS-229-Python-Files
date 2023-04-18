### Working with Server Manager
1. Used to monitor and manage several different Windows Server Systems
* Server Manager Dashboard panes
   * Dashboard section at the top
   * Welcome to Server Manager pane (often hidden by administrators)
   * Roles and Server Groups pane
* Dashboard users various colors and icons
* Additional Server Manager panes
   * Events, Service, Best Practices Analyzer, Performance, Roles and Features
* Server roles introduced starting with Windows Server 2012
   * Have configuration tools built into the Server Manager interface
   * Example: Storage Spaces
* Some Server roles have their own MMC tool for configuration
* Starting an MMC tool
   * Navigate to a server group or role section within the navigation area
   * Right-click a server in the Servers Pane and choose the appropriate tool
   * Example: DHCP server role
Adding Roles and Features Using Server Manager
* Three different ways to add roles and features within Server Manager
   * Selecting Add roles and features from the Welcome to Server Manager pane within the Dashboard section
   * Selecting Add Roles and Features from the Manage menu
   * Selecting Add Roles and Features from the Tasks menu within Roles and Features pane doe a server or server role
* Starting the installation of a role is the same for all three methods
   * Use the Add Roles and Features Wizard
Using the BPA to Verify Server Roles
* BPA scan
   * Determines if role configuration meets Microsoft minimum guidelines
   * Scan results indicate security level and category for recommendations
* Levels of severity
   * Information, warning, error
* Categories for BPA recommendations
   * Configuration, predeployment, postdeployment, performance, BPA prerequisites
Working with the Windows Admin Center
* Server Manager disadvantage
   * Needs to connect to Windows Server system to run it
   * Need to install the RSAT on a Windows 10 PC
* Windows Admin Center
   * Relatively new tool
   * Remotely manage Windows Server 2019 using a modern Web browser
   * Preferred if hosting large numbers of remote Windows Server systems
   * Boasts a wide range of monitoring and management functionality
Installing the Windows Admin Center
* Download the desired version (preview or regular)
* Start the installer; navigate through several screens, clicking Next each time
   * Accept license
   * Automatically update the Windows Admin Center
   * Prompt for function capabilities in different scenarios
   * Prompt to modify local computer’s trusted host settings
   * Prompt on how to generate encryption certificate
* URL to access Admin Center displayed on final screen
Using the Windows Admin Center
* First use requires log-in with valid credentials
   * Prompted to complete a quick tour
* Placed at the connections screen within the Windows Admin Center
   * Can manage server hosting the Windows Admin Center
   * Can add Windows Server 2012 and later systems and edit tags
* Many similarities to Server Manager
* Many tools within the navigation pane
   * Configuration, remote access, Azure cloud integration
Configuring Server Hardware Devices
* Many types of hardware devices
* Plug and Play (PnP)
   * Operating system works with hardware devices to automatically detect and configure recently installed hardware to work with the operating system
* Simple PnP device installation process
   * Attach device
   * Wait for Windows Server 2019 to detect it
   * Install appropriate device drivers
Adding Hardware Using Control Panel
* Devices and Printer utility
   * Force the operating system to detect and install new PnP hardware
   * Install non-PnP hardware
   * Troubleshoot problems you might be having with existing hardware
* Start Devices and Printers utility from the Control Panel
   * Two views: Category view or Classic view
* Simple tasks
   * Add device, display device, troubleshoot device
Using Device Manager
* Device Manager shows all devices on the system
* Open Device Manager from Control Panel to update a device driver
   * Generic or Unknown devices require updates drivers for full functionality
   * PnP hardware resource must be considered to prevent conflicts
      * Interrupt Request (IRQ) line, Input/Output (I/O) address, reserved memory range
* Can check for a resource conflict and examine other device properties
   * Device Properties box has four tabs to review
Verifying System Files
* System file signatures can become invalid
   * Overwritten, corrupted, modified by malware
* System File Checker
   * Scans system files for integrity
   * Replaces damaged or overwritten files with the proper version
* File Signature Verification tool (Sigverif)
   * A scan-only tool that determines if files have a signature
   * Output written to a log file called sigverif.txt
Configuring Windows Settings
* Configurable elements of the operating system
   * Performance options
   * Environment variables
   * Startup and recovery options
   * Power options
Configuring Performance Options
* Configuring processor scheduling and Data Execution Prevention
* Processor scheduling
   * Configures processor resources allocated to a program
* Data Execution Prevention (DEP)
   * Monitors server programs for memory issues
* In Control Panel, navigate to System and Security, and select System
   * Select Advanced system settings, click Settings in the Performance section
   * Highlight Advanced tab or Data Execution Prevention tab
* Configuring virtual memory
* Virtual memory: disk storage used to expand capacity of physical memory
   * Uses a paging technique
      * Pages move from physical memory into virtual memory on disk
* Paging file: area of disk allocated for virtual memory
   * Location of the paging file is important
   * Parameters used to tune paging file size: initial size and maximum size
   * Configure initial size by multiplying amount of installed RAM times 1.5
* Configuring file caching
* File caching turned on by default
   * Speeds up the time it takes to read from or write to a disk
* Flushing
   * Freeing memory used for cached data after data written to disk
* Can turn off caching and flushing to easily how swap a drive
   * Server can seem slower to users
   * May lose during hot swap while the server is in use
Configuring Environment Variables
* Environment variable
   * Tells the operating system where to find certain programs and program-related information
* System environment variables are defined by the operating system
   * Apply to any user logged in to the computer
* User environment variables are defined on a per-user basis
   * Used to provide a wide variety of different information
Configuring Power Options
* Power options that can be set
   * Select a power plan
   * Choose what the power button does
   * Create a power plan
   * Choose when to turn off the display
* Three power plans
   * Balanced, Power Saver, and High Performance
Windows Registry Contents
Working with Windows PowerShell
System Administration Commands
Using WMI within Windows PowerShell
Creating PowerShell Scripts