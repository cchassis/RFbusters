# Setup Instructions

## Setting up the Single Board Computer 
``` 
https://wiki.up-community.org/Ubuntu
```
### Operating System Installation

Download Ubuntu 16.04 ISO from the Ubuntu download page (works with desktop and server edition)
```
https://www.ubuntu.com/download/desktop
https://www.ubuntu.com/download/server
```
Burn the downloaded image on a USB stick. We suggest to use etcher for doing that. You can download it from
https://etcher.io
Insert the USB installer disk in a empty USB port and proceed with a normal Ubuntu installation.
After the system is rebooted, login into it and type the following commands in a terminal:
```
sudo apt update
sudo apt full-upgrade -y
sudo reboot
```

#### Install Ubuntu kernel for UP from PPA

After the reboot you need to add our repository:
```
sudo add-apt-repository ppa:ubilinux/up
```
Update the repository list
```
sudo apt update
```
Remove all the generic installed kernel
```
sudo apt-get autoremove --purge 'linux-.*generic'
```
Install our kernel:
```
sudo apt-get install linux-image-generic-hwe-16.04-upboard
```
Reboot
```
sudo reboot
```
After the reboot you can verify that the kernel is indeed installed by typing
```
$ uname -srv
```
Linux 4.10.0-42-generic #5000~upboard9-Ubuntu SMP Tue Dec 12 11:46:16 UTC 2017

--------------

### Enable the HAT functionality from userspace
To be able to use the GPIO, PWM, SPI, I2C and uart functionality with a normal user we created a ubuntu package that set the correct permission.

NOTE: this could create security problem, do only if you know what are you doing

After adding our PPA you can install it with:
```
sudo apt install upboard-extras
```
after that you need to add the user that need to access the HAT functionality to the corresponding groups:

for example this command permit to the current user to access to the gpio functionality
```
sudo usermod -a -G gpio ${USER}
```
leds
```
sudo usermod -a -G leds ${USER}
```
spi
```
sudo usermod -a -G spi ${USER}
```
i2c
```
sudo usermod -a -G i2c ${USER}
```
uart
```
sudo usermod -a -G dialout ${USER}
```
to apply the permission changes after issuing the previous command a reboot is needed
```
sudo reboot
```
--------------------------------------------------------------------------------------------------------------------------

### GPIO Library
```
https://github.com/intel-iot-devkit/mraa/blob/master/docs/up.md
```
Installing on Ubuntu

Here is a PPA for installing on Ubuntu Xenial or Bionic: https://launchpad.net/~mraa/+archive/ubuntu/mraa
```
sudo add-apt-repository ppa:mraa/mraa
sudo apt-get update
sudo apt-get install libmraa1 libmraa-dev libmraa-java python-mraa python3-mraa node-mraa mraa-tools
```
Running MRAA tools or applications on Ubuntu systems requires elevated permissions (e.g. run with sudo).


--------------------------------------------------------------------------------------------------------------------------
## Install GNURadio and UHD
```
https://kb.ettus.com/Building_and_Installing_the_USRP_Open-Source_Toolchain_(UHD_and_GNU_Radio)_on_Linux
```
### Update and Install dependencies
Before building UHD and GNU Radio, you need to make sure that all the dependencies are first installed.

However, before installing any dependencies, you should first make sure that all the packages that are already installed on your system are up-to-date. You can do this from a GUI, or from the command-line, as shown below.

On Ubuntu systems, run:
```
   sudo apt-get update
```
On Ubuntu 17.04 systems, run:
```
   sudo apt-get -y install git swig cmake doxygen build-essential libboost-all-dev libtool libusb-1.0-0 libusb-1.0-0-dev libudev-dev libncurses5-dev libfftw3-bin libfftw3-dev libfftw3-doc libcppunit-1.13-0v5 libcppunit-dev libcppunit-doc ncurses-bin cpufrequtils python-numpy python-numpy-doc python-numpy-dbg python-scipy python-docutils qt4-bin-dbg qt4-default qt4-doc libqt4-dev libqt4-dev-bin python-qt4 python-qt4-dbg python-qt4-dev python-qt4-doc python-qt4-doc libqwt6abi1 libfftw3-bin libfftw3-dev libfftw3-doc ncurses-bin libncurses5 libncurses5-dev libncurses5-dbg libfontconfig1-dev libxrender-dev libpulse-dev swig g++ automake autoconf libtool python-dev libfftw3-dev libcppunit-dev libboost-all-dev libusb-dev libusb-1.0-0-dev fort77 libsdl1.2-dev python-wxgtk3.0 git-core libqt4-dev python-numpy ccache python-opengl libgsl-dev python-cheetah python-mako python-lxml doxygen qt4-default qt4-dev-tools libusb-1.0-0-dev libqwt5-qt4-dev libqwtplot3d-qt4-dev pyqt4-dev-tools python-qwt5-qt4 cmake git-core wget libxi-dev gtk2-engines-pixbuf r-base-dev python-tk liborc-0.4-0 liborc-0.4-dev libasound2-dev python-gtk2 libzmq3-dev libzmq5 python-requests python-sphinx libcomedi-dev python-zmq
   ```
