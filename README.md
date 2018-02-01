Work in progress for ATSC ROUTE Demuxer:

Compilation
-------------------

Linux (Ubuntu 16.04) :

* Tested with the following dependancies (libcurl/7.57.0-DEV OpenSSL/1.0.2g zlib/1.2.8)
* From top directory, run make.
* Binaries are generated in the bin directory/

Windows:

* Not tested, see OLD_README.txt for legacy compilation instructions.


Running
-------------------

To bootstrap the Service List Table (SLT), use the script "receiver_korean.py" with python2.7 located in the SLT_Signalling directory:

* python receiver_korean.py

Warning the ethernet interface is currently hardcoded (vboxnet0) in the script. Modify it to match yours.

Once you have the SLT, you can use the binary in the bin folder.

For example, to get object TOI 0 TSI 0:

* ./flute -o:0 -t:0 -A -B:$PWD/DASH_Content2 -m:239.255.56.235 -s:192.168.5.121 -p:8002 -I:vboxnet0


