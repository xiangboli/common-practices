import os
import argparse

class GenerateRTMP:
    def __init__(self, out_rtmp, input_media=None):
        self.input_media = input_media
        self.out_rtmp = out_rtmp

        self.rtmp_cmd = None
    
    def generate_cmd(self):
        cmd = 'ffmpeg -y '
        if self.input_media:
            cmd += f'-i {self.input_media} '
        else:
            cmd += '-f avfoundation -i "0" '
        
        cmd += f'-c:v libx264 -tune zerolatency -b:v 900k -c:a copy -f flv {self.out_rtmp}'
        print(cmd)
        self.rtmp_cmd = cmd
    
    def rtmp(self):
        self.generate_cmd()
        os.system(self.rtmp_cmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate RTMP")

    parser.add_argument('-i', '--input', help="input")
    parser.add_argument('-o', '--out_rtmp', help="output rtmp")

    args = parser.parse_args()

    input_media = args.input
    out_rtmp = args.out_rtmp

    gr = GenerateRTMP(out_rtmp, input_media=None)
    gr.rtmp()
