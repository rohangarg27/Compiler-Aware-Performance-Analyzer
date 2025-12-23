import subprocess

def measure(binary):
    cmd = ["/usr/bin/time", "-v", binary]
    result = subprocess.run(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        text=True
    )
    return result.stderr

