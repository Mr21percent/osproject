import os, fnmatch, shutil
import xml.etree.ElementTree as ElementTree
import zipfile

class TestError(Exception):
	"""
		Exception class for the Test suite
	"""

class Structure(object):
	"""
		Basic class with helper functions that help derived classes to 
		access data
	"""
	
	def getJenkinsSettings(self):
		"""
			Find Jenkins settings and report data to user
			
			getJenkinsSettings() function returns the settings for the 
			validation integration tool. It reads some variables that are set
			by the tool and returns a dictionary of valid instances. 
			
			In case the script is launched outside Jenkins, some default value
			is return otherwise.
			
			Args:
				self: self of the given object
			Returns:
				job:      the Jenkins JOB name
				name:     the name cleaned from the pre-pended part (X-CUBE or FP-XXX-)
				scm:      which SCM is used (could be svn, git or None)
				tag:      the tag name (if set, otherwise None)
				rev:      the revision (hash code for git)
				version:  the version is the tag (if set), rev otherwise
		"""
		try:
			package = os.environ["JOB_NAME"]
			# if we are on a matrix job, please separate from Node indication
			package = package.split('/')[0]
			name    = package.split('-')[2]
		except KeyError as e: 
			package = "NONAME"
			name    = "NONE"
			
		# we try the two supported SCM (SVN, GIT) and see which settings are
		# used for the job
		
		scm = None
		tag = None
		rev = None
		
		# try SVN, if exception try GIT
		try:
			url = os.environ["SVN_URL"]
			if url.count("tags") > 0:
				tag = url.split("tags/")[1]
			rev = os.environ["SVN_REVISION"]
			scm    = "svn"
		except KeyError:
			# try git
			try: 
				url = os.environ["GIT_URL"]
				brn = os.environ["GIT_BRANCH"]
				if brn.count("tags") > 0:
					tag = brn.split("tags/")[1]
				rev = os.environ["GIT_COMMIT"]
				scm = "git"
			except KeyError:
				pass
		
		if tag != None:
			version = tag
		else:
			if rev != None:
				version = rev
			else:
				version = None
		
		return {"job": package, "name": name, "scm":scm, "tag":tag, "rev":rev, "version":version}
	
	def findList(self, name, path):
		"""
			Find files matching name in path.
			
			findList creates a list of files matching all given name, 
			but it does not search with wildcards
			
			Args:
				self: self of the given object
				name: the name to be searched (wildcards not interpreted)
				path: the top folder where to search
			Returns:
				a list of matching patterns
		"""
		result = []
		for root, dirs, files in os.walk(path):
			if name in files:
				result.append(os.path.join(root,name))
		return result
		
	def findFirstFile(self, name, path):
		"""
			Find the first file match in path
			
			findFirstFile returns only the first matching filename, returning an
			easy-to-manage string
			
			Args:
				self: self of the given object
				name: the name to be searched (wildcards not interpreted)
				path: the top folder where to search
			Returns:
				a single filename in a string
		"""
		for root, dirs, files in os.walk(path):
			if name in files:
				return os.path.join(root,name)
				
	def findFirstDir(self, name, path):
		"""
			Find the first dir match in path
			
			findFirstDir returns only the first matching directory, returning an
			easy-to-manage string
			
			Args:
				self: self of the given object
				name: the name to be searched (wildcards not interpreted)
				path: the top folder where to search
			Returns:
				a single directory in a string
		"""
		for root, dirs, files in os.walk(path):
			if name in dirs:
				return os.path.join(root,name)

		
	def findPattern(self, pattern, path):
		"""
			Find a list of files matching pattern in path
			
			findPattern expands wildcards as * and ? for the 
			pattern name that should be searched for
			
			Args:
				self: 		self of the given object
				pattern: 	the name to be searched *with* wildcatds
				path: 		the top folder where to search
			Returns:
				a list of matching patterns 
		"""
		result = []
		for root, dirs, files in os.walk(path):
			for name in files:
				if fnmatch.fnmatch(name,pattern):
					foundpath  = os.path.join(root, name)
					foundpath  = foundpath.replace('//','/').replace('\\','/')
					result.append(foundpath)
		return result
		
	def findImmediateSubdirectories(self, dir):
		"""
			Find the subdirectories in given dir, without recursion
			
			findImmediateSubdirectories returns a list of subdirectories that are immediately
			under the given path (no search recursion)
			
			Args:
				self: 		self of the given object
				dir:  		the path where to search
		"""
		if os.path.isdir(dir):
			return [ name for name in os.listdir(dir) if os.path.isdir(os.path.join(dir,name)) ]
		else:
			return []
			
	def insertFilenameInZip(self, zipname, filelist, prefix=None):
		"""
			Insert files in an archive
			
			insertFilenameinZip inserts in zipname archive the list of files contained 
			in the filelist list
			
			Args:
				self: 		self of the given object
				zipname:	filename of the zip file
				filelist:	list of files that are inserted in the zip
		"""
		
		# import zip deflation compresssion
		try:
			import zlib
			compression = zipfile.ZIP_DEFLATED
		except:
			compression = zipfile.ZIP_STORED
		
		if prefix != None:
			# create a list with filenames with prefix
			prefix_filelist = [ prefix+"/"+name for name in filelist ]
			
			# remove any trailing directories
			if os.path.isdir(prefix):
				shutil.rmtree(prefix)
			
			# copy files in the new folder
			os.mkdir(prefix)
			
			
			for f in filelist:
				name = prefix + '/' + f
				name = os.path.dirname(name)
				if not os.path.exists(name): os.makedirs( name )
				shutil.copy(f, name)
		else:
			prefix_filelist = filelist
					
		# now create the zip file 
		try:
			with zipfile.ZipFile(zipname, mode='a') as zf:
				for f in prefix_filelist:
					zf.write(f, compress_type=compression)
		except zipfile.BadZipFile as e:
			print("Specified a Bad Zip File")
		except FileNotFoundError as e:
			print("Cannot find file" + e)
			
		if prefix != None:
			# remove the folder as not needed anymore
			shutil.rmtree(prefix)
			
	def extractFilesinZip(self, zipname, folder=None, wildcard=None):
		"""
			Extract all files in the zip (in case filter with woldcard) 
			to current folder (otherwise use folder to specify where)
			
			Args:
				self: 		self of the given object
				zipname:	filename of the zip file
				folder:	    if not None, place where files are decompressed
				wildcard:   if not None, uncompress matching files
		"""
		
		matches = []
		with zipfile.ZipFile(zipname) as zf:
			arcfiles = zf.namelist()
			if wildcard != None:
				for f in arcfiles:
					if wildcard in f:
						matches.append(f)
			else:
				matches = arcfiles
			for f in matches:
				if folder != None:
					zf.extract(f, folder)
				else:
					zf.extract(f)
					
		return matches