On Ubuntu 16.04 systems, run:
```
   sudo apt-get -y install git swig cmake doxygen build-essential libboost-all-dev libtool libusb-1.0-0 libusb-1.0-0-dev libudev-dev libncurses5-dev libfftw3-bin libfftw3-dev libfftw3-doc libcppunit-1.13-0v5 libcppunit-dev libcppunit-doc ncurses-bin cpufrequtils python-numpy python-numpy-doc python-numpy-dbg python-scipy python-docutils qt4-bin-dbg qt4-default qt4-doc libqt4-dev libqt4-dev-bin python-qt4 python-qt4-dbg python-qt4-dev python-qt4-doc python-qt4-doc libqwt6abi1 libfftw3-bin libfftw3-dev libfftw3-doc ncurses-bin libncurses5 libncurses5-dev libncurses5-dbg libfontconfig1-dev libxrender-dev libpulse-dev swig g++ automake autoconf libtool python-dev libfftw3-dev libcppunit-dev libboost-all-dev libusb-dev libusb-1.0-0-dev fort77 libsdl1.2-dev python-wxgtk3.0 git-core libqt4-dev python-numpy ccache python-opengl libgsl-dev python-cheetah python-mako python-lxml doxygen qt4-default qt4-dev-tools libusb-1.0-0-dev libqwt5-qt4-dev libqwtplot3d-qt4-dev pyqt4-dev-tools python-qwt5-qt4 cmake git-core wget libxi-dev gtk2-engines-pixbuf r-base-dev python-tk liborc-0.4-0 liborc-0.4-dev libasound2-dev python-gtk2 libzmq-dev libzmq1 python-requests python-sphinx libcomedi-dev python-zmq
```

After installing the dependencies, you should reboot the system.

If the installation of the dependencies completes without any errors, then you can proceed to build and install UHD and GNU Radio.

### Building and installing UHD from source code
UHD is open-source, and is hosted on GitHub. You can browse the code online at the link below, which points to version 3.10.1.0, which is the the latest release at the time of this writing.

UHD repository on GitHub
There are several good reasons to build GNU Radio from source code, especially for doing development and prototyping. It it enables an easy way to customize the location of the installation, and to install multiple UHD versions in parallel, and switch between them. It also provides much more flexibility in upgrading and downgrading versions, and allows the user to modify the code and create customized versions, which could possibly include a patch or other bug-fix.

To build UHD from source code, clone the GitHub repository, check out a branch or tagged release of the repository, and build and install. Please follow the steps below. Make sure that no USRP device is connected to the system at this point.

First, make a folder to hold the repository.
```
   cd $HOME
   mkdir workarea-uhd
   cd workarea-uhd
```
Next, clone the repository and change into the cloned directory.
```
   git clone https://github.com/EttusResearch/uhd
   cd uhd
```
Next, checkout the desired UHD version. You can get a full listing of tagged releases by running the command:
```
   git tag -l
```
Example truncated output of git tag -l:
```
$ git tag -l
...
release_003_009_004
release_003_009_005
release_003_010_000_000
```
Note: As of UHD Version 3.10.0.0, the versioning scheme has changed to be a quadruplet format. Each element and version will follow the format of: Major.API.ABI.Patch. Additional details on this versioning change can be found here.

After identifying the version and corresponding release tag you need, check it out:
```
   # Example: For UHD 3.9.5:
   git checkout release_003_009_005
   # Example: For UHD 3.10.1.0: 
   git checkout release_003_010_001_000
```
Next, create a build folder within the repository.
```
   cd host
   mkdir build
   cd build
```
Next, invoke CMake to create the Makefiles.
```
   cmake ../
```   
Next, run Make to build UHD.
```
   make
```   
Next, you can optionally run some basic tests to verify that the build process completed properly.
```
   make test
```
Next, install UHD, using the default install prefix, which will install UHD under the /usr/local/lib folder. You need to run this as root due to the permissions on that folder.
```
   sudo make install
```
Next, update the system's shared library cache.
```
   sudo ldconfig
```
Finally, make sure that the LD_LIBRARY_PATH environment variable is defined and includes the folder under which UHD was installed. Most commonly, you can add the line below to the end of your $HOME/.bashrc file:
```
   export LD_LIBRARY_PATH=/usr/local/lib
```
At this point, UHD should be installed and ready to use. You can quickly test this, with no USRP device attached, by running uhd_find_devices. You should see something similar to the following.

