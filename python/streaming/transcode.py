
import argparse
import os

class Transcoder:
    def __init__(self, input_file, output_dir):
        self.input_file = input_file
        self.output_dir = output_dir

        self.transcode_cmd = None

    def generate_cmd(self):
        cmd = f"ffmpeg -y -i {self.input_file} -sws_flags lanczos "
        cmd += f'-c:v libx264 -x264opts "keyint=24:keyint_min=24:no_scenecut" -r 24 -s 1920x1080 -b:v 3000k -maxrate 4000k -bufsize 6000k -preset medium -profile main -an {self.output_dir}/video_1080p.mp4 '
        cmd += f'-c:v libx264 -x264opts "keyint=24:keyint_min=24:no_scenecut" -r 24 -s 1280x720 -b:v 2000k -maxrate 3000k -bufsize 4000k -preset medium -profile main -an {self.output_dir}/video_720p.mp4 '
        cmd += f'-c:v libx264 -x264opts "keyint=24:keyint_min=24:no_scenecut" -r 24 -s 852x480 -b:v 1500k -maxrate 2000k -bufsize 3000k -preset medium -profile main -an {self.output_dir}/video_480p.mp4 '
        cmd += f'-c:v libx264 -x264opts "keyint=24:keyint_min=24:no_scenecut" -r 24 -s 640x360 -b:v 1000k -maxrate 1500k -bufsize 2000k -preset medium -profile main -an {self.output_dir}/video_360p.mp4 '
        cmd += f'-vn -c:a aac -b:a 128k -ac 2 -ar 48k {self.output_dir}/audio_128k.mp4 '
        cmd += f'-vn -c:a aac -b:a 96k -ac 2 -ar 48k {self.output_dir}/audio_96k.mp4'
        print(cmd)
        self.transcode_cmd = cmd

    def transcode(self):
        self.generate_cmd()
        os.system(self.transcode_cmd)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Transcode Video')

    parser.add_argument('-i', '--input', type=str, help='input video')
    parser.add_argument('-o', '--output', type=str, help="output folder")

    args = parser.parse_args()

    input_file = args.input
    output_dir = args.output

    transcoder = Transcoder(input_file, output_dir)
    transcoder.transcode()

