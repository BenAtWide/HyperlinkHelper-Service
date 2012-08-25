#!/usr/bin/python

# Python template 1.0 by Peter Hosey
# 2007-08-02

#######################
# EDIT THIS PART HERE #
#######################

"""
Usage: HyperLink Helper - format a link from the clipboard

This service recalibrates the framistan using the geeblefritzer.
(Write your own description, and replace the description above with the description you created, and delete this line.)
"""
import re
import urllib2
import chardet

def get_url_title(url):
	try:
		req = urllib2.Request(url, headers={'User-Agent' : "Sublime Text 2 Hyperlink Helper"}) 
		f = urllib2.urlopen(req)
		url = f.geturl()
		# decoded_content = content.decode(chardet.detect(content)['encoding'])
		content = f.read()
		decoded_content = content.decode(chardet.detect(content)['encoding'])
		title = re.search(r"<title>([^<>]*)</title>", decoded_content, re.I).group(1)
		title = title.strip()
		return title
	except:
		return ""

def make_url(text):
	# convert email addresses to mailto: links
	match = re.match(r"^(mailto:)?(.*?@.*\..*)$", text)
	if match:
		return "mailto:%s" % match.group(2)
	else:
		# convert Amazon links (possibly containing affiliate codes) to canonical URLs
		match = re.match(r"^https?://www.(amazon.(?:com|co.uk|co.jp|ca|fr|de))/.+?/([A-Z0-9]{10})/[-a-zA-Z0-9_./%?=&]+$", text)
		if match: 
			return "http://%s/dp/%s" % (match.group(1), match.group(2))
		else:
			# pass through other URLs untouched
			match = re.match(r"^[a-zA-Z][a-zA-Z0-9.+-]*://.*$", text)
			if match:
				return text
			else:
				# add http:// protocol to URLs without them
				match = re.match(r"^(www\..*|.*\.(com|net|org|info|[a-z]{2}))$", text)
				if match:
					return "http://%s" % text
				else:
					# pass through non-whitespace text unmodified
					match = re.match(r"^\S+$", text)
					if match:
						return text
					else:
						return "http://example.com/"

def get_clipboard():
	import subprocess 
	p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
	retcode = p.wait() 
	data = p.stdout.read() 
	return data 


def main(input_text):
	# Write your documentation above, and implement your service here.

	# This statement, if left alone and unchanged, acts as a pass-through filter: The text enters the program, then exits, with nothing in between.
	url = make_url(get_clipboard().strip())
	text = input_text
	title ='' 
	if re.match(r"^https?://", url) and url != "http://example.com/":
		title = get_url_title(url)
	output_text = '<a href="%s" title="%s">%s</a>' % (url, title, text)
	return output_text

################################
# OK, YOU CAN STOP EDITING NOW #
################################

if __name__ == "__main__":
	import sys

	if sys.argv[1:] == ['--help']:
		sys.exit(__doc__.strip())

	import codecs

	# Read the input.
	input_data = sys.stdin.read()
	try:
		# If it's UTF-8, this converts it to a proper Unicode string.
		input_text = codecs.utf_8_decode(input_data)[0]
	except UnicodeDecodeError:
		# Apparently, it's not UTF-8. We'll give you the raw bytes instead.
		input_text = input_data

	# Obtain the output from your function.
	output_text = main(input_text)
	# Convert it to UTF-8 for output.
	output_data = codecs.utf_8_encode(output_text)[0]
	# Write it to stdout.
	sys.stdout.write(output_data)

