
Project 6-2: Provide screen shot for step 11
Project 6-3 **use attached HP Driver** Provide screen shot for step 6L
Skip Project 6-4:
Project 6-5: Provide screen shot for step 4d
Project 6-6: Provide screen shot for step 9b
Skip Project 6-7:
### Project 6-1: Provide screen shot for step 3

### Enhanced Session Mode Removal

If your system is configured according to Lab Environment 2, you will configure the Hyper-V virtual machine for your Windows Server 2019 host to prevent Windows 10 print devices from being made available within Windows Server 2019.

1. On your Windows 10 system, log in as a user that has administrative privileges, right-click the Start button, and select **Run**. In the Run dialog box, type **virtmgmt.msc** and click **OK** to open Hyper-V Manager.
    
2. In the Actions pane of Hyper-V Manager, click **Hyper-V Settings**.
    
3. In the Hyper-V Settings window, select **Enhanced Session Mode** under the User section within the navigation pane. Deselect **Use enhanced session mode** and click **OK**.
    

### Project 6-2

### Print Server Installation

In this Hands-On Project, you install, on your Windows Server 2019 host, the server roles and features required for the remaining Hands-On Projects in this module. These include the Print and Document Services role as well as the Internet Printing Client and LPR Port Monitor features.

1.  1
    
    Boot your Windows Server 2019 host and log into domain_X_.com as Administrator using the password **Secret555**. Next, click **Start** and then click **Server Manager**.
    
2.  2
    
    Within Server Manager, click the **Manage** menu and then click **Add Roles and Features**.
    
3.  3
    
    At the Select installation type page, click **Next**.
    
4.  4
    
    At the Select destination server page, click **Next**.
    
5.  5
    
    At the Select server roles page, select **Print and Document Services** and click **Add Features** when prompted. Click **Next**.
    
7.  6
    
    At the Select features page, select **Internet Printing Client** and **LPR Port Monitor** and click **Next**.
    
8.  7
    
    At the Print and Document Services page, click **Next**.
    
9.  8
    
    At the Select role services page, note that Print Server is automatically selected.
    
    1.  Select **Internet Printing** and click **Add Features** when prompted.
        
    2.  Select **LPD Service** and click **Next**.
        
10.  9
    
    At the Web Server Role (IIS) page, click **Next**.
    
11.  10
    
    At the Select role services page, click **Next**.
    
12.  11
    
    At the Confirm installation selections page, click **Install** to install the Print and Document Services role, as well as the Internet Printing Client and LPR Port Monitor features.
    
13.  12
    
    At the Installation progress page, click **Close**.
    

Project 6-3

### Print Server Configuration

In this Hands-On Project, you examine the configuration of your Windows Server 2019 print server and then add two sample shared printers (SamplePrinter1 and SamplePrinter2).

1.  1
    
    Within Server Manager on your Windows Server 2019 host, click the **Tools** menu and then click **Print Management**.
    
2.  2
    
    In the navigation pane of the Print Management tool, expand **Print Servers**, and then expand **SERVER_X_**.
    
3.  3
    
    Highlight **Drivers** in the navigation pane and note the default printer drivers that are installed on your print server. For each driver, scroll to the right and note whether the printer driver is an XPS driver. Next, click **More Actions**, **Add Driver** from the Actions pane.
    
    1.  At the Add Printer Driver Wizard, click **Next**.
        
    2.  At the Processor Selection page, note the default architecture listed and click **Next**.
        
    3.  At the Printer Driver Selection page, note the default selection (Generic/Text Only) and click **Next**.
        
    4.  At the Completing the Add Printer Driver Wizard page, click **Finish**.
        
    5.  For your newly added driver, scroll to the right and note whether the printer driver is an XPS driver.
        
4.  4
    
    Highlight **Forms** in the navigation pane and note the default forms installed on your print server.
    
5.  5
    
    Highlight **Ports** in the navigation pane and note the default ports available on your print server.
    