class Ide(Structure):

	def __init__(self):
		#raise NotImplementedError()
		pass

	def compile(self, path, type, board, name, target, output):
		print("in IDE compile")
		raise NotImplementedError()
	def compileByName(self, path, project ):
		entries=[]
		
		# cycle over possible folder where the project are stored
		for type in ['Applications' ]:
			boards = self.findSupportedBoards(path, type, project)
			# if this is the place where the project is, otherwise if would find 0 supported boards...
			print (boards)
			if len(boards) > 0:
				# cycle over supported boards
				for board in boards:
					output = "output_" + str(self) + "_" + project + "_" + board 
					entry  = self.compile( path, type, board, project, "-ALL", output )
					entries.extend(entry)
		
		return entries
		
	def flash(self):
		raise NotImplementedError()
		
	def clean(self, path, type, board, name, target):
		raise NotImplementedError()
		
	def findProjectFolder(self, path, type, board, name ):
		"""
			Returns the project top folder
			
			findProjectFolder is a function that returns the top folder path
			
			Args:
				self:  		self of the given object
				path:  		top folder where the projects should be contained
				type:  		is it an 'Application' or an 'Example' type
				board: 		which kind of board (i.e. STMF4xx_Nucleo etc.)
				name:		the name of the project that should be searched
			Returns:
				a string containing path to current project path
		"""
		multi = path + '/Multi'
		if os.path.isdir(multi):
			projectdir = multi + '/' + type + '/' + name + '/' 
		else:
			projectdir = path + '/' + board + '/' + type + '/' + name + '/'
		
		return projectdir
		
	def findProject(self, path, type, board, name, idename, pattern):
		"""
			Returns a single project name
			
			findProject is a function that is specialized in the IDEs to search the 
			specific file for that IDE
			
			Args:
				self:  		self of the given object
				path:  		top folder where the projects should be contained
				type:  		is it an 'Application' or an 'Example' type
				board: 		which kind of board (i.e. STMF4xx_Nucleo etc.)
				name:		the name of the project that should be searched
				idename: 	IAR, Keil or SW
				pattern:    pattern to search, i.e. this is specialized in the specialized class
			Returns:
				a string containing path to current project filename
		"""

		multi = path + '/Multi'
		if os.path.isdir(multi):
			projecttopfolder = multi + '/' + type 
			projectdir       = self.findFirstDir( name, projecttopfolder )
			if projectdir == None:
				return ""

			projectdir = projectdir + '/' + idename + '/' + board
		else:
			projectdir = path + '/' + board + '/' + type + '/' + name + '/' + idename 
		
		projects = self.findPattern( pattern, projectdir )
		
		project = [ x for x in projects if not ".svn"    in x ]
		project = [ x for x in projects if not "Backup " in x ]
		
		if len(project) == 0:
			return ""
		else:
			return project[0]
		
	def findTargets(self, projname, target):
		"""
			returns the found targets in the XML file
			
			findProject is a function that is specialized in the IDEs and searches 
			into the project file the targets that are present and could be compiled
			
			Args:
				self:  		self of the given object
				projname:   the project name where to search
				target:     the node in XML that should be searched (depends on the IDE)
			Returns:
				a list of targets for the current project
		"""
		targetlist=[]
		with open(projname) as f:
			et = ElementTree.parse(f)
			for element in et.findall(target):
				targetlist.append(element.text)
		return targetlist

	def findSupportedBoards(self, path, type, name, idename):
		"""
			returns a list of supported boards
			
			findSupportedBoards is a function that searches all the boards that
			are present in the specific subdirectory and list them
			
			Args:
				self:  		self of the given object
				path:  		top folder where the projects should be contained
				type:  		is it an 'Application' or an 'Example' type
				name:		the name of the project that should be searched
				idename: 	IAR, Keil or SW
			Returns:
				a list of boards that are supported
		"""
		multi = path + '/Multi'
		if os.path.isdir(multi):
			projecttopfolder = multi + '/' + type 
			projectdir       = self.findFirstDir( name, projecttopfolder )
			# in case of non-existing path
			if projectdir == None:
				return []
			projectdir       = projectdir + '/' + idename
		else:
			projectdir = path 
		
		boards = self.findImmediateSubdirectories( projectdir )
		boards = [ x for x in boards if not ".svn" in x ]
		
		return boards
		
	def findAllProjects(self, path, type ):
		"""
			returns a list containing all the projects in current package
			
			findAllProjects is a function that searches all the projects folder 
			as immediate subfolder of a given folder
			
			Args:
				self:  		self of the given object
				path:  		top folder where the projects should be contained
				type:  		is it an 'Application' or an 'Example' type
			Returns:
				a list of directories as a list of strings
		"""
		multi = path + '/Multi'
		projects = []
		if os.path.isdir(multi):
			projectdir = multi + '/' + type
		else:
			board = self.findImmediateSubdirectories( path )
			projectdir = path  + '/' + board[0] + '/' + type
		if os.path.isdir(projectdir):
			projects = self.findImmediateSubdirectories( projectdir )
		return projects
		
