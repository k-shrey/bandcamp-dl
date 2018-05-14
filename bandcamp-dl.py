import bc
import sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument('--url', default = None, type = str, help = 'URL to album page or song')
parser.add_argument('--dir', default = None, type = str, help = 'Directory to save songs')

args = parser.parse_args()

if not args.url:
	print ("No URL found, exiting..")
	sys.exit(-1)
if __name__ == '__main__':
	down = bc.Download(args)
	down.download()