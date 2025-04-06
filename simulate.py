import sys

# Simple command line argument parsing
qr_port = None
for i, arg in enumerate(sys.argv):
    if arg == "--qr-port" and i+1 < len(sys.argv):
        qr_port = sys.argv[i+1]

# Create port configuration file if specified
if qr_port:
    with open('qr_port.txt', 'w') as f:
        f.write(qr_port)
    print("QR scanner port set to %s" % qr_port)

sys.path.append('./src')
sys.path.append('./f469-disco/libs/common')
sys.path.append('./f469-disco/libs/unix')
sys.path.append('./f469-disco/usermods/udisplay_f469/display_unixport')

import main

main.main()