6.  6
    
    Highlight **Printers** in the navigation pane and note the two default printers available on your print server.
    
    1.  Click **More Actions**, **Add Printer** from the Actions pane.
        
    2.  At the Network Printer Installation Wizard, select **Add a new printer using an existing port**, ensure that **LPT1: (Printer Port)** is listed in the associated drop-down box, and click **Next**.
        
    4.  At the Printer Driver page, select **Use an existing printer driver on the computer**, ensure that **Generic/Text Only** is listed in the associated drop-down box and click **Next**.
        
    5.  At the Printer Name and Sharing Settings page, note that printer sharing is enabled by default, type **SamplePrinter1** in both the Printer Name and Share Name text boxes. Next, type **Marketing Department** in the Location text box, type **Sample Marketing Printer for** Module 6 in the Comment text box and click **Next**.
        
    6.  At the Printer Found page, click **Next**.
        
    7.  At the Completing the Network Printer Installation Wizard, select **Add another printer** and click **Finish**.
        
    8.  At the Printer Installation page, ensure that **Add a new printer using an existing port** is selected, that **LPT1: (Printer Port)** is listed in the drop-down box, and click **Next**.
        
    9.  At the Printer Driver page, ensure that **Use an existing printer driver on the computer** is selected and that **Generic/Text Only** is listed in the associated drop-down box and click **Next**.
        
    10.  At the Printer Name and Sharing Settings page, type **SamplePrinter2** in both the Printer Name and Share Name text boxes. Next, type **Accounting Department** in the Location text box, type **Sample Accounting Printer for Module 6** in the Comment text box and click **Next**.
        
    11.  At the Printer Found page, click **Next**.
        
    12.  At the Completing the Network Printer Installation Wizard, click **Finish**.
        
    13.  Note that SamplePrinter1 and SamplePrinter2 have been added to the Printers node. Scroll to the right and note that each printer uses a Type 3 printer driver.
        
7.  7
    
    Highlight **SERVER_X_** in the navigation pane and click **More Actions**, **Properties** from the Actions pane. Note the default location of the spool folder and that notifications are enabled by default.
    
    1.  Highlight the **Security** tab and note the default printer and print server permissions are granted to the Everyone, CREATOR OWNER, and Administrators groups.
        
    2.  Click **Add**, type **Bob Burtt,** and click **OK**.
        
    3.  Note that Bob Burtt is assigned Print and View Server permissions by default. Select **Manage Documents** and click **OK**.
        
8.  8
    
    Click **More Actions**, **Properties** from the Actions pane. Note the email and script options available notifications and click **OK**.
    

Project 6-4

### Printer Properties

In this Hands-On Project, you explore and configure various properties and features for SamplePrinter1 as well as verify that it was published successfully to Active Directory.

1.  1
    
    In the navigation pane of the Print Management tool on your Windows Server 2019 host, highlight **Printers** under SERVER_X_. Next, select **SamplePrinter1** and click **More Actions**, **Pause Printing** from the Actions pane to ensure that documents printed to SamplePrinter1 are held in the print queue.
    
3.  2
    
    Click **More Actions**, **Properties** from the Actions pane.
    
    1.  On the General tab, note the name, location, comment, features, and paper information for SamplePrinter1.
        
    2.  Click **Preferences** and note the default options on the Layout tab. Highlight the **Paper/Quality** tab, note the default paper source setting, and click **OK**.
        
    3.  Click **Print Test Page** to submit a test page document to SamplePrinter1, and click **Close** at the confirmation window.
        
    4.  Highlight the **Sharing** tab, note the default sharing options render print jobs on client computers, and select **List in the directory**.
        
    5.  Highlight the **Ports** tab and note that SamplePrinter1 prints to the print device located on LPT1. Select **Enable printer pooling** and then select **LPT2** and **LPT3**. Next, select **Add Port**, note the default port types available, and click **Cancel**.
        
    6.  Highlight the **Advanced** tab and note the default time, priority, driver, and spooling options. Select **Start printing after last page is spooled** and then select **Hold mismatched documents**.
        
        1.  Click **Print Processor**, note the available spooling formats available for a non-XPS print device, and click **OK**.
            
        2.  Click **Separator Page** and then click **Browse**. Select **pcl.sep** from the System32 directory and click **Open**. Click **OK** to add the separator page to SamplePrinter1.
            
    7.  Highlight the **Security** tab, highlight **Bob Burtt**, and note the permissions you assigned on the print server were inherited to SamplePrinter1.
        
        1.  Select **Manage this printer** under the Allow column and click **Apply** to ensure that Bob Burtt has all printer permissions.
            
        2.  Click **Advanced**, highlight the **Bob Burtt** entry that grants _Manage this printer,_ and click **Edit**. Click **Show advanced permissions**, note the advanced permissions that make up the _Manage this printer_ print permission, and click **OK**.
            
        3.  Highlight the **Auditing** tab and click **Add**.
            
        4.  Click **Select a principal**, type **Domain Admins** in the text box, and click **OK**. Note that Print permission is audited by default. Select **Manage this printer** and **Manage documents** to additionally audit printer and document management events, and click **OK**.
            
        5.  Highlight the **Effective Access** tab and note the information message. Click **Apply**. Next, click **Select a user**, type **Bob Burtt** in the text box, and click **OK**. Click **View effective access**, note that Bob Burtt is granted all printer permissions, and click **OK**.
            
    8.  Highlight the **Device Settings** tab, note the default paper options, and click **OK**. Note that SamplePrinter1 has a status of Paused and that there is 1 print job within the queue that contains the test page you printed.
        
