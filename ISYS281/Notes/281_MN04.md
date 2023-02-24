Working with Local Users and Groups
* Local user account authentication
   * Must provide valid user name and password
* Local user account assigned righteous to the operating system
   * Examples: change system time or shut down the system
* Local user account granted access to resources
   * Based on the resource’s Access Control List (ACL)
* Local group accounts
* Simplify rights and permissions to multiple local user accounts
* Security Accounts Manager (SAM) Registry Database
   * Stores local user and group accounts
* Local user accounts used to authenticate users following workgroup installation
   * Administrator and Guest
* Local group accounts for assigning rights and permissions following system installation
   * Administrators, Guests, and users
* To create local user and group accounts
   * Use the Local Users and Groups MMC snap-in
* To create a new local user account
   * Select the Users folder from Local Users and Groups MMC snap-in
      * Choose appropriate user’s tasks after installation
* To create a new local group account
   * Select the Groups folder from Local Users and Groups MMC snap-in
Active Directory Basics
* Options for logging into an Active Directory domain computer
   * Local user account
      * Hostname is local user account
   * Domain user account
      * Encrypted token and domain group account issues to the computer
* Domain user, group, and computer accounts stored as objects in a database
   * Active Directory database conforms to ITU X.500 standard
* Lightweight Directory Access Protocol (LDAP) provides quick access
* Active Directory Group Policy provides advantageous features
Active Directory Objects
* Active Directory schema
   * All available object types (classes) and associated properties (attributes)
   * Schema can be extended
* Leaf objects represent a user account, group account, or computer account
* Container objects within the Active Directory database
   * Group leaf objects for ease of administration and Group Policy application
   * Domains, organization units (OUs), sites
Active Directory Forests, Trees, and Trusts
* Forests are used to provide for multiple domains within the same organization
   * GMC
      * Chevrolet
      * Buick
      * Cadillac
* Establish trust relationships with other forest
* Active Directory forests
   * Provide for multiple domains within the same organization
   * Forest root domainL first domain in a forest
* Using additional domain controllers
   * Ass them to the forest root domain
   * Configure them to host an Active Directory database for another domain within the same forest
* Active Directory tree has parent and child domains
* Trust relationship (trust)
   * Allows users to access resources within other domains
   * Requires access within the resource’s ACL
   * Trust relationships represented by arrow symbols in tree diagram
* Transitive property minimizes number of trust relationships needed
* Other types of trusts
   * Shortcut trust speeds up resource access
   * External trust, forest trust realm trust
Active Directory Groups
* Two main types of group accounts
   * Distribution groups and security groups
* Group scopes
   * Organize rights and permissions assignments across multiple domains
   * Use a combination within a forest to organize the assignment of permissions
   * Global scope
   * Domain local scope
   * Universal scope
Domain and Forest Functional Levels
* Microsoft NT4 Server single sign-on implementation
   * Primary domain controller (PDC) and backup domain controllers (BDCs)
* Windows 2000 Server Active Directory required backward compatibility
* New Windows Server versions introduce additional Active Directory features
* Domain functional levels
   * Allow backward compatibility to older versions of Active Directory
* Active Directory forest functional level
   * Defines minimum domain functional level for each domain within the forest
Sites and Active Directory Replication
* Active Directory database
   * Schema partition: contains information that defines object classes within the domain. Determines what objects can exist with AD
   * Configuration partition: Stores the structure and layout of the forest, including the trust relationship between domains
   * Domain partition: stores all objects within a specific OU
* Control Active Directory replication bandwidth usage
   * Site object (site) represents a physical location in an organization
      * Associates with one or more subnet objects representing IP networks containing domain controllers
      * Connected to other site link objects
Global Catalog
* Global catalog provides a list of all object names in a forest
   * Stored on at least one domain controller in the forest
   * Required to complete authentication process and log in to the domain
      * Cached credentials might provide access if global catalog not available
* User Principal Name (UPN) is a unique name in the global catalog
   * Users can use it to log in to their domain from any computer int he forest
* Global catalog updates
   * Issue might be resolved with Universal Group Membership Caching (UGMC)
FSMO roles
* Flexible Single Master Operation (FSMO) functions
   * Functions that must be coordinated from a single domain controller
* Domain controller configuration
   * To hold a single FSMO role
   * To hold all FSMO roles for its domain or forest
* Five FSMO roles available within Active Directory
   * First domain controller installed within the forest root domain contains all five
* Problem if domain comptroller holding an FSMO role becomes unavailable
Azure Active Directory
* Active Directory service within the Microsoft Azure cloud
* Provides the same single-sign-on features of Active Directory
* Designed to allow access to cloud applications
* Can be configured to trust an organization’s Active Directory forest
* Can be configured to mirror an organization’s Active Directory forest using a synchronization service.
* Can be used to replace an Active Directory forest within an organization
   * If Internet connection is consistently robust
Installing Active Directory
* Open Server Manager and select the Active Directory Domain Services role
* Progress through the Add Roles and Features Wizard
   * Installs files necessary to create a domain controller, management tools, and Windows PowerShell cmdlets
