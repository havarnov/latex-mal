#/usr/bin/env python2

from subprocess import call

call(["latexmk.exe",
		"-pdf",
		"-pdflatex=\"pdflatex -interaction=nonstopmode\"",
		"-output-directory=build/",
		"-recorder-",
		"-r",
		".latexmkrc",
		"-silent",
		"-quiet",
		"masteroppg.tex",
	])