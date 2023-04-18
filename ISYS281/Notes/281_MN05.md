Configuring Folder and File Attributes
* Attributes
   * Features of a folder of file that are used by a filesystem
* Metadata
   * Stores information about a folder or file
   * Stores attributes
   * Stores ownership, permissions, date of creation, and time of last access characteristics
Working with Basic Attributes
* Filesystems supported by Windows Server 2019
   * NTFS, ReFS, FAT32, and exFAT
* Common attributes: read-only and hidden
* View and set attributes
   * Right-click a folder or file within a File Explorer window and click Properties
* Affects of read-only attribute on a file
   * Changes to its contents cannot be saved to the same file name
   * Cannot be deleted using a command (can be deleted within File Explorer)
* Affect of read-only attribute on a folder
   * It applies to existing files within the folder only, not the folder itself
* Hidden attribute prevents users from listing the folder and file names
   * Can override with commands or in the File Explorer
      * Dir /ah MS-DOS command
      * Get-ChildItem -hidden Windows PowerShell Command
Working with Advances Attributes
* Advances attributes
   * Archive, index, compress, and encrypt
* Archive attribute
   * Indicates the folder or file needs to be backed up
   * Automatically enabled on files
   * Not automatically enabled on folders
   * Can manually set the archive attribute on all files within a folder
   * Backup software removes the archive attribute following the backup process
* Index attribute
   * Index: pre-created list used in searching
   * Commonly access user folders indexed by default
   * System folders excluded to reduce index size for speed
   * Files with index attribute set are indexed by the Windows Search Service
   * All new files have the index attribute for a file or folder
   * Can deselect the index attribute for a file or folder
* Compress attribute
   * System compresses the file on the filesystem
   * Automatically decompresses it when accessed
   * Changes to the file are compressed before being written to the filesystem
* Encrypt attribute
   * Applies encryption algorithm to protect data before it is written to filesystem
   * Symmetric encryption (uses one key) and asymmetric encryption (uses public and private keys)
   * Encrypting File System (EFS) works within a workgroup or Active Directory domain environment
Managing Folder and File Security
* Need to modify resource access control lists (ACLs) and set up sharing
* Discretionary access control list (DACK)
   * Permissions given to user and group accounts
   * Used to grant or deny access to the resource
* System access control list
   * Contains information used to audit the access to the resource
* User who creates resource owns the resource
   * Owners can change folder and file ownership, configure DACLs and SACLs
Configuring Folder and File Permissions
* To view and configure DACL for an NTFS or ReFS filesystem folder or file
   * Open File Explorer, right-click a folder or file, click Properties
   * The file Properties window opens: highlight the Security tab
      * Basic folder and file permissions supported by NTFS and ReFS display
      * SYSTEM group is allowed Full control permission
      * Grey permission are inherited from parent folder containing the file
   * Click Edit to open the Permissions windows
      * Can add or remove existing users or groups and set basic permissions
* More advanced permissions provide a specific type of access
   * Open the File Properties window: highlight the Security tab
      * Click Advanced to open the Permission Entry window to add advanced permissions
      * Can click Disable inheritance to prevent parent folder permissions from being inherited by the file being edited
Configuring Folder and File Ownership
* Folder of file has one owner
   * Default owner id the creator
   * Owner an change the ownership to another user
* User with Take ownership advanced permission or Full control permission to a folder or file
   * Can change the owner to be themselves
* To modify the owner of a folder or file
   * Access the Advanced Security Settings window
      * Click Change next to the current owner, and specify the new owner
Troubleshooting Folder and File Permissions
* Example: User receives an access denied message for a folder because their user account is also a member of a group that has been denied
   * Two troubleshooting techniques
      * Review permissions assigned on the folder to the user, and all groups to wish the user belongs, taking permission inheritance into consideration
      * Access the Advanced Security Settings window for the folder and highlight the Effective Access tab
      * Click Select a user  to choose the appropriate user account, and then clickView effective access to list the effective permissions the user has
* Permission-related problems can occur after a file or folder is copied or moved
Configuring Folder and File Auditing
* Audit configuration stored within the SACL on the folder or file
* Configure auditing with the Auditing Entry window
* Auditing is not enabled onWindows Server 2019 by default
* To enable auditing functionality
   * Edit the audit policy within a Group Policy object that applies to a computer
   * Within Active Directory environment
      * Edit the Default Domain Policy object settings to enable auditing functionality on every computer within the domain
Configuring Shared Folders
* Shared folder
   * Allows users to access the files within the folder from across a network
* Two protocols for sharing folders onWindows Server 2019 systems
   * Server Message Block (SMB)
   * Network File System (NFS)
Sharing Folders Using SMB
* SMB is enabled by default
* PC can be set to be discovered by other PCs at installation time
* Can enable or disable SMB sharing for current network profile
* Can modify SMB sharing settings using the Network and Sharing Center
   * Click Change advanced sharing settings
