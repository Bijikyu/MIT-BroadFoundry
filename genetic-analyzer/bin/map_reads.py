#!/usr/bin/env python

# Copyright (C) 2017 by
# Thomas E. Gorochowski <tom@chofski.co.uk>, Voigt Lab, MIT
# All rights reserved
# Released under MIT license (see LICENSE.txt)

# Supporting modules
import argparse
import genetic_analyzer as ga

def main():
	# Parse the command line inputs
	parser = argparse.ArgumentParser(description="map_reads")
	parser.add_argument("-settings",  dest="settings",  required=True,  help="settings.txt", metavar="string")
	parser.add_argument("-samples",  dest="samples",  required=True,  help="1,2", metavar="string")
	args = parser.parse_args()
	# Run the command
	samples = args.samples.split(',')
	settings = ga.load_settings(args.settings)
	for s in samples:
		ga.map_reads(settings, s)

if __name__ == "__main__":
	main()