4.  3
    
    Click **More Actions**, **Enable Branch Office Direct Printing** from the Actions pane. Because Branch Office Direct Printing only applies to printers that print to network-attached print devices, click **More Actions**, **Disable Branch Office Direct Printing** from the Actions pane to remove this setting.
    
5.  4
    
    Close the Print Management tool.
    
7.  5
    
    Within Server Manager, click the **Tools** menu and then click **ADSI Edit**.
    
    1.  In the ADSI Edit tool, select **More Actions**, **Connect to** within the Actions pane.
        
    2.  At the Connection Settings window, click **OK** to add the domain partition of the Active Directory database (Default naming context).
        
    3.  In the navigation pane, expand **Default naming context**, **DC=domain_X_, DC=com**, **OU=Domain Controllers**, and then highlight **CN=SERVER_X_**. Note the printQueue object that represents SamplePrinter1.
        
    4.  Close ADSI Edit.
        

Project 6-5

### Adding Shared Printers

In this Hands-On Project, you add SamplePrinter1 and SamplePrinter2 on your WindowsServer2019VM2 virtual machine. Then you submit print jobs to both SamplePrinter1 and SamplePrinter2.

1.  1
    
    Within Server Manager on your Windows Server 2019 host, select the **Tools** menu and then click **Hyper-V Manager**.
    
2.  2
    
    Highlight **WindowsServer2019VM2** within the virtual machines pane of Hyper-V Manager and click **Connect** in the Actions pane. In the Virtual Machine Connection window, click **Start** to boot your new virtual machine.
    
3.  3
    
    At the login screen, click the **Ctrl+Alt+Delete** button within the Virtual Machine Connection window, supply the password **Secret555** for Administrator and press **Enter** to log into the system.
    
4.  4
    
    Click **Start** and then click **Control Panel**. Click **View devices and printers** under the Hardware section, and note the default printers shown.
    
    1.  Click **Add a printer** to start the Add Printer wizard. Note that SamplePrinter1 on SERVER_X_ was automatically detected because it was published in Active Directory.
        
    2.  Ensure that **SamplePrinter1** is selected and click **Next**. The printer driver for SamplePrinter1 is automatically downloaded and configured on your system during this process. When the process has completed, note the shared printer called _SamplePrinter1 on SERVERX.domainX.com_ within the Devices and Printers section of Control Panel. Click **Finish**.
        
    3.  Click **Add a printer** to start the Add Printer wizard. Next, click **The printer that I want isn’t steped**.
        
    4.  Select **Select a shared printer by name** and type \\serverX\SamplePrinter2 in the text box and click **Next**.
        
    5.  Click **Next**.
        
    6.  Click **Print a test page** and note that Windows Server 2019 indicates that there was an error printing the test page. Click **Close**.
        
    7.  Click **Finish**. Note the shared printer _SamplePrinter2 on serverX_ within the Devices and Printers section of Control Panel.
        
    8.  Right-click **SamplePrinter1 on SERVER_X_.domain_X_.com** and click **Printer properties**. Click **Print Test Page** and note that Windows Server 2019 indicates that the printer is in an error state. Click **Close** to close the information window and click **OK** to close the _SamplePrinter1 on SERVERX.domainX.com_ Properties window.
        

Project 6-6

### Print Job Management

In this Hands-On Project, you view and manage the print jobs that you have submitted to SamplePrinter1 and SamplePrinter2 on your WindowsServer2019VM2 virtual machine and Windows Server 2019 host.

1.  1
    
    Within the Devices and Printers section of Control panel on your WindowsServer2019VM2 virtual machine, double-click **SamplePrinter1 on** **SERVER_X_.domain_X_.com** to open the associated print queue. Note the two Test Page print jobs and their submission times. The first one was submitted in Project 6-4, and the second one was submitted in Project 6-5. Also note the absence of a Status value.
    
2.  2
    
    Highlight the second (most recent) print job, select the **Document** menu, and note the options available. Click **Properties**, drag the Priority slider to the right side to set a value of **99** and click **OK**.
    
3.  3
    
    Highlight the first (oldest) print job, select the **Document** menu, click **Cancel,** and click **Yes** when prompted.
    
