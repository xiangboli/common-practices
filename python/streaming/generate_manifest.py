import os
import argparse

class ManifestGenerator:
    def __init__(self, medias, output_dir, dash_segment_type='segment_template', segment_duration=10, hls_version=4, single_file=True):
        #self.manifest_type = manifest_type
        self.medias = medias
        self.output = output_dir

        self.dash_segment_type = dash_segment_type

        self.segment_duration = segment_duration
        self.hls_version = hls_version
        self.single_file = single_file

        self.hls_cmd = None
        self.dash_cmd = None

    
    def generate_hls_cmd(self):
        cmd = f'mp4hls --hls-version {self.hls_version} --segment-duration {self.segment_duration} --audio-format ts '
        if self.single_file:
            cmd += '--output-single-file '
        
        cmd += f'--output-dir={self.output}/hls '
        medias = ' '.join(self.medias)
        cmd += f'{medias}'

        print(cmd)
        self.hls_cmd = cmd
    
    def generate_dash_cmd(self):
        cmd = f'mp4dash '
        if self.dash_segment_type == 'segmentbase':
            cmd += '--use-segment-timeline --no-split --profile on-demand '
        elif self.dash_segment_type == 'segmentlist':
            cmd += '--use-segment-list '
        else:
            cmd += '--use-segment-template-number-padding '
        
        cmd += f'--output-dir={self.output}/dash '
        medias = ' '.join(self.medias)
        cmd += f'{medias}'
        print(cmd)
        self.dash_cmd = cmd

    def generate_manifest(self):
        self.generate_hls_cmd()
        self.generate_dash_cmd()

        #os.system(self.hls_cmd)
        os.system(self.dash_cmd)

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Manifest Generator")

    parser.add_argument('-i', '--input', help="input directory")
    parser.add_argument('-o', '--output', help="output directory")

    parser.add_argument('--dash_segment_type', help="dash segment information type")

    parser.add_argument('--segment_duration', type=int, help="hls segment duration")
    parser.add_argument('--hls_version', type=int, help="hls version")
    parser.add_argument('--single_file', type=bool, help="output single file")

    args = parser.parse_args()

    input_dir = args.input
    output_dir = args.output

    dash_segment_type =args.dash_segment_type

    hls_segment_duration = args.segment_duration
    hls_version = args.hls_version
    hls_single_file = args.single_file

    medias = []
    for filename in os.listdir(input_dir):
        if not filename.endswith('.mp4'):
            continue

        input_media = os.path.join(input_dir, filename)
        medias.append(input_media)
    
    gm = ManifestGenerator(medias, output_dir, dash_segment_type)
    gm.generate_manifest()
    


