Windows Printing Basics
* PnP configurable printers
   * Connect using a physical port
   * Configured by the system automatically using a printer driver
* Non-PnP configurable printers and network interfaced printers
   * Connect using a network connection
   * Require manual addition using the Devices and Printers utility
* Printers are represented by a printer name and icon within Devices and Printers
* Can configure printers as shared resources
The Printing Process
* Step 1
   * User chooses to print a document to a printer installed on the system
* Step 2
   * Software application contacts a print application programming interface (API)
   * Spool folder located under C:\Windows\System32\spool\PRINTERS
   * Two different APIs available
      * Graphics Device Interface (GDI)
      * CML Paper Specification (XPS)
* Step 3
   * Spool folder documents rendered
   * Document is called a print job
* Step 4
   * Print job sent to the print device
* Step 5
   * Print device prints the document
   * Notifies user when print job has completed
Printing to a Shared Printer
* Network-attached print devices within organizations are configured to only accept print jobs from a print server
   * Creates a charred printer for each print device
* Configuring client computer printer to print to a shared printer across a network
   * Specify print server sharing the printer and name of the shared printer
   * Specify one of three printer sharing protocols
      * Server Message Block (SMB), Internet Printing Protocol (IPP, or Line Printer Daemon (LPD)
* Printing to a shared IPP printer required the Internet Printing Client feature
* Printing to a shared LPD printer required the LPR Port Monitor feature
* Install these features on Windows 2019 server system
   * Use the Add Roles and Features wizard
* Install these features on a Windows 8 or later system
   * Access the Programs and Features tool within Control Panel
   * Click Turn Windows Features on or off to select them under the Print and Document Services
The Printing Process for a Shared Printer
* Step 1
   * User chooses to print a document to a shared printer
* Step 2
   * Software application contacts a Print API (GDI or XPS) on the print client
   * Document stores in print spooler using the appropriate format (EMF or XPS)
* Step 3
   * Spool folder document converted between EMF and XPS formats (to match the requirements of the print device) and rendered
* Step 4
   * Print job sent from the print client to the print server across the network using the correct protocol (SMB, IPP, or LPD)
* Step 5
   * Print server stores the print job
   * Stored within a spool folder under C:\Windows\System32\spool\PRINTERS
* Step 6
   * Print server sends the print job to the locally attached or network attached print device
* Step 7
   * Print device prints the document
   * Notifies the print server that the print job has completed
* Step 8
   * Print server notifies the print client that the print job has completed
* Step 9
   * Print client notifies the user that the print job has completed
Configuring a Windows Server 2019 Print Server
* Adding and sharing locally attached or network-attached printers
   * Use the Print and Document Services server role
      * Print Management tool
* Advantages
   * Can add, share, and manage several locally attached or network-attached printers on one or more print servers within an Active Directory environment
   * Contains print server configuration options that are not available within the Devices and Printers utility
Installing Print and Document Services
* Print Management tool and the IPP and LPD printer sharing protocols
   * Require the Print and Document Services server role
* Wizard prompts for Print and Document Services components
   * Print Server
   * Internet Printing
   * LPD Service
Configuring a Print Server
* Print Management tool
   * Local server is listed under the Print Servers section by default
   * Configure the other nodes before adding
      * Drivers, Forms, Ports
   * Can modify the spool folder location or display notification for printers
   * Various permissions available to the printers and print server itself
   * Can configure the Print Management console to email printer notifications to an email address, or run a script
Add Printers to a Print Server
* Use the Network Printer Installation Wizard
   * Select installation method
      * Search the network
      * Select Add a TCP/IP or Web Services Printer by IP address or hostname
      * Select Add a new printer using an existing port
      * Select Create a new port and add a new printer
   * Select or specify the location of the print device
   * Supply the appropriate drivers
   * Enter the printer name and sharing settings
Configuring Printer Properties
* Use the Print Management console
   * The Sharing tab
   * The Ports tab
   * The Advanced tab
   * The Security tab
   * The Device Settings tab
Using Group Policy to Deploy Shared Printers
* Group policy simplifies addition of printers on client computers
   * Can automatically add SMB shared printers to computers joined to a domain
      * Requires appropriate printer drivers installed on the print server
* Right-click a printer within the Print Management console
   * Select Deploy with Group Policy to open the Deploy with Group Policy window
      * Can select an existing Group Policy
      * Can add the shared printer to user or computer objects receiving the group policy
Configuring Branch Office Direct Printing
* Offices may contain a network-attached print device
   * Created a slow printing process and congestion across Internet connection for the branch office
* Solve by enabling Branch Office Direct Printing (BODP) on the shared printer
   * Print server does not spool the print job
* To enable BODP
   * Right-click a printer within the Print Management console
   * Click Enable Branch office Direct Printing
Managing Print Jobs
* Several options are available for managing a print job waiting to print
   * Users with Print permission can view and manage their own print jobs
   * Users with manage Documents permissions can view and manage print jobs of other users
   * Open the print queue window
      * Select Document menu to choose options such as Pause, Resume, Restart, Cancel and Properties
      * Select Printer menu to choose additional options: Pause Printing and Cancel All Documents
* Installing Print and Document Services on a print server
   * Provides an Internet Pintiting component
   * Access a website (https://printservername/printers) to manage print jobs
      * Clicking a printer on the webpage displays the associated print queue webpage
   * Users can then manage print jobs depending on their permission level
Monitoring and Troubleshooting Printers
* Print Management tool
   * Provides custom filters an administrator uses to quickly check printer status
   * Printers Not Ready custom filter displays printers that cannot complete the print process
      * Provides the status of the printer within the Queue Status column
   * Other custom filters available by default
      * List printers and printer drivers and printers with jobs in the print queue
   * Can create additional custom filters that display printers that have different criteria
* Some problems cannot be resolved using Print Manager custom filters
   * Problem is specific to the document, hardware capabilities of the print server, or the print device model
* Troubleshooting will require other methods
   * Researching error codes, configuring print settings, modifying print device settings, restarting the Print Spooler service, trying different printer settings, or reinstalling printer drivers
* Some common printing problems follow general rules