
# Windows Health Tool

This tool is a user-friendly Python script for monitoring and enhancing the system and security functions on Windows. It executes various CMD commands to display system information, perform hardware and network tests, and provide security checks and remediations. 

 
## Features

- **Network Information:** Displays local and public IP addresses, MAC address, open ports and more
- **Hardware Information:** Retrieves details on the GPU, disks, motherboard, and CPU using WMIC commands.
- **Network/Hardware Check:** Performs system tests such as ping, chkdsk, sfc, DISM, netsh, etc.
- **Basic Security:** Checks and remediates settings for Antivirus, Firewall, BitLocker (activation and deactivation), Remote Desktop, UAC, and user accounts.


## Preview
![1](https://github.com/user-attachments/assets/9a8c4611-ebbc-46d2-9fb1-e4638e040487)


## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the ***.bat*** file to make sure you have **administrative rights.**




## TPM/BitLocker Instructions

To use BitLocker without a compatible TPM, open the Group Policy Editor gpedit.mscand navigate to:

- **Computer Configuration &rarr; Administrative Templates &rarr; Windows Components &rarr; BitLocker Drive Encryption &rarr; Operating System Drives**

Double-click **"Require additional authentication at startup"**, enable the policy, and check **"Allow BitLocker without a compatible TPM"**.
Apply the changes and restart your computer.

If you prefer to use TPM, ensure that a compatible TPM is installed and enabled in your BIOS.

Here is a small [Tutorial](https://youtu.be/1daHNjzOzjI?t=82), how to activate TPM in your BIOS

## License

[MIT](https://choosealicense.com/licenses/mit/)

  <h2>Contact</h2>
  <p>
    For any questions or issues, please open an issue on the <a href="https://github.com/IddoxLatifi/HealthTool/issues" target="_blank">GitHub repository </a> or join my <a href="https://iddox.tech/" target="_blank">Website</a> for more Contact Informations.
  </p>
  <h2 align="left">I code with</h2>

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" height="40" alt="javascript logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" height="40" alt="docker logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/visualstudio/visualstudio-plain.svg" height="40" alt="visualstudio logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" height="40" alt="css3 logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" height="40" alt="git logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-original.svg" height="40" alt="rust logo"  />
</div>

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=IddoxLatifi&hide_title=false&hide_rank=false&show_icons=true&include_all_commits=true&count_private=true&disable_animations=false&theme=dracula&locale=en&hide_border=false&order=1" height="150" alt="stats graph"  />
  <img src="https://github-readme-stats.vercel.app/api/top-langs?username=IddoxLatifi&locale=en&hide_title=false&layout=compact&card_width=320&langs_count=5&theme=dracula&hide_border=false&order=2" height="150" alt="languages graph"  />
</div>

</body>
</html>

