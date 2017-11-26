import subprocess

def excute_cmd(_cmd):
    """
        excute cmd and return the out put string
    """
    code = 0
    try:
        out_bytes = subprocess.check_output(_cmd, shell=True)
    except subprocess.CalledProcessError as e:
        out_bytes = e.output
        code = e.returncode
    return out_bytes.decode('utf-8'), code
    

def main():
    cmd = 'bash check-process.sh getReview.py'
    output, code = excute_cmd(cmd)
    print(code)
    pass

if __name__ == '__main__':
    main()