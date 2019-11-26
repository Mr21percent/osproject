import os, re, platform, string
from ide import Ide, TestError
import subprocess

class Keil_W(Ide):
	"""
		The Keil class is derived from the Ide abstract class and 
		provides support for the Keil IDE.
	"""
	_executable=[]
	_Folder='MDK-ARM'
	_Extension='*.uvprojx'
	
	def __init__(self):
		"""
		Initializes the environment
		
		__init__ setup the environment and raises an exception if it does
		not find what it is searching: the Keil UV4 executable
		
		Args:
				self:  		self of the given object
		"""
		keil = []
		# search for the compiler paths
		for drive in string.ascii_lowercase:

			searchpath="C:/Keil_v5/UV4/"
			if os.path.isdir(searchpath):
				execs = self.findPattern( 'UV4.exe', searchpath )
				keil.extend(execs)
		
		if len(keil) < 1:
			raise TestError()
		
		self._executable = keil[0]

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
		ret=[]
		print( " IDE --------------------------------KEIL  ")
		binstore=[]
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
			print("--KEIL [ " + board + " ]: checking " + name + ' for configuration ' + t )
			cmdstring = self._executable + " -b " + project + " -j0 -t " + t + " -o " + output
			cmdline=cmdstring.split()
			num_error = 0
			num_warn  = 0
			
			try:
				process=subprocess.Popen( cmdline, stdout=subprocess.PIPE )
				process.wait()
			except OSError:
				print("Error in executing command " + self._executable)
				num_error = -1
			except ValueError:
				print("Command line error, some parameters are incorrect")
				num_error = -1
			"""
			if num_error == 0:
				with open(projectfolder + '/' + output, 'r') as f:
					ftext=f.read()
				match=re.search('[0-9]+ Warning',ftext)
				text=match.group(0)
				num_warn  = int(text.split(' ')[0])
				num_error = process.returncode
				# num_error = 1 for Keil means warnings, so we exclude that from reporting
			"""
			if num_error == 1:
					num_error = 0


			bin = self.findPattern('*.bin', projectfolder)
			hex = self.findPattern('*.hex', projectfolder)
			lib = self.findPattern('*.lib', projectfolder)
			a   = self.findPattern('*.a',   projectfolder)
			if bin==[]:
			    print('\n')
			    print("binary not generted")
			    bin="empty"
			    print('\n')
			entry={'ide':'Keil', 'project': name, 'folder': projectfolder, 'board':board, 'target':t, 'error':num_error, 'warning':num_warn, 'bin': bin, 'hex':hex, 'lib':lib, 'a':a}
			print ("PROJECT NAME  : ",name)
			print ("BOARD : ",board)
			print('\n')
			print("Number of Errors" ,num_error )
			print("Number of Warnings" ,num_warn )
			end=1

			binstore.append(board)
			binstore.append(bin)
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
			return 0
		
		projectfolder=os.path.dirname(project)
		if target == "-ALL":
			targets=self.findTargets(project)
		else:
			targets=[ target ]
		
		for t in targets:
			print("--Keil [ " + board + " ]: cleaning " + name + ' for configuration ' + target )
			cmdstring = self._executable + " -c " + project + " -j0 -t " + t 
			cmdline=cmdstring.split()
			try:
				process=subprocess.Popen( cmdline, stdout=subprocess.PIPE )
				process.wait()
			except OSError:
				print("Error in executing command " + self._executable)
				return 1
			except ValueError:
				print("Command line error, some parameters are incorrect")
				return 1
		
		return 0

	def flash(self, path, type, board, name, target, output):
		"""
			flashes the given project file onto a board
			
			compile function calls the IDE to clean the project, raising an
			exception if anything fails
			
			Args:
				self:  		self of the given object
				path:  		top folder where the projects should be contained
				type:  		is it an 'Application' or an 'Example' type
				board: 		which kind of board (i.e. STMF4xx_Nucleo etc.)
				name: 	    project name
				target:		the target that should be cleaned
				output:     store output on a file (not implemented)
		"""
		project=self.findProject(path, type, board, name)
		projectfolder=os.path.dirname(project)
		if target == "-ALL":
			targets=self.findTargets(project)
		else:
			targets=[ target ]
		
		for t in targets:
			print("--Keil [ " + board + " ]: flashing " + name )
			cmdstring = self._executable + " -f " + project + " -j0 -t " + t + " -o " + output
			cmdline=cmdstring.split()
			try:
				process=subprocess.Popen( cmdline, stdout=subprocess.PIPE )
				process.wait()
			except OSError:
				print("Error in executing command " + self._executable)
				return 1
			except ValueError:
				print("Command line error, some parameters are incorrect")
				return 1
			
			if process.returncode != 0:
				print('Keil returned with an ERROR [ ' + str(process.returncode) + ' ] ')
				return 2
		
		return 0


