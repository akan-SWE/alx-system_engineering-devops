# This directory contains all the scripts for 0x01-shell_permissions 

**0-iam_betty** - this script switches the current user to the user *betty*.<br>
**1-who_am_i** - this script prints the effective username of the current user.<br>
**2-groups** - this script prints the groups of the current user is part of.<br>
**3-new_owner** - this script changes the owner of the file *hello* to the user betty<br>
**4-empty** - this script creates an empty file called *hello*.<br>
**5-execute** - this script adds execute permissions to the owner of the file *hello*.<br>
**6-multiple_permissions** - this script adds execute permissions to the owner and the group owner<br> 
and the read permissions to other users, to the file *hello*.<br>
**7-everybody** - this script adds execution permissions to the owner, the group owner and the other users, to the file *hello*.<br>
**8-James_Bond** - this script sets the permissions to the file *hello* as follows:<br>
* *Owner:* no permissions at all
* *Group:* no pemissions at all
* *Other:* all the permissions

**9-John_Doe** - this script sets the mode of the file *hello* to this.<br>
        [ -rwxr-x-wx 1 user group 3 Aug  3 14:34 *hello* ]<br>

**10-mirror_permissions** - this script set the mode of the file *hello* the same as *olleh*'s mode.<br>
**11-directories_permissions** - this script adds execute permissions to all subdirectories of the current directory for the owner,<br>
the group owner and all other users.<br>
**12-directory_permissions** - this script creates a directory called *my_dir* with permissions 751 in the working directory.<br>
**13-change_group** - this script changes the group owner to *school* for the file *hello*.<br>
**100-change_owner_and_group** - this script changes the owner *vincent* and the group owner to *staff* for all the files and directories<br>
in the working directory.<br>
**101-symbolic_link_permissions** - this script changes the owner and group of *_hello* to *vincent* and *staff* respectively.<br>
**102-if_only** - this script changes the owner of the file *hello* to *betty* only if it is owner by *guillaume*.<br>
**103-Star_Wars** - this script will play the StarWarls IV episode in the terminal.<br>