* Select Promote this server to a domain controller from the Add Roles and Features Wizard
* Make sure to install DNS services as well as ADDS
Installing a Forest Root Domain
* Active Directory Domain Services Configuration Wizard
   * Select  Add a new forest and specify new root domain name
   * Select domain controller options
      * Specify domain and forest functional levels, domain controller capabilities, and Directory Services Restore Mode (DSRM) password
   * Select DNS to specify DNS delegation
   * Select Additional Options to specify NetBIOS name
   * Select Paths to specify for folders
   * Review options and install
* Select domain.local or lastname.local
Installing a domain within an Existing Forest
* Start the Active Directory Domain Services Configuration Wizard
   * Select Add a new domain to an existing
   * Adding a child domain
      * Specify name of the parent domain and name of the new child domain
   * Adding a new parent domain for a new tree
      * Select Tree Domain and specify the name of the parent domain
   * Authenticate as a user within a forest that is part of Enterprise Admins group
   * Process through Wizard as if configuring a new forest root domain
Installing a Domain Controller within an Existing Domain
* Start the Active Directory Domain Services Configuration Wizard
   * Select Add a domain controller to an existing domain
      * Specify the existing domain name within the Domain text box
   * Authenticate within the domain that is part of the Domain Admins group
      * Click Change and supply credentials
   * Progress through Wizard as if configuring a new forest root domain
      * No need to set the forest or domain functional levels
      * Can select where to obtain initial copy of Azure Directory database
Raising Functional Levels
* Use the Active Directory Domains and Trusts tool
   * Select domain within the navigation pane
   * Click More Actions, Raise Domain Functional Level from the Actions pane
   * Select the appropriate functional level from the drop-down box and click Raise
* Can raise the forest functional level
   * Select Active Directory Domains and Trusts within the navigation pane
   * Click More Actions, Raise Forest Functional level from the Actions pane
   * Select appropriate functional level from the drop-down box and click Raise
Creating Trust Relationships
* Use conditional forwarder to ensure DNS servers can resolve the DNS records
* Open the Active Directory Domains and Trusts tool
   * Select the domain within the navigation pane
   * Click More Actions, Properties from the Actions pane
* Domain window opens
   * Select the Trusts tab and click New Trust to start the New Trust Wizard
   * Choose options: external or forest; one-way outgoing or incoming or two-way; transitive or non-transitive, etc.
   * Select the trust and click Properties to validate or change trust settings
Managing FSMO Roles
* Command to view all FSMO roles held by domain controllers within your forest
   * netdom query fsmo command
* Other commands show domain controllers holding the forest-wide and domain-wide FSMO roles
* Fault tolerance may require movement of FSMO roles from one domain controller to another
   * Move one or multiple FSMO roles from one domain controller to another
   * If source domain controller offline, ass the -Force option to the command
      * Move-ADDirectoryServerOperationMasterRole
Configuring sites and Replication
* Configuring sites
   * Open Active Directory Sites and Services tool
   * Right-click Default-First-Site-Name and rename
   * Right-click Sites folder to create additional sites
   * Supply site name and select the appropriate site link
   * Specify appropriate IP network and select the associated site
* Two protocols perform Activity Directory replication
   * IP and Simple Mail Transfer Protocol (SMTP)
Configuring Global Catalog and UGMC
* Configure a domain controller to host a copy of the global catalog
* Open Active Directory Sites and Services and click Properties
   * Right-click NTDS Settings under the server object for the domain controller
   * Select the Global Catalog option to place a copy of the global catalog on the domain controller
* UGMC can host a copy of the global catalog if replication concerns exist
   * Allows universal groups to be cached on domain controllers within the site
   * Allows fast logon
Working with Organizational Units
* Open the Active Directory Users and Computers tool
   * New domain only has one OU called Domain Controller by default
   * Other folders exist to organize objects within the domain
   * Create an OU
      * Right-click folder/domain object under which create the OU
      * Click New, Organizational Unit
      * New Window opens; supply the name of the OU
      * Verify Protect container from accidental deletion option
Working with User Objects
* Prior to a user logging in to an Active Directory domain:
   * Create a domain user account object for the user in the appropriate OU
      * Within Active Directory Users and computers
      * Right-click the appropriate OU, click New, then click User
      * Opens the New Object - User wizard; supply appropriate information
      * Supply the new user password, account options
      * Create user object
      * Ass the appropriate user attributes
      * Perform other common user management functions
Working with Group Objects
* Group objects simplify the assignment of rights and permissions to users
* Create a group object using the New Object - Group window
   * Within Active Directory Users and Computers
   * Right-click the appropriate OU and click New, Group
   * Supply the group type, scope, and name
* Manage group membership
   * Within Active Directory Users and Computers
   * Click Properties and highlight the Members tab
Working with Computer Objects
* Two ways to move a computer account object to an OU
   * Open Active Directory Users and Computers
      * Right-click the computer account within the Computers folder
      * Click Move and select the target OU
   * Open Active Directory Users and Computers (prestage computer accounts)
      * Right-click the appropriate OU, and click New, Computer
* Encryption key within computer accounts needed for communication
* Handle computers joined to an Active Directory domain with hardware failure
Read-Only Domain Controllers
* Contains a read-only copy of the Active Directory database for the domain
* Object creation and management replicated from large office
   * Primary concern during replication is security
   * Replicate password attributes for users within the branch office only
* Install RODC using Active Directory Domain Services Configuration Wizard
* Can prestage a RODC computer account using the Active Directory Domain Services Installation Wizard
* Can delete RODC if stolen and reset computer account for stolen computers