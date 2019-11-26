import os, re, platform, string
from ide import Ide
import subprocess

from distutils.version import LooseVersion, StrictVersion
import xml.etree.ElementTree as ElementTree




class IAR_W(Ide):
	"""
		The IAR class is derived from the Ide abstract class and 
		provides support for the IAR IDE.
	"""
	_executable=""
	_installed=[]
	_Folder='EWARM'
	_Extension='*.ewp'
	
	def getVersion(self, bin=None):
		"""
			get the current set version of IAR
			
			getVersion gets the current set version of the IAR executable
			
			Args:
					self:  		self of the given object
					bin:		path to current set binary
			Returns:
					Returns a string with the current version of the executable
		"""
		if bin == None:
			return self._version['version']
		
		# this command fails as we do not give enough params, it goes to
		# CalledProcessError but we can extract the version there
		try:
			retval = subprocess.check_output( bin, shell=True )
		except OSError:
			print("Error in executing command " + cmdline)
			return "OSError"
		except ValueError:
			print("Command line error, some parameters are incorrect   " + cmdline )
			return "ValueError"
		except subprocess.CalledProcessError as e:
			output      = str(e.output)
			versionline = output.split('\\r\\n')[1]
			
			version     = re.search(r'V(\d+\.\d+\.\d+)', versionline).group(1)
			
			return version
		
		retval = repr(retval)

		#versionline = retval.split('\\r\\n')[1]
		#c=versionline.find('V')
		#ver=versionline[c+1:c+12]
		#print " ver is ",ver
		#version     = re.search(r'V(\d+\.\d+\.\d+\.\d)', versionline).group(1)
		#print "version value ",version
		#versionline = "IAR ANSI C/C++ Compiler V7.40.5.9725/W32 for ARM"
		version='7.70.2.11706'
		
		return version

		
	def setVersion(self, version=None):
		"""
			set the current set version of IAR
			
			setVersion sets the current set version of the IAR executable
			
			Args:
					self:  		self of the given object
					version:	set the current version of the IAR
			Returns:
					returns True if executable is set, False if the version 
					was not found among the installed versions
		"""
		if version == None:
			version=self._installed[-1]['version']
		
		search_version = LooseVersion(version)
		
		for v in self._installed:
			item_version = LooseVersion(v['version'])
			if search_version == item_version:
				self._executable = v['exec']
				self._version    = v
				return True
			else:
				if search_version < item_version:
					self._executable = v['exec']
					self._version    = v
					return True
		
		print("ERROR: incorrect version, too new")
		if self._executable == "":
			self._executable = self._installed[-1]['exec']
			self._version    = self._installed[-1]
		
		return False
		
	def __init__(self):
		"""
		Initializes the environment
		
		__init__ setup the environment and raises an exception if it does
		not find what it is searching: the SystemWorkbench eclipsec executable,
		a make and arm-none-eabi-gcc binaries
		
		Args:
				self:  		self of the given object
		"""
		iar=[]
		for drive in string.ascii_lowercase:

			searchpath1 ="C:/Program Files (x86)/IAR Systems/"
			
			
			searchpath2 = drive + ":/IAR Systems/"
			
			for searchpath in [ searchpath1, searchpath2 ]:
				if os.path.isdir(searchpath):
					execs = self.findPattern( 'IarBuild.exe', searchpath )
					iar.extend(execs)
					
					for exe in execs:
						ccomp   = os.path.dirname(exe) + "/../../arm/bin/iccarm.exe"
						version = self.getVersion(ccomp)
						item    = {'exec': exe, 'comp': ccomp, 'version': version }
						self._installed.append(item)
		
		if len(iar) < 1:
			raise Error()
			
		# presumably the newest
		self._executable = iar[-1]
		
				
	def compile(self, path, type, board, name, target, output):
		"""
			compile the given project and returns the generated binary
			
			compile function calls the IDE to compile the project, raising an
			error if the project fails (printing only number of found warnings)
			and returns a list of filenames of the created binaries
			
			Args:
				self:  		self of the given object
				path:  		top folder where the projects should be contained
				type:  		is it an 'Application' or an 'Example' type
				board: 		which kind of board (i.e. STMF4xx_Nucleo etc.)
				name: 	    project name
				target:		the target that should be compiled
				output:		a filename where to store the output
			Returns:
				A list of dictionary entries, organized in this way
				entry={'ide':'IAR', 'project': name, 'folder': projectfolder, 'board':board, 'target':t, 'error':num_error, 'warning':num_warn, 'bin': bin, 'hex':hex}
				ide:		name of the IDE that generated the entry
				version:    number of the version used to compile
				project:	name of the project that generated the entry
				folder:     name of the top folder where the project is saved
				board: 		name of the Nucleo board for which the project was generated
				target:   	the name of the compiled target
				error:    	the error code, following this nomenclature
						-1: the program failed to start 
						 0: no error
						>0: some error occurred, exit code depending from the IDE, for Keil
								1: some warnings when compiling
								2: errors
				warning:  	number of warnings
				binaries: 	a list of compiled binaries		
		"""
		ret = []
		print (" -----------IDE -IAR------------------  ")
		project = self.findProject(path, type, board, name)
		# project not found or not existing
		if len(project) == 0:
			return ret
		binstore=[]
		# find in the project file the IAR toolchain version and use the nearest match
		version = self.findVersion(project)
		self.setVersion(version)
		
		projectfolder=os.path.dirname(project)

		if target == "-ALL":
			targets=self.findTargets(project)
		else:
			targets=[ target ]
		binaries=[]
		for t in targets:
			print("--IAR  [ " + board + " ]: checking " + name + ' for configuration ' + t + ' toolchain ' + version )
			cmdstring = "\"" + self._executable + "\"  " + project + " -build " + t
			
			num_error = 0
			num_warn  = 0
			try:
				retval=subprocess.check_output( cmdstring, shell=True )
				
			except OSError:
				print("Error in executing command " + self._executable)
				num_error = -1
			except ValueError:
				print("Command line error, some parameters are incorrect")
				num_error = -1
			except subprocess.CalledProcessError as e:
				filename = output + "_" + t + ".txt"
				#print(" ERROR executing the command ")
				#print("       " + cmdstring )
				print("Output saved on " + filename )
				num_error = e.returncode
				with open(filename , 'w') as f:
					f.write(str(e.output))
			
			if num_error == 0:
				retval=str(retval)
				
				match=re.search('Total number of errors: \d+',retval)
				text=match.group(0)
				num_error = int(text.split(':')[-1])
				
				match=re.search('Total number of warnings: \d+',retval)
				text=match.group(0)
				num_warn = int(text.split(':')[-1])
			
			binfolder=projectfolder + '/' + t
			bin = self.findPattern('*.bin', binfolder)
			hex = self.findPattern('*.hex', binfolder)
			lib = self.findPattern('*.lib', binfolder)
			a   = self.findPattern('*.a',   binfolder)
			if bin==[]:
			    print('\n')
			    print("binary not generted")
			    bin="empty"
			    print('\n')

			entry={'ide':'IAR', 'version': version, 'project': name, 'folder': projectfolder, 'board':board, 'target':t, 'error':num_error, 'warning':num_warn, 'bin': bin, 'hex':hex, 'lib':lib, 'a':a}
			#print " -----------IDE -IAR------------------  "
			print ("PROJECT NAME  : ",name)
			print ("BOARD : ",board)
			print('\n')
			print("Number of Errors" ,num_error )
			print("Number of Warnings" ,num_warn )

			binstore.append(board)
			binstore.append(bin)
			#print ("binary value is",bin)
			ret.append(entry)
		return binstore
	
	def clean(self, path, type, board, name, target):
		"""
			clean the given project 
			
			compile function calls the IDE to clean the project, 
			
			Args:
				self:  		self of the given object
				path:  		top folder where the projects should be contained
				type:  		is it an 'Application' or an 'Example' type
				board: 		which kind of board (i.e. STMF4xx_Nucleo etc.)
				name: 	    project name
				target:		the target that should be cleaned
		"""
		project=self.findProject(path, type, board, name)
		# project not found or not existing
		if len(project) == 0:
			return ret
		
		projectfolder=os.path.dirname(project)

		if target == "-ALL":
			targets=self.findTargets(project)
		else:
			targets=[ target ]
			
		for t in targets:
			print("--IAR  [ " + board + " ]: cleaning " + name + ' for configuration ' + t )
			cmdstring = "\"" + self._executable + "\"  " + project + " -clean " + t
			try:
				retval=subprocess.check_output( cmdstring, shell=True )
			except OSError:
				print("Error in executing command " + self._executable)
				return 2
			except ValueError:
				print("Command line error, some parameters are incorrect")
				return 2
			except subprocess.CalledProcessError as e:
				print(" ERROR executing the command ")
				print("       " + cmdstring )
			
		return 0
		

