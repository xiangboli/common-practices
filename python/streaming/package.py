import os
import argparse

class Packager:
    def __init__(self, input_file, output_file, fragment_duration):
        self.input = input_file
        self.output = output_file
        self.fragment_duration = fragment_duration

        self.package_cmd = None

    def generate_cmd(self):
        cmd = f'mp4fragment --fragment-duration {self.fragment_duration} --index '
        cmd += f'{self.input} {self.output}'
        print(cmd)
        self.package_cmd = cmd
    
    def package(self):
        self.generate_cmd()
        os.system(self.package_cmd)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="package video")

    parser.add_argument("-i", "--input", help="input dir")
    parser.add_argument("-o", "--output", help="output dir")
    parser.add_argument("-d", "--duration", type=int, help="fragment duration")

    args = parser.parse_args()

    input_dir = args.input
    output_dir = args.output
    fragment_duration = args.duration

    for filename in os.listdir(input_dir):
        if not filename.endswith('mp4'):
            continue

        video_name, _ = os.path.splitext(filename)
        input_video = os.path.join(input_dir, f'{filename}')
        output_video = os.path.join(output_dir, f'{video_name}_frag.mp4')
        packager = Packager(input_video, output_video, fragment_duration)
        packager.package()
    

    