class Keil_L(Ide):
	"""
		The Keil class is derived from the Ide abstract class and 
		provides support for the Keil IDE.
	"""
	_executable=[]
	_Folder='/MDK-ARM'
	_Extension='*.uvprojx'
	
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

	def flash(self, path, type, board, name, target, output):
		"""
			flashes the given project file onto a board
			
			compile function calls the IDE to clean the project, raising an
			exception if anything fails
			
			Args:
				self:  		self of the given object
				path:  		top folder where the projects should be contained
				type:  		is it an 'Application' or an 'Example' type
				board: 		which kind of board (i.e. STMF4xx_Nucleo etc.)
				name: 	    project name
				target:		the target that should be cleaned
				output:     store output on a file (not implemented)
		"""
		return 0

				
class Keil_M(Ide):
	"""
		The Keil class is derived from the Ide abstract class and 
		provides support for the Keil IDE.
	"""
	_executable=[]
	_Folder='/MDK-ARM'
	_Extension='*.uvprojx'

	def __init__(self):
		"""
			Nothing to do for Mac
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

	def flash(self, path, type, board, name, target, output):
		"""
			flashes the given project file onto a board
			
			compile function calls the IDE to clean the project, raising an
			exception if anything fails
			
			Args:
				self:  		self of the given object
				path:  		top folder where the projects should be contained
				type:  		is it an 'Application' or an 'Example' type
				board: 		which kind of board (i.e. STMF4xx_Nucleo etc.)
				name: 	    project name
				target:		the target that should be cleaned
				output:     store output on a file (not implemented)
		"""
		return 0

				
class Keil(Keil_W if platform.system() == "Windows" else Keil_L if platform.system() == "Linux" else Keil_M):
	"""
		The Keil class is derived from the Ide abstract class and 
		provides support for the Keil IDE.
	"""
	_executable=[]
	_Folder='/MDK-ARM'
	_Extension='*.uvprojx'
	
	def __str__(self):
		"""
		returns the class name
		
		Args:
				self:  		self of the given object
		Returns:
				a string containing the class name
		"""
		return "Keil"
		
	def configurations(self):
		pass
		
	def findProject(self, path, type, board, name):
		"""
			Returns a single project name
			
			findProject is a function that is returns the filename for the current Keil project
			
			Args:
				self:  		self of the given object
				path:  		top folder where the projects should be contained
				type:  		is it an 'Applications' or an 'Examples' type
				board: 		which kind of board (i.e. STMF4xx_Nucleo etc.)
				name: 	    project name
			Returns:
				a string containing path to current project filename
		"""
		return super(self.__class__, self).findProject(path, type, board, name, self._Folder, self._Extension )
  
	def findTargets(self, projname):
		"""
			returns the found targets in the XML file
			
			findTargets is a function that is specialized in the IDEs and searches 
			into the project file the targets that are present and could be compiled
			
			Args:
				self:  		self of the given object
				projname:   the project name where to search
			Returns:
				a list of targets for the current project
		"""
		return super(self.__class__, self).findTargets(projname, 'Targets/Target/TargetName')
		
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
		
		