#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
c = "ab"
while True:
	while len(c) > 1:
		c = str(input("\nÍrj be egy karaktert: "))
	print("\nA(z) '" + c + "' ASCII kódja:", ord(c))
	c = "ab"