* Sharing a folder using folder properties
   * Right-click the folder, click Properties, and highlight the Sharing tab
   * Click the Share button to see the Network access window
      * Specify user or group name, click Add, and specify the permission level for the shared folder
   * Or click the Advanced Sharing button, then select Share the folder within the Advanced Sharing Window
      * Specify share name, limit simultaneous connections to the shares folder, supply a description or click the Permissions button
   * Caching button allows configuration of SMB offline file caching features
* Sharing a folder using Server Manager
   * Open File and Storage Services within the navigation pane
      * Click Shares, select the Tasks drop-down box, click New Share
   * Starts the New Share Wizard
      * Select the desired SMB File share profile option
      * Supply the share name and optional share description
      * Configure the optional share features
      * Modify the MTFS/ReFS permissions on the folder to match the desired level of access for groups and users
Sharing Folders Using NFS
* Need to install the Server for NFS server role
* Sharing a folder using folder Properties
   * Open the NFS Advanced Sharing window
   * NFS shared folder authentication options for UNIX, Linux, macOS, and Windows users within the Active Directory domain
      * Kerberos options allow three forms of Kerberos authentication
      * Options allow access by passing UID and GID to the server
      * Can force users to connect as the Guest account if not configured to use Kerberos
   * Connection to an NFS shared folder requires shared folder permissions
   * NFS shared folder permissions granted to computers - not users
   * Two levels of access for computers
      * Read-Only
      * Read-Write
   * Default permissions assigns Read-ONly NFS share permission to all computers
   * Users use operating system specific commands to access the shared folder
* Sharing a folder using server Manager
* Server Manager Shares section can create and manage NFS shared folders
   * New Share Wizard shared folder creation options (Quick and Advanced)
   * NFS Share - Quick
      * Provide location and share name
      * Select authentication methods used when connecting to the NFS share
      * Add NFS shared folder permission entries for computers on the network
      * Modify NTFS/ReFS permissions to match the desired level of access for groups and users
Publishing a Shared Folder in Active Directory
* Steps to publish a shared folder to the Active Directory database
   * Right-click an OU within the Active Directory Users and Computers tool
   * Click New, Shared Folder
   * Opens a New Object - Shared Folder window
      * Supply the name and UNC path to the SMB or NFS shared folder
      * Click OK to create a shared folder object within the associated OU
   * Domain users can search Active Directory for shared folders using File Explorer
Implementing Distributed File System
* DFS used for accessing and managing content on file servers
   * Two server roles: DFS Namespaces and DFS Replication
* Each server role works independently of the other
* Each server role managed using the dame DFS Management tool
* Install DFS Namespaces and DFS Replication roles
   * Use the Add Roles and Features Wizard in Server Manager
Configuring DFS Namespaces
* Open Server Manager and select DFS Management from the tools menu
   * Click New Namespace within the Actions pane
* Start the New Namespace Wizard
   * Specify the name of the server that will host the DFS namespace
   * Specify the shared folder name for the DFS namespace
   * Specify the namespace type
   * Click Create to create the DFS namespace
   * Add target to a DFS namespace within the DFS Management tool
Configuring DFS Replication
* Server Manager DFS Management tool, click Start New Replication Group
   * New Replication Group wizard starts and user adds appropriate settings
* If configuring DFS namespace and a target contains more than one UNC
   * Replicate Folder Wizard starts and user adds appropriate settings
      * Demine replication group and folder anime
      * Verify replicated folders
      * Select primary server for file overwrite
      * Select the DFS replication topology
      * Define replication group schedule and bandwidth and create
Implementing Quotas and File Screens
* Need for restrictions
   * Prevents users from confusing too much space on the file server
   * Block users from adding the wrong type of files to shared folders
* Three NTFS features for restricting content
   * User quotas, folder quotas, file screens
* Install File Server Resource Manager server role on the file server
   * Required before configuring folder quotas and file screens
Configuring User Quotas
* Enable NTFS quotas for a filesystems
   * Right-click the root folder of a filesystem (e.g., C:;\) within File Explorer
   * Click Properties, highlight the Quota tab, and select the appropriate options
   * Click the Quota Entries button
      * Provide specific quota options for individual users and groups that override the default options
* Administrators group members receive no limits
Configuring Folder Quotas
* Two types: hard quotas and soft quotas
* File Server Resource Manager tool
   * File Quota Management section contains two subsections
      * Quotas and Quota Templates
* Create a new folder quota by highlighting Quotas folder
   * Click Create Quota within the Actions pane, specify folder path and settings
   * Can modify setting using the Custom Properties button
   * Can select a pre-configured template and can save quota settings in a new quota template
Configuring File Screens
* Two types: active screening and passive screening
* File Server Resource manager tool
   * File Screening Management section contains three subsections
      * File Screens, File Screen Templates, and File Groups
* Create a new file screen by highlighting File Screens folder
   * Click Create File Screen within the Actions pane, specify folder path and settings
   * Can modify settings using the Custom Properties button
   * Can select pre-configured property templates