class IAR_L(Ide):
	"""
		The IAR class is derived from the Ide abstract class and 
		provides support for the IAR IDE.
	"""
	
	_executable=[]
	_Folder='EWARM'
	_Extension='*.ewp'
	
	def getVersion(self, bin):
		"""
			get the current set version of IAR
			
			getVersion gets the current set version of the IAR executable
			
			Args:
					self:  		self of the given object
					bin:		path to current set binary
			Returns:
					Returns a string with the current version of the executable
		"""
		pass
		
	def setVersion(self, version):
		"""
			set the current set version of IAR
			
			setVersion sets the current set version of the IAR executable
			
			Args:
					self:  		self of the given object
					version:	set the current version of the IAR
			Returns:
					returns True if executable is set, False if the version 
					was not found among the installed versions
		"""
		pass
	
	def __init__(self):
		"""
			Nothing to do for Linux
		"""
		pass
	
	def compile(self, path, type, board, name, target, output):
		"""
			compile the given project and returns the generated binary
			
			compile function calls the IDE to compile the project, raising an
			error if the project fails (printing only number of found warnings)
			and returns a list of filenames of the created binaries
			
			Args:
				self:  		self of the given object
				path:  		top folder where the projects should be contained
				type:  		is it an 'Application' or an 'Example' type
				board: 		which kind of board (i.e. STMF4xx_Nucleo etc.)
				name: 	    project name
				target:		the target that should be compiled
				output:		a filename where to store the output
			Returns:
				a list of binaries generated in the compile phase
		"""
		return []
		
		
	def clean(self, path, type, board, name, target):
		"""
			clean the given project 
			
			compile function calls the IDE to clean the project, 
			
			Args:
				self:  		self of the given object
				path:  		top folder where the projects should be contained
				type:  		is it an 'Application' or an 'Example' type
				board: 		which kind of board (i.e. STMF4xx_Nucleo etc.)
				name: 	    project name
				target:		the target that should be cleaned
		"""
		return 0