4.  4
    
    Select the **Printer** menu and note that printing is paused for all documents within the SamplePrinter1 print queue. Click **Close** to close the print queue window for SamplePrinter1.
    
5.  5
    
    Double-click **SamplePrinter2 on server_X_** to open the associated print queue. Note the Test Page print job that was submitted in Project 6-5. Also note that the Test Page print job has a status of _Error - Printing_ since the print queue for SamplePrinter2 was not paused, and the print server attempted to print the Test Page to a non-existent print device.
    
6.  6
    
    Select the **Printer** menu and click **Close** to close the print queue window for SamplePrinter2.
    
7.  7
    
    Close Control Panel.
    
8.  8
    
    Within Server Manager on your Windows Server 2019 host, select the **Tools** menu and then click **Print Management**.
    
    1.  Highlight **Printers** under SERVER_X_ and note the value in the Queue Status column for SamplePrinter1 and SamplePrinter2.
        
    2.  Select **SamplePrinter1** and select **More Actions**, **Open Printer Queue**. Note that the print queue for SamplePrinter1 indicates the same information shown within the same print queue on your WindowsServer2019VM2 virtual machine.
        
    3.  Highlight the Test Page print job, select the **Document** menu, and note the options available.
        
    4.  Select the **Printer** menu, note the options available, and click **Close** to close the print queue window for SamplePrinter1.
        
    5.  Select **SamplePrinter2** and select **More Actions**, **Open Printer Queue**. Note that the print queue for SamplePrinter2 indicates the same information shown within the same print queue on your WindowsServer2019VM2 virtual machine.
        
    6.  Close the Print Management tool.
        
10.  9
    
    Open the Google Chrome Web browser, and navigate to the URL http://serverX/printers. Note the status, location, and comment for SamplePrinter1 and SamplePrinter2.
    
    1.  Click **SamplePrinter1** to open the SamplePrinter1 print queue. Note your Test Page and view the document and printer actions available.
        
    2.  Click **All Printers** to return to the printer list.
        
    3.  Click **SamplePrinter2** to open the SamplePrinter2 print queue. Select the **Test Page** print job and click **Pause** under the DOCUMENT ACTIONS section to place the print job on hold. Note the new status of _Paused – Error – Printing_.
        
    4.  Close the Google Chrome Web browser.
        

Project 6-7

### Printer Troubleshooting

In this Hands-On Project, you use custom filters within the Print Management tool to examine printer and print job errors, as well as restart the Print Spooler service on your Windows Server 2019 host.

1.  1
    
    Within Server Manager on your Windows Server 2019 host, select the **Tools** menu and then click **Print Management**.
    
    1.  Expand **Custom Filters** in the navigation pane and highlight **Printers Not Ready**. Note the status of SamplePrinter1 and SamplePrinter2 within the Queue Status column.
        
    2.  Highlight **SamplePrinter1** and click **More Actions**, **Resume Printing** from the Actions pane. Note that the status of SamplePrinter1 now reports Error.
        
    3.  Click **More Actions**, **Show Extended View** under the Printers Not Ready section of the Actions pane. Note that the Test Page job for SamplePrinter1 lists _Error – Printing_ within the Job Status column.
        
    5.  Highlight **SamplePrinter2** and note that the Test Page job for SamplePrinter1 lists _Paused - Error – Printing_ within the Job Status column.
        
2.  2
    
    Right-click **Start** and click **Windows PowerShell (Admin)**. Type Restart-Service spooler -force at the Windows PowerShell prompt and press **Enter**. Close Windows PowerShell when finished.
    
3.  3
    
    In the Print Management tool, highlight **Printers Not Ready** in the navigation pane and click **More Actions**, **Refresh**. Note that the SamplePrinter1 and SamplePrinter2 are no longer visible within the Printers Not Ready custom filter.
    
4.  4
    
    Highlight **Printers With Jobs** in the navigation pane. Note that SamplePrinter1 and SamplePrinter2 are shown and that each one has a status of Ready within the Queue Status column and 1 print job listed within the Jobs In Queue column.
    
    1.  Highlight **SamplePrinter1** and note that the Test Page print job has a status of _Sent to Printer_ in the Job Status column.
        
    2.  Highlight **SamplePrinter2** and note that the Test Page print job has a status of _Paused_ in the Job Status column.
        
    3.  Right-click the **Test Page** print job in the SamplePrinter2 print queue and click **Resume**. Note that the status returns to _Error – Printing_.
        
    4.  Right-click the **Test Page** print job in the SamplePrinter2 print queue and click **Cancel**. After a few moments, SamplePrinter2 should disappear from the Printers With Jobs custom filter.
        
    5.  Close the Print Management console.