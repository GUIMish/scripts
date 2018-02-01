#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright: 2017 GUIMish <mish7913@gmail.com>
#  License:   GNU General Public License v2 or later

import os, time;
from multiprocessing import Process

def pricess_func(): time.sleep(5); print("done");

def main():
		
	process_1 = Process(target=pricess_func);
	text = "";
	while (text != "exit"):
		text = raw_input("-> command ~$ ");
		if (text == "start"):
			process_1.start();
		if (text == "stop"):
			process_1.terminate();
		
	return 0

if __name__ == '__main__': main();
