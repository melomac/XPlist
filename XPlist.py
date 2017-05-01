#!/usr/bin/python

import os, re, sys, time
from urllib import urlopen
from Foundation import NSArray, NSDictionary, NSString, NSURL


# ---------------------------------------------------------------------------

def init_with_files(fmeta, fdata):
	meta = NSDictionary.dictionaryWithContentsOfFile_(fmeta)
	data = NSArray.arrayWithContentsOfFile_(fdata)
	
	return meta, data


def init_with_sucatalog(sucatalog, pkg_re = "^.*/XProtectPlistConfigData.*\.pkg$"):
	meta = None
	data = None
	pkg_url = None
	
	u = NSURL.URLWithString_(sucatalog)
	d = NSDictionary.dictionaryWithContentsOfURL_(u)
	
	if not d:
		raise Exception("Invalid CatalogURL.", sucatalog)
	
	for k, v in d["Products"].items():
		for package in v["Packages"]:
			r = re.compile(pkg_re)
			if r.findall(package["URL"]) != []:
				pkg_url = package["URL"]
	
	if not pkg_url:
		raise Exception("Package not found.", sucatalog, pkg_name)
	
	tmp_t = "%f" % time.time()
	tmp_pkg = "/tmp/xplist_%s.pkg" % tmp_t
	tmp_dir = "/tmp/xplist_%s" % tmp_t
	tmp_tar = "/tmp/xplist_%s/Payload" % tmp_t
	
	cmds = [ "/usr/bin/curl -s -o '%s' '%s'" %(tmp_pkg, pkg_url),
			 "/usr/sbin/pkgutil --expand '%s' '%s'" %(tmp_pkg, tmp_dir),
			 "/usr/bin/tar xf '%s' -C '%s' -s '|.*/||' --include '*/XProtect.*'" %(tmp_tar, tmp_dir) ]
	
	for cmd in cmds:
		retcode = os.system(cmd)
		if retcode != 0:
			raise Exception("Error processing package.", pkg_url, retcode, cmd)
	
	fmeta = "%s/XProtect.meta.plist" % tmp_dir
	fdata = "%s/XProtect.plist" % tmp_dir
	
	if os.path.exists(fmeta) and os.path.exists(fdata):
		meta, data = init_with_files(fmeta, fdata)
	
	return meta, data, pkg_url


def init_with_url(url):
	contents = urlopen(url).read()
	start = contents.find("<?xml ")
	plist = NSString.stringWithString_(contents[start:]).propertyList()
	
	if not isinstance(plist, NSDictionary):
		raise Exception("Invalid URL contents.", url, contents)
	
	return plist["meta"], plist["data"]


def parse_description(description):
	sp = description.split(".")
	
	if len(sp) > 2:
		name = ".".join(sp[:-1])
		variant = sp[-1]
		return name, variant
	
	return description, ""


def count_matches(matches):
	count = 0
	
	for match in matches:
		if match["MatchType"] in [ "Match", "MatchAll" ]:
			count += 1
		elif match["MatchType"] == "MatchAny":
			count += len(match["Matches"])
		else:
			raise Exception("Invalid MatchType.")
	
	return count


# ---------------------------------------------------------------------------

if __name__ == "__main__":
	
	XPROTECTS = NSArray.arrayWithContentsOfFile_(os.path.join(sys.path[0], "XPlist.plist"))
	
	if not XPROTECTS:
		raise Exception("Invalid URLs property list file.")
	
	for xprotect in XPROTECTS:
		
		# print target
		print xprotect["name"]
		
		# print source
		# init meta and data
		if xprotect.has_key("url"):
			print xprotect["url"]
			meta, data = init_with_url(xprotect["url"])
		
		elif xprotect.has_key("surl"):
			print xprotect["surl"]
			if xprotect.has_key("pkg_re"):
				meta, data, pkg_url = init_with_sucatalog(xprotect["surl"], xprotect["pkg_re"])
			else:
				meta, data, pkg_url = init_with_sucatalog(xprotect["surl"])
			print pkg_url
		
		elif xprotect.has_key("data"):
			print xprotect["data"]
			print xprotect["meta"]
			meta, data = init_with_files(xprotect["meta"], xprotect["data"])
		
		if not meta or not data:
			raise Exception("Invalid meta or data.")
		
		# parse data
		try:
			from collections import OrderedDict
			d = OrderedDict()
		except ImportError: # Snow Leopard fallback
			d = {}
		
		for entry in data:
			name, variant = parse_description(entry["Description"])
			count = count_matches(entry["Matches"])
			
			if d.has_key(name):
				if variant not in d[name]["variants"]:
					d[name]["variants"].append(variant)
				d[name]["count"] += count
			else:
				d[name] = { "variants": [variant], "count": count }
		
		# print results
		total_variants = 0
		total_count = 0
		
		for k, v in d.items():
			total_variants += len(v["variants"])
			total_count += v["count"]
			
			print "{0:<20}  {1:>3}    {2:<45}".format(k, v["count"], ", ".join(v["variants"]))
		
		print "%d threats, %d variants, %d signatures (version %d)." % (len(d), total_variants, total_count, meta["Version"])
		print