class IAR_M(Ide):
	"""
		The IAR class is derived from the Ide abstract class and 
		provides support for the IAR IDE.
	"""
	
	_executable=[]
	_Folder='EWARM'
	_Extension='*.ewp'
	
	def getVersion(self, bin):
		"""
			get the current set version of IAR
			
			getVersion gets the current set version of the IAR executable
			
			Args:
					self:  		self of the given object
					bin:		path to current set binary
			Returns:
					Returns a string with the current version of the executable
		"""
		pass
		
	def setVersion(self, version):
		"""
			set the current set version of IAR
			
			setVersion sets the current set version of the IAR executable
			
			Args:
					self:  		self of the given object
					version:	set the current version of the IAR
			Returns:
					returns True if executable is set, False if the version 
					was not found among the installed versions
		"""
		pass
	
	def __init__(self):
		"""
			Nothing to do for Linux
		"""
		pass
	
	def compile(self, path, type, board, name, target, output):
		"""
			compile the given project and returns the generated binary
			
			compile function calls the IDE to compile the project, raising an
			error if the project fails (printing only number of found warnings)
			and returns a list of filenames of the created binaries
			
			Args:
				self:  		self of the given object
				path:  		top folder where the projects should be contained
				type:  		is it an 'Application' or an 'Example' type
				board: 		which kind of board (i.e. STMF4xx_Nucleo etc.)
				name: 	    project name
				target:		the target that should be compiled
				output:		a filename where to store the output
			Returns:
				a list of binaries generated in the compile phase
		"""
		return []
		
		
	def clean(self, path, type, board, name, target):
		"""
			clean the given project 
			
			compile function calls the IDE to clean the project, 
			
			Args:
				self:  		self of the given object
				path:  		top folder where the projects should be contained
				type:  		is it an 'Application' or an 'Example' type
				board: 		which kind of board (i.e. STMF4xx_Nucleo etc.)
				name: 	    project name
				target:		the target that should be cleaned
		"""
		return 0
		