linux; GNU C++ version 4.8.4; Boost_105400; UHD_003.010.000.HEAD-0-g6e1ac3fc

No UHD Devices Found
Building and installing GNU Radio from source code
As with UHD, GNU Radio is open-source and is hosted on GitHub. You can browse the code online at the link below, which points to version 3.7.10.1, which is the the latest release at the time of this writing.

GNU Radio repository on GitHub
As with UHD, there are several good reasons to build GNU Radio from source code, especially for doing development and prototyping. It it enables an easy way to customize the location of the installation, and to install multiple GNU Radio versions in parallel, and switch between them. It also provides much more flexibility in upgrading and downgrading versions, and allows the user to modify the code and create customized versions, which could possibly include a patch or other bug-fix.

Similar to the process for UHD, to build GNU Radio from source code, clone the GitHub repository, check out a branch or tagged release of the repository, and build and install. Please follow the steps below. Make sure that no USRP device is connected to the system at this point.

First, make a folder to hold the repository.
```
   cd $HOME
   mkdir workarea-gnuradio
   cd workarea-gnuradio
```   
Next, clone the repository.
```
   git clone --recursive https://github.com/gnuradio/gnuradio
```   
Next, go into the repository and check out the desired GNU Radio version.
```
   cd gnuradio
   git checkout v3.7.10.1
   git submodule update --init --recursive
```   
Next, create a build folder within the repository.
```
   mkdir build
   cd build
```   
Next, invoke CMake to create the Makefiles.
```
   cmake ../
```   
Next, run Make to build GNU Radio.
```
   make
```   
Next, you can optionally run some basic tests to verify that the build process completed properly.
```
   make test
```   
Next, install GNU Radio, using the default install prefix, which will install GNU Radio under the /usr/local/lib folder. You need to run this as root due to the permissions on that folder.
```
   sudo make install
```   
Finally, update the system's shared library cache.
```
   sudo ldconfig
```   
At this point, GNU Radio should be installed and ready to use. You can quickly test this, with no USRP device attached, by running the following quick tests.
```
   gnuradio-config-info --version
   gnuradio-config-info --prefix
   gnuradio-config-info --enabled-components
```   
There is a simple flowgraph that you can run that does not require any USRP hardware. It's called the dialtone test, and it produces a PSTN dial tone on the computer's speakers. Running it verifies that all the libraries can be found, and that the GNU Radio run-time is working.
```
   python $HOME/workarea-gnuradio/gnuradio/gr-audio/examples/python/dial_tone.py
```   
You can try launching the GNU Radio Companion (GRC) tool, a visual tool for building and running GNU Radio flowgraphs.
```
   gnuradio-companion
```   
If "gnuradio-companion" does not start and complains about the PYTHONPATH environment variable, then you may have to set this in your $HOME/.bashrc file, as shown below.
```
   export PYTHONPATH=/usr/local/lib/python2.7/dist-packages
```   

### Configuring USB
On Linux, udev handles USB plug and unplug events. The following commands install a udev rule so that non-root users may access the device. This step is only necessary for devices that use USB to connect to the host computer, such as the B200, B210, and B200mini. This setting should take effect immediately and does not require a reboot or logout/login. Be sure that no USRP device is connected via USB when running these commands.
```
   cd $HOME/workarea-uhd/uhd/host/utils
   sudo cp uhd-usrp.rules /etc/udev/rules.d/
   sudo udevadm control --reload-rules
   sudo udevadm trigger
```
   ---------
### Connect the USRP
The installation of UHD and GNU Radio should now be complete. At this point, connect the USRP to the host computer.

If the interface is Ethernet, then open a terminal window, and try to ping the USRP with "ping 192.168.10.2". The USRP should respond to the ping requests.

If the interface is USB, then open a terminal window, and run "lsusb". You should see the USRP listed on the USB bus with a VID of 2500 and PID of 0020, 0021, 0022, for B200, B210, B200mini, respectively.

Also try running "uhd_find_devices" and "uhd_usrp_probe".