class IAR(IAR_W if platform.system() == "Windows" else IAR_L if platform.system() == "Linux" else IAR_M):
	"""
		The IAR class is derived from the Ide abstract class and 
		provides support for the Keil IDE.
	"""
	board='STM'
	_executable=[]
	_Folder='EWARM'
	_Extension='*.ewp'
	def __str__(self):
		"""
		returns the class name
		
		Args:
				self:  		self of the given object
		Returns:
				a string containing the class name
		"""
		return "IAR"
		
	def configurations(self):
		pass
	
	def findProject(self, path, type, board, name):
		"""
			Returns a single project name
			
			findProject is a function that is returns the filename for the current IAR project
			
			Args:
				self:  		self of the given object
				path:  		top folder where the projects should be contained
				type:  		is it an 'Application' or an 'Example' type
				board: 		which kind of board (i.e. STMF4xx_Nucleo etc.)
				name: 	    project name
			Returns:
				a string containing path to current project filename
		"""
		return super(self.__class__, self).findProject(path, type, board, name, self._Folder, self._Extension )
  
	def findTargets(self, projname):
		"""
			returns the found targets in the XML file
			
			findProject is a function that is specialized in the IDEs and searches 
			into the project file the targets that are present and could be compiled
			
			Args:
				self:  		self of the given object
				projname:   the project name where to search
			Returns:
				a list of targets for the current project
		"""
		return super(self.__class__, self).findTargets(projname, 'configuration/name')
		
	def findVersion(self, projname):
		"""
			returns the version of the project file
			
			findVersion explores the XML project file and finds the correct version
			for the IAR IDE 
			
			Args:
				self:  		self of the given object
				projname:   the project name where to search
			Returns:
				the target IAR version for the current project
		"""
		optionlist=[]
		with open(projname) as f:
			et = ElementTree.parse(f)
			# check all paths for XML to "configuration/settings/data/option"
			for element in et.findall('configuration/settings/data/option'):
				optionlist.append(element)
			# option "OGLastSavedByProductVersion" contains last IAR toolchain that saved the project
			for element in optionlist: 
				if element.findtext('name') == "OGLastSavedByProductVersion":
					versionline = element.findtext('state')
					version     = re.search(r'(\d+\.\d+\.\d+)', versionline).group(1)
					return version

		return ""
		
	def findSupportedBoards(self, path, type, name):
		"""
			returns a list of supported boards
			
			findSupportedBoards is a function that searches all the boards that
			are present in the specific subdirectory and list them
			
			Args:
				self:  		self of the given object
				path:  		top folder where the projects should be contained
				type:  		is it an 'Application' or an 'Example' type
				name:	 	project filename
			Returns:
				a list of boards that are supported
		"""
		return super(self.__class__, self).findSupportedBoards(path, type, name, self._Folder)
	
	def flash(self):
		pass
		
